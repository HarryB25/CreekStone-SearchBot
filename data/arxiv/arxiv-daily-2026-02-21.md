# arXiv AI 论文日报 | 2026-02-21

> 共 15 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (4 篇)
- [cs.CV](#csCV) (5 篇)
- [cs.AI](#csAI) (4 篇)
- [cs.CL](#csCL) (2 篇)

---

## cs.AI

## [1. When Do LLM Preferences Predict Downstream Behavior?](https://arxiv.org/abs/2602.18971v1)

**作者**：Katarina Slama, Alexandra Souly, Dishank Bansal 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-21

### 📄 论文摘要

Preference-driven behavior in LLMs may be a necessary precondition for AI misalignment such as sandbagging: models cannot strategically pursue misaligned goals unless their behavior is influenced by their preferences. Yet prior work has typically prompted models explicitly to act in specific ways, leaving unclear whether observed behaviors reflect instruction-following capabilities vs underlying model preferences. Here we test whether this precondition for misalignment is present. Using entity preferences as a behavioral probe, we measure whether stated preferences predict downstream behavior in five frontier LLMs across three domains: donation advice, refusal behavior, and task performance. Conceptually replicating prior work, we first confirm that all five models show highly consistent preferences across two independent measurement methods. We then test behavioral consequences in a simulated user environment. We find that all five models give preference-aligned donation advice. All five models also show preference-correlated refusal patterns when asked to recommend donations, refusing more often for less-preferred entities. All preference-related behaviors that we observe here emerge without instructions to act on preferences. Results for task performance are mixed: on a question-answering benchmark (BoolQ), two models show small but significant accuracy differences favoring preferred entities; one model shows the opposite pattern; and two models show no significant relationship. On complex agentic tasks, we find no evidence of preference-driven performance differences. While LLMs have consistent preferences that reliably predict advice-giving behavior, these preferences do not consistently translate into downstream task performance.

### 🤖 AI 总结

**一句话总结**：论文发现：LLM的“偏好”能稳定预测其建议与拒绝行为，但并不稳定地转化为下游任务/性能差异。

**研究动机**：以往许多“偏好驱动行为/失配风险”的证据可能混杂了指令跟随效应，无法确认模型是否会在无显式指令下依据自身偏好行动。作者希望检验“偏好影响行为”这一潜在失配前提是否真实存在且可泛化到多种下游场景。

**核心方法**：在5个前沿LLM上，用“实体偏好”作为行为探针，先用两种独立测量方法验证偏好的一致性，再在模拟用户环境中测试偏好对三类下游行为的预测：捐赠建议、拒绝模式、任务表现（BoolQ与复杂agentic任务）。

**主要结论**：所有模型的偏好在两种测量方法下高度一致，且无需指令就会给出偏好一致的捐赠建议，并对不偏好的实体表现出更高的拒绝概率；但在任务表现上仅在BoolQ中出现混合且较小的相关性，在复杂agentic任务中未观察到偏好驱动的性能差异。

**关键词**：偏好驱动行为, 下游行为预测, 沙袋行为, 实体偏好探针, 偏好测量一致性, 捐赠建议, 拒绝行为, 代理任务性能

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18971v1) | [下载PDF](https://arxiv.org/pdf/2602.18971v1.pdf)

---

## [2. Robust and Efficient Tool Orchestration via Layered Execution Structures with Reflective Correction](https://arxiv.org/abs/2602.18968v1)

**作者**：Tao Zhe, Haoyu Wang, Bo Luo 等 9 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-21

### 📄 论文摘要

Tool invocation is a core capability of agentic systems, yet failures often arise not from individual tool calls but from how multiple tools are organized and executed together. Existing approaches tightly couple tool execution with stepwise language reasoning or explicit planning, leading to brittle behavior and high execution overhead. To overcome these limitations, we revisit tool invocation from the perspective of tool orchestration. Our key insight is that effective orchestration does not require precise dependency graphs or fine-grained planning. Instead, a coarse-grained layer structure suffices to provide global guidance, while execution-time errors can be corrected locally. Specifically, we model tool orchestration as learning a layered execution structure that captures high-level tool dependencies, inducing layer-wise execution through context constraints. To handle execution-time failures, we introduce a schema-aware reflective correction mechanism that detects and repairs errors locally. This design confines errors to individual tool calls and avoids re-planning entire execution trajectories. This structured execution paradigm enables a lightweight and reusable orchestration component for agentic systems. Experimental results show that our approach achieves robust tool execution while reducing execution complexity and overhead. Code will be made publicly available.

### 🤖 AI 总结

**一句话总结**：提出一种“分层执行结构 + 反思式纠错”的工具编排框架，在不依赖精细规划的情况下提升多工具协作的鲁棒性并降低执行开销。

**研究动机**：现有多工具调用常将执行与逐步推理/显式规划强耦合，导致流程脆弱且一处出错容易触发整体重规划、带来高复杂度与高成本。

**核心方法**：学习一个粗粒度的分层执行结构来表达高层依赖，并用上下文约束驱动按层执行；同时引入schema感知的反思式纠错，在运行时对单次工具调用的错误进行检测与局部修复，避免全局重规划。

**主要结论**：该结构化编排范式将错误限制在局部工具调用内，显著增强执行鲁棒性，并在实验中证明可降低执行复杂度与开销、形成轻量可复用的编排组件。

**关键词**：工具编排, 分层执行结构, 分层依赖建模, 上下文约束执行, 执行时错误修复, 反思式纠错, 局部修复机制, 轻量级编排组件, 执行复杂度降低

**评分**：42

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18968v1) | [下载PDF](https://arxiv.org/pdf/2602.18968v1.pdf)

---

## [3. Modularity is the Bedrock of Natural and Artificial Intelligence](https://arxiv.org/abs/2602.18960v1)

**作者**：Alessandro Salatiello  
**分类**：cs.AI, cs.NE, q-bio.NC  
**发布时间**：2026-02-21

### 📄 论文摘要

The remarkable performance of modern AI systems has been driven by unprecedented scales of data, computation, and energy -- far exceeding the resources required by human intelligence. This disparity highlights the need for new guiding principles and motivates drawing inspiration from the fundamental organizational principles of brain computation. Among these principles, modularity has been shown to be critical for supporting the efficient learning and strong generalization abilities consistently exhibited by humans. Furthermore, modularity aligns well with the No Free Lunch Theorem, which highlights the need for problem-specific inductive biases and motivates architectures composed of specialized components that solve subproblems. However, despite its fundamental role in natural intelligence and its demonstrated benefits across a range of seemingly disparate AI subfields, modularity remains relatively underappreciated in mainstream AI research. In this work, we review several research threads in artificial intelligence and neuroscience through a conceptual framework that highlights the central role of modularity in supporting both artificial and natural intelligence. In particular, we examine what computational advantages modularity provides, how it has emerged as a solution across several AI research areas, which modularity principles the brain exploits, and how modularity can help bridge the gap between natural and artificial intelligence.

### 🤖 AI 总结

**一句话总结**：论文综述并提出：模块化是自然智能与人工智能实现高效学习与强泛化的关键组织原则，应成为构建新一代AI系统的核心指导思想。

**研究动机**：现代AI依赖远超人类的大规模数据与算力才能取得高性能，暴露出效率与泛化差距；作者认为需要借鉴大脑计算的组织原则，而模块化提供了符合“No Free Lunch”所需归纳偏置的路径。

**核心方法**：通过概念框架对AI与神经科学中多个研究线索进行综述与对比，系统梳理模块化带来的计算优势、其在不同AI子领域的自发涌现形式，以及大脑中可借鉴的模块化机制。

**主要结论**：模块化能通过“专门化组件分解子问题”提升学习效率、可迁移性与泛化能力，并在多类AI方法中反复出现；将模块化原则系统化地纳入AI架构设计有望缩小自然智能与人工智能之间的差距。

**关键词**：模块化, 模块化架构, 归纳偏置, 子问题分解, 高效学习, 泛化能力, 脑计算, 神经科学启发, 无免费午餐定理, 自然智能-人工智能对齐

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18960v1) | [下载PDF](https://arxiv.org/pdf/2602.18960v1.pdf)

---

## [4. INDUCTION: Finite-Structure Concept Synthesis in First-Order Logic](https://arxiv.org/abs/2602.18956v1)

**作者**：Serafim Batzoglou  
**分类**：cs.AI  
**发布时间**：2026-02-21

### 📄 论文摘要

We introduce INDUCTION, a benchmark for finite structure concept synthesis in first order logic. Given small finite relational worlds with extensionally labeled target predicates, models must output a single first order logical formula that explains the target uniformly across worlds, with correctness verified via exact model checking. The benchmark includes three regimes, FullObs, CI (contrastive), and EC (existential completion), nd penalizes formula bloat. We find sharp difficulty gradients, persistent hard structural families, and observe that low bloat formulas generalize far better on held out worlds. Elite recent models show qualitatively different behaviors across tasks and performance metrics, hinting to their different strategies of concept generalization.

### 🤖 AI 总结

**一句话总结**：INDUCTION 提供了一个用于“一阶逻辑公式”概念归纳的基准：模型需在多个小型有限关系世界中输出统一且可精确验证的逻辑公式，并显示低冗余公式更能泛化。

**研究动机**：现有模型评测多停留在自然语言或统计拟合层面，难以衡量能否学到可解释、可验证且跨世界一致的符号概念。作者希望用精确模型检验来评估模型在有限结构上的概念综合能力与泛化规律。

**核心方法**：构建 INDUCTION 基准：给定若干有限关系结构世界及外延标注的目标谓词，要求输出单个一阶逻辑公式在所有世界上解释目标，并用精确 model checking 判对。设置 FullObs、CI（对比式）与 EC（存在补全）三种任务体制，并对公式膨胀（bloat）进行惩罚以鼓励简洁表达。

**主要结论**：实验显示任务存在明显难度梯度与持续困难的结构家族，且“低 bloat”的公式在留出世界上的泛化显著更好。不同顶级模型在任务与指标上的行为差异明显，暗示其概念泛化策略并不相同。

**关键词**：一阶逻辑, 概念合成, 有限结构, 关系世界, 逻辑公式生成, 精确模型检验, 基准评测, 存在补全, 公式膨胀惩罚, 结构泛化, 难例结构族

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18956v1) | [下载PDF](https://arxiv.org/pdf/2602.18956v1.pdf)

---

## cs.CL

## [5. Whisper: Courtside Edition Enhancing ASR Performance Through LLM-Driven Context Generation](https://arxiv.org/abs/2602.18966v1)

**作者**：Yonathan Ron, Shiri Gilboa, Tammuz Dubnov  
**分类**：cs.CL  
**发布时间**：2026-02-21

### 📄 论文摘要

Domain-specific speech remains a persistent challenge for automatic speech recognition (ASR), even for state-of-the-art systems like OpenAI's Whisper. We introduce Whisper: Courtside Edition, a novel multi-agent large language model (LLM) pipeline that enhances Whisper transcriptions without retraining. The pipeline intercepts Whisper's initial transcript, applies specialized LLM agents for domain context identification, named entity recognition, and jargon detection, and generates compact prompts that guide Whisper's decoder. Evaluated on 421 NBA basketball commentary segments (a domain characterized by dense proper nouns and technical terminology) our best pipeline achieves a statistically significant 17.0% relative reduction in word error rate (WER; from 0.217 to 0.180, p<0.001). Improvements are observed in 40.1% of segments with degradation in only 7.1%, substantially outperforming direct transcript post-editing. These results demonstrate that prompt-based augmentation can deliver scalable domain adaptation for ASR, offering a practical alternative to costly model fine-tuning.

### 🤖 AI 总结

**一句话总结**：提出“Whisper: Courtside Edition”用多智能体LLM生成领域上下文提示来引导Whisper解码，在不微调的情况下显著降低NBA解说ASR错误率。

**研究动机**：Whisper等通用ASR在NBA解说这类领域语音中容易被密集专有名词与术语拖累，而微调成本高、扩展性差。

**核心方法**：先截获Whisper初始转写，再由多个专用LLM代理完成领域上下文识别、命名实体识别和行话检测，并把结果压缩为提示词注入Whisper解码器以改进后续转写。

**主要结论**：在421段NBA解说上，最佳流水线将WER从0.217降至0.180（相对降低17%，p<0.001），40.1%片段变好且仅7.1%变差，并显著优于直接对转写做LLM后编辑，证明提示增强可作为低成本可扩展的领域自适应方案。

**关键词**：自动语音识别（ASR）, 领域自适应, 多智能体 LLM, 上下文生成, 命名实体识别（NER）, 术语检测, 解码器引导, 免训练增强, 体育解说语音, 词错误率（WER）

**评分**：40

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18966v1) | [下载PDF](https://arxiv.org/pdf/2602.18966v1.pdf)

---

## [6. Yor-Sarc: A gold-standard dataset for sarcasm detection in a low-resource African language](https://arxiv.org/abs/2602.18964v1)

**作者**：Toheeb Aduramomi Jimoh, Tabea De Wille, Nikola S. Nikolov  
**分类**：cs.CL  
**发布时间**：2026-02-21

### 📄 论文摘要

Sarcasm detection poses a fundamental challenge in computational semantics, requiring models to resolve disparities between literal and intended meaning. The challenge is amplified in low-resource languages where annotated datasets are scarce or nonexistent. We present \textbf{Yor-Sarc}, the first gold-standard dataset for sarcasm detection in Yorùbá, a tonal Niger-Congo language spoken by over $50$ million people. The dataset comprises 436 instances annotated by three native speakers from diverse dialectal backgrounds using an annotation protocol specifically designed for Yorùbá sarcasm by taking culture into account. This protocol incorporates context-sensitive interpretation and community-informed guidelines and is accompanied by a comprehensive analysis of inter-annotator agreement to support replication in other African languages. Substantial to almost perfect agreement was achieved (Fleiss' $κ= 0.7660$; pairwise Cohen's $κ= 0.6732$--$0.8743$), with $83.3\%$ unanimous consensus. One annotator pair achieved almost perfect agreement ($κ= 0.8743$; $93.8\%$ raw agreement), exceeding a number of reported benchmarks for English sarcasm research works. The remaining $16.7\%$ majority-agreement cases are preserved as soft labels for uncertainty-aware modelling. Yor-Sarc\footnote{https://github.com/toheebadura/yor-sarc} is expected to facilitate research on semantic interpretation and culturally informed NLP for low-resource African languages.

### 🤖 AI 总结

**一句话总结**：Yor-Sarc 是首个面向低资源非洲语言 Yorùbá 的高质量讽刺检测数据集，提供文化敏感的标注协议与高一致性标注结果。

**研究动机**：讽刺检测需要理解字面与真实意图的偏差，但低资源语言缺少标注语料，使相关语义与文化因素建模研究受限。作者希望为 Yorùbá 提供可复现的金标准数据与标注规范，推动非洲语言的讽刺与语义理解研究。

**核心方法**：构建包含 436 条实例的数据集，由三位不同方言背景的母语者依据面向 Yorùbá 文化语境的标注协议进行标注，并系统报告一致性指标（Fleiss κ、pairwise Cohen κ）。对非一致样本保留“软标签”（多数同意）以支持不确定性感知建模。

**主要结论**：数据集标注一致性达到“较高到近乎完美”（Fleiss κ=0.7660，83.3% 全一致），其中一对标注者达到近乎完美一致（κ=0.8743），并将 16.7% 的多数一致样本作为软标签保留；Yor-Sarc 预计可促进低资源非洲语言中具文化信息的讽刺检测与语义解释研究。

**关键词**：讽刺检测, 低资源语言, 约鲁巴语, 非洲语言NLP, 金标准数据集, 人工标注协议, 文化语境建模, 标注一致性评估, 软标签, 不确定性感知建模

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18964v1) | [下载PDF](https://arxiv.org/pdf/2602.18964v1.pdf)

---

## cs.CV

## [7. Frame2Freq: Spectral Adapters for Fine-Grained Video Understanding](https://arxiv.org/abs/2602.18977v1)

**作者**：Thinesh Thiyakesan Ponbagavathi, Constantin Seibold, Alina Roitberg  
**分类**：cs.CV  
**发布时间**：2026-02-21

### 📄 论文摘要

Adapting image-pretrained backbones to video typically relies on time-domain adapters tuned to a single temporal scale. Our experiments show that these modules pick up static image cues and very fast flicker changes, while overlooking medium-speed motion. Capturing dynamics across multiple time-scales is, however, crucial for fine-grained temporal analysis (i.e., opening vs. closing bottle).   To address this, we introduce Frame2Freq -- a family of frequency-aware adapters that perform spectral encoding during image-to-video adaptation of pretrained Vision Foundation Models (VFMs), improving fine-grained action recognition. Frame2Freq uses Fast Fourier Transform (FFT) along time and learns frequency-band specific embeddings that adaptively highlight the most discriminative frequency ranges. Across five fine-grained activity recognition datasets, Frame2Freq outperforms prior PEFT methods and even surpasses fully fine-tuned models on four of them. These results provide encouraging evidence that frequency analysis methods are a powerful tool for modeling temporal dynamics in image-to-video transfer. Code is available at https://github.com/th-nesh/Frame2Freq.

### 🤖 AI 总结

**一句话总结**：Frame2Freq通过在时间维做FFT并学习频段特定的适配器嵌入，更好地捕捉多时间尺度运动，从而提升细粒度视频理解/动作识别表现。

**研究动机**：现有从图像到视频的适配多依赖单一时间尺度的时域adapter，往往只学到静态线索和极快的闪烁变化，忽视中等速度运动；而细粒度动作区分需要覆盖多尺度动态信息。

**核心方法**：提出频率感知适配器Frame2Freq：对视频特征沿时间维进行FFT得到频谱表示，并为不同频段学习可调的频段专属嵌入/权重，以自适应突出最判别的频率范围，实现参数高效的图像预训练VFM到视频任务迁移。

**主要结论**：在5个细粒度活动识别数据集上，Frame2Freq整体优于以往PEFT方法，并在其中4个数据集上甚至超过全量微调模型，表明频率分析是建模时序动态、提升图像到视频迁移效果的有效途径。

**关键词**：细粒度动作识别, 图像到视频迁移, 视觉基础模型（VFM）, 参数高效微调（PEFT）, 频域适配器, 谱编码, 快速傅里叶变换（FFT）, 多时间尺度运动建模, 频带嵌入, 时序动态建模

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18977v1) | [下载PDF](https://arxiv.org/pdf/2602.18977v1.pdf)

---

## [8. Face Presentation Attack Detection via Content-Adaptive Spatial Operators](https://arxiv.org/abs/2602.18965v1)

**作者**：Shujaat Khan  
**分类**：cs.CV, eess.IV  
**发布时间**：2026-02-21

### 📄 论文摘要

Face presentation attack detection (FacePAD) is critical for securing facial authentication against print, replay, and mask-based spoofing. This paper proposes CASO-PAD, an RGB-only, single-frame model that enhances MobileNetV3 with content-adaptive spatial operators (involution) to better capture localized spoof cues. Unlike spatially shared convolution kernels, the proposed operator generates location-specific, channel-shared kernels conditioned on the input, improving spatial selectivity with minimal overhead. CASO-PAD remains lightweight (3.6M parameters; 0.64 GFLOPs at $256\times256$) and is trained end-to-end using a standard binary cross-entropy objective. Extensive experiments on Replay-Attack, Replay-Mobile, ROSE-Youtu, and OULU-NPU demonstrate strong performance, achieving 100/100/98.9/99.7\% test accuracy, AUC of 1.00/1.00/0.9995/0.9999, and HTER of 0.00/0.00/0.82/0.44\%, respectively. On the large-scale SiW-Mv2 Protocol-1 benchmark, CASO-PAD further attains 95.45\% accuracy with 3.11\% HTER and 3.13\% EER, indicating improved robustness under diverse real-world attacks. Ablation studies show that placing the adaptive operator near the network head and using moderate group sharing yields the best accuracy--efficiency balance. Overall, CASO-PAD provides a practical pathway for robust, on-device FacePAD with mobile-class compute and without auxiliary sensors or temporal stacks.

### 🤖 AI 总结

**一句话总结**：提出CASO-PAD：在MobileNetV3中引入内容自适应空间算子（involution）的轻量级单帧RGB人脸活体检测模型，在多数据集上取得接近满分的精度与极低HTER。

**研究动机**：现有FacePAD在移动端受限于算力与模型规模，同时卷积核空间共享导致对局部伪造线索（如打印纹理、屏幕摩尔纹、面具边缘）的空间选择性不足，需要更高效且更敏感的局部建模能力。

**核心方法**：在MobileNetV3中用内容自适应空间算子替换/插入部分卷积：根据输入在每个位置生成位置特定、通道共享的核（提升空间选择性且开销小），端到端以二分类交叉熵训练；消融表明将该算子放在网络靠近head处并采用适度分组共享可兼顾准确率与效率。

**主要结论**：CASO-PAD在Replay-Attack、Replay-Mobile、ROSE-Youtu、OULU-NPU上实现极高AUC与近零HTER，并在更具挑战的SiW-Mv2 Protocol-1上获得95.45%准确率与较低HTER/EER，证明其在仅RGB单帧、移动级计算预算下具备更强鲁棒性与落地可行性。

**关键词**：人脸活体检测, 展示攻击检测, 人脸反欺骗, 内容自适应空间算子, 轻量化模型, 端侧推理, 打印-回放-面具攻击, Face

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18965v1) | [下载PDF](https://arxiv.org/pdf/2602.18965v1.pdf)

---

## [9. Depth-Enhanced YOLO-SAM2 Detection for Reliable Ballast Insufficiency Identification](https://arxiv.org/abs/2602.18961v1)

**作者**：Shiyu Liu, Dylan Lester, Husnu Narman 等 5 位作者  
**分类**：cs.CV, eess.IV, eess.SY  
**发布时间**：2026-02-21

### 📄 论文摘要

This paper presents a depth-enhanced YOLO-SAM2 framework for detecting ballast insufficiency in railway tracks using RGB-D data. Although YOLOv8 provides reliable localization, the RGB-only model shows limited safety performance, achieving high precision (0.99) but low recall (0.49) due to insufficient ballast, as it tends to over-predict the sufficient class. To improve reliability, we incorporate depth-based geometric analysis enabled by a sleeper-aligned depth-correction pipeline that compensates for RealSense spatial distortion using polynomial modeling, RANSAC, and temporal smoothing. SAM2 segmentation further refines region-of-interest masks, enabling accurate extraction of sleeper and ballast profiles for geometric classification.   Experiments on field-collected top-down RGB-D data show that depth-enhanced configurations substantially improve the detection of insufficient ballast. Depending on bounding-box sampling (AABB or RBB) and geometric criteria, recall increases from 0.49 to as high as 0.80, and F1-score improves from 0.66 to over 0.80. These results demonstrate that integrating depth correction with YOLO-SAM2 yields a more robust and reliable approach for automated railway ballast inspection, particularly in visually ambiguous or safety-critical scenarios.

### 🤖 AI 总结

**一句话总结**：提出一种结合深度校正与YOLOv8+SAM2分割的RGB-D检测框架，以更可靠地识别铁路道砟不足并显著提升召回率。

**研究动机**：仅用RGB的YOLOv8虽精度高但召回低（易把“不足”误判为“充足”），在安全关键场景下不可靠；需要利用深度几何信息缓解视觉歧义并提升安全性能。

**核心方法**：构建与枕木对齐的深度校正流程，用多项式建模+RANSAC+时间平滑补偿RealSense空间畸变；再用SAM2细化ROI掩膜，提取枕木/道砟剖面并基于几何准则（配合AABB/RBB采样）进行不足判别。

**主要结论**：在实采顶视RGB-D数据上，加入深度增强后召回从0.49提升至最高0.80、F1从0.66提升至>0.80，证明深度校正+YOLO-SAM2能在视觉模糊或安全敏感情况下更稳健地检测道砟不足。

**关键词**：深度增强, 轨道检测, 道砟不足, 几何分析, 深度校正, 自动化检测, 安全性能, 模型精度

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18961v1) | [下载PDF](https://arxiv.org/pdf/2602.18961v1.pdf)

---

## [10. YOLOv10-Based Multi-Task Framework for Hand Localization and Laterality Classification in Surgical Videos](https://arxiv.org/abs/2602.18959v1)

**作者**：Kedi Sun, Le Zhang  
**分类**：cs.CV  
**发布时间**：2026-02-21

### 📄 论文摘要

Real-time hand tracking in trauma surgery is essential for supporting rapid and precise intraoperative decisions. We propose a YOLOv10-based framework that simultaneously localizes hands and classifies their laterality (left or right) in complex surgical scenes. The model is trained on the Trauma THOMPSON Challenge 2025 Task 2 dataset, consisting of first-person surgical videos with annotated hand bounding boxes. Extensive data augmentation and a multi-task detection design improve robustness against motion blur, lighting variations, and diverse hand appearances. Evaluation demonstrates accurate left-hand (67\%) and right-hand (71\%) classification, while distinguishing hands from the background remains challenging. The model achieves an $mAP_{[0.5:0.95]}$ of 0.33 and maintains real-time inference, highlighting its potential for intraoperative deployment. This work establishes a foundation for advanced hand-instrument interaction analysis in emergency surgical procedures.

### 🤖 AI 总结

**一句话总结**：提出了一种基于YOLOv10的框架，实现手部定位和侧别分类，以支持创伤手术中的实时手部跟踪。

**研究动机**：实时手部跟踪对于快速和准确的手术决策至关重要，尤其是在复杂的创伤手术场景中。

**核心方法**：利用YOLOv10模型，该模型在带有手部边界框注释的手术视频数据集上进行训练，并通过数据增强和多任务检测设计来提升鲁棒性。

**主要结论**：该模型在左手和右手分类上分别达到67%和71%的准确率，并展示了在实际手术中部署的潜力，尽管区分手与背景仍然具有挑战性。

**关键词**：手部定位, 侧别分类, 手术视频, 多任务检测, 数据增强, 实时推理, 运动模糊, 光照变化, 手-工具交互

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18959v1) | [下载PDF](https://arxiv.org/pdf/2602.18959v1.pdf)

---

## [11. Global Commander and Local Operative: A Dual-Agent Framework for Scene Navigation](https://arxiv.org/abs/2602.18941v1)

**作者**：Kaiming Jin, Yuefan Wu, Shengqiong Wu 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-21

### 📄 论文摘要

Vision-and-Language Scene navigation is a fundamental capability for embodied human-AI collaboration, requiring agents to follow natural language instructions to execute coherent action sequences in complex environments. Existing approaches either rely on multiple agents, incurring high coordination and resource costs, or adopt a single-agent paradigm, which overloads the agent with both global planning and local perception, often leading to degraded reasoning and instruction drift in long-horizon settings. To address these issues, we introduce DACo, a planning-grounding decoupled architecture that disentangles global deliberation from local grounding. Concretely, it employs a Global Commander for high-level strategic planning and a Local Operative for egocentric observing and fine-grained execution. By disentangling global reasoning from local action, DACo alleviates cognitive overload and improves long-horizon stability. The framework further integrates dynamic subgoal planning and adaptive replanning to enable structured and resilient navigation. Extensive evaluations on R2R, REVERIE, and R4R demonstrate that DACo achieves 4.9%, 6.5%, 5.4% absolute improvements over the best-performing baselines in zero-shot settings, and generalizes effectively across both closed-source (e.g., GPT-4o) and open-source (e.g., Qwen-VL Series) backbones. DACo provides a principled and extensible paradigm for robust long-horizon navigation. Project page: https://github.com/ChocoWu/DACo

### 🤖 AI 总结

**一句话总结**：DACo提出“全局指挥官+本地执行者”的双代理解耦框架，将长程规划与局部感知执行分离，从而提升视觉-语言场景导航的长时稳定性与零样本性能。

**研究动机**：单代理往往同时承担全局推理与局部落地，长序列任务中易认知过载并产生指令漂移；多代理方案又带来协调与资源开销。作者希望以更低协作成本获得更稳健的长程导航能力。

**核心方法**：框架包含Global Commander负责高层策略与子目标生成，Local Operative基于自我视角观测进行细粒度动作执行与环境对齐。并引入动态子目标规划与自适应重规划机制，在执行偏离或环境变化时及时调整以保持结构化推进。

**主要结论**：在R2R、REVERIE、R4R的零样本评测中，DACo相对最佳基线取得约4.9%、6.5%、5.4%的绝对提升。该方法可在闭源（如GPT-4o）与开源（如Qwen-VL系列）骨干上有效泛化，表明解耦式规划-落地范式有助于鲁棒长程导航。

**关键词**：视觉语言导航, 具身智能, 自然语言指令跟随, 长时序导航, 双智能体架构, 全局规划, 局部感知与执行, 规划-落地解耦, 子目标规划, 自适应重规划, 零样本泛化

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18941v1) | [下载PDF](https://arxiv.org/pdf/2602.18941v1.pdf)

---

## cs.LG

## [12. Conditionally Site-Independent Neural Evolution of Antibody Sequences](https://arxiv.org/abs/2602.18982v1)

**作者**：Stephen Zhewen Lu, Aakarsh Vermani, Kohei Sanno 等 7 位作者  
**分类**：cs.LG, q-bio.PE  
**发布时间**：2026-02-21

### 📄 论文摘要

Common deep learning approaches for antibody engineering focus on modeling the marginal distribution of sequences. By treating sequences as independent samples, however, these methods overlook affinity maturation as a rich and largely untapped source of information about the evolutionary process by which antibodies explore the underlying fitness landscape. In contrast, classical phylogenetic models explicitly represent evolutionary dynamics but lack the expressivity to capture complex epistatic interactions. We bridge this gap with CoSiNE, a continuous-time Markov chain parameterized by a deep neural network. Mathematically, we prove that CoSiNE provides a first-order approximation to the intractable sequential point mutation process, capturing epistatic effects with an error bound that is quadratic in branch length. Empirically, CoSiNE outperforms state-of-the-art language models in zero-shot variant effect prediction by explicitly disentangling selection from context-dependent somatic hypermutation. Finally, we introduce Guided Gillespie, a classifier-guided sampling scheme that steers CoSiNE at inference time, enabling efficient optimization of antibody binding affinity toward specific antigens.

### 🤖 AI 总结

**一句话总结**：提出CoSiNE：用神经网络参数化的连续时间马尔可夫链来建模抗体亲和力成熟的进化过程，并在零样本变体效应预测与定向亲和力优化上优于现有语言模型。

**研究动机**：仅拟合抗体序列边缘分布的深度模型忽略了亲和力成熟中“沿谱系演化”的信息，而传统系统发育模型虽刻画动力学但难以表达复杂上位性与上下文依赖突变。

**核心方法**：构建CoSiNE（连续时间Markov链+深度网络参数化的替换率）以近似序列点突变过程，并给出误差随分支长度二次增长的理论界；同时显式分离选择效应与体细胞高突变的上下文效应，并提出Guided Gillespie在采样时用分类器引导以高效搜索特定抗原的高亲和力序列。

**主要结论**：CoSiNE在零样本变体效应预测上超过SOTA语言模型，说明将进化动力学与可表达的神经参数化结合能更好捕获上位性与选择/突变机制；Guided Gillespie进一步实现了面向目标抗原的高效亲和力优化生成。

**关键词**：抗体序列设计, 亲和力成熟建模, 体细胞超突变, 表观遗传互作, 适应度景观, 连续时间马尔可夫链, 神经参数化进化模型, 系统发育动力学, 零样本变体效应预测, 分类器引导采样, 结合亲和力优化

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18982v1) | [下载PDF](https://arxiv.org/pdf/2602.18982v1.pdf)

---

## [13. Incremental Transformer Neural Processes](https://arxiv.org/abs/2602.18955v1)

**作者**：Philip Mortimer, Cristiana Diaconu, Tommy Rochussen 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-21

### 📄 论文摘要

Neural Processes (NPs), and specifically Transformer Neural Processes (TNPs), have demonstrated remarkable performance across tasks ranging from spatiotemporal forecasting to tabular data modelling. However, many of these applications are inherently sequential, involving continuous data streams such as real-time sensor readings or database updates. In such settings, models should support cheap, incremental updates rather than recomputing internal representations from scratch for every new observation -- a capability existing TNP variants lack. Drawing inspiration from Large Language Models, we introduce the Incremental TNP (incTNP). By leveraging causal masking, Key-Value (KV) caching, and a data-efficient autoregressive training strategy, incTNP matches the predictive performance of standard TNPs while reducing the computational cost of updates from quadratic to linear time complexity. We empirically evaluate our model on a range of synthetic and real-world tasks, including tabular regression and temperature prediction. Our results show that, surprisingly, incTNP delivers performance comparable to -- or better than -- non-causal TNPs while unlocking orders-of-magnitude speedups for sequential inference. Finally, we assess the consistency of the model's updates -- by adapting a metric of ``implicit Bayesianness", we show that incTNP retains a prediction rule as implicitly Bayesian as standard non-causal TNPs, demonstrating that incTNP achieves the computational benefits of causal masking without sacrificing the consistency required for streaming inference.

### 🤖 AI 总结

**一句话总结**：提出可增量更新的 Incremental Transformer Neural Process（incTNP），用因果掩码与KV缓存将流式更新计算从二次降到线性，同时保持与标准TNP相当甚至更好的预测表现与一致性。

**研究动机**：许多TNP应用天然是连续数据流场景（传感器/数据库更新等），但现有TNP每来新观测常需重算内部表示，增量推理代价高且不适合实时部署。

**核心方法**：借鉴LLM推理机制，引入因果（自回归）注意力、Key-Value缓存以复用历史计算，并采用更数据高效的自回归训练策略，使模型能在新增观测时进行廉价的顺序更新与预测。

**主要结论**：在合成与真实任务（如表格回归、温度预测）上，incTNP预测精度与非因果TNP持平或更优，并在顺序推理中实现数量级加速；通过改造的“隐式贝叶斯性”指标验证其更新规则的一致性不逊于标准TNP。

**关键词**：序列推理, 因果掩蔽, KV缓存, 自回归训练, 温度预测, 表格回归, 计算效率, 隐式贝叶斯性

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18955v1) | [下载PDF](https://arxiv.org/pdf/2602.18955v1.pdf)

---

## [14. Toward Manifest Relationality in Transformers via Symmetry Reduction](https://arxiv.org/abs/2602.18948v1)

**作者**：J. François, L. Ravera  
**分类**：cs.LG, cs.NE, hep-th, stat.ML  
**发布时间**：2026-02-21

### 📄 论文摘要

Transformer models contain substantial internal redundancy arising from coordinate-dependent representations and continuous symmetries, in model space and in head space, respectively. While recent approaches address this by explicitly breaking symmetry, we propose a complementary framework based on symmetry reduction. We reformulate representations, attention mechanisms, and optimization dynamics in terms of invariant relational quantities, eliminating redundant degrees of freedom by construction. This perspective yields architectures that operate directly on relational structures, providing a principled geometric framework for reducing parameter redundancy and analyzing optimization.

### 🤖 AI 总结

**一句话总结**：本文提出用“对称性约化”把Transformer的表示与注意力改写为不变量的关系量，从构造上消除冗余并获得更具几何原则的架构与优化分析视角。

**研究动机**：Transformer内部存在由坐标依赖表示与连续对称性（模型空间/注意力头空间）带来的冗余自由度，导致参数与表示重复、难以分析优化过程。现有“显式破坏对称性”的方法不够系统，因此希望以更原则化的方式去除冗余。

**核心方法**：将表示、注意力机制以及优化动力学统一重写为对称群作用下的不变量（relational quantities），通过对称性约化在建模层面直接消掉冗余坐标/自由度。由此得到直接在关系结构上运算的Transformer变体，并提供用于理解参数冗余与训练行为的几何框架。

**主要结论**：以不变量关系量为核心的对称性约化可在不依赖人为“破坏对称性”的情况下系统性减少Transformer的内部冗余，并为架构设计与优化分析提供更清晰的几何解释。该视角预示可构造更参数高效、可解释性更强的关系型注意力模型。

**关键词**：连续对称性, 坐标无关表示, 不变量关系量, 关系表示学习, 注意力机制不变量, 优化动力学, 参数冗余消除, 几何深度学习, 头空间对称性

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18948v1) | [下载PDF](https://arxiv.org/pdf/2602.18948v1.pdf)

---

## [15. Exponential Convergence of (Stochastic) Gradient Descent for Separable Logistic Regression](https://arxiv.org/abs/2602.18946v1)

**作者**：Sacchit Kale, Piyushi Manupriya, Pierre Marion 等 5 位作者  
**分类**：cs.LG, math.OC  
**发布时间**：2026-02-21

### 📄 论文摘要

Gradient descent and stochastic gradient descent are central to modern machine learning, yet their behavior under large step sizes remains theoretically unclear. Recent work suggests that acceleration often arises near the edge of stability, where optimization trajectories become unstable and difficult to analyze. Existing results for separable logistic regression achieve faster convergence by explicitly leveraging such unstable regimes through constant or adaptive large step sizes. In this paper, we show that instability is not inherent to acceleration. We prove that gradient descent with a simple, non-adaptive increasing step-size schedule achieves exponential convergence for separable logistic regression under a margin condition, while remaining entirely within a stable optimization regime. The resulting method is anytime and does not require prior knowledge of the optimization horizon or target accuracy. We also establish exponential convergence of stochastic gradient descent using a lightweight adaptive step-size rule that avoids line search and specialized procedures, improving upon existing polynomial-rate guarantees. Together, our results demonstrate that carefully structured step-size growth alone suffices to obtain exponential acceleration for both gradient descent and stochastic gradient descent.

### 🤖 AI 总结

**一句话总结**：提出一种简单的步长增长策略，使可分逻辑回归上的（随机）梯度下降在稳定区间内仍能达到指数收敛。

**研究动机**：以往在可分逻辑回归中获得加速往往依赖“大步长/接近稳定边界”的不稳定轨迹，理论分析困难且常需调参或已知优化时域；作者希望证明加速不必依赖不稳定性，并给出更“anytime”的步长方案。

**核心方法**：对GD设计非自适应、单调递增的步长日程，在满足margin条件下证明其全程处于稳定优化区域且实现指数收敛；对SGD提出轻量级自适应步长规则（无需线搜索等复杂机制），并建立相应的指数收敛分析。

**主要结论**：不需要利用不稳定动力学，仅通过结构化的步长增长即可让可分逻辑回归的GD获得指数收敛并具备anytime性质；同时SGD也可用简洁自适应步长从已有的多项式收敛提升到指数收敛保证。

**关键词**：可分逻辑回归, 指数收敛, 梯度下降, 随机梯度下降, 步长增长策略, 自适应步长, 稳定优化, 稳定性边界, 间隔条件, 加速收敛

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18946v1) | [下载PDF](https://arxiv.org/pdf/2602.18946v1.pdf)

---

