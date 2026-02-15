# arXiv AI 论文日报 | 2026-02-14

> 共 15 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (3 篇)
- [cs.LG](#csLG) (9 篇)
- [cs.AI](#csAI) (3 篇)

---

## cs.AI

## [1. CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn and Multi-Step Agentic Tool Use](https://arxiv.org/abs/2602.12268v1)

**作者**：Zhen Zhang, Kaiqiang Song, Xun Wang 等 14 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-12

### 📄 论文摘要

AI agents are increasingly used to solve real-world tasks by reasoning over multi-turn user interactions and invoking external tools. However, applying reinforcement learning to such settings remains difficult: realistic objectives often lack verifiable rewards and instead emphasize open-ended behaviors; moreover, RL for multi-turn, multi-step agentic tool use is still underexplored; and building and maintaining executable tool environments is costly, limiting scale and coverage. We propose CM2, an RL framework that replaces verifiable outcome rewards with checklist rewards. CM2 decomposes each turn's intended behavior into fine-grained binary criteria with explicit evidence grounding and structured metadata, turning open-ended judging into more stable classification-style decisions. To balance stability and informativeness, our method adopts a strategy of sparse reward assignment but dense evaluation criteria. Training is performed in a scalable LLM-simulated tool environment, avoiding heavy engineering for large tool sets. Experiments show that CM2 consistently improves over supervised fine-tuning. Starting from an 8B Base model and training on an 8k-example RL dataset, CM2 improves over the SFT counterpart by 8 points on tau^-Bench, by 10 points on BFCL-V4, and by 12 points on ToolSandbox. The results match or even outperform similarly sized open-source baselines, including the judging model. CM2 thus provides a scalable recipe for optimizing multi-turn, multi-step tool-using agents without relying on verifiable rewards. Code provided by the open-source community: https://github.com/namezhenzhang/CM2-RLCR-Tool-Agent.

### 🤖 AI 总结

**一句话总结**：CM2提出以“清单式奖励”替代可验证结果奖励，在LLM模拟工具环境中对多轮多步骤工具型代理做强化学习，显著优于SFT并达到/超越同规模开源基线。

**研究动机**：现实多轮工具使用任务缺乏可验证奖励且评判开放、易不稳定，搭建可执行工具环境成本高、限制规模；需要一种可扩展且稳定的RL优化方式。

**核心方法**：将每轮意图分解为细粒度二元标准并要求证据与结构化元数据支撑，用稀疏奖励但密集评估标准把开放式评判转为更稳的分类式决策；在LLM模拟的工具环境中训练，起始于8B基座、8k条RL数据。

**主要结论**：CM2相较SFT在tau^-Bench提升8分、BFCL-V4提升10分、ToolSandbox提升12分，达到或超过同规模开源基线（含判别模型）；为无需可验证结果奖励的多轮多步骤工具代理提供了可扩展的优化范式。

**关键词**：标题, CM2, Reinforcement, Learning, Checklist, Rewards, Multi-Turn, Multi-Step

**评分**：55

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12268v1) | [下载PDF](https://arxiv.org/pdf/2602.12268v1.pdf)

---

## [2. Think like a Scientist: Physics-guided LLM Agent for Equation Discovery](https://arxiv.org/abs/2602.12259v1)

**作者**：Jianke Yang, Ohm Venkatachalam, Mohammad Kianezhad 等 5 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-02-12

### 📄 论文摘要

Explaining observed phenomena through symbolic, interpretable formulas is a fundamental goal of science. Recently, large language models (LLMs) have emerged as promising tools for symbolic equation discovery, owing to their broad domain knowledge and strong reasoning capabilities. However, most existing LLM-based systems try to guess equations directly from data, without modeling the multi-step reasoning process that scientists often follow: first inferring physical properties such as symmetries, then using these as priors to restrict the space of candidate equations. We introduce KeplerAgent, an agentic framework that explicitly follows this scientific reasoning process. The agent coordinates physics-based tools to extract intermediate structure and uses these results to configure symbolic regression engines such as PySINDy and PySR, including their function libraries and structural constraints. Across a suite of physical equation benchmarks, KeplerAgent achieves substantially higher symbolic accuracy and greater robustness to noisy data than both LLM and traditional baselines.

### 🤖 AI 总结

**一句话总结**：KeplerAgent是一个遵循科学推理流程的物理引导LLM代理，先提取物理性质再约束符号回归，从而更准确且更抗噪地发现解释现象的方程。

**研究动机**：现有LLM多直接从数据猜公式，未显式建模科学家常用的多步推理与物理先验（如对称性），导致准确性与稳健性不足；需要把这些先验融入方程发现。

**核心方法**：代理框架协调物理工具提取中间结构（如对称性、守恒量），并据此配置PySINDy与PySR的函数库与结构约束，逐步收缩候选空间以进行符号回归。

**主要结论**：在多种物理方程基准上，KeplerAgent的符号准确率显著提升且对噪声更鲁棒，优于纯LLM方法和传统符号回归基线。

**关键词**：标题, Think, like, Scientist, Physics-guided, LLM, Agent, Equation

**评分**：51

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12259v1) | [下载PDF](https://arxiv.org/pdf/2602.12259v1.pdf)

---

## [3. "Sorry, I Didn't Catch That": How Speech Models Miss What Matters Most](https://arxiv.org/abs/2602.12249v1)

**作者**：Kaitlyn Zhou, Martijn Bartelds, Federico Bianchi 等 4 位作者  
**分类**：cs.AI, cs.CL, cs.CY  
**发布时间**：2026-02-12

### 📄 论文摘要

Despite speech recognition systems achieving low word error rates on standard benchmarks, they often fail on short, high-stakes utterances in real-world deployments. Here, we study this failure mode in a high-stakes task: the transcription of U.S. street names as spoken by U.S. participants. We evaluate 15 models from OpenAI, Deepgram, Google, and Microsoft on recordings from linguistically diverse U.S. speakers and find an average transcription error rate of 44%. We quantify the downstream impact of failed transcriptions by geographic locations and show that mis-transcriptions systematically cause errors for all speakers, but that routing distance errors are twice as large for non-English primary speakers compared to English primary speakers. To mitigate this harm, we introduce a synthetic data generation approach that produces diverse pronunciations of named entities using open-source text-to-speech models. Fine-tuning with less than 1,000 synthetic samples improves street name transcription accuracy by nearly 60% (relative to base models) for non-English primary speakers. Our results highlight a critical gap between benchmark performance and real-world reliability in speech systems and demonstrate a simple, scalable path to reducing high-stakes transcription errors.

### 🤖 AI 总结

**一句话总结**：商业语音识别在街道名等短而高风险语句上大幅失效（平均错误率44%），但用少量合成多样发音数据微调可显著降低错误并减少不公平。

**研究动机**：基准测试的低WER掩盖了真实场景中对导航等关键任务至关重要的短语句转写失败，且这些失败对非英语母语使用者伤害更大。

**核心方法**：收集多语言背景的美国说话人朗读美国街道名，评测来自OpenAI、Deepgram、Google、Microsoft的15个ASR；量化转写错误及由此导致的地理路由偏差；用开源TTS生成具有多样发音的专名合成数据，用不足1000条样本对模型微调并评估增益。

**主要结论**：所有群体均受误转写影响，但非英语母语者的路由距离误差约为英语母语者的两倍；通过少量合成数据微调使非英语母语者的街道名识别相对提升近60%，凸显基准与实用可靠性间的鸿沟并提供简单可扩展的缓解路径。

**关键词**：标题, "Sorry, Didn't, Catch, That", How, Speech, Models

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12249v1) | [下载PDF](https://arxiv.org/pdf/2602.12249v1.pdf)

---

## cs.CV

## [4. Stroke of Surprise: Progressive Semantic Illusions in Vector Sketching](https://arxiv.org/abs/2602.12280v1)

**作者**：Huai-Hsun Cheng, Siang-Ling Zhang, Yu-Lun Liu  
**分类**：cs.CV  
**发布时间**：2026-02-12

### 📄 论文摘要

Visual illusions traditionally rely on spatial manipulations such as multi-view consistency. In this work, we introduce Progressive Semantic Illusions, a novel vector sketching task where a single sketch undergoes a dramatic semantic transformation through the sequential addition of strokes. We present Stroke of Surprise, a generative framework that optimizes vector strokes to satisfy distinct semantic interpretations at different drawing stages. The core challenge lies in the "dual-constraint": initial prefix strokes must form a coherent object (e.g., a duck) while simultaneously serving as the structural foundation for a second concept (e.g., a sheep) upon adding delta strokes. To address this, we propose a sequence-aware joint optimization framework driven by a dual-branch Score Distillation Sampling (SDS) mechanism. Unlike sequential approaches that freeze the initial state, our method dynamically adjusts prefix strokes to discover a "common structural subspace" valid for both targets. Furthermore, we introduce a novel Overlay Loss that enforces spatial complementarity, ensuring structural integration rather than occlusion. Extensive experiments demonstrate that our method significantly outperforms state-of-the-art baselines in recognizability and illusion strength, successfully expanding visual anagrams from the spatial to the temporal dimension. Project page: https://stroke-of-surprise.github.io/

### 🤖 AI 总结

**一句话总结**：提出“Stroke of Surprise”，通过序列感知的联合优化让同一矢量草图在逐步添加笔画时从概念A平滑转化为概念B，并用Overlay Loss增强结构整合与幻觉效果。

**研究动机**：传统视觉错觉多依赖空间操控，难以实现随绘制进程改变语义的草图；作者希望前缀笔画既能构成对象A，又为加入增量笔画后生成对象B提供结构基础。

**核心方法**：采用序列感知的联合优化框架与双分支SDS，同时优化前缀与增量笔画以满足两阶段语义，动态调整前缀以发现两目标的共享结构子空间；引入Overlay Loss鼓励空间互补、避免遮挡，实现结构融合。

**主要结论**：实验显示该方法在可识别度与幻觉强度上显著优于基线，成功将视觉“变位”从空间拓展到时间维度的逐笔绘制过程。

**关键词**：标题, of, in, Stroke, Surprise, Progressive, Semantic, Illusions

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12280v1) | [下载PDF](https://arxiv.org/pdf/2602.12280v1.pdf)

---

## [5. UniT: Unified Multimodal Chain-of-Thought Test-time Scaling](https://arxiv.org/abs/2602.12279v1)

**作者**：Leon Liangyu Chen, Haoyu Ma, Zhipeng Fan 等 14 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-02-12

### 📄 论文摘要

Unified models can handle both multimodal understanding and generation within a single architecture, yet they typically operate in a single pass without iteratively refining their outputs. Many multimodal tasks, especially those involving complex spatial compositions, multiple interacting objects, or evolving instructions, require decomposing instructions, verifying intermediate results, and making iterative corrections. While test-time scaling (TTS) has demonstrated that allocating additional inference compute for iterative reasoning substantially improves language model performance, extending this paradigm to unified multimodal models remains an open challenge. We introduce UniT, a framework for multimodal chain-of-thought test-time scaling that enables a single unified model to reason, verify, and refine across multiple rounds. UniT combines agentic data synthesis, unified model training, and flexible test-time inference to elicit cognitive behaviors including verification, subgoal decomposition, and content memory. Our key findings are: (1) unified models trained on short reasoning trajectories generalize to longer inference chains at test time; (2) sequential chain-of-thought reasoning provides a more scalable and compute-efficient TTS strategy than parallel sampling; (3) training on generation and editing trajectories improves out-of-distribution visual reasoning. These results establish multimodal test-time scaling as an effective paradigm for advancing both generation and understanding in unified models.

### 🤖 AI 总结

**一句话总结**：UniT提出面向统一多模态模型的链式思维测试时扩展框架，使模型在多轮中分解、验证与修正，显著提升理解与生成能力。

**研究动机**：现有统一多模态模型多为单次前向、缺乏迭代推理与自我校验，而复杂空间关系与多对象/动态指令任务需要分解与纠错；语言模型的TTS已验证有效但尚未扩展到多模态统一模型。

**核心方法**：结合代理式数据合成、统一模型训练与灵活测试时推理策略，促发验证、子目标分解和内容记忆；采用顺序CoT迭代并训练生成与编辑轨迹，在测试时分配更多计算以实现推理、校验与精炼。

**主要结论**：统一模型在仅训练短推理轨迹下可于测试时推广到更长推理链；顺序链式推理较并行采样更可扩展且更省算；训练生成与编辑轨迹显著提升分布外视觉推理，确立多模态TTS为有效范式。

**关键词**：标题, 摘要, UniT, Unified, Multimodal, Chain-of-Thought, Test-time, Scaling

**评分**：43

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12279v1) | [下载PDF](https://arxiv.org/pdf/2602.12279v1.pdf)

---

## [6. MonarchRT: Efficient Attention for Real-Time Video Generation](https://arxiv.org/abs/2602.12271v1)

**作者**：Krish Agarwal, Zhuoming Chen, Cheng Luo 等 8 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-02-12

### 📄 论文摘要

Real-time video generation with Diffusion Transformers is bottlenecked by the quadratic cost of 3D self-attention, especially in real-time regimes that are both few-step and autoregressive, where errors compound across time and each denoising step must carry substantially more information. In this setting, we find that prior sparse-attention approximations break down, despite showing strong results for bidirectional, many-step diffusion. Specifically, we observe that video attention is not reliably sparse, but instead combines pronounced periodic structure driven by spatiotemporal position with dynamic, sparse semantic correspondences and dense mixing, exceeding the representational capacity of even oracle top-k attention. Building on this insight, we propose Monarch-RT, a structured attention parameterization for video diffusion models that factorizes attention using Monarch matrices. Through appropriately aligned block structure and our extended tiled Monarch parameterization, we achieve high expressivity while preserving computational efficiency. We further overcome the overhead of parameterization through finetuning, with custom Triton kernels. We first validate the high efficacy of Monarch-RT over existing sparse baselines designed only for bidirectional models. We further observe that Monarch-RT attains up to 95% attention sparsity with no loss in quality when applied to the state-of-the-art model Self-Forcing, making Monarch-RT a pioneering work on highly-capable sparse attention parameterization for real-time video generation. Our optimized implementation outperforms FlashAttention-2, FlashAttention-3, and FlashAttention-4 kernels on Nvidia RTX 5090, H100, and B200 GPUs respectively, providing kernel speedups in the range of 1.4-11.8X. This enables us, for the first time, to achieve true real-time video generation with Self-Forcing at 16 FPS on a single RTX 5090.

### 🤖 AI 总结

**一句话总结**：Monarch-RT提出基于Monarch矩阵的结构化注意力参数化，在少步自回归视频扩散中以高达95%稀疏度保持生成质量，并通过自研高效内核实现单卡16 FPS实时视频生成。

**研究动机**：3D自注意力的二次复杂度在少步自回归实时视频生成中成为瓶颈，而视频注意力呈现时空周期性+动态稀疏+致密混合的复合结构，使传统稀疏/Top-k近似在该设定下失效。

**核心方法**：利用Monarch矩阵对注意力进行因式分解，设计对齐块结构与扩展的tiled Monarch参数化以同时表达周期性时空结构、动态语义对应与致密混合；结合微调与Triton自定义内核，降低参数化开销并提升推理速度。

**主要结论**：相较面向双向多步扩散的稀疏基线，Monarch-RT在Self-Forcing上以最高95%稀疏度无质量损失，并在RTX 5090/H100/B200上较FlashAttention-2/3/4取得1.4–11.8倍加速，首次实现单张RTX 5090的16 FPS实时视频生成。

**关键词**：标题, 摘要, MonarchRT, Efficient, Attention, Real-Time, Video, Generation

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12271v1) | [下载PDF](https://arxiv.org/pdf/2602.12271v1.pdf)

---

## cs.LG

## [7. Function-Space Decoupled Diffusion for Forward and Inverse Modeling in Carbon Capture and Storage](https://arxiv.org/abs/2602.12274v1)

**作者**：Xin Ju, Jiachen Yao, Anima Anandkumar 等 5 位作者  
**分类**：cs.LG, physics.geo-ph  
**发布时间**：2026-02-12

### 📄 论文摘要

Accurate characterization of subsurface flow is critical for Carbon Capture and Storage (CCS) but remains challenged by the ill-posed nature of inverse problems with sparse observations. We present Fun-DDPS, a generative framework that combines function-space diffusion models with differentiable neural operator surrogates for both forward and inverse modeling. Our approach learns a prior distribution over geological parameters (geomodel) using a single-channel diffusion model, then leverages a Local Neural Operator (LNO) surrogate to provide physics-consistent guidance for cross-field conditioning on the dynamics field. This decoupling allows the diffusion prior to robustly recover missing information in parameter space, while the surrogate provides efficient gradient-based guidance for data assimilation. We demonstrate Fun-DDPS on synthetic CCS modeling datasets, achieving two key results: (1) For forward modeling with only 25% observations, Fun-DDPS achieves 7.7% relative error compared to 86.9% for standard surrogates (an 11x improvement), proving its capability to handle extreme data sparsity where deterministic methods fail. (2) We provide the first rigorous validation of diffusion-based inverse solvers against asymptotically exact Rejection Sampling (RS) posteriors. Both Fun-DDPS and the joint-state baseline (Fun-DPS) achieve Jensen-Shannon divergence less than 0.06 against the ground truth. Crucially, Fun-DDPS produces physically consistent realizations free from the high-frequency artifacts observed in joint-state baselines, achieving this with 4x improved sample efficiency compared to rejection sampling.

### 🤖 AI 总结

**一句话总结**：提出Fun-DDPS，将函数空间扩散先验与局部神经算子（LNO）解耦结合，实现CCS前向与反演中在稀疏观测下的物理一致生成与高效数据同化。

**研究动机**：CCS地下流动反演病态且观测稀疏，传统确定性代理在极端稀疏下失效，亟需既能补全参数信息又保持物理一致性的生成式方法，并对其后验进行严格验证。

**核心方法**：用单通道函数空间扩散模型学习地质参数先验，借助可微的局部神经算子提供跨场条件与物理一致的梯度引导；解耦设计使扩散先验补全缺失参数，LNO高效执行数据同化与指导采样。

**主要结论**：在仅25%观测下，前向建模相对误差为7.7%，显著优于标准代理的86.9%（约11倍提升）。反演中相对拒绝采样后验的JS散度<0.06，样本效率提升4倍，并生成无联合状态基线（Fun-DPS）高频伪影的物理一致解。

**关键词**：标题, Function-Space, Decoupled, Diffusion, Forward, Inverse, Modeling, in

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12274v1) | [下载PDF](https://arxiv.org/pdf/2602.12274v1.pdf)

---

## [8. Self-Supervised Learning via Flow-Guided Neural Operator on Time-Series Data](https://arxiv.org/abs/2602.12267v1)

**作者**：Duy Nguyen, Jiachen Yao, Jiayun Wang 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-12

### 📄 论文摘要

Self-supervised learning (SSL) is a powerful paradigm for learning from unlabeled time-series data. However, popular methods such as masked autoencoders (MAEs) rely on reconstructing inputs from a fixed, predetermined masking ratio. Instead of this static design, we propose treating the corruption level as a new degree of freedom for representation learning, enhancing flexibility and performance. To achieve this, we introduce the Flow-Guided Neural Operator (FGNO), a novel framework combining operator learning with flow matching for SSL training. FGNO learns mappings in functional spaces by using Short-Time Fourier Transform to unify different time resolutions. We extract a rich hierarchy of features by tapping into different network layers and flow times that apply varying strengths of noise to the input data. This enables the extraction of versatile representations, from low-level patterns to high-level global features, using a single model adaptable to specific tasks. Unlike prior generative SSL methods that use noisy inputs during inference, we propose using clean inputs for representation extraction while learning representations with noise; this eliminates randomness and boosts accuracy. We evaluate FGNO across three biomedical domains, where it consistently outperforms established baselines. Our method yields up to 35% AUROC gains in neural signal decoding (BrainTreeBank), 16% RMSE reductions in skin temperature prediction (DREAMT), and over 20% improvement in accuracy and macro-F1 on SleepEDF under low-data regimes. These results highlight FGNO's robustness to data scarcity and its superior capacity to learn expressive representations for diverse time series.

### 🤖 AI 总结

**一句话总结**：提出Flow-Guided Neural Operator（FGNO），将算子学习与flow matching结合，把噪声/腐蚀强度作为自监督自由度，训练时多层次噪声学习、推理用干净输入，在多项生物医学时序任务上显著超越基线。

**研究动机**：现有时序SSL（如MAE）依赖固定遮盖比例、难以适配多时间尺度与任务需求，且推理含噪造成随机性与性能损失。需要一种能跨尺度提取层次化表示、在小样本下仍稳健且推理稳定的方法。

**核心方法**：提出FGNO在函数空间中学习映射，使用STFT统一时间分辨率，并以flow matching注入可控噪声；从不同网络层与不同flow时间聚合多粒度特征。训练阶段用带噪样本促进表示学习，推理阶段改用干净输入提取表示以消除随机性。

**主要结论**：FGNO在BrainTreeBank、DREAMT和SleepEDF上分别实现最高35% AUROC提升、16% RMSE降低及低数据场景下>20%准确率与宏F1提升，展现出对数据稀缺的鲁棒性和对多样时序任务的强泛化能力。

**关键词**：标题, Self-Supervised, Learning, via, Flow-Guided, Neural, Operator, on

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12267v1) | [下载PDF](https://arxiv.org/pdf/2602.12267v1.pdf)

---

## [9. Community Concealment from Unsupervised Graph Learning-Based Clustering](https://arxiv.org/abs/2602.12250v1)

**作者**：Dalyapraz Manatova, Pablo Moriano, L. Jean Camp  
**分类**：cs.LG, cs.CR, cs.SI  
**发布时间**：2026-02-12

### 📄 论文摘要

Graph neural networks (GNNs) are designed to use attributed graphs to learn representations. Such representations are beneficial in the unsupervised learning of clusters and community detection. Nonetheless, such inference may reveal sensitive groups, clustered systems, or collective behaviors, raising concerns regarding group-level privacy. Community attribution in social and critical infrastructure networks, for example, can expose coordinated asset groups, operational hierarchies, and system dependencies that could be used for profiling or intelligence gathering. We study a defensive setting in which a data publisher (defender) seeks to conceal a community of interest while making limited, utility-aware changes in the network. Our analysis indicates that community concealment is strongly influenced by two quantifiable factors: connectivity at the community boundary and feature similarity between the protected community and adjacent communities. Informed by these findings, we present a perturbation strategy that rewires a set of selected edges and modifies node features to reduce the distinctiveness leveraged by GNN message passing. The proposed method outperforms DICE in our experiments on synthetic benchmarks and real network graphs under identical perturbation budgets. Overall, it achieves median relative concealment improvements of approximately 20-45% across the evaluated settings. These findings demonstrate a mitigation strategy against GNN-based community learning and highlight group-level privacy risks intrinsic to graph learning.

### 🤖 AI 总结

**一句话总结**：提出一种在有限预算下通过改边与特征修改来降低GNN无监督聚类可识别性，从而隐匿目标社区的方法，实验证明优于DICE并提升隐匿效果约20-45%。

**研究动机**：GNN驱动的无监督社区检测可能暴露社会或基础设施网络中的敏感群体结构，亟需在保留数据效用的前提下实现群体级隐私防护。

**核心方法**：分析并量化影响隐匿的两大因素——社区边界连通性与与邻近社区的特征相似度；据此在扰动预算内选择性重连边并修改节点特征，削弱GNN消息传递所依赖的可区分性。

**主要结论**：所提策略在合成与真实网络上均显著提升社区隐匿（相对提升约20-45%），优于DICE，表明可行的GNN社区学习对抗方案并揭示图学习内在的群体隐私风险。

**关键词**：标题, 摘要, Community, Concealment, Unsupervised, Graph, Learning-Based, Clustering

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12250v1) | [下载PDF](https://arxiv.org/pdf/2602.12250v1.pdf)

---

## [10. ExtractBench: A Benchmark and Evaluation Methodology for Complex Structured Extraction](https://arxiv.org/abs/2602.12247v1)

**作者**：Nick Ferguson, Josh Pennington, Narek Beghian 等 7 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-12

### 📄 论文摘要

Unstructured documents like PDFs contain valuable structured information, but downstream systems require this data in reliable, standardized formats. LLMs are increasingly deployed to automate this extraction, making accuracy and reliability paramount. However, progress is bottlenecked by two gaps. First, no end-to-end benchmark evaluates PDF-to-JSON extraction under enterprise-scale schema breadth. Second, no principled methodology captures the semantics of nested extraction, where fields demand different notions of correctness (exact match for identifiers, tolerance for quantities, semantic equivalence for names), arrays require alignment, and omission must be distinguished from hallucination. We address both gaps with ExtractBench, an open-source benchmark and evaluation framework for PDF-to-JSON structured extraction. The benchmark pairs 35 PDF documents with JSON Schemas and human-annotated gold labels across economically valuable domains, yielding 12,867 evaluatable fields spanning schema complexities from tens to hundreds of fields. The evaluation framework treats the schema as an executable specification: each field declares its scoring metric. Baseline evaluations reveal that frontier models (GPT-5/5.2, Gemini-3 Flash/Pro, Claude 4.5 Opus/Sonnet) remain unreliable on realistic schemas. Performance degrades sharply with schema breadth, culminating in 0% valid output on a 369-field financial reporting schema across all tested models. We release ExtractBench at https://github.com/ContextualAI/extract-bench.

### 🤖 AI 总结

**一句话总结**：提出ExtractBench，一个用于PDF到JSON复杂结构化抽取的开源基准与可执行评估方法，显示前沿LLM在企业级宽模式下可靠性明显不足。

**研究动机**：缺乏覆盖企业级模式广度的端到端PDF→JSON基准，以及能刻画嵌套抽取中多样正确性标准（精确匹配、数量容差、语义等价、数组对齐、区分漏报与幻觉）的评估方法，导致进展受限。

**核心方法**：构建包含35份PDF、配套JSON Schema与人工金标的ExtractBench（共12,867个可评估字段）。将Schema视为可执行规范：每个字段声明其评分度量，覆盖标识符精确匹配、数量容差、名称语义等价、数组对齐及漏报/幻觉识别，并提供多模型基线评测。

**主要结论**：前沿模型（GPT-5/5.2、Gemini-3 Flash/Pro、Claude 4.5 Opus/Sonnet）在现实复杂Schema上不可靠，性能随Schema扩展急剧下降；在369字段的财务报告Schema上所有模型均产生0%有效输出。ExtractBench提供统一数据与严谨评估框架，促进该方向的可靠性研究与系统改进。

**关键词**：标题, ExtractBench, Benchmark, Evaluation, Methodology, Complex, Structured, Extraction

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12247v1) | [下载PDF](https://arxiv.org/pdf/2602.12247v1.pdf)

---

## [11. Intrinsic-Energy Joint Embedding Predictive Architectures Induce Quasimetric Spaces](https://arxiv.org/abs/2602.12245v1)

**作者**：Anthony Kobanda, Waris Radji  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-12

### 📄 论文摘要

Joint-Embedding Predictive Architectures (JEPAs) aim to learn representations by predicting target embeddings from context embeddings, inducing a scalar compatibility energy in a latent space. In contrast, Quasimetric Reinforcement Learning (QRL) studies goal-conditioned control through directed distance values (cost-to-go) that support reaching goals under asymmetric dynamics. In this short article, we connect these viewpoints by restricting attention to a principled class of JEPA energy functions : intrinsic (least-action) energies, defined as infima of accumulated local effort over admissible trajectories between two states. Under mild closure and additivity assumptions, any intrinsic energy is a quasimetric. In goal-reaching control, optimal cost-to-go functions admit exactly this intrinsic form ; inversely, JEPAs trained to model intrinsic energies lie in the quasimetric value class targeted by QRL. Moreover, we observe why symmetric finite energies are structurally mismatched with one-way reachability, motivating asymmetric (quasimetric) energies when directionality matters.

### 🤖 AI 总结

**一句话总结**：本文将JEPA的“内在（最小行动）能量”与QRL的定向代价到达函数建立等价联系，证明其在潜空间中诱导拟度量，并强调非对称能量更适配一方向可达性。

**研究动机**：现有对称兼容能量难以表达单向可达性与方向性动态，作者希望用统一的能量-距离视角把JEPA的表示学习与QRL的目标驱动控制对齐。

**核心方法**：定义内在能量为两状态间可行轨迹上累计局部努力的下确界，在温和的闭合与可加性条件下证明其为拟度量；同时证明最优cost-to-go具有相同内在形式，并将JEPA训练目标对准该能量类。

**主要结论**：用内在能量训练的JEPA会在潜空间诱导拟度量，与目标达成控制的价值函数一致；对称有限能量与单向可达性结构不匹配，方向性任务应采用非对称（拟度量）能量。

**关键词**：标题, Intrinsic-Energy, Joint, Embedding, Predictive, Architectures, Induce, Quasimetric

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12245v1) | [下载PDF](https://arxiv.org/pdf/2602.12245v1.pdf)

---

## [12. Olmix: A Framework for Data Mixing Throughout LM Development](https://arxiv.org/abs/2602.12237v1)

**作者**：Mayee F. Chen, Tyler Murray, David Heineman 等 8 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-02-12

### 📄 论文摘要

Data mixing -- determining the ratios of data from different domains -- is a first-order concern for training language models (LMs). While existing mixing methods show promise, they fall short when applied during real-world LM development. We present Olmix, a framework that addresses two such challenges. First, the configuration space for developing a mixing method is not well understood -- design choices across existing methods lack justification or consensus and overlook practical issues like data constraints. We conduct a comprehensive empirical study of this space, identifying which design choices lead to a strong mixing method. Second, in practice, the domain set evolves throughout LM development as datasets are added, removed, partitioned, and revised -- a problem setting largely unaddressed by existing works, which assume fixed domains. We study how to efficiently recompute the mixture after the domain set is updated, leveraging information from past mixtures. We introduce mixture reuse, a mechanism that reuses existing ratios and recomputes ratios only for domains affected by the update. Over a sequence of five domain-set updates mirroring real-world LM development, mixture reuse matches the performance of fully recomputing the mix after each update with 74% less compute and improves over training without mixing by 11.6% on downstream tasks.

### 🤖 AI 总结

**一句话总结**：Olmix提出一个用于语言模型训练的数据混合框架，通过系统化设计与“混合重用”机制在域集合演变中维持性能并显著节省计算。

**研究动机**：现有混合方法缺乏对设计选择与数据约束的系统理解，且常假设域集合固定；现实开发中数据集会增删、分区与修订，亟需能随域演变高效更新混合比的方法。

**核心方法**：进行全面实证研究以梳理混合方法的配置空间与有效设计选择；提出“混合重用”机制，复用既有比例、仅对受影响域重算，并在五次贴近真实的域集合更新序列上评测。

**主要结论**：混合重用在保持与每次完全重算相当性能的同时减少74%计算，并较无混合训练在下游任务上提升11.6%；该框架为实用场景下强数据混合方法的设计与迭代提供依据。

**关键词**：标题, LM, Olmix, Framework, Data, Mixing, Throughout, Development

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12237v1) | [下载PDF](https://arxiv.org/pdf/2602.12237v1.pdf)

---

## [13. Categorical Flow Maps](https://arxiv.org/abs/2602.12233v1)

**作者**：Daan Roos, Oscar Davis, Floor Eijkelboom 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-12

### 📄 论文摘要

We introduce Categorical Flow Maps, a flow-matching method for accelerated few-step generation of categorical data via self-distillation. Building on recent variational formulations of flow matching and the broader trend towards accelerated inference in diffusion and flow-based models, we define a flow map towards the simplex that transports probability mass toward a predicted endpoint, yielding a parametrisation that naturally constrains model predictions. Since our trajectories are continuous rather than discrete, Categorical Flow Maps can be trained with existing distillation techniques, as well as a new objective based on endpoint consistency. This continuous formulation also automatically unlocks test-time inference: we can directly reuse existing guidance and reweighting techniques in the categorical setting to steer sampling toward downstream objectives. Empirically, we achieve state-of-the-art few-step results on images, molecular graphs, and text, with strong performance even in single-step generation.

### 🤖 AI 总结

**一句话总结**：提出 Categorical Flow Maps，用连续流匹配与自蒸馏加速类别数据的少步（甚至单步）生成，并在图像、分子图和文本上达成SOTA。

**研究动机**：离散/类别数据生成缺乏可用于蒸馏与加速推理的连续轨迹，且需要在概率单纯形上自然约束输出并复用扩散/流模型中的引导与重加权以提升下游目标。

**核心方法**：定义朝向单纯形的流映射，将概率质量运输到预测终点，实现受约束的参数化；训练结合现有自蒸馏技术并提出终点一致性目标，连续表述使得测试时可直接应用引导与重加权以控制采样。

**主要结论**：在图像、分子图与文本任务上取得最优的少步生成结果，单步亦具强性能；方法兼具速度与可控性，为类别数据的加速生成提供通用方案。

**关键词**：标题, 摘要, We, Categorical, Flow, Maps, introduce, flow-matching

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12233v1) | [下载PDF](https://arxiv.org/pdf/2602.12233v1.pdf)

---

## [14. Diffusion Alignment Beyond KL: Variance Minimisation as Effective Policy Optimiser](https://arxiv.org/abs/2602.12229v1)

**作者**：Zijing Ou, Jacob Si, Junyi Zhu 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-12

### 📄 论文摘要

Diffusion alignment adapts pretrained diffusion models to sample from reward-tilted distributions along the denoising trajectory. This process naturally admits a Sequential Monte Carlo (SMC) interpretation, where the denoising model acts as a proposal and reward guidance induces importance weights. Motivated by this view, we introduce Variance Minimisation Policy Optimisation (VMPO), which formulates diffusion alignment as minimising the variance of log importance weights rather than directly optimising a Kullback-Leibler (KL) based objective. We prove that the variance objective is minimised by the reward-tilted target distribution and that, under on-policy sampling, its gradient coincides with that of standard KL-based alignment. This perspective offers a common lens for understanding diffusion alignment. Under different choices of potential functions and variance minimisation strategies, VMPO recovers various existing methods, while also suggesting new design directions beyond KL.

### 🤖 AI 总结

**一句话总结**：提出VMPO，将扩散对齐从KL优化转为最小化对数重要性权重的方差，在on-policy采样下与KL对齐梯度一致，并为奖励倾斜采样提供统一且更灵活的视角。

**研究动机**：从SMC视角看，奖励引导形成重要性权重，直接降低权重方差可更好逼近目标分布并可能带来更稳定的优化；希望用统一框架理解并拓展扩散对齐方法，摆脱对KL的依赖。

**核心方法**：把扩散对齐建模为沿去噪轨迹的SMC过程，以奖励倾斜分布为目标，提出最小化log重要性权重方差的VMPO；证明该目标在目标分布处取得最小值，且在on-policy采样时其梯度等同于标准KL对齐，并通过不同潜能/方差策略复现并拓展既有方法。

**主要结论**：VMPO为扩散对齐提供了有效的策略优化器和统一理论视角，既能解释并涵盖现有方法，又指向超越KL的新的设计方向；其与奖励倾斜目标一致且在特定条件下与KL梯度等价。

**关键词**：标题, Diffusion, KL, as, Alignment, Beyond, Variance, Minimisation

**评分**：19

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12229v1) | [下载PDF](https://arxiv.org/pdf/2602.12229v1.pdf)

---

## [15. Towards On-Policy SFT: Distribution Discriminant Theory and its Applications in LLM Training](https://arxiv.org/abs/2602.12222v1)

**作者**：Miaosen Zhang, Yishan Liu, Shuxia Lin 等 11 位作者  
**分类**：cs.LG, cs.AI, cs.CV  
**发布时间**：2026-02-12

### 📄 论文摘要

Supervised fine-tuning (SFT) is computationally efficient but often yields inferior generalization compared to reinforcement learning (RL). This gap is primarily driven by RL's use of on-policy data. We propose a framework to bridge this chasm by enabling On-Policy SFT. We first present \textbf{\textit{Distribution Discriminant Theory (DDT)}}, which explains and quantifies the alignment between data and the model-induced distribution. Leveraging DDT, we introduce two complementary techniques: (i) \textbf{\textit{In-Distribution Finetuning (IDFT)}}, a loss-level method to enhance generalization ability of SFT, and (ii) \textbf{\textit{Hinted Decoding}}, a data-level technique that can re-align the training corpus to the model's distribution. Extensive experiments demonstrate that our framework achieves generalization performance on par with prominent offline RL algorithms, including DPO and SimPO, while maintaining the efficiency of an SFT pipeline. The proposed framework thus offers a practical alternative in domains where RL is infeasible. We open-source the code here: https://github.com/zhangmiaosen2000/Towards-On-Policy-SFT

### 🤖 AI 总结

**一句话总结**：提出分布判别理论（DDT）及两项技术（IDFT与Hinted Decoding），实现近似“on-policy”的SFT，在保持SFT高效性的同时实现接近DPO/SimPO的泛化表现。

**研究动机**：传统SFT尽管高效，但因缺乏on-policy数据而在泛化上落后于RL；为降低RL成本并弥补泛化差距，需让SFT在不引入RL复杂度的前提下更贴近模型诱导分布。

**核心方法**：DDT用于解释与量化训练数据与模型诱导分布的对齐度；据此提出损失层面的IDFT以提升泛化，以及数据层面的Hinted Decoding以重整语料分布，从而将二者整合到标准SFT流程。

**主要结论**：实验表明该框架在泛化性能上可媲美离线RL算法（如DPO、SimPO），同时保持SFT的计算效率，为RL不可行的场景提供切实可用的替代方案。

**关键词**：标题, Towards, On-Policy, SFT, Distribution, Discriminant, Theory, its

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12222v1) | [下载PDF](https://arxiv.org/pdf/2602.12222v1.pdf)

---

