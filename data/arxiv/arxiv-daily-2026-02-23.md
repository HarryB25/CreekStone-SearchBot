# arXiv AI 论文日报 | 2026-02-23

> 共 15 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (7 篇)
- [cs.AI](#csAI) (3 篇)
- [cs.CV](#csCV) (3 篇)
- [cs.CL](#csCL) (2 篇)

---

## cs.AI

## [1. Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use](https://arxiv.org/abs/2602.20426v1)

**作者**：Ruocheng Guo, Kaiwen Dong, Xiang Gao 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-23

### 📄 论文摘要

The performance of LLM-based agents depends not only on the agent itself but also on the quality of the tool interfaces it consumes. While prior work has focused heavily on agent fine-tuning, tool interfaces-including natural language descriptions and parameter schemas-remain largely human-oriented and often become a bottleneck, especially when agents must select from large candidate tool sets. Existing approaches to improving tool interfaces rely on execution traces, which are frequently unavailable in cold-start or privacy-constrained settings, and typically optimize each tool independently, limiting scalability and generalization to unseen tools. We propose Trace-Free+, a curriculum learning framework that progressively transfers supervision from trace-rich settings to trace-free deployment, encouraging the model to abstract reusable interface-usage patterns and tool usage outcomes. To support this approach, we construct a large-scale dataset of high-quality tool interfaces using a structured workflow over a diverse collection of tools. Experiments on StableToolBench and RestBench show consistent gains on unseen tools, strong cross-domain generalization, and robustness as the number of candidate tools scales to over 100, demonstrating that tool interface optimization is a practical and deployable complement to agent fine-tuning.

### 🤖 AI 总结

**一句话总结**：提出Trace-Free+通过“重写工具描述/接口”而非只微调Agent，在无执行轨迹条件下也能显著提升LLM-Agent的工具选择与调用可靠性。

**研究动机**：现有工具接口多为人类设计，面对上百候选工具时会成为LLM-Agent使用瓶颈；而基于执行轨迹的接口优化在冷启动或隐私受限场景常不可用，且逐工具优化难以扩展到未见工具。

**核心方法**：Trace-Free+采用课程学习，把监督从“有轨迹训练”逐步迁移到“无轨迹部署”设置，促使模型抽象可复用的接口使用模式与结果导向信号；同时通过结构化流程构建大规模高质量工具接口数据，用于学习自动重写工具描述与参数schema以更适配Agent。

**主要结论**：在StableToolBench与RestBench上，该方法对未见工具持续提升、跨域泛化强，并在候选工具规模扩大到100+时仍保持稳健，表明工具接口优化是可部署且能补充Agent微调的有效路径。

**关键词**：工具接口优化, 工具描述重写, 参数模式设计, 无执行轨迹学习, 课程学习, 冷启动部署, 隐私受限训练, 大规模工具选择, 跨域泛化, 未见工具泛化

**评分**：42

**论文链接**：[查看原文](https://arxiv.org/abs/2602.20426v1) | [下载PDF](https://arxiv.org/pdf/2602.20426v1.pdf)

---

## [2. Implicit Intelligence -- Evaluating Agents on What Users Don't Say](https://arxiv.org/abs/2602.20424v1)

**作者**：Ved Sirdeshmukh, Marc Wetter  
**分类**：cs.AI  
**发布时间**：2026-02-23

### 📄 论文摘要

Real-world requests to AI agents are fundamentally underspecified. Natural human communication relies on shared context and unstated constraints that speakers expect listeners to infer. Current agentic benchmarks test explicit instruction-following but fail to evaluate whether agents can reason about implicit requirements spanning accessibility needs, privacy boundaries, catastrophic risks, and contextual constraints. We present Implicit Intelligence, an evaluation framework testing whether AI agents can move beyond prompt-following to become genuine goal-fulfillers, paired with Agent-as-a-World (AaW), a harness where interactive worlds are defined in human-readable YAML files and simulated by language models. Our scenarios feature apparent simplicity in user requests, hidden complexity in correct solutions, and discoverability of constraints through environmental exploration. Evaluating 16 frontier and open-weight models across 205 scenarios, we find that even the best-performing model achieves only 48.3% scenario pass rate, revealing substantial room for improvement in bridging the gap between literal instruction-following and human-like contextual reasoning.

### 🤖 AI 总结

**一句话总结**：提出“Implicit Intelligence”评测框架，用于衡量AI代理在用户未明说的隐含约束下是否能真正完成目标，而不仅是机械遵循提示。

**研究动机**：真实用户请求往往信息不足且依赖共享语境，包含可访问性、隐私边界、风险规避等隐含要求；但现有基准多只考察显式指令遵循，无法评估这种“读懂潜台词”的能力。

**核心方法**：构建Implicit Intelligence基准，并配套Agent-as-a-World（AaW）测试平台：用可读YAML定义交互世界，由语言模型模拟环境，场景表面简单但正确解需通过探索发现隐藏约束；在205个场景上评测16个前沿与开源权重模型。

**主要结论**：即便表现最佳的模型场景通过率也仅48.3%，表明当前模型在从字面执行到基于上下文推断隐含需求的能力上仍有显著差距。

**关键词**：隐式需求推理, 欠规范化指令, 上下文约束推断, 智能体评测基准, 目标满足型智能体, 交互式环境评测, 环境探索, YAML 场景定义, 隐私边界约束, 可访问性需求, 灾难性风险约束, LLM 模拟环境

**评分**：42

**论文链接**：[查看原文](https://arxiv.org/abs/2602.20424v1) | [下载PDF](https://arxiv.org/pdf/2602.20424v1.pdf)

---

## [3. Diffusion Modulation via Environment Mechanism Modeling for Planning](https://arxiv.org/abs/2602.20422v1)

**作者**：Hanping Zhang, Yuhong Guo  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-02-23

### 📄 论文摘要

Diffusion models have shown promising capabilities in trajectory generation for planning in offline reinforcement learning (RL). However, conventional diffusion-based planning methods often fail to account for the fact that generating trajectories in RL requires unique consistency between transitions to ensure coherence in real environments. This oversight can result in considerable discrepancies between the generated trajectories and the underlying mechanisms of a real environment. To address this problem, we propose a novel diffusion-based planning method, termed as Diffusion Modulation via Environment Mechanism Modeling (DMEMM). DMEMM modulates diffusion model training by incorporating key RL environment mechanisms, particularly transition dynamics and reward functions. Experimental results demonstrate that DMEMM achieves state-of-the-art performance for planning with offline reinforcement learning.

### 🤖 AI 总结

**一句话总结**：DMEMM通过显式建模并注入环境转移动力学与奖励机制来调制扩散式轨迹生成，从而提升离线RL规划的可行性与性能。

**研究动机**：现有扩散规划往往只拟合数据分布，忽略RL轨迹中转移一致性与环境机制约束，导致生成轨迹与真实环境动力学/奖励不匹配、落地执行偏差大。

**核心方法**：在扩散模型训练/生成过程中引入环境机制建模，利用转移动力学与奖励函数对去噪过程进行调制（约束/引导），以保证相邻状态-动作转移的连贯性并偏好高回报轨迹。

**主要结论**：实验表明DMEMM在离线强化学习规划任务上达到SOTA，能生成更符合环境机制、执行更一致且回报更高的轨迹。

**关键词**：离线强化学习, 轨迹生成, Diffusion, 扩散规划, 环境机制建模, 转移动力学建模, 奖励函数建模, 一致性约束

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.20422v1) | [下载PDF](https://arxiv.org/pdf/2602.20422v1.pdf)

---

## cs.CL

## [4. Case-Aware LLM-as-a-Judge Evaluation for Enterprise-Scale RAG Systems](https://arxiv.org/abs/2602.20379v1)

**作者**：Mukul Chhabra, Luigi Medrano, Arush Verma  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-23

### 📄 论文摘要

Enterprise Retrieval-Augmented Generation (RAG) assistants operate in multi-turn, case-based workflows such as technical support and IT operations, where evaluation must reflect operational constraints, structured identifiers (e.g., error codes, versions), and resolution workflows. Existing RAG evaluation frameworks are primarily designed for benchmark-style or single-turn settings and often fail to capture enterprise-specific failure modes such as case misidentification, workflow misalignment, and partial resolution across turns.   We present a case-aware LLM-as-a-Judge evaluation framework for enterprise multi-turn RAG systems. The framework evaluates each turn using eight operationally grounded metrics that separate retrieval quality, grounding fidelity, answer utility, precision integrity, and case/workflow alignment. A severity-aware scoring protocol reduces score inflation and improves diagnostic clarity across heterogeneous enterprise cases. The system uses deterministic prompting with strict JSON outputs, enabling scalable batch evaluation, regression testing, and production monitoring.   Through a comparative study of two instruction-tuned models across short and long workflows, we show that generic proxy metrics provide ambiguous signals, while the proposed framework exposes enterprise-critical tradeoffs that are actionable for system improvement.

### 🤖 AI 总结

**一句话总结**：提出一种面向企业多轮RAG“工单/案件”场景的LLM-as-a-Judge评测框架，用更贴近真实运维流程的指标与严重度评分揭示关键失效模式与可行动改进点。

**研究动机**：企业级RAG常在多轮、基于案件的支持/运维流程中工作，需关注错误码/版本等结构化标识与流程闭环，而现有偏单轮/基准集的评测往往无法识别案件错配、流程偏离和跨轮次部分解决等企业特有问题。

**核心方法**：构建“case-aware”的逐轮评测：用8个贴近运营的指标分别衡量检索质量、依据一致性(grounding)、回答效用、精确性完整性，以及案件/工作流对齐；并引入严重度感知的评分协议以抑制分数虚高，采用确定性提示词与严格JSON输出以支持批量评测、回归测试与线上监控。

**主要结论**：对两种指令微调模型在短/长流程对比显示，通用代理指标信号模糊，而该框架能清晰暴露企业关键取舍与失败点（如案件/流程对齐问题），从而提供更具可操作性的系统改进诊断。

**关键词**：多轮对话评测, 案例感知评测, 工作流对齐, 检索质量评估, 事实一致性评估, 严重度感知评分, 确定性提示, JSON结构化输出, 回归测试与线上监控

**评分**：44

**论文链接**：[查看原文](https://arxiv.org/abs/2602.20379v1) | [下载PDF](https://arxiv.org/pdf/2602.20379v1.pdf)

---

## [5. How communicatively optimal are exact numeral systems? Once more on lexicon size and morphosyntactic complexity](https://arxiv.org/abs/2602.20372v1)

**作者**：Chundra Cathcart, Arne Rubehn, Katja Bocklage 等 10 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-23

### 📄 论文摘要

Recent research argues that exact recursive numeral systems optimize communicative efficiency by balancing a tradeoff between the size of the numeral lexicon and the average morphosyntactic complexity (roughly length in morphemes) of numeral terms. We argue that previous studies have not characterized the data in a fashion that accounts for the degree of complexity languages display. Using data from 52 genetically diverse languages and an annotation scheme distinguishing between predictable and unpredictable allomorphy (formal variation), we show that many of the world's languages are decisively less efficient than one would expect. We discuss the implications of our findings for the study of numeral systems and linguistic evolution more generally.

### 🤖 AI 总结

**一句话总结**：论文指出以往关于“精确递归数词系统在词汇规模与形态句法复杂度之间实现交际效率最优”的结论可能被高估，因为在更细致的复杂度标注下，许多语言的数词系统明显低于预期效率。

**研究动机**：近期研究主张数词系统会在“数词词库大小”与“数词表达的平均形态句法复杂度”之间做最优权衡，但作者认为这些研究未充分刻画语言中复杂度差异，尤其忽略了形式变体（allomorphy）的可预测性。

**核心方法**：作者收集52种谱系多样语言的数据，并采用能区分“可预测/不可预测”异形同态（形式变体）的标注方案，对数词表达的复杂度进行更精细量化，再据此评估其交际效率相对理论权衡曲线的位置。

**主要结论**：在该标注框架下，许多世界语言的数词系统并未接近所谓的交际效率最优前沿，而是显著更低效；这表明数词系统的演化可能受非效率因素或更复杂约束影响，需重新审视以往关于效率驱动的解释。

**关键词**：精确递归数词系统, 交际效率, 词汇表规模, 形态句法复杂度, 语素长度, 数词词汇, 可预测异形体, 不可预测异形体, 跨语言类型学, 语言效率偏离, 语言进化, 语言标注方案

**评分**：14

**论文链接**：[查看原文](https://arxiv.org/abs/2602.20372v1) | [下载PDF](https://arxiv.org/pdf/2602.20372v1.pdf)

---

## cs.CV

## [6. gQIR: Generative Quanta Image Reconstruction](https://arxiv.org/abs/2602.20417v1)

**作者**：Aryan Garg, Sizhuo Ma, Mohit Gupta  
**分类**：cs.CV  
**发布时间**：2026-02-23

### 📄 论文摘要

Capturing high-quality images from only a few detected photons is a fundamental challenge in computational imaging. Single-photon avalanche diode (SPAD) sensors promise high-quality imaging in regimes where conventional cameras fail, but raw \emph{quanta frames} contain only sparse, noisy, binary photon detections. Recovering a coherent image from a burst of such frames requires handling alignment, denoising, and demosaicing (for color) under noise statistics far outside those assumed by standard restoration pipelines or modern generative models. We present an approach that adapts large text-to-image latent diffusion models to the photon-limited domain of quanta burst imaging. Our method leverages the structural and semantic priors of internet-scale diffusion models while introducing mechanisms to handle Bernoulli photon statistics. By integrating latent-space restoration with burst-level spatio-temporal reasoning, our approach produces reconstructions that are both photometrically faithful and perceptually pleasing, even under high-speed motion. We evaluate the method on synthetic benchmarks and new real-world datasets, including the first color SPAD burst dataset and a challenging \textit{Deforming (XD)} video benchmark. Across all settings, the approach substantially improves perceptual quality over classical and modern learning-based baselines, demonstrating the promise of adapting large generative priors to extreme photon-limited sensing. Code at \href{https://github.com/Aryan-Garg/gQIR}{https://github.com/Aryan-Garg/gQIR}.

### 🤖 AI 总结

**一句话总结**：gQIR 将大规模文本到图像的潜空间扩散模型适配到SPAD量子突发成像，在极少光子与运动场景下从稀疏二值“quanta frames”重建出更真实且更美观的图像。

**研究动机**：SPAD在极低照度下可工作，但其量子帧呈现伯努利统计下的稀疏、噪声二值观测，传统对齐/去噪/去马赛克流程与常规生成模型的噪声假设都不适用，导致重建质量受限。

**核心方法**：方法将互联网级扩散模型的语义与结构先验引入光子受限重建，并通过面向伯努利光子统计的机制在潜空间做恢复；同时结合burst级时空推理以处理帧间对齐与运动，从而联合完成去噪、对齐与（彩色）去马赛克。

**主要结论**：在合成基准与新采集真实数据（含首个彩色SPAD burst与XD形变视频）上，gQIR相较经典与学习型基线显著提升感知质量，并在高速运动下仍保持较好的光度一致性，验证了“大生成先验+极端传感”适配的有效性。

**关键词**：光子受限成像, 单光子雪崩二极管（SPAD）, 图像重建, 文本到图像扩散先验, 伯努利光子统计, 运动鲁棒重建, gQIR, Generative

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2602.20417v1) | [下载PDF](https://arxiv.org/pdf/2602.20417v1.pdf)

---

## [7. SimLBR: Learning to Detect Fake Images by Learning to Detect Real Images](https://arxiv.org/abs/2602.20412v1)

**作者**：Aayush Dhakal, Subash Khanal, Srikumar Sastry 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-23

### 📄 论文摘要

The rapid advancement of generative models has made the detection of AI-generated images a critical challenge for both research and society. Recent works have shown that most state-of-the-art fake image detection methods overfit to their training data and catastrophically fail when evaluated on curated hard test sets with strong distribution shifts. In this work, we argue that it is more principled to learn a tight decision boundary around the real image distribution and treat the fake category as a sink class. To this end, we propose SimLBR, a simple and efficient framework for fake image detection using Latent Blending Regularization (LBR). Our method significantly improves cross-generator generalization, achieving up to +24.85\% accuracy and +69.62\% recall on the challenging Chameleon benchmark. SimLBR is also highly efficient, training orders of magnitude faster than existing approaches. Furthermore, we emphasize the need for reliability-oriented evaluation in fake image detection, introducing risk-adjusted metrics and worst-case estimates to better assess model robustness. All code and models will be released on HuggingFace and GitHub.

### 🤖 AI 总结

**一句话总结**：SimLBR通过学习真实图像分布来提高假图像检测的性能和效率。

**研究动机**：随着生成模型的快速发展，检测AI生成图像成为一个重要的研究与社会挑战，现有方法在处理分布变化时表现不佳。

**核心方法**：提出了一种名为SimLBR的框架，采用潜在混合正则化（LBR）技术，以提高跨生成器的泛化能力。

**主要结论**：SimLBR在Chameleon基准测试中显著提升了检测准确率和召回率，并强调了使用风险调整指标来评估模型的可靠性。

**关键词**：伪造图像检测, 生成图像检测, 跨生成器泛化, 分布移位鲁棒性, 真实分布决策边界, 汇类分类, 潜变量混合正则化（LBR）, 可靠性导向评测, 风险调整指标, 最坏情况估计

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2602.20412v1) | [下载PDF](https://arxiv.org/pdf/2602.20412v1.pdf)

---

## [8. CLIPoint3D: Language-Grounded Few-Shot Unsupervised 3D Point Cloud Domain Adaptation](https://arxiv.org/abs/2602.20409v1)

**作者**：Mainak Singha, Sarthak Mehrotra, Paolo Casari 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-23

### 📄 论文摘要

Recent vision-language models (VLMs) such as CLIP demonstrate impressive cross-modal reasoning, extending beyond images to 3D perception. Yet, these models remain fragile under domain shifts, especially when adapting from synthetic to real-world point clouds. Conventional 3D domain adaptation approaches rely on heavy trainable encoders, yielding strong accuracy but at the cost of efficiency. We introduce CLIPoint3D, the first framework for few-shot unsupervised 3D point cloud domain adaptation built upon CLIP. Our approach projects 3D samples into multiple depth maps and exploits the frozen CLIP backbone, refined through a knowledge-driven prompt tuning scheme that integrates high-level language priors with geometric cues from a lightweight 3D encoder. To adapt task-specific features effectively, we apply parameter-efficient fine-tuning to CLIP's encoders and design an entropy-guided view sampling strategy for selecting confident projections. Furthermore, an optimal transport-based alignment loss and an uncertainty-aware prototype alignment loss collaboratively bridge source-target distribution gaps while maintaining class separability. Extensive experiments on PointDA-10 and GraspNetPC-10 benchmarks show that CLIPoint3D achieves consistent 3-16% accuracy gains over both CLIP-based and conventional encoder-based baselines. Codes are available at https://github.com/SarthakM320/CLIPoint3D.

### 🤖 AI 总结

**一句话总结**：CLIPoint3D 利用冻结的 CLIP 视觉-语言能力与轻量3D几何编码器，通过提示调优与对齐损失实现少样本无监督3D点云跨域适配，并在基准上显著提升准确率。

**研究动机**：现有3D域适配方法多依赖重型可训练编码器，精度高但效率差；而CLIP等VLM虽具跨模态泛化能力，却在合成到真实点云的域偏移下表现脆弱。

**核心方法**：将点云投影为多视角深度图输入冻结CLIP，并结合知识驱动的prompt tuning（语言先验+几何线索）与参数高效微调来适配任务特征；同时用熵引导视角采样选取高置信投影，并以最优传输对齐损失+不确定性感知的原型对齐损失缩小源/目标分布差异并保持类间可分。

**主要结论**：在PointDA-10与GraspNetPC-10上，CLIPoint3D 相比CLIP类与传统编码器基线均获得稳定的3–16%准确率提升，证明冻结VLM配合轻量几何与高效对齐策略可有效应对3D点云域迁移。

**关键词**：3D点云, 领域适应, 无监督学习, 少样本学习, 深度图, 知识驱动, 参数高效微调, 实验评测

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2602.20409v1) | [下载PDF](https://arxiv.org/pdf/2602.20409v1.pdf)

---

## cs.LG

## [9. GauS: Differentiable Scheduling Optimization via Gaussian Reparameterization](https://arxiv.org/abs/2602.20427v1)

**作者**：Yaohui Cai, Vesal Bakhtazad, Cunxi Yu 等 4 位作者  
**分类**：cs.LG, cs.AR  
**发布时间**：2026-02-23

### 📄 论文摘要

Efficient operator scheduling is a fundamental challenge in software compilation and hardware synthesis. While recent differentiable approaches have sought to replace traditional ones like exact solvers or heuristics with gradient-based search, they typically rely on categorical distributions that fail to capture the ordinal nature of time and suffer from a parameter space that scales poorly. In this paper, we propose a novel differentiable framework, GauS, that models operator scheduling as a stochastic relaxation using Gaussian distributions, which fully utilize modern parallel computing devices like GPUs. By representing schedules as continuous Gaussian variables, we successfully capture the ordinal nature of time and reduce the optimization space by orders of magnitude. Our method is highly flexible to represent various objectives and constraints, which provides the first differentiable formulation for the complex pipelined scheduling problem. We evaluate our method on a range of benchmarks, demonstrating that Gaus achieves Pareto-optimal results.

### 🤖 AI 总结

**一句话总结**：GauS用高斯重参数化将算子调度连续化并可微优化，在GPU上高效进行梯度搜索，取得多目标下的Pareto最优调度结果。

**研究动机**：现有可微调度多用类别分布建模，既难表达时间的序关系（ordinal），又导致参数空间随时间/候选规模膨胀、优化效率差。

**核心方法**：将每个算子开始时间/调度决策松弛为连续高斯随机变量，通过高斯重参数化实现端到端可微的梯度优化，并以可组合的目标与约束项统一表达（含复杂流水线pipelined调度）。

**主要结论**：在多组基准上，GauS在不同目标权衡下达到或逼近Pareto最优，同时相比类别化方法显著降低优化维度并更好利用并行硬件加速。

**关键词**：可微分调度优化, 算子调度, 高斯重参数化, 随机松弛, 连续调度表示, 梯度优化搜索, 编译器优化, 硬件综合, 流水线调度, 多目标帕累托优化, 调度约束建模

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2602.20427v1) | [下载PDF](https://arxiv.org/pdf/2602.20427v1.pdf)

---

## [10. CREDIT: Certified Ownership Verification of Deep Neural Networks Against Model Extraction Attacks](https://arxiv.org/abs/2602.20419v1)

**作者**：Bolin Shen, Zhan Cheng, Neil Zhenqiang Gong 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-23

### 📄 论文摘要

Machine Learning as a Service (MLaaS) has emerged as a widely adopted paradigm for providing access to deep neural network (DNN) models, enabling users to conveniently leverage these models through standardized APIs. However, such services are highly vulnerable to Model Extraction Attacks (MEAs), where an adversary repeatedly queries a target model to collect input-output pairs and uses them to train a surrogate model that closely replicates its functionality. While numerous defense strategies have been proposed, verifying the ownership of a suspicious model with strict theoretical guarantees remains a challenging task. To address this gap, we introduce CREDIT, a certified ownership verification against MEAs. Specifically, we employ mutual information to quantify the similarity between DNN models, propose a practical verification threshold, and provide rigorous theoretical guarantees for ownership verification based on this threshold. We extensively evaluate our approach on several mainstream datasets across different domains and tasks, achieving state-of-the-art performance. Our implementation is publicly available at: https://github.com/LabRAI/CREDIT.

### 🤖 AI 总结

**一句话总结**：CREDIT 提出一种对抗模型抽取攻击的“可认证”神经网络所有权验证方法，用互信息度量模型相似性并给出带理论保证的判定阈值。

**研究动机**：MLaaS 场景下模型易被反复查询并训练出高相似的替代模型，现有防御多但对“如何严格证明某可疑模型是否为被盗拷贝”缺乏可验证的理论保障。

**核心方法**：用互信息（mutual information）量化目标模型与可疑模型在输出行为上的相似度，构建一个可实践的验证阈值，并围绕该阈值推导所有权判定的严格理论保证；随后在多数据集、多任务上进行实证评估。

**主要结论**：CREDIT 在不同领域与任务的数据集上取得了优于现有方法的所有权验证效果，并能在模型抽取攻击背景下提供更强的、可证明的所有权判定依据。

**关键词**：机器学习即服务, 深度神经网络, 模型提取攻击, 模型所有权验证, 认证鲁棒性, 模型相似度度量, 验证阈值, 理论保证, 替代模型检测

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2602.20419v1) | [下载PDF](https://arxiv.org/pdf/2602.20419v1.pdf)

---

## [11. CITED: A Decision Boundary-Aware Signature for GNNs Towards Model Extraction Defense](https://arxiv.org/abs/2602.20418v1)

**作者**：Bolin Shen, Md Shamim Seraj, Zhan Cheng 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-23

### 📄 论文摘要

Graph neural networks (GNNs) have demonstrated superior performance in various applications, such as recommendation systems and financial risk management. However, deploying large-scale GNN models locally is particularly challenging for users, as it requires significant computational resources and extensive property data. Consequently, Machine Learning as a Service (MLaaS) has become increasingly popular, offering a convenient way to deploy and access various models, including GNNs. However, an emerging threat known as Model Extraction Attacks (MEAs) presents significant risks, as adversaries can readily obtain surrogate GNN models exhibiting similar functionality. Specifically, attackers repeatedly query the target model using subgraph inputs to collect corresponding responses. These input-output pairs are subsequently utilized to train their own surrogate models at minimal cost. Many techniques have been proposed to defend against MEAs, but most are limited to specific output levels (e.g., embedding or label) and suffer from inherent technical drawbacks. To address these limitations, we propose a novel ownership verification framework CITED which is a first-of-its-kind method to achieve ownership verification on both embedding and label levels. Moreover, CITED is a novel signature-based method that neither harms downstream performance nor introduces auxiliary models that reduce efficiency, while still outperforming all watermarking and fingerprinting approaches. Extensive experiments demonstrate the effectiveness and robustness of our CITED framework. Code is available at: https://github.com/LabRAI/CITED.

### 🤖 AI 总结

**一句话总结**：CITED提出一种“决策边界感知”的GNN签名框架，可在不损害模型性能与效率的前提下，同时在嵌入与标签两层面实现对抗模型抽取攻击的所有权验证。

**研究动机**：GNN以MLaaS形式部署时易遭模型抽取攻击，攻击者通过大量子图查询训练功能相近的替代模型；现有防御多仅覆盖单一输出层级（嵌入或标签）且常伴随性能/效率代价。

**核心方法**：CITED构建基于决策边界的签名机制，将可验证的“所有权特征”同时注入/绑定到嵌入表示与最终标签输出中；该方法无需额外辅助模型、对下游任务精度影响小，并作为签名式验证优于传统水印/指纹方案。

**主要结论**：实验表明CITED在嵌入与标签双层面的所有权验证上更有效且鲁棒，能在保持下游性能与推理效率的同时，对抗多种模型抽取场景并整体优于现有水印与指纹方法。

**关键词**：图神经网络（GNN）, 模型抽取攻击（MEA）, 模型所有权验证, 决策边界感知, 模型签名, 水印防护, 模型指纹, 嵌入级验证, 标签级验证, 子图查询攻击

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2602.20418v1) | [下载PDF](https://arxiv.org/pdf/2602.20418v1.pdf)

---

## [12. $κ$-Explorer: A Unified Framework for Active Model Estimation in MDPs](https://arxiv.org/abs/2602.20404v1)

**作者**：Xihe Gu, Urbashi Mitra, Tara Javidi  
**分类**：cs.LG  
**发布时间**：2026-02-23

### 📄 论文摘要

In tabular Markov decision processes (MDPs) with perfect state observability, each trajectory provides active samples from the transition distributions conditioned on state-action pairs. Consequently, accurate model estimation depends on how the exploration policy allocates visitation frequencies in accordance with the intrinsic complexity of each transition distribution. Building on recent work on coverage-based exploration, we introduce a parameterized family of decomposable and concave objective functions $U_κ$ that explicitly incorporate both intrinsic estimation complexity and extrinsic visitation frequency. Moreover, the curvature $κ$ provides a unified treatment of various global objectives, such as the average-case and worst-case estimation error objectives. Using the closed-form characterization of the gradient of $U_κ$, we propose $κ$-Explorer, an active exploration algorithm that performs Frank-Wolfe-style optimization over state-action occupancy measures. The diminishing-returns structure of $U_κ$ naturally prioritizes underexplored and high-variance transitions, while preserving smoothness properties that enable efficient optimization. We establish tight regret guarantees for $κ$-Explorer and further introduce a fully online and computationally efficient surrogate algorithm for practical use. Experiments on benchmark MDPs demonstrate that $κ$-Explorer provides superior performance compared to existing exploration strategies.

### 🤖 AI 总结

**一句话总结**：提出κ-Explorer统一框架，通过可调曲率κ的目标函数在MDP中自适应分配访问频次，实现更高效的主动模型估计与更优探索性能。

**研究动机**：在表格型MDP中，模型估计误差取决于探索策略如何在不同(s,a)上分配采样次数，但不同转移分布的内在估计难度（如方差）不一，现有覆盖式方法难以同时兼顾平均与最坏情况等不同全局目标。

**核心方法**：构造一族可分解且凹的目标函数U_κ，将“内在估计复杂度”和“外在访问频次”显式结合，并用曲率κ统一刻画平均/最坏等误差目标；基于U_κ梯度的闭式形式，采用Frank-Wolfe风格在状态-动作占用度量上做优化得到κ-Explorer，并给出在线、计算更高效的替代实现。

**主要结论**：理论上证明κ-Explorer具有紧的遗憾（regret）保证，能自然优先探索低覆盖且高方差的转移；实验上在基准MDP中优于现有探索策略，体现出更准确的模型估计与更好的总体性能。

**关键词**：主动模型估计, 转移概率估计, 覆盖式探索, 凹目标函数, 曲率参数κ, 平均-最坏误差统一, 高方差转移优先, 遗憾界

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2602.20404v1) | [下载PDF](https://arxiv.org/pdf/2602.20404v1.pdf)

---

## [13. Three Concrete Challenges and Two Hopes for the Safety of Unsupervised Elicitation](https://arxiv.org/abs/2602.20400v1)

**作者**：Callum Canavan, Aditya Shrivastava, Allison Qi 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-23

### 📄 论文摘要

To steer language models towards truthful outputs on tasks which are beyond human capability, previous work has suggested training models on easy tasks to steer them on harder ones (easy-to-hard generalization), or using unsupervised training algorithms to steer models with no external labels at all (unsupervised elicitation). Although techniques from both paradigms have been shown to improve model accuracy on a wide variety of tasks, we argue that the datasets used for these evaluations could cause overoptimistic evaluation results. Unlike many real-world datasets, they often (1) have no features with more salience than truthfulness, (2) have balanced training sets, and (3) contain only data points to which the model can give a well-defined answer. We construct datasets that lack each of these properties to stress-test a range of standard unsupervised elicitation and easy-to-hard generalization techniques. We find that no technique reliably performs well on any of these challenges. We also study ensembling and combining easy-to-hard and unsupervised techniques, and find they only partially mitigate performance degradation due to these challenges. We believe that overcoming these challenges should be a priority for future work on unsupervised elicitation.

### 🤖 AI 总结

**一句话总结**：论文指出现有“无监督诱导/由易到难泛化”评测数据集过于理想化，并构造三类更贴近现实的压力测试数据集后发现主流方法在这些挑战下都不稳定、难以可靠提升真实性。

**研究动机**：在超出人类能力的任务上验证模型是否“说真话”很难，现有工作依赖易任务监督或无监督信号来对齐，但作者怀疑常用基准因数据分布过于干净而高估了方法效果。为此需要在更现实的条件（强干扰特征、类别不平衡、存在无明确答案样本）下检验这些方法的鲁棒性。

**核心方法**：作者分别构造缺失三种“理想性质”的数据集：(1) 存在比真实性更显著的特征干扰，(2) 训练集类别不平衡，(3) 包含模型无法给出定义良好答案的数据点；然后系统评测多种标准无监督诱导与由易到难泛化技术，并进一步测试集成(ensembling)及两类方法的组合能否缓解退化。

**主要结论**：结果显示：在任一挑战设置下，没有一种技术能稳定保持良好表现，集成或组合方法只能部分缓解性能下降但无法根治；作者因此认为解决这三项现实数据挑战应成为未来无监督诱导研究的优先方向。

**关键词**：无监督引出, 易到难泛化, LLM 真实输出, 超人任务对齐, 评测集偏差, 分布外评测, 特征显著性干扰, 类别不平衡, 不可判定样本, 压力测试数据集, 模型集成

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2602.20400v1) | [下载PDF](https://arxiv.org/pdf/2602.20400v1.pdf)

---

## [14. GeoPT: Scaling Physics Simulation via Lifted Geometric Pre-Training](https://arxiv.org/abs/2602.20399v1)

**作者**：Haixu Wu, Minghao Guo, Zongyi Li 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-23

### 📄 论文摘要

Neural simulators promise efficient surrogates for physics simulation, but scaling them is bottlenecked by the prohibitive cost of generating high-fidelity training data. Pre-training on abundant off-the-shelf geometries offers a natural alternative, yet faces a fundamental gap: supervision on static geometry alone ignores dynamics and can lead to negative transfer on physics tasks. We present GeoPT, a unified pre-trained model for general physics simulation based on lifted geometric pre-training. The core idea is to augment geometry with synthetic dynamics, enabling dynamics-aware self-supervision without physics labels. Pre-trained on over one million samples, GeoPT consistently improves industrial-fidelity benchmarks spanning fluid mechanics for cars, aircraft, and ships, and solid mechanics in crash simulation, reducing labeled data requirements by 20-60% and accelerating convergence by 2$\times$. These results show that lifting with synthetic dynamics bridges the geometry-physics gap, unlocking a scalable path for neural simulation and potentially beyond. Code is available at https://github.com/Physics-Scaling/GeoPT.

### 🤖 AI 总结

**一句话总结**：GeoPT通过“合成动力学”增强几何自监督预训练，显著降低高保真物理仿真神经模型对标注数据的依赖并加速收敛。

**研究动机**：神经物理仿真扩展受限于高保真训练数据生成成本；仅用静态几何做预训练忽略动力学信息，容易在真实物理任务上产生负迁移。

**核心方法**：提出Lifted Geometric Pre-Training：在无物理标签条件下为几何样本注入合成动力学信号，进行动力学感知的自监督预训练，得到统一的通用物理仿真预训练模型GeoPT。

**主要结论**：在汽车/飞机/船舶流体与碰撞固体等工业级基准上，GeoPT稳定提升性能，标注数据需求减少20-60%，收敛速度提升约2倍，验证合成动力学可弥合几何-物理鸿沟并支持规模化神经仿真。

**关键词**：神经物理仿真器, 物理仿真替代模型, 几何预训练, 提升式表示学习, 合成动力学, 动力学感知自监督, 无标签预训练, 几何-物理迁移, 负迁移, 工业级流体力学仿真, 工业级固体力学仿真, 标注数据缩减

**评分**：41

**论文链接**：[查看原文](https://arxiv.org/abs/2602.20399v1) | [下载PDF](https://arxiv.org/pdf/2602.20399v1.pdf)

---

## [15. cc-Shapley: Measuring Multivariate Feature Importance Needs Causal Context](https://arxiv.org/abs/2602.20396v1)

**作者**：Jörg Martin, Stefan Haufe  
**分类**：cs.LG, stat.ME  
**发布时间**：2026-02-23

### 📄 论文摘要

Explainable artificial intelligence promises to yield insights into relevant features, thereby enabling humans to examine and scrutinize machine learning models or even facilitating scientific discovery. Considering the widespread technique of Shapley values, we find that purely data-driven operationalization of multivariate feature importance is unsuitable for such purposes. Even for simple problems with two features, spurious associations due to collider bias and suppression arise from considering one feature only in the observational context of the other, which can lead to misinterpretations. Causal knowledge about the data-generating process is required to identify and correct such misleading feature attributions. We propose cc-Shapley (causal context Shapley), an interventional modification of conventional observational Shapley values leveraging knowledge of the data's causal structure, thereby analyzing the relevance of a feature in the causal context of the remaining features. We show theoretically that this eradicates spurious association induced by collider bias. We compare the behavior of Shapley and cc-Shapley values on various, synthetic, and real-world datasets. We observe nullification or reversal of associations compared to univariate feature importance when moving from observational to cc-Shapley.

### 🤖 AI 总结

**一句话总结**：cc-Shapley将Shapley特征重要性从“观测关联”改为基于因果结构的“干预语境”，以消除碰撞偏差等导致的虚假多变量归因。

**研究动机**：传统Shapley值在多特征设置下仅依赖观测分布，容易因碰撞器偏差与抑制效应把相关性误当因果贡献，从而误导解释与科学发现。作者认为要得到可信的特征归因，必须引入数据生成过程的因果知识。

**核心方法**：提出cc-Shapley（causal context Shapley），利用已知因果图对某特征进行干预式替换/取值，并在“其余特征的因果语境”下计算边际贡献，从而替代纯观测条件下的Shapley计算。理论上证明该改动可消除由碰撞器偏差引起的虚假关联，并在合成与真实数据上对比其与常规Shapley的差异。

**主要结论**：在多变量重要性评估中，忽略因果结构会产生系统性误归因；cc-Shapley能在理论上根除碰撞器偏差带来的虚假重要性。实验显示从观测Shapley转向cc-Shapley后，某些特征的重要性会被“归零”甚至方向反转，强调解释需要因果语境。

**关键词**：多变量特征重要性, 特征归因, 因果推断, 观测归因偏差, 因果结构图（DAG）, cc-Shapley, Measuring, Multivariate

**评分**：19

**论文链接**：[查看原文](https://arxiv.org/abs/2602.20396v1) | [下载PDF](https://arxiv.org/pdf/2602.20396v1.pdf)

---

