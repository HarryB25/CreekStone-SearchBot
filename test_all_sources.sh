#!/bin/bash
# 综合测试脚本 - 测试所有数据源

# 颜色定义
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 自动检测操作系统
detect_os() {
    case "$(uname -s)" in
        Linux*)
            OS="linux"
            # Linux 通常有 timeout 命令
            if command -v timeout &> /dev/null; then
                TIMEOUT_CMD="timeout"
            else
                TIMEOUT_CMD="python_timeout"
            fi
            ;;
        Darwin*)
            OS="macos"
            # macOS 可能没有 timeout，检查是否有 gtimeout (GNU coreutils)
            if command -v gtimeout &> /dev/null; then
                TIMEOUT_CMD="gtimeout"
            elif command -v timeout &> /dev/null; then
                TIMEOUT_CMD="timeout"
            else
                TIMEOUT_CMD="python_timeout"
            fi
            ;;
        *)
            OS="unknown"
            TIMEOUT_CMD="python_timeout"
            ;;
    esac
}

# 使用 Python 实现跨平台超时
run_with_python_timeout() {
    local script_name=$1
    local timeout_seconds=$2
    local log_file=$3
    local python_cmd=$4
    
    $python_cmd -c "
import subprocess
import sys

try:
    result = subprocess.run(
        ['$python_cmd', '$script_name'],
        capture_output=True,
        text=True,
        timeout=$timeout_seconds
    )
    with open('$log_file', 'w', encoding='utf-8') as f:
        f.write(result.stdout)
        if result.stderr:
            f.write(result.stderr)
    sys.exit(result.returncode)
except subprocess.TimeoutExpired:
    with open('$log_file', 'w', encoding='utf-8') as f:
        f.write('Script execution timeout after ${timeout_seconds} seconds\n')
    sys.exit(124)
except Exception as e:
    with open('$log_file', 'w', encoding='utf-8') as f:
        f.write(f'Error: {e}\n')
    sys.exit(1)
" > /dev/null 2>&1
    return $?
}

# 检测操作系统
detect_os
echo -e "${BLUE}检测到系统: $OS${NC}"
echo -e "${BLUE}使用超时命令: $TIMEOUT_CMD${NC}"
echo ""

# 测试结果统计
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

# 测试结果数组
declare -a TEST_RESULTS

echo "=========================================="
echo "  数据源自动执行测试"
echo "=========================================="
echo ""
echo "测试时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# 检查是否在 conda 环境中
if [ -n "$CONDA_DEFAULT_ENV" ]; then
    echo -e "${GREEN}✓${NC} Conda 环境: $CONDA_DEFAULT_ENV"
else
    echo -e "${YELLOW}⚠${NC} 未检测到 Conda 环境"
    echo "  建议运行: conda activate agent"
fi
echo ""

# 加载环境变量
if [ -f .env ]; then
    source .env
    echo -e "${GREEN}✓${NC} 已加载 .env 文件"
else
    echo -e "${RED}✗${NC} .env 文件不存在"
    exit 1
fi
echo ""

# 测试函数
test_script() {
    local script_name=$1
    local data_source=$2
    local expected_dir=$3
    local timeout_seconds=${4:-300}
    
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo -e "${BLUE}测试 $TOTAL_TESTS: $data_source${NC}"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "脚本: $script_name"
    echo "预期目录: $expected_dir"
    echo ""
    
    # 记录开始时间
    start_time=$(date +%s)
    
    # 运行脚本（带超时）
    echo "→ 执行脚本..."
    # 优先使用 conda 环境中的 python
    if [ -n "$CONDA_DEFAULT_ENV" ]; then
        python_cmd="python"
    elif command -v python3 &> /dev/null; then
        python_cmd="python3"
    else
        python_cmd="python"
    fi
    
    # 根据检测到的系统使用相应的超时方法
    safe_name=$(echo "$data_source" | tr ' /' '__')
    log_file="/tmp/${safe_name}_test.log"
    
    if [ "$TIMEOUT_CMD" = "python_timeout" ]; then
        # 使用 Python 实现跨平台超时
        run_with_python_timeout "$script_name" "$timeout_seconds" "$log_file" "$python_cmd"
        exit_code=$?
    else
        # 使用系统的 timeout 命令
        $TIMEOUT_CMD $timeout_seconds $python_cmd "$script_name" > "$log_file" 2>&1
        exit_code=$?
    fi
    
    # 记录结束时间
    end_time=$(date +%s)
    duration=$((end_time - start_time))
    
    # 检查执行结果
    if [ $exit_code -eq 0 ]; then
        echo -e "${GREEN}✓${NC} 脚本执行成功 (耗时: ${duration}秒)"
        
        # 检查生成的文件
        today=$(date +%Y-%m-%d)
        yesterday=$(date -v-1d +%Y-%m-%d 2>/dev/null || date -d "1 day ago" +%Y-%m-%d)
        day_before_yesterday=$(date -v-2d +%Y-%m-%d 2>/dev/null || date -d "2 days ago" +%Y-%m-%d)
        
        # 尝试查找文件（部分源如 arXiv 有一天滞后，增加前天兜底）
        file_found=""
        for date_str in "$today" "$yesterday" "$day_before_yesterday"; do
            case $data_source in
                "Product Hunt")
                    pattern="$expected_dir/producthunt-daily-${date_str}.md"
                    ;;
                "arXiv")
                    pattern="$expected_dir/arxiv-daily-${date_str}.md"
                    ;;
                "GitHub Trending")
                    pattern="$expected_dir/github-trending-${date_str}.md"
                    ;;
            esac
            
            if [ -f "$pattern" ]; then
                file_found="$pattern"
                break
            fi
        done
        
        if [ -n "$file_found" ]; then
            file_size=$(ls -lh "$file_found" | awk '{print $5}')
            line_count=$(wc -l < "$file_found" | tr -d ' ')
            
            echo -e "${GREEN}✓${NC} 文件生成成功"
            echo "  文件: $file_found"
            echo "  大小: $file_size"
            echo "  行数: $line_count"
            
            # 检查文件内容
            if [ $line_count -gt 10 ]; then
                echo -e "${GREEN}✓${NC} 文件内容正常 (行数 > 10)"
                
                # 检查关键内容
                case $data_source in
                    "Product Hunt")
                        if grep -q "PH今日热榜\|Product Hunt" "$file_found"; then
                            echo -e "${GREEN}✓${NC} 文件格式正确"
                        else
                            echo -e "${YELLOW}⚠${NC} 文件格式可能异常"
                        fi
                        ;;
                    "arXiv")
                        if grep -q "arXiv AI 论文日报\|论文摘要" "$file_found"; then
                            echo -e "${GREEN}✓${NC} 文件格式正确"
                        else
                            echo -e "${YELLOW}⚠${NC} 文件格式可能异常"
                        fi
                        ;;
                    "GitHub Trending")
                        if grep -q "GitHub Trending\|Stars:" "$file_found"; then
                            echo -e "${GREEN}✓${NC} 文件格式正确"
                        else
                            echo -e "${YELLOW}⚠${NC} 文件格式可能异常"
                        fi
                        ;;
                esac
                
                PASSED_TESTS=$((PASSED_TESTS + 1))
                TEST_RESULTS+=("${GREEN}✓${NC} $data_source - 通过")
            else
                echo -e "${RED}✗${NC} 文件内容异常 (行数 <= 10)"
                FAILED_TESTS=$((FAILED_TESTS + 1))
                TEST_RESULTS+=("${RED}✗${NC} $data_source - 文件内容异常")
            fi
        else
            echo -e "${RED}✗${NC} 未找到生成的文件"
            echo "  查找模式: $pattern"
            FAILED_TESTS=$((FAILED_TESTS + 1))
            TEST_RESULTS+=("${RED}✗${NC} $data_source - 文件未生成")
        fi
        
    elif [ $exit_code -eq 124 ]; then
        echo -e "${RED}✗${NC} 脚本执行超时 (超过 ${timeout_seconds}秒)"
        echo "  查看日志: $log_file"
        FAILED_TESTS=$((FAILED_TESTS + 1))
        TEST_RESULTS+=("${RED}✗${NC} $data_source - 执行超时")
    else
        echo -e "${RED}✗${NC} 脚本执行失败 (退出码: $exit_code)"
        echo "  查看日志: $log_file"
        echo "  最后10行日志:"
        tail -10 "$log_file" | sed 's/^/  /'
        FAILED_TESTS=$((FAILED_TESTS + 1))
        TEST_RESULTS+=("${RED}✗${NC} $data_source - 执行失败")
    fi
    
    echo ""
}

# 测试 Product Hunt
test_script \
    "scripts/product_hunt_list_to_md.py" \
    "Product Hunt" \
    "data/producthunt" \
    600

# 测试 arXiv
test_script \
    "scripts/arxiv_papers_to_md.py" \
    "arXiv" \
    "data/arxiv" \
    600

# 测试 GitHub Trending
test_script \
    "scripts/github_trending_to_md.py" \
    "GitHub Trending" \
    "data/github" \
    300

# 测试总结
echo "=========================================="
echo "  测试总结"
echo "=========================================="
echo ""

for result in "${TEST_RESULTS[@]}"; do
    echo -e "$result"
done

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "统计:"
echo "  总测试数: $TOTAL_TESTS"
echo -e "  ${GREEN}通过: $PASSED_TESTS${NC}"
echo -e "  ${RED}失败: $FAILED_TESTS${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 检查目录结构
echo "📁 生成的文件:"
echo ""
for dir in data/producthunt data/arxiv data/github; do
    if [ -d "$dir" ]; then
        file_count=$(ls -1 "$dir"/*.md 2>/dev/null | wc -l | tr -d ' ')
        echo "  $dir: $file_count 个文件"
        ls -lh "$dir"/*.md 2>/dev/null | tail -1 | awk '{print "    最新: " $9 " (" $5 ")"}'
    fi
done

echo ""

# 最终结果
if [ $FAILED_TESTS -eq 0 ]; then
    echo -e "${GREEN}✅ 所有测试通过！${NC}"
    echo ""
    echo "🎉 所有数据源脚本运行正常，可以推送到 GitHub 了！"
    exit 0
else
    echo -e "${RED}❌ 部分测试失败${NC}"
    echo ""
    echo "请检查失败的测试日志:"
    echo "  - /tmp/Product_Hunt_test.log"
    echo "  - /tmp/arXiv_test.log"
    echo "  - /tmp/GitHub_Trending_test.log"
    exit 1
fi
