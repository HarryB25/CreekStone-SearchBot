# arXiv AI 论文日报 | 2026-02-25

> 共 15 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (8 篇)
- [cs.CV](#csCV) (7 篇)

---

## cs.CV

## [1. Synergizing Understanding and Generation with Interleaved Analyzing-Drafting Thinking](https://arxiv.org/abs/2602.21435v1)

**作者**：Shengqiong Wu, Bobo Li, Xinkai Wang 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-24

### 📄 论文摘要

Unified Vision-Language Models (UVLMs) aim to advance multimodal learning by supporting both understanding and generation within a single framework. However, existing approaches largely focus on architectural unification while overlooking the need for explicit interaction between the two capabilities during task solving. As a result, current models treat understanding and generation as parallel skills rather than synergistic processes. To achieve real synergy, we introduce the interleaved Analyzing-Drafting problem-solving loop (AD-Loop), a new think paradigm that dynamically alternates between analytic and drafting operations. By interleaving textual thoughts with visual thoughts, AD-Loop enables models to iteratively refine both comprehension and outputs, fostering genuine synergy. To train this mechanism, we design a two-stage strategy: supervised learning on interleaved thought data to initialize alternation, followed by reinforcement learning to promote adaptive and autonomous control. Extensive experiments demonstrate that AD-Loop consistently improves performance across standard benchmarks for both understanding and generation, with strong transferability to various UVLMs architectures. Visual analyses further validate the effectiveness of implicit visual thoughts. These results highlight AD-Loop as a principled and broadly applicable strategy for synergizing comprehension and creation. The project page is at https://sqwu.top/AD-Loop.

### 🤖 AI 总结

**一句话总结**：提出交错的“分析-起草”思考循环（AD-Loop），让统一视觉语言模型在理解与生成间动态迭代，从而同时提升多模态理解与生成性能。

**研究动机**：现有UVLM多强调架构层面的统一，但在解题过程中缺少理解与生成的显式交互，导致两种能力更像并行技能而非相互促进的协同过程。

**核心方法**：AD-Loop在推理时交替进行分析（理解、推断）与起草（生成、改写）步骤，并将文本思考与隐式视觉思考交错融合以逐步修正认知与输出；训练采用两阶段：先用交错思维数据做监督学习初始化交替机制，再用强化学习学习更自适应的循环控制策略。

**主要结论**：在多种理解与生成基准上，AD-Loop带来稳定一致的提升，并能较好迁移到不同UVLM架构；可视化分析也支持“隐式视觉思考”确实有助于改进推理与生成质量。

**关键词**：统一视觉语言模型, 交错分析-起草循环, 交错思维链, 视觉思维, 文本-视觉交错推理, 两阶段训练, 监督微调, 强化学习控制, 多模态基准评测, 跨架构迁移

**评分**：38

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21435v1) | [下载PDF](https://arxiv.org/pdf/2602.21435v1.pdf)

---

## [2. PSF-Med: Measuring and Explaining Paraphrase Sensitivity in Medical Vision Language Models](https://arxiv.org/abs/2602.21428v1)

**作者**：Binesh Sadanandan, Vahid Behzadan  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-02-24

### 📄 论文摘要

Medical Vision Language Models (VLMs) can change their answers when clinicians rephrase the same question, which raises deployment risks. We introduce Paraphrase Sensitivity Failure (PSF)-Med, a benchmark of 19,748 chest Xray questions paired with about 92,000 meaningpreserving paraphrases across MIMIC-CXR and PadChest. Across six medical VLMs, we measure yes/no flips for the same image and find flip rates from 8% to 58%. However, low flip rate does not imply visual grounding: text-only baselines show that some models stay consistent even when the image is removed, suggesting they rely on language priors. To study mechanisms in one model, we apply GemmaScope 2 Sparse Autoencoders (SAEs) to MedGemma 4B and analyze FlipBank, a curated set of 158 flip cases. We identify a sparse feature at layer 17 that correlates with prompt framing and predicts decision margin shifts. In causal patching, removing this feature's contribution recovers 45% of the yesminus-no logit margin on average and fully reverses 15% of flips. Acting on this finding, we show that clamping the identified feature at inference reduces flip rates by 31% relative with only a 1.3 percentage-point accuracy cost, while also decreasing text-prior reliance. These results suggest that flip rate alone is not enough; robustness evaluations should test both paraphrase stability and image reliance.

### 🤖 AI 总结

**一句话总结**：PSF-Med提出一个医疗VLM复述敏感性基准，发现模型对同义改写会出现显著“是/否”翻转，并通过稀疏自编码器定位可干预的内部特征以降低翻转且代价很小。

**研究动机**：临床部署中同一问题的不同表述可能导致医疗VLM给出不同答案，带来安全与可信风险；且仅看翻转率可能掩盖模型其实主要依赖语言先验而非图像证据。

**核心方法**：构建PSF-Med（19,748个胸片问题+约92,000条保义复述）评测6个医学VLM的同图同义问法“yes/no翻转率”，并用去图文本基线检验图像依赖；进一步对MedGemma 4B用GemmaScope2的SAE分析FlipBank翻转样例，做因果patching并在推理时对关键稀疏特征进行clamp以减少翻转。

**主要结论**：不同医学VLM的翻转率高达8%–58%，且低翻转并不代表视觉扎根（去图仍可能保持一致）；在MedGemma中定位到与提示框架相关的层17稀疏特征，干预该特征可恢复部分logit margin并将翻转率相对降低31%且仅损失约1.3个百分点准确率，同时减少对文本先验的依赖。

**关键词**：医疗视觉语言模型, 释义鲁棒性, 释义敏感性失败, 胸部X光问答, 鲁棒性基准, 是非翻转率, 视觉基础评测, 文本先验依赖, 稀疏自编码器（SAE）, 可解释特征分析, 因果补丁, 推理时特征钳制

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21428v1) | [下载PDF](https://arxiv.org/pdf/2602.21428v1.pdf)

---

## [3. Automating Timed Up and Go Phase Segmentation and Gait Analysis via the tugturn Markerless 3D Pipeline](https://arxiv.org/abs/2602.21425v1)

**作者**：Abel Gonçalves Chinaglia, Guilherme Manna Cesar, Paulo Roberto Pereira Santiago  
**分类**：cs.CV  
**发布时间**：2026-02-24

### 📄 论文摘要

Instrumented Timed Up and Go (TUG) analysis can support clinical and research decision-making, but robust and reproducible markerless pipelines are still limited. We present \textit{tugturn.py}, a Python-based workflow for 3D markerless TUG processing that combines phase segmentation, gait-event detection, spatiotemporal metrics, intersegmental coordination, and dynamic stability analysis. The pipeline uses spatial thresholds to segment each trial into stand, first gait, turning, second gait, and sit phases, and applies a relative-distance strategy to detect heel-strike and toe-off events within valid gait windows. In addition to conventional kinematics, \textit{tugturn} provides Vector Coding outputs and Extrapolated Center of Mass (XCoM)-based metrics. The software is configured through TOML files and produces reproducible artifacts, including HTML reports, CSV tables, and quality-assurance visual outputs. A complete runnable example is provided with test data and command-line instructions. This manuscript describes the implementation, outputs, and reproducibility workflow of \textit{tugturn} as a focused software contribution for markerless biomechanical TUG analysis.

### 🤖 AI 总结

**一句话总结**：提出并开源了tugturn.py：一个可复现的无标记3D TUG自动处理流水线，覆盖相位分割、步态事件检测与多类步态/稳定性指标输出。

**研究动机**：临床与研究中的TUG量化分析需要稳健、可复现的无标记流程，但现有方案在自动分相、事件检测与标准化产物输出上仍较不足。

**核心方法**：用空间阈值将TUG分为起立、第一段行走、转身、第二段行走、坐下五相，并在有效步态窗口内用相对距离策略检测足跟着地/离地；同时计算时空参数、Vector Coding段间协调与基于XCoM的动态稳定性指标，采用TOML配置并输出HTML/CSV与质检可视化。

**主要结论**：tugturn提供了端到端、可配置且可复现的无标记3D TUG分析实现与示例数据/命令行流程，能够稳定产出分相、步态事件及传统与高级生物力学指标，作为聚焦软件贡献支撑标准化TUG研究与应用。

**关键词**：无标记3D动作捕捉, 步态阶段分割, 步态事件检测, 足跟着地/足尖离地, 步态时空参数, 动态稳定性分析, 外推质心（XCoM）, 可复现生物力学工作流

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21425v1) | [下载PDF](https://arxiv.org/pdf/2602.21425v1.pdf)

---

## [4. ECHOSAT: Estimating Canopy Height Over Space And Time](https://arxiv.org/abs/2602.21421v1)

**作者**：Jan Pauls, Karsten Schrödter, Sven Ligensa 等 10 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-02-24

### 📄 论文摘要

Forest monitoring is critical for climate change mitigation. However, existing global tree height maps provide only static snapshots and do not capture temporal forest dynamics, which are essential for accurate carbon accounting. We introduce ECHOSAT, a global and temporally consistent tree height map at 10 m resolution spanning multiple years. To this end, we resort to multi-sensor satellite data to train a specialized vision transformer model, which performs pixel-level temporal regression. A self-supervised growth loss regularizes the predictions to follow growth curves that are in line with natural tree development, including gradual height increases over time, but also abrupt declines due to forest loss events such as fires. Our experimental evaluation shows that our model improves state-of-the-art accuracies in the context of single-year predictions. We also provide the first global-scale height map that accurately quantifies tree growth and disturbances over time. We expect ECHOSAT to advance global efforts in carbon monitoring and disturbance assessment. The maps can be accessed at https://github.com/ai4forest/echosat.

### 🤖 AI 总结

**一句话总结**：ECHOSAT 利用多源卫星数据与专门的视觉Transformer，在10米分辨率上生成全球多年一致的树高时序图，实现对森林生长与扰动的动态监测。

**研究动机**：现有全球树高产品多为单一年份的静态快照，难以反映森林随时间的生长与损失，进而影响碳核算与扰动评估的准确性。

**核心方法**：融合多传感器卫星观测训练视觉Transformer做像素级时间回归，并引入自监督“生长损失”约束预测符合自然生长曲线（缓慢增高）且能刻画火灾等导致的突发下降。

**主要结论**：在单年树高预测上优于现有SOTA，同时提供首个全球尺度、可量化多年生长与扰动的10米树高时序地图，支持更可靠的碳监测与森林扰动评估。

**关键词**：冠层高度估计, 全球树高制图, 时序一致性制图, 多传感器遥感数据, 像素级时间回归, 自监督学习, 生长曲线正则化, 森林扰动监测, 森林火灾损失检测, 碳核算监测

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21421v1) | [下载PDF](https://arxiv.org/pdf/2602.21421v1.pdf)

---

## [5. WildSVG: Towards Reliable SVG Generation Under Real-Word Conditions](https://arxiv.org/abs/2602.21416v1)

**作者**：Marco Terral, Haotian Zhang, Tianyang Zhang 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-24

### 📄 论文摘要

We introduce the task of SVG extraction, which consists in translating specific visual inputs from an image into scalable vector graphics. Existing multimodal models achieve strong results when generating SVGs from clean renderings or textual descriptions, but they fall short in real-world scenarios where natural images introduce noise, clutter, and domain shifts. A central challenge in this direction is the lack of suitable benchmarks. To address this need, we introduce the WildSVG Benchmark, formed by two complementary datasets: Natural WildSVG, built from real images containing company logos paired with their SVG annotations, and Synthetic WildSVG, which blends complex SVG renderings into real scenes to simulate difficult conditions. Together, these resources provide the first foundation for systematic benchmarking SVG extraction. We benchmark state-of-the-art multimodal models and find that current approaches perform well below what is needed for reliable SVG extraction in real scenarios. Nonetheless, iterative refinement methods point to a promising path forward, and model capabilities are steadily improving

### 🤖 AI 总结

**一句话总结**：提出并构建 WildSVG 基准以评测“从真实世界图像中提取并生成SVG”的能力，发现现有多模态模型在真实噪声场景下显著不足，但迭代式精炼显示出改进潜力。

**研究动机**：现有SVG生成方法多在干净渲染或纯文本条件下表现良好，但面对真实照片中的噪声、遮挡与域偏移时可靠性不足；同时缺少可系统评测真实场景SVG提取的基准数据集。

**核心方法**：提出“SVG extraction”任务，并发布 WildSVG Benchmark：Natural WildSVG（真实图像中的公司logo与对应SVG标注）与 Synthetic WildSVG（将复杂SVG渲染合成到真实场景以模拟困难条件）；在该基准上系统评测多种SOTA多模态模型，并考察迭代式生成/精炼策略。

**主要结论**：实验表明当前SOTA模型在真实世界SVG提取上距离可用仍有明显差距；不过通过迭代精炼等方法可显著提升效果，且整体能力呈持续进步趋势。

**关键词**：多模态模型, 真实场景, 自然图像, 合成图像, 迭代优化, 基准评测, WildSVG, Towards

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21416v1) | [下载PDF](https://arxiv.org/pdf/2602.21416v1.pdf)

---

## [6. Exploring Vision-Language Models for Open-Vocabulary Zero-Shot Action Segmentation](https://arxiv.org/abs/2602.21406v1)

**作者**：Asim Unmesh, Kaki Ramesh, Mayank Patel 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-24

### 📄 论文摘要

Temporal Action Segmentation (TAS) requires dividing videos into action segments, yet the vast space of activities and alternative breakdowns makes collecting comprehensive datasets infeasible. Existing methods remain limited to closed vocabularies and fixed label sets. In this work, we explore the largely unexplored problem of Open-Vocabulary Zero-Shot Temporal Action Segmentation (OVTAS) by leveraging the strong zero-shot capabilities of Vision-Language Models (VLMs). We introduce a training-free pipeline that follows a segmentation-by-classification design: Frame-Action Embedding Similarity (FAES) matches video frames to candidate action labels, and Similarity-Matrix Temporal Segmentation (SMTS) enforces temporal consistency. Beyond proposing OVTAS, we present a systematic study across 14 diverse VLMs, providing the first broad analysis of their suitability for open-vocabulary action segmentation. Experiments on standard benchmarks show that OVTAS achieves strong results without task-specific supervision, underscoring the potential of VLMs for structured temporal understanding.

### 🤖 AI 总结

**一句话总结**：提出开放词汇零样本时序动作分割（OVTAS），用视觉-语言模型在无需训练的情况下将逐帧匹配与时序一致性分割结合，实现对任意候选动作标签的分割。

**研究动机**：TAS 面临动作类别空间巨大且标注代价高的问题，现有方法多依赖封闭标签集，难以泛化到未见动作。VLM 具备强零样本识别能力，因此探索其用于开放词汇的结构化时序理解。

**核心方法**：训练自由的“先分类再分割”流水线：用 FAES 计算帧特征与文本动作标签的嵌入相似度得到逐帧类别响应；再用 SMTS 基于相似度矩阵施加时序一致性约束，生成连续动作片段边界与标签。并系统评测 14 种 VLM 在 OVTAS 上的适用性。

**主要结论**：在标准基准上无需任务监督即可取得有竞争力的分割效果，表明 VLM 能支持开放词汇的时序动作理解。不同 VLM 在该任务上的表现存在显著差异，系统评测为选择/改进 VLM 用于动作分割提供了依据。

**关键词**：时序动作分割, 开放词表, 零样本学习, 视觉-语言模型, 训练-free 推理, 分割-分类框架, 帧-动作嵌入相似度, 相似度矩阵分割, 时序一致性约束, 多模型系统评测, 开放词表动作识别

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21406v1) | [下载PDF](https://arxiv.org/pdf/2602.21406v1.pdf)

---

## [7. FlowFixer: Towards Detail-Preserving Subject-Driven Generation](https://arxiv.org/abs/2602.21402v1)

**作者**：Jinyoung Jun, Won-Dong Jang, Wenbin Ouyang 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-24

### 📄 论文摘要

We present FlowFixer, a refinement framework for subject-driven generation (SDG) that restores fine details lost during generation caused by changes in scale and perspective of a subject. FlowFixer proposes direct image-to-image translation from visual references, avoiding ambiguities in language prompts. To enable image-to-image training, we introduce a one-step denoising scheme to generate self-supervised training data, which automatically removes high-frequency details while preserving global structure, effectively simulating real-world SDG errors. We further propose a keypoint matching-based metric to properly assess fidelity in details beyond semantic similarities usually measured by CLIP or DINO. Experimental results demonstrate that FlowFixer outperforms state-of-the-art SDG methods in both qualitative and quantitative evaluations, setting a new benchmark for high-fidelity subject-driven generation.

### 🤖 AI 总结

**一句话总结**：FlowFixer是一种细节保留的主题驱动生成框架，能够恢复在生成过程中因主题尺度和视角变化而丢失的细节。

**研究动机**：随着主题驱动生成技术的发展，如何有效恢复生成过程中丢失的细节成为重要研究问题。

**核心方法**：FlowFixer采用直接的图像到图像翻译方法，结合一步去噪方案生成自监督训练数据，并引入基于关键点匹配的度量标准以评估细节保真度。

**主要结论**：实验结果表明，FlowFixer在定性和定量评估中超越了现有的主题驱动生成方法，为高保真生成设定了新基准。

**关键词**：主体驱动生成, 细节保真生成, 图像到图像翻译, 视觉参考条件生成, 尺度与视角变化鲁棒性, 高频细节恢复, 自监督训练数据生成, 一步去噪方案, 退化模拟, 关键点匹配评测, 细节保真度评估

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21402v1) | [下载PDF](https://arxiv.org/pdf/2602.21402v1.pdf)

---

## cs.LG

## [8. MINAR: Mechanistic Interpretability for Neural Algorithmic Reasoning](https://arxiv.org/abs/2602.21442v1)

**作者**：Jesse He, Helen Jenne, Max Vargas 等 7 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-24

### 📄 论文摘要

The recent field of neural algorithmic reasoning (NAR) studies the ability of graph neural networks (GNNs) to emulate classical algorithms like Bellman-Ford, a phenomenon known as algorithmic alignment. At the same time, recent advances in large language models (LLMs) have spawned the study of mechanistic interpretability, which aims to identify granular model components like circuits that perform specific computations. In this work, we introduce Mechanistic Interpretability for Neural Algorithmic Reasoning (MINAR), an efficient circuit discovery toolbox that adapts attribution patching methods from mechanistic interpretability to the GNN setting. We show through two case studies that MINAR recovers faithful neuron-level circuits from GNNs trained on algorithmic tasks. Our study sheds new light on the process of circuit formation and pruning during training, as well as giving new insight into how GNNs trained to perform multiple tasks in parallel reuse circuit components for related tasks. Our code is available at https://github.com/pnnl/MINAR.

### 🤖 AI 总结

**一句话总结**：MINAR 将机制可解释性的归因/patching 电路发现方法迁移到GNN的神经算法推理任务上，能在神经元级别找出与经典算法对齐的可验证电路。

**研究动机**：NAR 关注GNN为何能“学会”执行如 Bellman-Ford 等算法，但缺少细粒度机制解释；机制可解释性在LLM上已发展出电路分析工具，作者希望将其引入GNN以揭示算法对齐的内部计算结构与训练过程。

**核心方法**：提出 MINAR 工具箱，改造 attribution patching 等方法以适配图结构与GNN计算流程，通过干预/替换激活并度量输出影响来高效定位对任务关键的神经元级电路；并用两个算法任务案例研究验证电路发现的忠实性与可解释性。

**主要结论**：MINAR 能从训练好的GNN中恢复出与算法执行相关的忠实电路，并揭示电路在训练中的形成与剪枝规律；在多任务并行训练时，模型会在相关任务间复用部分电路组件，说明存在可组合的共享计算子结构。

**关键词**：神经算法推理, 图神经网络, 算法对齐, 机制可解释性, 归因补丁, 神经元级电路, 多任务学习, 训练剪枝

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21442v1) | [下载PDF](https://arxiv.org/pdf/2602.21442v1.pdf)

---

## [9. Provably Safe Generative Sampling with Constricting Barrier Functions](https://arxiv.org/abs/2602.21429v1)

**作者**：Darshan Gadginmath, Ahmed Allibhoy, Fabio Pasqualetti  
**分类**：cs.LG, cs.AI, eess.SY, math.OC  
**发布时间**：2026-02-24

### 📄 论文摘要

Flow-based generative models, such as diffusion models and flow matching models, have achieved remarkable success in learning complex data distributions. However, a critical gap remains for their deployment in safety-critical domains: the lack of formal guarantees that generated samples will satisfy hard constraints. We address this by proposing a safety filtering framework that acts as an online shield for any pre-trained generative model. Our key insight is to cooperate with the generative process rather than override it. We define a constricting safety tube that is relaxed at the initial noise distribution and progressively tightens to the target safe set at the final data distribution, mirroring the coarse-to-fine structure of the generative process itself. By characterizing this tube via Control Barrier Functions (CBFs), we synthesize a feedback control input through a convex Quadratic Program (QP) at each sampling step. As the tube is loosest when noise is high and intervention is cheapest in terms of control energy, most constraint enforcement occurs when it least disrupts the model's learned structure. We prove that this mechanism guarantees safe sampling while minimizing the distributional shift from the original model at each sampling step, as quantified by the KL divergence. Our framework applies to any pre-trained flow-based generative scheme requiring no retraining or architectural modifications. We validate the approach across constrained image generation, physically-consistent trajectory sampling, and safe robotic manipulation policies, achieving 100% constraint satisfaction while preserving semantic fidelity.

### 🤖 AI 总结

**一句话总结**：提出一种无需重训的“安全过滤/护盾”框架，用控制屏障函数在采样过程中逐步收紧约束，证明可在最小分布偏移下实现可证明安全的生成采样。

**研究动机**：扩散/流式生成模型虽强，但在安全关键场景缺乏生成样本满足硬约束的形式化保证；现有做法往往强行改动模型或代价高、破坏语义。

**核心方法**：构造从初始噪声分布到最终安全集逐步收紧的“安全管道（tube）”，用控制屏障函数（CBF）刻画，并在每个采样步通过凸二次规划（QP）求解最小控制能量的反馈修正，使约束主要在早期高噪声阶段被低干扰地施加，同时给出逐步最小化KL偏移的理论保证。

**主要结论**：理论上证明该在线护盾能保证采样全程安全并在每步尽量贴近原生成分布；实验在受约束图像生成、物理一致轨迹与安全机器人操作中实现100%约束满足且保持语义/质量。

**关键词**：安全生成采样, 安全过滤器, 约束扩散模型, 流匹配模型, 控制障碍函数（CBF）, 二次规划（QP）, 硬约束满足, KL散度最小化, 约束图像生成, 安全机器人操控

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21429v1) | [下载PDF](https://arxiv.org/pdf/2602.21429v1.pdf)

---

## [10. Proximal-IMH: Proximal Posterior Proposals for Independent Metropolis-Hastings with Approximate Operators](https://arxiv.org/abs/2602.21426v1)

**作者**：Youguang Chen, George Biros  
**分类**：cs.LG, stat.CO  
**发布时间**：2026-02-24

### 📄 论文摘要

We consider the problem of sampling from a posterior distribution arising in Bayesian inverse problems in science, engineering, and imaging. Our method belongs to the family of independence Metropolis-Hastings (IMH) sampling algorithms, which are common in Bayesian inference. Relying on the existence of an approximate posterior distribution that is cheaper to sample from but may have significant bias, we introduce Proximal-IMH, a scheme that removes this bias by correcting samples from the approximate posterior through an auxiliary optimization problem. This yields a local adjustment that trades off adherence to the exact model against stability around the approximate reference point. For idealized settings, we prove that the proximal correction tightens the match between approximate and exact posteriors, thereby improving acceptance rates and mixing. The method applies to both linear and nonlinear input-output operators and is particularly suitable for inverse problems where exact posterior sampling is too expensive. We present numerical experiments including multimodal and data-driven priors with nonlinear input-output operators. The results show that Proximal-IMH reliably outperforms existing IMH variants.

### 🤖 AI 总结

**一句话总结**：Proximal-IMH 通过对廉价的近似后验样本做一次“近端优化校正”，在保持独立MH框架的同时显著降低近似偏差并提升采样效率。

**研究动机**：贝叶斯反问题中的精确后验采样代价高，而可快速采样的近似后验往往偏差大、导致IMH接受率和混合性变差；需要一种既利用近似后验的效率又能纠偏的通用机制。

**核心方法**：以近似后验作为独立提议分布，并对每个提议样本求解一个辅助优化（近端/Proximal校正）来做局部调整，在“贴近精确模型”与“围绕近似参考点稳定”之间权衡；理论上证明该校正可拉近近似与精确后验、提高接受率与混合，并适用于线性/非线性算子与多峰、数据驱动先验等场景。

**主要结论**：在理想化设定下，近端校正能系统性改善提议质量并提升IMH的接受率和混合性；数值实验表明在多种反问题设置中 Proximal-IMH 相比现有IMH变体更稳健、性能更优。

**关键词**：贝叶斯逆问题, 后验采样, 近似后验提议分布, 偏差校正, 辅助优化问题, 马尔可夫链混合, 接受率提升, 非线性前向算子, 多峰后验, 数据驱动先验

**评分**：19

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21426v1) | [下载PDF](https://arxiv.org/pdf/2602.21426v1.pdf)

---

## [11. On the Structural Non-Preservation of Epistemic Behaviour under Policy Transformation](https://arxiv.org/abs/2602.21424v1)

**作者**：Alexander Galozy  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-24

### 📄 论文摘要

Reinforcement learning (RL) agents under partial observability often condition actions on internally accumulated information such as memory or inferred latent context. We formalise such information-conditioned interaction patterns as behavioural dependency: variation in action selection with respect to internal information under fixed observations. This induces a probe-relative notion of $ε$-behavioural equivalence and a within-policy behavioural distance that quantifies probe sensitivity. We establish three structural results. First, the set of policies exhibiting non-trivial behavioural dependency is not closed under convex aggregation. Second, behavioural distance contracts under convex combination. Third, we prove a sufficient local condition under which gradient ascent on a skewed mixture objective decreases behavioural distance when a dominant-mode gradient aligns with the direction of steepest contraction. Minimal bandit and partially observable gridworld experiments provide controlled witnesses of these mechanisms. In the examined settings, behavioural distance decreases under convex aggregation and under continued optimisation with skewed latent priors, and in these experiments it precedes degradation under latent prior shift. These results identify structural conditions under which probe-conditioned behavioural separation is not preserved under common policy transformations.

### 🤖 AI 总结

**一句话总结**：论文提出“行为依赖性/行为距离”来刻画部分可观测RL中策略对内部信息（记忆/潜变量推断）的依赖，并证明这种“认知式行为分离”在常见的策略变换（如凸组合与继续优化）下往往不被结构性保留。

**研究动机**：在部分可观测环境里，智能体往往依赖内部状态而非仅依赖观测，但这种依赖在策略混合、集成或训练目标改变（例如潜变量先验偏置）后是否还能维持缺乏清晰理论刻画。

**核心方法**：将“固定观测下动作随内部信息变化”的现象形式化为行为依赖性，并定义探针（probe）相对的ε-行为等价与策略内行为距离，用于量化策略对探针/内部信息的敏感性；随后给出三个结构性定理并用最小bandit与部分可观测gridworld实验作机制见证。

**主要结论**：结果表明：非平凡行为依赖性的策略集合对凸聚合不封闭，且行为距离在凸组合下收缩；在带偏置的混合目标做梯度上升时，满足局部对齐条件会进一步降低行为距离，实验中这种距离下降常先于潜在先验漂移下的性能退化。

**关键词**：强化学习, 行为依赖, 部分可观测性, 行为距离, 策略变换, 凸聚合, 梯度上升, 潜在先验

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21424v1) | [下载PDF](https://arxiv.org/pdf/2602.21424v1.pdf)

---

## [12. Overconfident Errors Need Stronger Correction: Asymmetric Confidence Penalties for Reinforcement Learning](https://arxiv.org/abs/2602.21420v1)

**作者**：Yuanda Xu, Hejian Sang, Zhengze Zhou 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-24

### 📄 论文摘要

Reinforcement Learning with Verifiable Rewards (RLVR) has become the leading paradigm for enhancing reasoning in Large Language Models (LLMs). However, standard RLVR algorithms suffer from a well-documented pathology: while they improve Pass@1 accuracy through sharpened sampling, they simultaneously narrow the model's reasoning boundary and reduce generation diversity. We identify a root cause that existing methods overlook: the uniform penalization of errors. Current approaches -- whether data-filtering methods that select prompts by difficulty, or advantage normalization schemes -- treat all incorrect rollouts within a group identically. We show that this uniformity allows overconfident errors (incorrect reasoning paths that the RL process has spuriously reinforced) to persist and monopolize probability mass, ultimately suppressing valid exploratory trajectories. To address this, we propose the Asymmetric Confidence-aware Error Penalty (ACE). ACE introduces a per-rollout confidence shift metric, c_i = log(pi_theta(y_i|x) / pi_ref(y_i|x)), to dynamically modulate negative advantages. Theoretically, we demonstrate that ACE's gradient can be decomposed into the gradient of a selective regularizer restricted to overconfident errors, plus a well-characterized residual that partially moderates the regularizer's strength. We conduct extensive experiments fine-tuning Qwen2.5-Math-7B, Qwen3-8B-Base, and Llama-3.1-8B-Instruct on the DAPO-Math-17K dataset using GRPO and DAPO within the VERL framework. Evaluated on MATH-500 and AIME 2025, ACE composes seamlessly with existing methods and consistently improves the full Pass@k spectrum across all three model families and benchmarks.

### 🤖 AI 总结

**一句话总结**：本文提出了一种不对称置信罚（ACE）方法，旨在通过动态调节错误惩罚来改进强化学习中的推理能力，特别是针对过度自信的错误进行更强的修正。

**研究动机**：现有的强化学习可验证奖励算法在改善准确性和推理边界时，忽视了对错误的均匀惩罚，导致过度自信的错误持续存在并抑制了探索多样性。

**核心方法**：ACE方法引入了一种按回报动态调整的置信度偏移度量，结合选择性正则化来有针对性地修正过度自信的错误。

**主要结论**：通过在多个模型和基准测试中进行实验，ACE方法在提升准确性方面表现出色，改善了现有方法在全范围内的表现。

**关键词**：可验证奖励强化学习, LLM推理强化学习, 过度自信错误, 非对称错误惩罚, 置信度偏移, 负优势加权, 选择性正则化, 策略参考比率, 生成多样性

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21420v1) | [下载PDF](https://arxiv.org/pdf/2602.21420v1.pdf)

---

## [13. Benchmarking State Space Models, Transformers, and Recurrent Networks for US Grid Forecasting](https://arxiv.org/abs/2602.21415v1)

**作者**：Sunki Hong, Jisoo Lee, Yuanyuan Shi  
**分类**：cs.LG, eess.SY  
**发布时间**：2026-02-24

### 📄 论文摘要

Selecting the right deep learning model for power grid forecasting is challenging, as performance heavily depends on the data available to the operator. This paper presents a comprehensive benchmark of five modern neural architectures: two state space models (PowerMamba, S-Mamba), two Transformers (iTransformer, PatchTST), and a traditional LSTM. We evaluate these models on hourly electricity demand across six diverse US power grids for forecast windows between 24 and 168 hours. To ensure a fair comparison, we adapt each model with specialized temporal processing and a modular layer that cleanly integrates weather covariates. Our results reveal that there is no single best model for all situations. When forecasting using only historical load, PatchTST and the state space models provide the highest accuracy. However, when explicit weather data is added to the inputs, the rankings reverse: iTransformer improves its accuracy three times more efficiently than PatchTST. By controlling for model size, we confirm that this advantage stems from the architecture's inherent ability to mix information across different variables. Extending our evaluation to solar generation, wind power, and wholesale prices further demonstrates that model rankings depend on the forecast task: PatchTST excels on highly rhythmic signals like solar, while state space models are better suited for the chaotic fluctuations of wind and price. Ultimately, this benchmark provides grid operators with actionable guidelines for selecting the optimal forecasting architecture based on their specific data environments.

### 🤖 AI 总结

**一句话总结**：本文系统基准对比了状态空间模型、Transformer与LSTM在美国多电网负荷及多种能源/价格预测任务上的表现，发现最优架构强依赖输入特征（是否含天气）与任务信号特性（节律性 vs 混沌性）。

**研究动机**：电网预测中模型效果高度依赖运营方可用数据（仅历史负荷或含天气等协变量），导致“选哪种深度模型”缺乏通用结论与可操作指南。

**核心方法**：在6个美国电网的小时级负荷数据上，针对24–168小时预测窗口，公平比较PowerMamba、S-Mamba、iTransformer、PatchTST与LSTM，并为各模型统一加入专门的时间处理与可模块化融合天气协变量的层；同时控制模型规模并扩展到光伏、风电与批发电价任务。

**主要结论**：仅用历史负荷时，PatchTST与状态空间模型精度最高；加入显式天气后，iTransformer的改进效率显著高于PatchTST（约3倍），优势来自其跨变量信息混合能力而非模型大小。不同任务排名不同：PatchTST更适合强节律信号（如光伏），状态空间模型更适合波动更混沌的风电与电价。

**关键词**：电网负荷预测, 电力时间序列预测, 多变量时间序列, 外生变量融合, 气象协变量, 模型基准评测, 状态空间模型, 循环神经网络（LSTM）, 可再生能源预测, 电力现货价格预测, 多步预测（24-168h）

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21415v1) | [下载PDF](https://arxiv.org/pdf/2602.21415v1.pdf)

---

## [14. Generative Bayesian Computation as a Scalable Alternative to Gaussian Process Surrogates](https://arxiv.org/abs/2602.21408v1)

**作者**：Nick Polson, Vadim Sokolov  
**分类**：cs.LG, stat.AP, stat.CO, stat.ME, stat.ML  
**发布时间**：2026-02-24

### 📄 论文摘要

Gaussian process (GP) surrogates are the default tool for emulating expensive computer experiments, but cubic cost, stationarity assumptions, and Gaussian predictive distributions limit their reach. We propose Generative Bayesian Computation (GBC) via Implicit Quantile Networks (IQNs) as a surrogate framework that targets all three limitations. GBC learns the full conditional quantile function from input--output pairs; at test time, a single forward pass per quantile level produces draws from the predictive distribution.   Across fourteen benchmarks we compare GBC to four GP-based methods. GBC improves CRPS by 11--26\% on piecewise jump-process benchmarks, by 14\% on a ten-dimensional Friedman function, and scales linearly to 90,000 training points where dense-covariance GPs are infeasible. A boundary-augmented variant matches or outperforms Modular Jump GPs on two-dimensional jump datasets (up to 46\% CRPS improvement). In active learning, a randomized-prior IQN ensemble achieves nearly three times lower RMSE than deep GP active learning on Rocket LGBB. Overall, GBC records a favorable point estimate in 12 of 14 comparisons. GPs retain an edge on smooth surfaces where their smoothness prior provides effective regularization.

### 🤖 AI 总结

**一句话总结**：提出Generative Bayesian Computation（GBC）基于Implicit Quantile Networks（IQN）作为替代高斯过程（GP）的可扩展代理模型，在非平稳/跳变任务与大数据规模上取得更好预测分布质量。

**研究动机**：GP代理虽常用但存在训练立方复杂度、平稳性等先验假设限制，以及预测分布受高斯形状约束，难以处理跳变等复杂输出并扩展到大规模数据。作者希望用能直接学习更灵活预测分布且计算可线性扩展的方法替代GP。

**核心方法**：GBC用IQN从输入-输出对学习条件分位数函数（conditional quantile function），测试时对不同分位数水平一次前向传播即可采样得到预测分布；并提出边界增强变体与随机先验IQN集成用于主动学习提升不确定性与采样效率。

**主要结论**：在14个基准上，GBC在多数任务（12/14）给出更优点估计或分布评分，尤其在跳变/分段过程与高维函数上CRPS显著提升，并可线性扩展到9万训练点；但在光滑曲面上GP的平滑先验仍提供更强正则化而占优。

**关键词**：生成贝叶斯计算, 隐式分位网络, 高斯过程, 代理框架, 条件分位函数, 主动学习, 均方根误差, 训练点, 模块化跳跃GP

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21408v1) | [下载PDF](https://arxiv.org/pdf/2602.21408v1.pdf)

---

## [15. FedVG: Gradient-Guided Aggregation for Enhanced Federated Learning](https://arxiv.org/abs/2602.21399v1)

**作者**：Alina Devkota, Jacob Thrasher, Donald Adjeroh 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CV  
**发布时间**：2026-02-24

### 📄 论文摘要

Federated Learning (FL) enables collaborative model training across multiple clients without sharing their private data. However, data heterogeneity across clients leads to client drift, which degrades the overall generalization performance of the model. This effect is further compounded by overemphasis on poorly performing clients. To address this problem, we propose FedVG, a novel gradient-based federated aggregation framework that leverages a global validation set to guide the optimization process. Such a global validation set can be established using readily available public datasets, ensuring accessibility and consistency across clients without compromising privacy. In contrast to conventional approaches that prioritize client dataset volume, FedVG assesses the generalization ability of client models by measuring the magnitude of validation gradients across layers. Specifically, we compute layerwise gradient norms to derive a client-specific score that reflects how much each client needs to adjust for improved generalization on the global validation set, thereby enabling more informed and adaptive federated aggregation. Extensive experiments on both natural and medical image benchmarking datasets, across diverse model architectures, demonstrate that FedVG consistently improves performance, particularly in highly heterogeneous settings. Moreover, FedVG is modular and can be seamlessly integrated with various state-of-the-art FL algorithms, often further improving their results. Our code is available at https://github.com/alinadevkota/FedVG.

### 🤖 AI 总结

**一句话总结**：FedVG利用全局验证集的分层验证梯度范数为客户端打分并自适应聚合，从而在数据高度异质的联邦学习中提升泛化性能。

**研究动机**：联邦学习中客户端数据异质性会导致client drift并损害全局模型泛化，且按数据量加权可能过度强调表现差的客户端。需要一种能直接反映“对泛化有帮助程度”的聚合依据。

**核心方法**：引入可由公共数据构建的全局验证集，用其计算各客户端模型在各层的验证梯度范数，并据此形成客户端得分（表示为提升全局验证泛化需调整的幅度）。聚合时不再仅按样本量，而是依据该得分进行更有信息的加权/选择，并可模块化接入多种现有FL算法。

**主要结论**：在自然图像与医学图像等多数据集、多架构实验中，FedVG在异质性更强的场景下稳定提升性能；同时作为通用聚合模块，常能进一步增强现有联邦学习方法的效果。

**关键词**：联邦学习, 客户端漂移, 梯度引导聚合, 验证梯度, 全局验证集, 公共数据集, 层级梯度范数, 客户端加权, 自适应聚合, 跨客户端泛化, 医学影像联邦学习

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21399v1) | [下载PDF](https://arxiv.org/pdf/2602.21399v1.pdf)

---

