# arXiv AI 论文日报 | 2026-02-20

> 共 15 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (9 篇)
- [cs.CL](#csCL) (2 篇)
- [cs.AI](#csAI) (2 篇)
- [cs.CV](#csCV) (2 篇)

---

## cs.AI

## [1. Decoding ML Decision: An Agentic Reasoning Framework for Large-Scale Ranking System](https://arxiv.org/abs/2602.18640v1)

**作者**：Longfei Yun, Yihan Wu, Haoran Liu 等 12 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-20

### 📄 论文摘要

Modern large-scale ranking systems operate within a sophisticated landscape of competing objectives, operational constraints, and evolving product requirements. Progress in this domain is increasingly bottlenecked by the engineering context constraint: the arduous process of translating ambiguous product intent into reasonable, executable, verifiable hypotheses, rather than by modeling techniques alone. We present GEARS (Generative Engine for Agentic Ranking Systems), a framework that reframes ranking optimization as an autonomous discovery process within a programmable experimentation environment. Rather than treating optimization as static model selection, GEARS leverages Specialized Agent Skills to encapsulate ranking expert knowledge into reusable reasoning capabilities, enabling operators to steer systems via high-level intent vibe personalization. Furthermore, to ensure production reliability, the framework incorporates validation hooks to enforce statistical robustness and filter out brittle policies that overfit short-term signals. Experimental validation across diverse product surfaces demonstrates that GEARS consistently identifies superior, near-Pareto-efficient policies by synergizing algorithmic signals with deep ranking context while maintaining rigorous deployment stability.

### 🤖 AI 总结

**一句话总结**：GEARS 将大规模排序优化重构为在可编程实验环境中的“自治发现”过程，用具备专家技能的代理在高层意图引导下搜索近 Pareto 最优且可稳定上线的策略。

**研究动机**：大规模排序系统的瓶颈不再主要是建模技巧，而是工程上下文约束：把模糊的产品意图转化为可执行、可验证的假设与实验方案非常困难。需要一种能结合业务/约束/专家经验并保证生产可靠性的自动化优化框架。

**核心方法**：提出 GEARS（Generative Engine for Agentic Ranking Systems），以“Specialized Agent Skills”封装排序专家知识为可复用推理能力，支持操作者用高层意图（vibe personalization）驱动策略搜索。框架内置验证 hooks，强化统计稳健性并过滤对短期信号过拟合的脆弱策略，确保部署稳定。

**主要结论**：在多种产品场景实验中，GEARS 能持续找到更优、接近 Pareto 前沿的排序策略，并在融合算法信号与深度业务上下文的同时保持严格的上线稳定性与可靠性。

**关键词**：大规模排序系统, 多目标优化, 自动化实验平台, 专家知识模块化, 意图驱动调参, 统计显著性检验, 线上A/B实验, 生产部署稳定性, 个性化推荐场景

**评分**：52

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18640v1) | [下载PDF](https://arxiv.org/pdf/2602.18640v1.pdf)

---

## [2. Feedback-based Automated Verification in Vibe Coding of CAS Adaptation Built on Constraint Logic](https://arxiv.org/abs/2602.18607v1)

**作者**：Michal Töpfer, František Plášil, Tomáš Bureš 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-20

### 📄 论文摘要

In CAS adaptation, a challenge is to define the dynamic architecture of the system and changes in its behavior. Implementation-wise, this is projected into an adaptation mechanism, typically realized as an Adaptation Manager (AM). With the advances of generative LLMs, generating AM code based on system specification and desired AM behavior (partially in natural language) is a tempting opportunity. The recent introduction of vibe coding suggests a way to target the problem of the correctness of generated code by iterative testing and vibe coding feedback loops instead of direct code inspection.   In this paper, we show that generating an AM via vibe coding feedback loops is a viable option when the verification of the generated AM is based on a very precise formulation of the functional requirements. We specify these as constraints in a novel temporal logic FCL that allows us to express the behavior of traces with much finer granularity than classical LTL enables.   Furthermore, we show that by combining the adaptation and vibe coding feedback loops where the FCL constraints are evaluated for the current system state, we achieved good results in the experiments with generating AMs for two example systems from the CAS domain. Typically, just a few feedback loop iterations were necessary, each feeding the LLM with reports describing detailed violations of the constraints. This AM testing was combined with high run path coverage achieved by different initial settings.

### 🤖 AI 总结

**一句话总结**：提出用“vibe coding”反馈回路结合基于FCL（细粒度时序约束逻辑）的自动验证，迭代生成并验证CAS系统的适配管理器（AM）代码。

**研究动机**：CAS适配中AM需要精确定义动态架构与行为变化，而LLM生成AM代码存在正确性难以保证的问题；作者希望用可执行、可反馈的形式化需求来替代人工审查。

**核心方法**：将AM功能需求用新时序逻辑FCL表达为约束（比LTL能更细粒度刻画轨迹行为），在运行中对当前系统状态/执行轨迹评估约束并生成违规报告，作为vibe coding反馈输入LLM迭代修正代码；同时通过不同初始设置提升运行路径覆盖率。

**主要结论**：实验表明该流程可行：在两个CAS示例中通常只需少量反馈迭代即可生成满足约束的AM，且详细的约束违规报告能有效引导LLM修复，配合高路径覆盖带来较好的验证效果。

**关键词**：复杂自适应系统（CAS）, 自适应管理器（AM）, 反馈循环测试, LLM代码生成, 自动化验证, 约束规范, 时序逻辑FCL, 轨迹行为验证, 路径覆盖率

**评分**：42

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18607v1) | [下载PDF](https://arxiv.org/pdf/2602.18607v1.pdf)

---

## cs.CL

## [3. PolyFrame at MWE-2026 AdMIRe 2: When Words Are Not Enough: Multimodal Idiom Disambiguation](https://arxiv.org/abs/2602.18652v1)

**作者**：Nina Hosseini-Kivanani  
**分类**：cs.CL  
**发布时间**：2026-02-20

### 📄 论文摘要

Multimodal models struggle with idiomatic expressions due to their non-compositional meanings, a challenge amplified in multilingual settings. We introduced PolyFrame, our system for the MWE-2026 AdMIRe2 shared task on multimodal idiom disambiguation, featuring a unified pipeline for both image+text ranking (Subtask A) and text-only caption ranking (Subtask B). All model variants retain frozen CLIP-style vision--language encoders and the multilingual BGE M3 encoder, training only lightweight modules: a logistic regression and LLM-based sentence-type predictor, idiom synonym substitution, distractor-aware scoring, and Borda rank fusion. Starting from a CLIP baseline (26.7% Top-1 on English dev, 6.7% on English test), adding idiom-aware paraphrasing and explicit sentence-type classification increased performance to 60.0% Top-1 on English and 60.0% Top-1 (0.822 NDCG@5) in zero-shot transfer to Portuguese. On the multilingual blind test, our systems achieved average Top-1/NDCG scores of 0.35/0.73 for Subtask A and 0.32/0.71 for Subtask B across 15 languages. Ablation results highlight idiom-aware rewriting as the main contributor to performance, while sentence-type prediction and multimodal fusion enhance robustness. These findings suggest that effective idiom disambiguation is feasible without fine-tuning large multimodal encoders.

### 🤖 AI 总结

**一句话总结**：PolyFrame通过“习语改写+句型判别+多模型排序融合”的轻量化流水线，在不微调大型多模态编码器的情况下显著提升多语言多模态习语消歧表现。

**研究动机**：多模态模型对习语的非组合语义理解不足，且跨语言时歧义与数据稀缺使问题更难；因此需要一种可迁移、低成本、无需重训大模型的方案来提升习语消歧。

**核心方法**：保持CLIP式视觉-语言编码器与多语BGE M3嵌入模型冻结，仅训练/使用轻量模块：逻辑回归打分、LLM句子类型预测、习语同义替换/释义改写、考虑干扰项的打分策略，并用Borda进行排名融合以统一处理图文排序与纯文本排序两子任务。

**主要结论**：实验与消融表明习语感知的改写是性能提升的主要来源，句型预测与多模态融合进一步增强鲁棒性；整体结果证明无需微调大型多模态编码器也能实现有效的多语言习语消歧与零样本迁移。

**关键词**：多模态成语消歧, 多语言迁移, 图文检索排序, 文本描述排序, 冻结视觉语言编码器, CLIP视觉语言模型, BGE-M3多语言编码器, 参数高效微调, 句子类型分类, 成语释义改写, 干扰项感知评分

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18652v1) | [下载PDF](https://arxiv.org/pdf/2602.18652v1.pdf)

---

## [4. DP-RFT: Learning to Generate Synthetic Text via Differentially Private Reinforcement Fine-Tuning](https://arxiv.org/abs/2602.18633v1)

**作者**：Fangyuan Xu, Sihao Chen, Zinan Lin 等 16 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-20

### 📄 论文摘要

Differentially private (DP) synthetic data generation plays a pivotal role in developing large language models (LLMs) on private data, where data owners cannot provide eyes-on access to individual examples. Generating DP synthetic data typically involves a difficult trade-off. On one hand, DP finetuning methods train an LLM as a synthetic data generator with formal privacy guarantees, yet it still requires the raw content of private examples for model training. However, methods that avoid direct exposure to private data are bounded by an off-the-shelf, un-finetuned model, whose outputs often lack domain fidelity. Can we train an LLM to generate high-quality synthetic text without eyes-on access to individual private examples? In this work, we introduce Differentially Private Reinforcement Fine-Tuning (DP-RFT), an online reinforcement learning algorithm for synthetic data generation with LLMs. DP-RFT leverages DP-protected nearest-neighbor votes from an eyes-off private corpus as a reward signal for on-policy synthetic samples generated by an LLM. The LLM iteratively learns to generate synthetic data to maximize the expected DP votes through Proximal Policy Optimization (PPO). We evaluate DP-RFT for long-form and domain-specific synthetic data generation, such as news articles, meeting transcripts, and medical article abstracts. Our experiments show that DP-RFT closes the gap between private evolution and DP finetuning methods in terms of the fidelity and downstream utility of the generated synthetic data, while respecting the private data boundary.

### 🤖 AI 总结

**一句话总结**：DP-RFT通过差分隐私保护的近邻投票作为奖励信号，用在线强化学习微调LLM，在不“眼见”私有样本内容的情况下生成高保真合成文本。

**研究动机**：现有DP微调虽有正式隐私保证但训练仍需直接接触私有文本，而不接触私有数据的现成模型又难以生成足够贴合领域的高质量文本；因此需要一种既不暴露单条私有样本又能提升领域保真的训练方式。

**核心方法**：提出DP-RFT：模型按策略生成合成样本后，在私有语料上用差分隐私机制做最近邻投票（DP-protected nearest-neighbor votes）得到奖励，并用PPO进行在线在策略（on-policy）强化学习，迭代最大化期望DP投票。

**主要结论**：在新闻、会议记录、医学摘要等长文本与领域数据上，DP-RFT在遵守私有数据边界的同时显著提升合成数据的保真度与下游任务效用，缩小了“私有演化/非DP方法”和DP微调之间的性能差距。

**关键词**：差分隐私, 隐私保护合成文本, 合成数据生成, 强化学习微调, 基于奖励的文本生成, 近邻投票奖励, 无眼访问私有语料, 领域特定长文本生成

**评分**：41

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18633v1) | [下载PDF](https://arxiv.org/pdf/2602.18633v1.pdf)

---

## cs.CV

## [5. Narrating For You: Prompt-guided Audio-visual Narrating Face Generation Employing Multi-entangled Latent Space](https://arxiv.org/abs/2602.18618v1)

**作者**：Aashish Chandra, Aashutosh A, Abhijit Das  
**分类**：cs.CV  
**发布时间**：2026-02-20

### 📄 论文摘要

We present a novel approach for generating realistic speaking and talking faces by synthesizing a person's voice and facial movements from a static image, a voice profile, and a target text. The model encodes the prompt/driving text, the driving image, and the voice profile of an individual and then combines them to pass them to the multi-entangled latent space to foster key-value pairs and queries for the audio and video modality generation pipeline. The multi-entangled latent space is responsible for establishing the spatiotemporal person-specific features between the modalities. Further, entangled features are passed to the respective decoder of each modality for output audio and video generation.

### 🤖 AI 总结

**一句话总结**：提出一种在提示文本引导下，从静态人脸图像、个体声音档案与目标文本联合生成同步的说话音频与口型/表情视频的框架。

**研究动机**：现有说话人脸生成往往难以同时保持“人物身份一致性”和“音画时序对齐”，且难以将文本语义、个体声纹与面部运动有效耦合。

**核心方法**：分别编码驱动文本、驱动图像与目标人物的声音档案，并在“多重纠缠潜空间”中融合为跨模态的query与key-value表征，用于建立音频与视频之间的人物特定时空关联；随后将纠缠特征送入各自模态解码器生成音频与视频输出。

**主要结论**：该方法通过多重纠缠潜空间显式建模跨模态的人物特征与时序关系，从而提升了生成结果的真实感、身份一致性以及音画同步性。

**关键词**：音视联合生成, 说话人脸生成, 静态图像驱动, 语音条件生成, 文本提示引导, 跨模态对齐, 多纠缠潜空间, 时空一致性建模, 身份保持生成, 注意力键值查询

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18618v1) | [下载PDF](https://arxiv.org/pdf/2602.18618v1.pdf)

---

## [6. Effect of Patch Size on Fine-Tuning Vision Transformers in Two-Dimensional and Three-Dimensional Medical Image Classification](https://arxiv.org/abs/2602.18614v1)

**作者**：Massoud Dehghan, Ramona Woitek, Amirreza Mahbod  
**分类**：cs.CV  
**发布时间**：2026-02-20

### 📄 论文摘要

Vision Transformers (ViTs) and their variants have become state-of-the-art in many computer vision tasks and are widely used as backbones in large-scale vision and vision-language foundation models. While substantial research has focused on architectural improvements, the impact of patch size, a crucial initial design choice in ViTs, remains underexplored, particularly in medical domains where both two-dimensional (2D) and three-dimensional (3D) imaging modalities exist.   In this study, using 12 medical imaging datasets from various imaging modalities (including seven 2D and five 3D datasets), we conduct a thorough evaluation of how different patch sizes affect ViT classification performance. Using a single graphical processing unit (GPU) and a range of patch sizes (1, 2, 4, 7, 14, 28), we fine-tune ViT models and observe consistent improvements in classification performance with smaller patch sizes (1, 2, and 4), which achieve the best results across nearly all datasets. More specifically, our results indicate improvements in balanced accuracy of up to 12.78% for 2D datasets (patch size 2 vs. 28) and up to 23.78% for 3D datasets (patch size 1 vs. 14), at the cost of increased computational expense. Moreover, by applying a straightforward ensemble strategy that fuses the predictions of the models trained with patch sizes 1, 2, and 4, we demonstrate a further boost in performance in most cases, especially for the 2D datasets. Our implementation is publicly available on GitHub: https://github.com/HealMaDe/MedViT

### 🤖 AI 总结

**一句话总结**：在12个2D/3D医学影像分类数据集上系统评估ViT的patch size，发现更小patch（1/2/4）几乎普遍带来更高准确率但计算更贵，且小patch模型集成可进一步提升表现。

**研究动机**：ViT的patch size是关键但常被忽视的设计选择，尤其在同时存在2D与3D模态的医学影像中其影响缺乏系统研究；因此需要明确不同patch size在医学分类任务上的效果与代价权衡。

**核心方法**：在单GPU条件下，对12个医学数据集（7个2D、5个3D）用多种patch size（1,2,4,7,14,28）微调ViT并比较分类性能；同时将patch size为1/2/4的模型预测进行简单融合做集成评估。

**主要结论**：更小的patch size（1/2/4）在几乎所有数据集上取得最佳或接近最佳的balanced accuracy，相比大patch可带来最高约12.78%(2D)与23.78%(3D)的提升但增加计算开销；将小patch模型进行集成通常还能进一步提升效果，尤其在2D数据集上更明显。

**关键词**：二维医学影像分类, 三维医学影像分类, 多模态医学影像数据集, 计算开销与性能权衡, 多模型集成（ensemble）, 单GPU训练评估, 开源代码实现, Effect

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18614v1) | [下载PDF](https://arxiv.org/pdf/2602.18614v1.pdf)

---

## cs.LG

## [7. Large Causal Models for Temporal Causal Discovery](https://arxiv.org/abs/2602.18662v1)

**作者**：Nikolaos Kougioulis, Nikolaos Gkorgkolis, MingXue Wang 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-20

### 📄 论文摘要

Causal discovery for both cross-sectional and temporal data has traditionally followed a dataset-specific paradigm, where a new model is fitted for each individual dataset. Such an approach limits the potential of multi-dataset pretraining. The concept of large causal models (LCMs) envisions a class of pre-trained neural architectures specifically designed for temporal causal discovery. Prior approaches are constrained to small variable counts, degrade with larger inputs, and rely heavily on synthetic data, limiting generalization. We propose a principled framework for LCMs, combining diverse synthetic generators with realistic time-series datasets, allowing learning at scale. Extensive experiments on synthetic, semi-synthetic and realistic benchmarks show that LCMs scale effectively to higher variable counts and deeper architectures while maintaining strong performance. Trained models achieve competitive or superior accuracy compared to classical and neural baselines, particularly in out-of-distribution settings, while enabling fast, single-pass inference. Results demonstrate LCMs as a promising foundation-model paradigm for temporal causal discovery. Experiments and model weights are available at https://github.com/kougioulis/LCM-paper/.

### 🤖 AI 总结

**一句话总结**：提出“Large Causal Models (LCMs)”这一预训练范式，用单次前向推理实现可扩展的时间因果发现，并在多类基准上取得强泛化表现。

**研究动机**：传统时间/横截面因果发现通常对每个数据集单独训练，难以利用多数据集预训练带来的迁移能力；现有神经方法还常受变量数限制、规模变大性能下降且过度依赖合成数据。

**核心方法**：构建面向时间因果发现的LCM框架：结合多样化的合成数据生成器与更贴近真实的时间序列数据进行大规模训练，并通过更深/更大的神经架构实现对高变量维度输入的有效建模与快速单次推理。

**主要结论**：实验显示LCMs在合成、半合成与真实数据集上能随变量数与模型深度扩展而保持强性能，整体准确率与经典/神经基线相当或更优，尤其在分布外场景泛化更好，验证了其作为时间因果发现“基础模型”范式的潜力。

**关键词**：时序因果图学习, 大规模因果模型（LCM）, 多数据集预训练, 高维变量因果推断, 合成数据生成器, 半合成基准, 分布外泛化（OOD）, 单次前向推理, 可扩展神经架构

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18662v1) | [下载PDF](https://arxiv.org/pdf/2602.18662v1.pdf)

---

## [8. Global Low-Rank, Local Full-Rank: The Holographic Encoding of Learned Algorithms](https://arxiv.org/abs/2602.18649v1)

**作者**：Yongzhong Xu  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-20

### 📄 论文摘要

Grokking -- the abrupt transition from memorization to generalization after extended training -- has been linked to the emergence of low-dimensional structure in learning dynamics. Yet neural network parameters inhabit extremely high-dimensional spaces. How can a low-dimensional learning process produce solutions that resist low-dimensional compression?   We investigate this question in multi-task modular arithmetic, training shared-trunk Transformers with separate heads for addition, multiplication, and a quadratic operation modulo 97. Across three model scales (315K--2.2M parameters) and five weight decay settings, we compare three reconstruction methods: per-matrix SVD, joint cross-matrix SVD, and trajectory PCA.   Across all conditions, grokking trajectories are confined to a 2--6 dimensional global subspace, while individual weight matrices remain effectively full-rank. Reconstruction from 3--5 trajectory PCs recovers over 95\% of final accuracy, whereas both per-matrix and joint SVD fail at sub-full rank. Even when static decompositions capture most spectral energy, they destroy task-relevant structure.   These results show that learned algorithms are encoded through dynamically coordinated updates spanning all matrices, rather than localized low-rank components. We term this the holographic encoding principle: grokked solutions are globally low-rank in the space of learning directions but locally full-rank in parameter space, with implications for compression, interpretability, and understanding how neural networks encode computation.

### 🤖 AI 总结

**一句话总结**：本文探讨了在多任务模块算术中低维学习过程如何产生抵抗低维压缩的解决方案，提出了全局低秩与局部全秩的全息编码原理。

**研究动机**：研究动机在于理解在高维参数空间中，低维学习动态如何实现从记忆到泛化的转变，即grokking现象。

**核心方法**：通过训练共享主干的Transformer模型，比较不同重建方法（如SVD和PCA）在多任务算术中的表现。

**主要结论**：结果表明，学习的算法通过动态协调的更新来编码，而不是依赖于局部低秩组件，提出的全息编码原理对压缩、可解释性及神经网络计算的理解具有重要意义。

**关键词**：记忆-泛化转变, 低维学习动力学, 参数更新子空间, 全局低秩, 局部满秩, 变换器多任务学习, 模块算术任务, 全息编码原理

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18649v1) | [下载PDF](https://arxiv.org/pdf/2602.18649v1.pdf)

---

## [9. Information-Guided Noise Allocation for Efficient Diffusion Training](https://arxiv.org/abs/2602.18647v1)

**作者**：Gabriel Raya, Bac Nguyen, Georgios Batzolis 等 9 位作者  
**分类**：cs.LG, cs.AI, cs.CV, cs.IT  
**发布时间**：2026-02-20

### 📄 论文摘要

Training diffusion models typically relies on manually tuned noise schedules, which can waste computation on weakly informative noise regions and limit transfer across datasets, resolutions, and representations. We revisit noise schedule allocation through an information-theoretic lens and propose the conditional entropy rate of the forward process as a theoretically grounded, data-dependent diagnostic for identifying suboptimal noise-level allocation in existing schedules. Based on these insight, we introduce InfoNoise, a principled data-adaptive training noise schedule that replaces heuristic schedule design with an information-guided noise sampling distribution derived from entropy-reduction rates estimated from denoising losses already computed during training. Across natural-image benchmarks, InfoNoise matches or surpasses tuned EDM-style schedules, in some cases with a substantial training speedup (about $1.4\times$ on CIFAR-10). On discrete datasets, where standard image-tuned schedules exhibit significant mismatch, it reaches superior quality in up to $3\times$ fewer training steps. Overall, InfoNoise makes noise scheduling data-adaptive, reducing the need for per-dataset schedule design as diffusion models expand across domains.

### 🤖 AI 总结

**一句话总结**：提出InfoNoise：用信息论指标自适应分配扩散训练中的噪声采样，从而减少无效计算并提升跨数据集/表示的可迁移性。

**研究动机**：手工调噪声日程常在信息量低的噪声区间浪费训练步数，且在不同数据集、分辨率或离散表示上容易失配，需要一种数据依赖、可诊断且可迁移的噪声分配原则。

**核心方法**：以前向扩散过程的条件熵率（conditional entropy rate）作为诊断量，衡量不同噪声水平带来的信息减少/学习收益；据此从训练中已计算的去噪损失估计各噪声段的熵减少率，并构造信息引导的噪声采样分布（InfoNoise）替代启发式固定schedule。

**主要结论**：在自然图像上InfoNoise达到或超过精调的EDM式schedule，并带来显著加速（如CIFAR-10约1.4×）；在离散数据上缓解图像调参schedule的失配，可用最多3×更少训练步数获得更好质量，降低按数据集单独设计噪声日程的需求。

**关键词**：扩散模型训练, 噪声调度, 数据自适应噪声采样, 信息论诊断, 条件熵率, 前向扩散过程, 熵减率估计, 去噪损失, 训练效率加速, 跨数据集迁移, 离散数据生成

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18647v1) | [下载PDF](https://arxiv.org/pdf/2602.18647v1.pdf)

---

## [10. Adaptive Time Series Reasoning via Segment Selection](https://arxiv.org/abs/2602.18645v1)

**作者**：Shvat Messica, Jiawen Zhang, Kevin Li 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-20

### 📄 论文摘要

Time series reasoning tasks often start with a natural language question and require targeted analysis of a time series. Evidence may span the full series or appear in a few short intervals, so the model must decide what to inspect. Most existing approaches encode the entire time series into a fixed representation before inference, regardless of whether or not the entire sequence is relevant. We introduce ARTIST, which formulates time-series reasoning as a sequential decision problem. ARTIST interleaves reasoning with adaptive temporal segment selection. It adopts a controller-reasoner architecture and uses reinforcement learning to train the controller role to select informative segments and the reasoner role to generate segment-conditioned reasoning traces and final answers. During inference, the model actively acquires task-relevant information instead of relying on a static summary of the full sequence. We use a novel hierarchical policy optimization approach for post-training that allows the model to excel in both segment selection and question-answering behavior. We evaluate ARTIST on six time-series reasoning benchmarks and compare it with large language models, vision-language models, and prior time-series reasoning systems. ARTIST improves average accuracy by 6.46 absolute percentage points over the strongest baseline. The largest gains appear on rare event localization and multi-segment reasoning tasks. Supervised fine-tuning improves performance, and reinforcement learning provides additional gains by optimizing question-adaptive segment selection. These results show that selective data use drives effective time-series reasoning.

### 🤖 AI 总结

**一句话总结**：ARTIST通过自适应时间段选择来增强时间序列推理，显著提升了准确性。

**研究动机**：现有方法往往对整个时间序列进行固定表示，而实际上只有部分片段可能与问题相关，因此需要改进推理策略。

**核心方法**：ARTIST将时间序列推理视为一个顺序决策问题，采用控制器-推理器架构，通过强化学习优化信息选择和推理生成过程。

**主要结论**：ARTIST在多个时间序列推理基准上表现优越，尤其在稀有事件定位和多片段推理任务中，证明了选择性数据使用对有效推理的重要性。

**关键词**：时间序列推理, 时间片段选择, 自适应信息获取, 序列决策, 强化学习, 分层策略优化, 控制器-推理器架构, 片段条件推理, 时间序列问答, 稀有事件定位, 多片段推理, 监督微调

**评分**：43

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18645v1) | [下载PDF](https://arxiv.org/pdf/2602.18645v1.pdf)

---

## [11. Learning Invariant Visual Representations for Planning with Joint-Embedding Predictive World Models](https://arxiv.org/abs/2602.18639v1)

**作者**：Leonardo F. Toso, Davit Shadunts, Yunyang Lu 等 7 位作者  
**分类**：cs.LG, math.OC  
**发布时间**：2026-02-20

### 📄 论文摘要

World models learned from high-dimensional visual observations allow agents to make decisions and plan directly in latent space, avoiding pixel-level reconstruction. However, recent latent predictive architectures (JEPAs), including the DINO world model (DINO-WM), display a degradation in test time robustness due to their sensitivity to "slow features". These include visual variations such as background changes and distractors that are irrelevant to the task being solved. We address this limitation by augmenting the predictive objective with a bisimulation encoder that enforces control-relevant state equivalence, mapping states with similar transition dynamics to nearby latent states while limiting contributions from slow features. We evaluate our model on a simple navigation task under different test-time background changes and visual distractors. Across all benchmarks, our model consistently improves robustness to slow features while operating in a reduced latent space, up to 10x smaller than that of DINO-WM. Moreover, our model is agnostic to the choice of pretrained visual encoder and maintains robustness when paired with DINOv2, SimDINOv2, and iBOT features.

### 🤖 AI 总结

**一句话总结**：在联合嵌入预测世界模型（JEPA）中引入双模拟（bisimulation）编码约束，显著提升对背景变化与干扰物等“慢特征”的测试时鲁棒性，并可用更小的潜空间完成规划。

**研究动机**：现有JEPA类视觉世界模型（如DINO-WM）对与任务无关的慢特征敏感，导致测试时遇到背景/干扰变化鲁棒性下降，从而影响潜空间规划的可靠性。

**核心方法**：在预测式潜表示学习目标上增添bisimulation encoder，使具有相似控制相关转移动态的状态在潜空间中更接近，从而抑制慢特征对表示的贡献；并验证该方法可与不同预训练视觉编码器特征（DINOv2/SimDINOv2/iBOT）组合使用。

**主要结论**：在导航任务的多种背景变化与视觉干扰评测中，该模型相较DINO-WM更稳健，同时潜空间维度可缩小至其约1/10，且对所选预训练视觉特征具备良好泛化与兼容性。

**关键词**：视觉世界模型, 潜变量规划, 联合嵌入预测架构（JEPA）, 控制相关表征, 慢特征抑制, 测试时鲁棒性, 视觉分布偏移, 背景变化与干扰物, 自监督视觉特征

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18639v1) | [下载PDF](https://arxiv.org/pdf/2602.18639v1.pdf)

---

## [12. Online decoding of rat self-paced locomotion speed from EEG using recurrent neural networks](https://arxiv.org/abs/2602.18637v1)

**作者**：Alejandro de Miguel, Nelson Totah, Uri Maoz  
**分类**：cs.LG, q-bio.NC  
**发布时间**：2026-02-20

### 📄 论文摘要

$\textit{Objective.}$ Accurate neural decoding of locomotion holds promise for advancing rehabilitation, prosthetic control, and understanding neural correlates of action. Recent studies have demonstrated decoding of locomotion kinematics across species on motorized treadmills. However, efforts to decode locomotion speed in more natural contexts$-$where pace is self-selected rather than externally imposed$-$are scarce, generally achieve only modest accuracy, and require intracranial implants. Here, we aim to decode self-paced locomotion speed non-invasively and continuously using cortex-wide EEG recordings from rats. $\textit{Approach.}$ We introduce an asynchronous brain$-$computer interface (BCI) that processes a stream of 32-electrode skull-surface EEG (0.01$-$45 Hz) to decode instantaneous speed from a non-motorized treadmill during self-paced locomotion in head-fixed rats. Using recurrent neural networks and a dataset of over 133 h of recordings, we trained decoders to map ongoing EEG activity to treadmill speed. $\textit{Main results.}$ Our decoding achieves a correlation of 0.88 ($R^2$ = 0.78) for speed, primarily driven by visual cortex electrodes and low-frequency ($< 8$ Hz) oscillations. Moreover, pre-training on a single session permitted decoding on other sessions from the same rat, suggesting uniform neural signatures that generalize across sessions but fail to transfer across animals. Finally, we found that cortical states not only carry information about current speed, but also about future and past dynamics, extending up to 1000 ms. $\textit{Significance.}$ These findings demonstrate that self-paced locomotion speed can be decoded accurately and continuously from non-invasive, cortex-wide EEG. Our approach provides a framework for developing high-performing, non-invasive BCI systems and contributes to understanding distributed neural representations of action dynamics.

### 🤖 AI 总结

**一句话总结**：本研究通过非侵入性脑电图（EEG）准确解码大鼠自我选择的运动速度，展示了高效的脑-计算机接口（BCI）潜力。

**研究动机**：准确解码运动速度有助于推进康复、假肢控制及理解动作的神经相关性，但在自然环境中解码的研究较少且精度有限。

**核心方法**：采用递归神经网络对32电极脑电图数据进行处理，以解码固定头部大鼠在非电动跑步机上的自我选择速度，训练数据超过133小时。

**主要结论**：研究表明，通过非侵入性EEG可以持续而准确地解码自我选择的运动速度，且这一方法为开发高性能的非侵入性BCI系统提供了框架。

**关键词**：自选步速解码, 运动速度解码, 脑机接口, 异步脑机接口, 非侵入式EEG, 大鼠脑电, 复发神经网络, 时序回归, 低频振荡, 视觉皮层贡献

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18637v1) | [下载PDF](https://arxiv.org/pdf/2602.18637v1.pdf)

---

## [13. Non-Interfering Weight Fields: Treating Model Parameters as a Continuously Extensible Function](https://arxiv.org/abs/2602.18628v1)

**作者**：Sarim Chaudhry  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-20

### 📄 论文摘要

Large language models store all learned knowledge in a single, fixed weight vector. Teaching a model new capabilities requires modifying those same weights, inevitably degrading previously acquired knowledge. This fundamental limitation, known as catastrophic forgetting, has resisted principled solutions for decades. Existing approaches treat weights as immutable artifacts that must be protected through techniques like regularization heuristics, replay buffers, or isolated adapter modules. The problem is none of these provide a structural guarantee against forgetting. In this work, we propose Non-Interfering Weight Fields (NIWF), a framework that replaces the fixed weight paradigm with a learned function that generates weight configurations on demand from a continuous capability coordinate space. After training on a task, we commit the occupied coordinate region by snapshotting the fields outputs on anchor points to enforce a functional lock during all future training. We validate NIWF on sequential instructionfollowing and code generation tasks using Mistral-7B, demonstrating zero forgetting on committed tasks with competitive perplexity on new tasks. The framework introduces the notion of software-like versioning for neural network intelligence, where capabilities can be committed, extended, composed, and rolled back without retraining.

### 🤖 AI 总结

**一句话总结**：提出NIWF将模型参数从固定权重向量改为可生成权重的连续函数，并通过“提交/锁定”已学能力区域实现顺序学习下的零遗忘。

**研究动机**：传统LLM把所有知识压在同一组权重里，新任务微调会不可避免地干扰旧知识导致灾难性遗忘；现有正则化、回放、适配器等方法缺乏结构性的不遗忘保证。

**核心方法**：用“权重场”函数从连续的能力坐标空间按需生成对应的权重配置；每学完一个任务就在其占用的坐标区域选取锚点并快照权重场输出，后续训练对这些锚点施加约束以功能性锁定已提交能力，实现类似软件版本管理的提交/扩展/组合/回滚。

**主要结论**：在Mistral-7B上的顺序指令跟随与代码生成实验表明，对已提交任务可实现零遗忘，同时在新任务上保持有竞争力的困惑度，展示了用“版本化能力坐标”持续扩展模型能力的可行性。

**关键词**：灾难性遗忘, 持续学习, 非干扰权重场（NIWF）, 权重场函数, 能力坐标空间, 权重快照锚点, 功能锁定, 顺序指令微调, 顺序代码生成, 零遗忘评测, 能力版本控制, 能力组合与回滚

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18628v1) | [下载PDF](https://arxiv.org/pdf/2602.18628v1.pdf)

---

## [14. Diagnosing LLM Reranker Behavior Under Fixed Evidence Pools](https://arxiv.org/abs/2602.18613v1)

**作者**：Baris Arat, Emre Sefer  
**分类**：cs.LG, cs.CL, cs.IR  
**发布时间**：2026-02-20

### 📄 论文摘要

Standard reranking evaluations study how a reranker orders candidates returned by an upstream retriever. This setup couples ranking behavior with retrieval quality, so differences in output cannot be attributed to the ranking policy alone. We introduce a controlled diagnostic that isolates reranking by using Multi-News clusters as fixed evidence pools. We limit each pool to exactly eight documents and pass identical inputs to all rankers. Within this setup, BM25 and MMR serve as interpretable reference points for lexical matching and diversity optimization. Across 345 clusters, we find that redundancy patterns vary by model: one LLM implicitly diversifies at larger selection budgets, while another increases redundancy. In contrast, LLMs underperform on lexical coverage at small selection budgets. As a result, LLM rankings diverge substantially from both baselines rather than consistently approximating either strategy. By eliminating retrieval variance, we can attribute these differences directly to the ranking policy. This diagnostic is model-agnostic and applicable to any ranker, including open source systems and proprietary APIs.

### 🤖 AI 总结

**一句话总结**：提出一种在固定证据池下诊断LLM重排序器行为的评测框架，发现不同LLM的冗余/多样性与词法覆盖策略差异显著且不稳定地偏离BM25与MMR基线。

**研究动机**：传统重排序评测依赖上游检索结果，排序表现与检索质量耦合，难以将差异归因到“排序策略”本身。需要一种可控设置来隔离检索方差，直接观察重排序器的行为特征。

**核心方法**：以Multi-News的每个聚类作为固定证据池，将候选文档数严格限制为8篇，并对所有ranker输入完全一致的候选集合。用BM25（词法匹配）与MMR（多样性优化）作为可解释参照，在345个聚类上比较不同选择预算下的冗余模式与词法覆盖等指标。

**主要结论**：在固定证据池中，不同LLM随选择预算变化呈现不同冗余趋势：有的在大预算下隐式多样化，有的反而更冗余；且在小预算下LLM的词法覆盖普遍弱于基线。总体上LLM排序结果并非稳定逼近BM25或MMR，而是显著分歧，说明差异可直接归因于排序策略而非检索波动。

**关键词**：LLM 重排序, 重排序评测, 固定证据池, 可控诊断评测, 检索-排序解耦, BM25 基线, 最大边际相关性（MMR）, 多样性优化, 冗余度分析, 词汇覆盖率, 选择预算（top-k）

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18613v1) | [下载PDF](https://arxiv.org/pdf/2602.18613v1.pdf)

---

## [15. MapTab: Can MLLMs Master Constrained Route Planning?](https://arxiv.org/abs/2602.18600v1)

**作者**：Ziqiao Shang, Lingyue Ge, Yang Chen 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-20

### 📄 论文摘要

Systematic evaluation of Multimodal Large Language Models (MLLMs) is crucial for advancing Artificial General Intelligence (AGI). However, existing benchmarks remain insufficient for rigorously assessing their constrained reasoning capabilities. To bridge this gap, we introduce MapTab, a multimodal benchmark specifically designed to evaluate constrained reasoning in MLLMs via route planning tasks. MapTab requires MLLMs to perceive and ground visual cues from map images alongside route attributes (e.g., Time, Price) from structured tabular data. The benchmark encompasses two scenarios: Metromap, covering metro networks in 160 cities across 52 countries, and Travelmap, depicting 168 representative tourist attractions from 19 countries. In total, MapTab comprises 328 images, 196,800 route planning queries, and 3,936 QA queries, all incorporating 4 key constraints: Time, Price, Comfort, and Reliability. Extensive evaluations across 15 representative MLLMs reveal that current models face substantial challenges in constrained multimodal reasoning. Notably, under conditions of limited visual perception, multimodal collaboration often underperforms compared to unimodal approaches. We believe MapTab provides a challenging and realistic testbed to advance the systematic evaluation of MLLMs.

### 🤖 AI 总结

**一句话总结**：提出并发布MapTab基准，用多模态地图+表格约束的路径规划任务系统评测MLLM的受约束推理能力，发现现有模型整体表现仍显著不足。

**研究动机**：现有多模态评测基准难以严格衡量模型在“多约束条件下的推理与决策”能力，尤其缺少贴近真实场景的路径规划类任务。为此需要一个同时要求视觉定位、表格属性对齐与约束优化的统一测试平台。

**核心方法**：构建MapTab：包含Metromap（52国160城地铁网络）与Travelmap（19国168景点）两类地图图像，并配套结构化表格路由属性与查询，覆盖时间/价格/舒适/可靠性四大约束；在15个代表性MLLM上进行大规模评测（196,800条规划查询与3,936条QA）。

**主要结论**：实验表明当前MLLM在多模态受约束路径规划上存在显著困难；在视觉感知受限时，多模态协作方案甚至可能不如纯单模态方法，说明多模态融合与约束推理仍是关键瓶颈。

**关键词**：多模态LLM评测, 多模态基准, 约束推理, 约束路径规划, 视觉语义对齐, 视觉-表格融合, 多约束优化, 地铁网络导航, 多模态协作

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18600v1) | [下载PDF](https://arxiv.org/pdf/2602.18600v1.pdf)

---

