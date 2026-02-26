# arXiv AI 论文日报 | 2026-02-24

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

**一句话总结**：提出“交错分析-起草循环”(AD-Loop)思维范式，让统一视觉语言模型在理解与生成之间动态交替推理，从而实现更强的协同解题能力。

**研究动机**：现有UVLM多停留在结构统一层面，理解与生成在解题时缺少显式互动，导致两种能力更像并行技能而非相互促进的过程。

**核心方法**：设计AD-Loop，在文本与“视觉思考”之间交错进行分析与草拟、迭代修正理解与输出；训练上采用两阶段：先用交错思维数据做监督学习初始化交替模式，再用强化学习促使模型自适应地控制交替与策略。

**主要结论**：在多项理解与生成基准上，AD-Loop稳定提升性能，并可迁移到不同UVLM架构；可视化分析表明隐式视觉思考有效支撑了这种理解-生成的协同优化。

**关键词**：统一视觉语言模型, 交错分析-起草循环, 交错思维链, 文本-视觉思维融合, 两阶段训练, 监督微调, 强化学习, 隐式视觉思维, 跨架构迁移

**评分**：37

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21435v1) | [下载PDF](https://arxiv.org/pdf/2602.21435v1.pdf)

---

## [2. PSF-Med: Measuring and Explaining Paraphrase Sensitivity in Medical Vision Language Models](https://arxiv.org/abs/2602.21428v1)

**作者**：Binesh Sadanandan, Vahid Behzadan  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-02-24

### 📄 论文摘要

Medical Vision Language Models (VLMs) can change their answers when clinicians rephrase the same question, which raises deployment risks. We introduce Paraphrase Sensitivity Failure (PSF)-Med, a benchmark of 19,748 chest Xray questions paired with about 92,000 meaningpreserving paraphrases across MIMIC-CXR and PadChest. Across six medical VLMs, we measure yes/no flips for the same image and find flip rates from 8% to 58%. However, low flip rate does not imply visual grounding: text-only baselines show that some models stay consistent even when the image is removed, suggesting they rely on language priors. To study mechanisms in one model, we apply GemmaScope 2 Sparse Autoencoders (SAEs) to MedGemma 4B and analyze FlipBank, a curated set of 158 flip cases. We identify a sparse feature at layer 17 that correlates with prompt framing and predicts decision margin shifts. In causal patching, removing this feature's contribution recovers 45% of the yesminus-no logit margin on average and fully reverses 15% of flips. Acting on this finding, we show that clamping the identified feature at inference reduces flip rates by 31% relative with only a 1.3 percentage-point accuracy cost, while also decreasing text-prior reliance. These results suggest that flip rate alone is not enough; robustness evaluations should test both paraphrase stability and image reliance.

### 🤖 AI 总结

**一句话总结**：PSF-Med 系统评测医学VLM对同义改写问题的敏感性，发现大量“答案翻转”且部分稳定性来自语言先验而非图像理解，并提出基于稀疏特征干预的方法显著降低翻转。

**研究动机**：临床中同一问题的不同表述可能导致医学VLM输出改变，带来部署风险；同时仅看一致性无法判断模型是否真正依赖影像证据。

**核心方法**：构建包含19,748个胸片问题与约92,000个语义等价改写的PSF-Med基准，在6个医学VLM上测量同图同义问句的yes/no翻转率并用text-only基线检验“去图像”依赖；进一步对MedGemma 4B用GemmaScope 2 SAE分析FlipBank翻转样例，定位与提示框架相关的稀疏特征并通过因果patching与推理时clamp进行干预。

**主要结论**：不同模型翻转率达8%~58%，且低翻转率不代表良好视觉对齐（可能只是语言先验导致的稳定）；对单个关键稀疏特征进行干预可恢复logit margin并使翻转率相对下降31%，仅带来约1.3个百分点精度损失，同时降低对文本先验的依赖。

**关键词**：医疗视觉语言模型, 胸部X光问答, 释义鲁棒性, 提示改写敏感性, 视觉依赖评测, 语言先验偏置, 基准数据集, 回答翻转率, 稀疏自编码器（SAE）, 推理时特征钳制

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21428v1) | [下载PDF](https://arxiv.org/pdf/2602.21428v1.pdf)

---

## [3. Automating Timed Up and Go Phase Segmentation and Gait Analysis via the tugturn Markerless 3D Pipeline](https://arxiv.org/abs/2602.21425v1)

**作者**：Abel Gonçalves Chinaglia, Guilherme Manna Cesar, Paulo Roberto Pereira Santiago  
**分类**：cs.CV  
**发布时间**：2026-02-24

### 📄 论文摘要

Instrumented Timed Up and Go (TUG) analysis can support clinical and research decision-making, but robust and reproducible markerless pipelines are still limited. We present \textit{tugturn.py}, a Python-based workflow for 3D markerless TUG processing that combines phase segmentation, gait-event detection, spatiotemporal metrics, intersegmental coordination, and dynamic stability analysis. The pipeline uses spatial thresholds to segment each trial into stand, first gait, turning, second gait, and sit phases, and applies a relative-distance strategy to detect heel-strike and toe-off events within valid gait windows. In addition to conventional kinematics, \textit{tugturn} provides Vector Coding outputs and Extrapolated Center of Mass (XCoM)-based metrics. The software is configured through TOML files and produces reproducible artifacts, including HTML reports, CSV tables, and quality-assurance visual outputs. A complete runnable example is provided with test data and command-line instructions. This manuscript describes the implementation, outputs, and reproducibility workflow of \textit{tugturn} as a focused software contribution for markerless biomechanical TUG analysis.

### 🤖 AI 总结

**一句话总结**：论文提出并开源了一个名为 tugturn.py 的无标记3D TUG（Timed Up and Go）分析流水线，可自动完成分期、步态事件检测与多种生物力学指标输出，并强调可复现的报告化产出。

**研究动机**：TUG 在临床与研究中常用，但现有无标记（markerless）处理流程在鲁棒性、标准化与可复现性方面仍不足，限制了跨实验/跨场景对比与落地应用。

**核心方法**：通过空间阈值将一次TUG试次分割为起立、第一段步行、转身、第二段步行、坐下五个阶段，并在有效步行窗口内用相对距离策略检测 heel-strike/toe-off；同时计算时空参数、矢量编码（Vector Coding）协同指标与基于 XCoM 的动态稳定性指标，并用TOML配置与自动生成HTML/CSV/质检可视化确保复现。

**主要结论**：tugturn 提供了一个覆盖分期、事件检测、指标计算与可复现报告的端到端无标记TUG软件实现，降低了规范化生物力学TUG分析的门槛并便于复用与审计。

**关键词**：无标记动作捕捉, 三维人体姿态估计, 阶段分割, 步态事件检测, 时空步态指标, 关节间协调, 动态稳定性, 外推质心（XCoM）, 可复现生物力学流水线

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21425v1) | [下载PDF](https://arxiv.org/pdf/2602.21425v1.pdf)

---

## [4. ECHOSAT: Estimating Canopy Height Over Space And Time](https://arxiv.org/abs/2602.21421v1)

**作者**：Jan Pauls, Karsten Schrödter, Sven Ligensa 等 10 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-02-24

### 📄 论文摘要

Forest monitoring is critical for climate change mitigation. However, existing global tree height maps provide only static snapshots and do not capture temporal forest dynamics, which are essential for accurate carbon accounting. We introduce ECHOSAT, a global and temporally consistent tree height map at 10 m resolution spanning multiple years. To this end, we resort to multi-sensor satellite data to train a specialized vision transformer model, which performs pixel-level temporal regression. A self-supervised growth loss regularizes the predictions to follow growth curves that are in line with natural tree development, including gradual height increases over time, but also abrupt declines due to forest loss events such as fires. Our experimental evaluation shows that our model improves state-of-the-art accuracies in the context of single-year predictions. We also provide the first global-scale height map that accurately quantifies tree growth and disturbances over time. We expect ECHOSAT to advance global efforts in carbon monitoring and disturbance assessment. The maps can be accessed at https://github.com/ai4forest/echosat.

### 🤖 AI 总结

**一句话总结**：ECHOSAT 利用多传感器卫星数据与专用视觉Transformer，生成全球10m分辨率、跨多年的时序一致树高地图，能同时刻画生长与扰动。

**研究动机**：现有全球树高产品多为单年份静态快照，无法反映森林随时间的生长与火灾/砍伐等突发下降，从而限制碳核算与扰动评估的准确性。

**核心方法**：融合多源卫星观测训练一个进行像素级时间回归的Vision Transformer，并引入自监督“生长损失”约束预测符合自然生长曲线（缓慢增高）且允许森林损失事件导致的突降。

**主要结论**：在单年份树高预测精度上优于现有方法，并首次提供能够在全球尺度上可靠量化树高增长与扰动的多年序列地图，支持碳监测与灾害/扰动评估。

**关键词**：林冠高度估计, 全球树高制图, 时序森林动态, 多传感器遥感融合, 10米分辨率, 像素级时间回归, 自监督学习损失, 树木生长曲线约束, 森林扰动检测, 火灾致损监测, 碳核算监测

**评分**：37

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21421v1) | [下载PDF](https://arxiv.org/pdf/2602.21421v1.pdf)

---

## [5. WildSVG: Towards Reliable SVG Generation Under Real-Word Conditions](https://arxiv.org/abs/2602.21416v1)

**作者**：Marco Terral, Haotian Zhang, Tianyang Zhang 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-24

### 📄 论文摘要

We introduce the task of SVG extraction, which consists in translating specific visual inputs from an image into scalable vector graphics. Existing multimodal models achieve strong results when generating SVGs from clean renderings or textual descriptions, but they fall short in real-world scenarios where natural images introduce noise, clutter, and domain shifts. A central challenge in this direction is the lack of suitable benchmarks. To address this need, we introduce the WildSVG Benchmark, formed by two complementary datasets: Natural WildSVG, built from real images containing company logos paired with their SVG annotations, and Synthetic WildSVG, which blends complex SVG renderings into real scenes to simulate difficult conditions. Together, these resources provide the first foundation for systematic benchmarking SVG extraction. We benchmark state-of-the-art multimodal models and find that current approaches perform well below what is needed for reliable SVG extraction in real scenarios. Nonetheless, iterative refinement methods point to a promising path forward, and model capabilities are steadily improving

### 🤖 AI 总结

**一句话总结**：提出面向真实场景的SVG提取任务与WildSVG基准，系统评测发现现有多模态模型在自然图像噪声下的SVG生成仍明显不可靠。

**研究动机**：现有模型在干净渲染或纯文本条件下能生成SVG，但在真实照片中受噪声、遮挡与域偏移影响表现显著下降；同时缺乏能反映真实困难的统一评测基准。

**核心方法**：构建WildSVG Benchmark：包含真实图像公司Logo及其SVG标注的Natural WildSVG，以及将复杂SVG渲染合成到真实场景以模拟困难条件的Synthetic WildSVG；在该基准上对多种SOTA多模态模型进行对比评测，并探索迭代式精炼生成策略。

**主要结论**：基准测试显示当前方法距离真实可用的可靠SVG提取仍有差距，但迭代精炼等策略展现出改进潜力，且模型能力整体呈持续提升趋势。

**关键词**：图像到矢量图, 真实场景鲁棒性, 噪声与遮挡, 域偏移, 多模态模型评测, 基准测试数据集, 合成数据生成, 迭代式精炼

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21416v1) | [下载PDF](https://arxiv.org/pdf/2602.21416v1.pdf)

---

## [6. Exploring Vision-Language Models for Open-Vocabulary Zero-Shot Action Segmentation](https://arxiv.org/abs/2602.21406v1)

**作者**：Asim Unmesh, Kaki Ramesh, Mayank Patel 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-24

### 📄 论文摘要

Temporal Action Segmentation (TAS) requires dividing videos into action segments, yet the vast space of activities and alternative breakdowns makes collecting comprehensive datasets infeasible. Existing methods remain limited to closed vocabularies and fixed label sets. In this work, we explore the largely unexplored problem of Open-Vocabulary Zero-Shot Temporal Action Segmentation (OVTAS) by leveraging the strong zero-shot capabilities of Vision-Language Models (VLMs). We introduce a training-free pipeline that follows a segmentation-by-classification design: Frame-Action Embedding Similarity (FAES) matches video frames to candidate action labels, and Similarity-Matrix Temporal Segmentation (SMTS) enforces temporal consistency. Beyond proposing OVTAS, we present a systematic study across 14 diverse VLMs, providing the first broad analysis of their suitability for open-vocabulary action segmentation. Experiments on standard benchmarks show that OVTAS achieves strong results without task-specific supervision, underscoring the potential of VLMs for structured temporal understanding.

### 🤖 AI 总结

**一句话总结**：提出并系统评估一种基于视觉-语言模型的开放词表零样本时序动作分割（OVTAS）训练免方案，在无需任务监督下取得有竞争力的分割效果。

**研究动机**：传统时序动作分割依赖封闭标签与标注数据，但现实动作类别空间巨大且分解方式多样，难以覆盖；因此需要能在开放词表、零样本条件下泛化的方法。

**核心方法**：采用“先分类后分割”的训练免流水线：用FAES计算帧特征与候选动作文本嵌入的相似度完成帧级匹配，再用SMTS基于相似度矩阵施加时间一致性以得到稳定的动作段边界；并在14个VLM上做系统对比分析。

**主要结论**：实验表明该OVTAS在标准基准上无需额外训练即可获得强结果，不同VLM对时序分割适配性存在差异，整体验证了VLM在开放词表结构化时序理解中的潜力。

**关键词**：时间动作分割, 开放词表, 零样本学习, 视觉-语言模型（VLM）, 分割-分类范式, 帧-动作嵌入相似度（FAES）, 相似度矩阵时间分割（SMTS）, 时间一致性约束, 开放词表动作分割评测

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21406v1) | [下载PDF](https://arxiv.org/pdf/2602.21406v1.pdf)

---

## [7. FlowFixer: Towards Detail-Preserving Subject-Driven Generation](https://arxiv.org/abs/2602.21402v1)

**作者**：Jinyoung Jun, Won-Dong Jang, Wenbin Ouyang 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-24

### 📄 论文摘要

We present FlowFixer, a refinement framework for subject-driven generation (SDG) that restores fine details lost during generation caused by changes in scale and perspective of a subject. FlowFixer proposes direct image-to-image translation from visual references, avoiding ambiguities in language prompts. To enable image-to-image training, we introduce a one-step denoising scheme to generate self-supervised training data, which automatically removes high-frequency details while preserving global structure, effectively simulating real-world SDG errors. We further propose a keypoint matching-based metric to properly assess fidelity in details beyond semantic similarities usually measured by CLIP or DINO. Experimental results demonstrate that FlowFixer outperforms state-of-the-art SDG methods in both qualitative and quantitative evaluations, setting a new benchmark for high-fidelity subject-driven generation.

### 🤖 AI 总结

**一句话总结**：FlowFixer 提出一种面向主体驱动生成的细节修复框架，通过参考图像的端到端翻译恢复因尺度/视角变化而丢失的主体高频细节，并引入更合适的细节保真评测指标。

**研究动机**：现有主体驱动生成在主体发生尺度与视角变化时容易丢失纹理等细节，而依赖文本提示会带来描述歧义，且常用 CLIP/DINO 相似度难以真实反映细节保真度。

**核心方法**：采用“参考图像→生成结果”的直接图像到图像精修以避免语言歧义；提出一步去噪的自监督数据合成方案，自动抹去高频细节但保留全局结构以模拟真实 SDG 误差；并设计基于关键点匹配的细节保真度量用于评估。

**主要结论**：在定性与定量实验中，FlowFixer 相比现有 SOTA 主体驱动生成方法能更好恢复主体细节并取得更高的细节保真指标表现，从而树立高保真 SDG 的新基准。

**关键词**：主体驱动生成, 细节保持生成, 图像到图像翻译, 视觉参考条件生成, 自监督数据生成, 一步去噪, 高频细节恢复, 尺度与视角鲁棒性, 关键点匹配指标, 细节保真评测, CLIP/DINO语义相似度局限

**评分**：31

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

**一句话总结**：MINAR将机制可解释性中的归因补丁（attribution patching）方法迁移到GNN的神经算法推理中，高效发现能实现算法计算的神经元级电路。

**研究动机**：神经算法推理研究表明GNN能对齐经典算法，但其内部如何形成“算法电路”仍不清晰；机制可解释性提供了定位具体计算回路的思路，但缺少面向GNN/NAR的实用工具。

**核心方法**：提出MINAR电路发现工具箱，将归因补丁等电路定位技术适配到GNN结构上，并在算法任务训练的GNN中进行神经元级电路提取与验证；通过两个案例研究分析训练过程中的电路形成/剪枝，以及多任务并行训练时电路组件的复用。

**主要结论**：MINAR能够从NAR-GNN中恢复“忠实”的神经元级电路，揭示电路在训练中逐步形成并被剪枝的动态过程；同时发现多任务设置下相关任务会共享与复用部分电路组件，从而提供对算法对齐机理的更细粒度解释。

**关键词**：神经算法推理, 图神经网络, 算法对齐, 机理可解释性, 归因补丁, 神经元级电路, 经典算法模拟, 训练剪枝

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21442v1) | [下载PDF](https://arxiv.org/pdf/2602.21442v1.pdf)

---

## [9. Provably Safe Generative Sampling with Constricting Barrier Functions](https://arxiv.org/abs/2602.21429v1)

**作者**：Darshan Gadginmath, Ahmed Allibhoy, Fabio Pasqualetti  
**分类**：cs.LG, cs.AI, eess.SY, math.OC  
**发布时间**：2026-02-24

### 📄 论文摘要

Flow-based generative models, such as diffusion models and flow matching models, have achieved remarkable success in learning complex data distributions. However, a critical gap remains for their deployment in safety-critical domains: the lack of formal guarantees that generated samples will satisfy hard constraints. We address this by proposing a safety filtering framework that acts as an online shield for any pre-trained generative model. Our key insight is to cooperate with the generative process rather than override it. We define a constricting safety tube that is relaxed at the initial noise distribution and progressively tightens to the target safe set at the final data distribution, mirroring the coarse-to-fine structure of the generative process itself. By characterizing this tube via Control Barrier Functions (CBFs), we synthesize a feedback control input through a convex Quadratic Program (QP) at each sampling step. As the tube is loosest when noise is high and intervention is cheapest in terms of control energy, most constraint enforcement occurs when it least disrupts the model's learned structure. We prove that this mechanism guarantees safe sampling while minimizing the distributional shift from the original model at each sampling step, as quantified by the KL divergence. Our framework applies to any pre-trained flow-based generative scheme requiring no retraining or architectural modifications. We validate the approach across constrained image generation, physically-consistent trajectory sampling, and safe robotic manipulation policies, achieving 100% constraint satisfaction while preserving semantic fidelity.

### 🤖 AI 总结

**一句话总结**：提出一种无需重训练的“安全过滤/护盾”框架，用控制屏障函数在生成采样过程中逐步收紧约束，理论上保证生成样本满足硬约束且尽量不偏离原模型分布。

**研究动机**：扩散/流式生成模型虽能生成高质量样本，但在安全关键场景缺乏“生成结果必满足硬约束”的形式化保证，限制了实际部署。

**核心方法**：构造从初始噪声到最终安全集合逐步收紧的“安全管道”，用控制屏障函数（CBF）表征并在每个采样步通过凸二次规划（QP）求解最小干预的反馈控制输入；同时证明该干预在每步以KL散度意义下最小化对原生成分布的偏移并保证安全性。

**主要结论**：方法可作为任意预训练流式生成模型的在线安全盾牌，实现100%约束满足，并在受限图像生成、物理一致轨迹采样与安全机器人操作策略等任务中保持较高语义/任务保真度。

**关键词**：生成模型, 安全过滤, 控制屏障函数, 约束采样, 分布转移, 图像生成, 轨迹采样, 机器人操控

**评分**：42

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21429v1) | [下载PDF](https://arxiv.org/pdf/2602.21429v1.pdf)

---

## [10. Proximal-IMH: Proximal Posterior Proposals for Independent Metropolis-Hastings with Approximate Operators](https://arxiv.org/abs/2602.21426v1)

**作者**：Youguang Chen, George Biros  
**分类**：cs.LG, stat.CO  
**发布时间**：2026-02-24

### 📄 论文摘要

We consider the problem of sampling from a posterior distribution arising in Bayesian inverse problems in science, engineering, and imaging. Our method belongs to the family of independence Metropolis-Hastings (IMH) sampling algorithms, which are common in Bayesian inference. Relying on the existence of an approximate posterior distribution that is cheaper to sample from but may have significant bias, we introduce Proximal-IMH, a scheme that removes this bias by correcting samples from the approximate posterior through an auxiliary optimization problem. This yields a local adjustment that trades off adherence to the exact model against stability around the approximate reference point. For idealized settings, we prove that the proximal correction tightens the match between approximate and exact posteriors, thereby improving acceptance rates and mixing. The method applies to both linear and nonlinear input-output operators and is particularly suitable for inverse problems where exact posterior sampling is too expensive. We present numerical experiments including multimodal and data-driven priors with nonlinear input-output operators. The results show that Proximal-IMH reliably outperforms existing IMH variants.

### 🤖 AI 总结

**一句话总结**：Proximal-IMH 通过对“便宜但有偏”的近似后验样本做一次近端优化校正，在保持独立MH框架下显著提高对真实后验的贴合度与采样效率。

**研究动机**：贝叶斯逆问题的精确后验采样常因前向算子昂贵而难以进行，而直接用可快速采样的近似后验又会引入明显偏差并导致IMH接受率/混合变差。

**核心方法**：以近似后验为独立提议分布，并在每次提议后求解一个辅助“近端/正则化”的优化问题，对样本做局部调整，在贴近精确模型与围绕近似参考点保持稳定之间折中；理论上证明该校正可收紧近似与精确后验的差异，从而改善接受率与混合。

**主要结论**：在理想化设定下给出接受率与混合改善的理论保证，并在包含多峰分布、数据驱动先验及非线性算子的数值实验中稳定优于现有IMH变体，适用于线性与非线性逆问题的高成本后验采样。

**关键词**：后验分布, 贝叶斯逆问题, 近似后验, 优化问题, 接受率, 混合性, 非线性输入输出, 数值实验

**评分**：17

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21426v1) | [下载PDF](https://arxiv.org/pdf/2602.21426v1.pdf)

---

## [11. On the Structural Non-Preservation of Epistemic Behaviour under Policy Transformation](https://arxiv.org/abs/2602.21424v1)

**作者**：Alexander Galozy  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-24

### 📄 论文摘要

Reinforcement learning (RL) agents under partial observability often condition actions on internally accumulated information such as memory or inferred latent context. We formalise such information-conditioned interaction patterns as behavioural dependency: variation in action selection with respect to internal information under fixed observations. This induces a probe-relative notion of $ε$-behavioural equivalence and a within-policy behavioural distance that quantifies probe sensitivity. We establish three structural results. First, the set of policies exhibiting non-trivial behavioural dependency is not closed under convex aggregation. Second, behavioural distance contracts under convex combination. Third, we prove a sufficient local condition under which gradient ascent on a skewed mixture objective decreases behavioural distance when a dominant-mode gradient aligns with the direction of steepest contraction. Minimal bandit and partially observable gridworld experiments provide controlled witnesses of these mechanisms. In the examined settings, behavioural distance decreases under convex aggregation and under continued optimisation with skewed latent priors, and in these experiments it precedes degradation under latent prior shift. These results identify structural conditions under which probe-conditioned behavioural separation is not preserved under common policy transformations.

### 🤖 AI 总结

**一句话总结**：在部分可观测RL中，策略对内部信息（记忆/潜变量推断）的“行为依赖”在常见的策略变换（凸组合与特定优化过程）下可能不被结构性保持，并往往表现为可探测的行为差异被压缩。

**研究动机**：现实中的POMDP智能体常依赖内部状态做决策，但实践里经常对策略做集成/混合或继续优化；作者希望弄清这些变换是否会破坏（或削弱）这种“基于内部信息的可区分行为”。

**核心方法**：形式化“行为依赖”为在固定观测下动作分布随内部信息变化，并据此定义探针相对的ε-行为等价与策略内的行为距离（衡量探针敏感度）；随后给出关于凸聚合与梯度上升（偏置混合目标）的三个结构性定理，并用最小bandit与部分可观测gridworld做对照实验验证机制。

**主要结论**：(1) 具有非平凡行为依赖的策略集合对凸聚合不封闭；(2) 行为距离在凸组合下收缩；(3) 在满足局部条件时，针对偏置混合目标的梯度上升会进一步降低行为距离；实验中观察到行为距离随聚合/继续优化下降，且其下降往往先于潜在先验移位下的性能退化。

**关键词**：强化学习, 部分可观测环境, 策略变换, 行为依赖, 行为等价（ε）, 行为距离, 探针敏感性, 凸组合策略, 梯度上升, 混合目标, 潜在先验偏移, 部分可观测网格世界

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21424v1) | [下载PDF](https://arxiv.org/pdf/2602.21424v1.pdf)

---

## [12. Overconfident Errors Need Stronger Correction: Asymmetric Confidence Penalties for Reinforcement Learning](https://arxiv.org/abs/2602.21420v1)

**作者**：Yuanda Xu, Hejian Sang, Zhengze Zhou 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-24

### 📄 论文摘要

Reinforcement Learning with Verifiable Rewards (RLVR) has become the leading paradigm for enhancing reasoning in Large Language Models (LLMs). However, standard RLVR algorithms suffer from a well-documented pathology: while they improve Pass@1 accuracy through sharpened sampling, they simultaneously narrow the model's reasoning boundary and reduce generation diversity. We identify a root cause that existing methods overlook: the uniform penalization of errors. Current approaches -- whether data-filtering methods that select prompts by difficulty, or advantage normalization schemes -- treat all incorrect rollouts within a group identically. We show that this uniformity allows overconfident errors (incorrect reasoning paths that the RL process has spuriously reinforced) to persist and monopolize probability mass, ultimately suppressing valid exploratory trajectories. To address this, we propose the Asymmetric Confidence-aware Error Penalty (ACE). ACE introduces a per-rollout confidence shift metric, c_i = log(pi_theta(y_i|x) / pi_ref(y_i|x)), to dynamically modulate negative advantages. Theoretically, we demonstrate that ACE's gradient can be decomposed into the gradient of a selective regularizer restricted to overconfident errors, plus a well-characterized residual that partially moderates the regularizer's strength. We conduct extensive experiments fine-tuning Qwen2.5-Math-7B, Qwen3-8B-Base, and Llama-3.1-8B-Instruct on the DAPO-Math-17K dataset using GRPO and DAPO within the VERL framework. Evaluated on MATH-500 and AIME 2025, ACE composes seamlessly with existing methods and consistently improves the full Pass@k spectrum across all three model families and benchmarks.

### 🤖 AI 总结

**一句话总结**：提出了一种不对称的置信度惩罚方法，以改进强化学习中的错误修正，增强生成模型的推理能力和多样性。

**研究动机**：标准的强化学习算法在提高准确率的同时，过于统一的错误惩罚策略导致模型推理边界收窄和生成多样性下降。

**核心方法**：提出了不对称置信度错误惩罚（ACE），通过动态调节负优势来解决过于自信的错误问题。

**主要结论**：ACE方法在多个模型上进行实验验证，显示出与现有方法的良好兼容性，并在多个基准测试中一致性提高了性能。

**关键词**：可验证奖励强化学习（RLVR）, 大语言模型推理强化学习, 过度自信错误, 非对称置信度惩罚（ACE）, 置信度偏移度量, 负优势调制, 选择性正则化, 策略梯度优化, 生成多样性退化

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21420v1) | [下载PDF](https://arxiv.org/pdf/2602.21420v1.pdf)

---

## [13. Benchmarking State Space Models, Transformers, and Recurrent Networks for US Grid Forecasting](https://arxiv.org/abs/2602.21415v1)

**作者**：Sunki Hong, Jisoo Lee, Yuanyuan Shi  
**分类**：cs.LG, eess.SY  
**发布时间**：2026-02-24

### 📄 论文摘要

Selecting the right deep learning model for power grid forecasting is challenging, as performance heavily depends on the data available to the operator. This paper presents a comprehensive benchmark of five modern neural architectures: two state space models (PowerMamba, S-Mamba), two Transformers (iTransformer, PatchTST), and a traditional LSTM. We evaluate these models on hourly electricity demand across six diverse US power grids for forecast windows between 24 and 168 hours. To ensure a fair comparison, we adapt each model with specialized temporal processing and a modular layer that cleanly integrates weather covariates. Our results reveal that there is no single best model for all situations. When forecasting using only historical load, PatchTST and the state space models provide the highest accuracy. However, when explicit weather data is added to the inputs, the rankings reverse: iTransformer improves its accuracy three times more efficiently than PatchTST. By controlling for model size, we confirm that this advantage stems from the architecture's inherent ability to mix information across different variables. Extending our evaluation to solar generation, wind power, and wholesale prices further demonstrates that model rankings depend on the forecast task: PatchTST excels on highly rhythmic signals like solar, while state space models are better suited for the chaotic fluctuations of wind and price. Ultimately, this benchmark provides grid operators with actionable guidelines for selecting the optimal forecasting architecture based on their specific data environments.

### 🤖 AI 总结

**一句话总结**：该论文系统基准测试了状态空间模型、Transformer与LSTM在美国多电网多任务预测中的表现，发现“最优模型”取决于是否有天气等外生变量以及具体预测对象。

**研究动机**：电网负荷/新能源/价格预测中模型选择高度依赖可用数据（仅历史序列 vs. 带天气协变量），缺少跨区域、跨任务、跨架构的公平对比来指导运营方选型。

**核心方法**：在6个美国电网的小时级用电需求上，对PowerMamba、S-Mamba、iTransformer、PatchTST和LSTM进行24–168小时滚动预测基准，并通过统一的时间处理与可插拔模块公平整合天气协变量；同时扩展到光伏、风电与批发电价任务，并控制模型规模分析架构差异来源。

**主要结论**：仅用历史负荷时PatchTST与状态空间模型精度最佳；加入显式天气后iTransformer的收益显著更大且更高效，优势来自更强的跨变量信息混合能力；不同任务呈现不同赢家（PatchTST适合强节律如光伏，状态空间模型更适合风电/价格等高噪声波动），因此应按数据环境与任务特性选模型。

**关键词**：电力系统预测, 电网负荷预测, 时间序列预测, 多变量预测, 外生变量（天气）, 预测区间（24-168小时）, 模型基准评测, 状态空间模型（SSM）, 可再生能源发电预测, 电力市场价格预测

**评分**：17

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21415v1) | [下载PDF](https://arxiv.org/pdf/2602.21415v1.pdf)

---

## [14. Generative Bayesian Computation as a Scalable Alternative to Gaussian Process Surrogates](https://arxiv.org/abs/2602.21408v1)

**作者**：Nick Polson, Vadim Sokolov  
**分类**：cs.LG, stat.AP, stat.CO, stat.ME, stat.ML  
**发布时间**：2026-02-24

### 📄 论文摘要

Gaussian process (GP) surrogates are the default tool for emulating expensive computer experiments, but cubic cost, stationarity assumptions, and Gaussian predictive distributions limit their reach. We propose Generative Bayesian Computation (GBC) via Implicit Quantile Networks (IQNs) as a surrogate framework that targets all three limitations. GBC learns the full conditional quantile function from input--output pairs; at test time, a single forward pass per quantile level produces draws from the predictive distribution.   Across fourteen benchmarks we compare GBC to four GP-based methods. GBC improves CRPS by 11--26\% on piecewise jump-process benchmarks, by 14\% on a ten-dimensional Friedman function, and scales linearly to 90,000 training points where dense-covariance GPs are infeasible. A boundary-augmented variant matches or outperforms Modular Jump GPs on two-dimensional jump datasets (up to 46\% CRPS improvement). In active learning, a randomized-prior IQN ensemble achieves nearly three times lower RMSE than deep GP active learning on Rocket LGBB. Overall, GBC records a favorable point estimate in 12 of 14 comparisons. GPs retain an edge on smooth surfaces where their smoothness prior provides effective regularization.

### 🤖 AI 总结

**一句话总结**：论文提出用基于隐式分位数网络（IQN）的生成式贝叶斯计算（GBC）替代高斯过程（GP）代理模型，以更好处理非平稳/跳变现象并实现大规模线性扩展的预测分布建模。

**研究动机**：传统GP代理模型存在训练/推断立方复杂度、常见平稳性假设不适用于跳变或分段函数、以及高斯预测分布表达能力受限等问题，限制了在复杂与大数据仿真中的适用性。

**核心方法**：GBC通过IQN直接学习条件分位数函数（给定输入输出对），测试时对不同分位水平做一次前向传播即可生成预测分布样本；并引入边界增强变体与随机先验的IQN集成用于提升跳变建模与主动学习表现。

**主要结论**：在14个基准上，GBC相对多种GP方法在多数任务中取得更优或可比的CRPS/RMSE，尤其在跳变/分段与高维任务上提升明显，且可扩展到9万训练样本；但在平滑表面上GP凭借平滑先验仍具有一定优势。

**关键词**：代理建模, 高斯过程回归, 生成式贝叶斯计算, 隐式分位数网络, 条件分位数函数, 预测分布采样, 跳跃过程建模, 非平稳过程, 大规模训练扩展, 主动学习, 连续秩概率得分

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21408v1) | [下载PDF](https://arxiv.org/pdf/2602.21408v1.pdf)

---

## [15. FedVG: Gradient-Guided Aggregation for Enhanced Federated Learning](https://arxiv.org/abs/2602.21399v1)

**作者**：Alina Devkota, Jacob Thrasher, Donald Adjeroh 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CV  
**发布时间**：2026-02-24

### 📄 论文摘要

Federated Learning (FL) enables collaborative model training across multiple clients without sharing their private data. However, data heterogeneity across clients leads to client drift, which degrades the overall generalization performance of the model. This effect is further compounded by overemphasis on poorly performing clients. To address this problem, we propose FedVG, a novel gradient-based federated aggregation framework that leverages a global validation set to guide the optimization process. Such a global validation set can be established using readily available public datasets, ensuring accessibility and consistency across clients without compromising privacy. In contrast to conventional approaches that prioritize client dataset volume, FedVG assesses the generalization ability of client models by measuring the magnitude of validation gradients across layers. Specifically, we compute layerwise gradient norms to derive a client-specific score that reflects how much each client needs to adjust for improved generalization on the global validation set, thereby enabling more informed and adaptive federated aggregation. Extensive experiments on both natural and medical image benchmarking datasets, across diverse model architectures, demonstrate that FedVG consistently improves performance, particularly in highly heterogeneous settings. Moreover, FedVG is modular and can be seamlessly integrated with various state-of-the-art FL algorithms, often further improving their results. Our code is available at https://github.com/alinadevkota/FedVG.

### 🤖 AI 总结

**一句话总结**：FedVG通过全局验证集的梯度信息为客户端分配自适应聚合权重，从而缓解联邦学习中的非IID导致的客户端漂移并提升泛化性能。

**研究动机**：传统FL聚合常按数据量加权，易过度强调表现差或分布偏的客户端，在数据异质性强时引发客户端漂移并损害全局模型泛化。

**核心方法**：引入可由公共数据构建的全局验证集，计算各客户端模型在验证集上的分层梯度范数，并据此形成反映“为提升泛化需要调整多少”的客户端得分，用该得分指导聚合权重；该框架可模块化嵌入多种现有FL算法。

**主要结论**：在自然图像与医学图像等多数据集、不同模型架构与高异质性设定下，FedVG稳定优于基线并常能进一步提升SOTA联邦学习方法的效果，同时不依赖共享私有数据。

**关键词**：联邦学习, 客户端漂移, 梯度引导聚合, 自适应客户端加权, 全局验证集, 公共数据集, 层级梯度范数, 泛化评估, 异构客户端鲁棒性, 医学影像基准

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21399v1) | [下载PDF](https://arxiv.org/pdf/2602.21399v1.pdf)

---

