# arXiv AI 论文日报 | 2026-02-16

> 共 15 篇论文，由AI自动总结

## 📑 目录

- [cs.AI](#csAI) (3 篇)
- [cs.LG](#csLG) (8 篇)
- [cs.CL](#csCL) (1 篇)
- [cs.CV](#csCV) (3 篇)

---

## cs.AI

## [1. Predicting Invoice Dilution in Supply Chain Finance with Leakage Free Two Stage XGBoost, KAN (Kolmogorov Arnold Networks), and Ensemble Models](https://arxiv.org/abs/2602.15248v1)

**作者**：Pavel Koptev, Vishnu Kumar, Konstantin Malkov 等 5 位作者  
**分类**：cs.AI, math.OC, q-fin.MF  
**发布时间**：2026-02-16

### 📄 论文摘要

Invoice or payment dilution is the gap between the approved invoice amount and the actual collection is a significant source of non credit risk and margin loss in supply chain finance. Traditionally, this risk is managed through the buyer's irrevocable payment undertaking (IPU), which commits to full payment without deductions. However, IPUs can hinder supply chain finance adoption, particularly among sub-invested grade buyers. A newer, data-driven methods use real-time dynamic credit limits, projecting dilution for each buyer-supplier pair in real-time. This paper introduces an AI, machine learning framework and evaluates how that can supplement a deterministic algorithm to predict invoice dilution using extensive production dataset across nine key transaction fields.

### 🤖 AI 总结

**一句话总结**：论文提出一个结合“无泄漏”的两阶段XGBoost、KAN与集成模型的框架，用生产级交易字段实时预测买方-供应商维度的发票稀释（实际回款低于核准金额）。

**研究动机**：发票稀释会带来显著的非信用风险与利润损失，而传统依赖买方不可撤销付款承诺（IPU）的方式会抬高准入门槛、阻碍供应链金融在非投资级买方中的推广。

**核心方法**：基于覆盖9个关键交易字段的真实生产数据，构建可与现有确定性规则互补的机器学习预测体系，采用“Leakage Free”两阶段建模思路并对XGBoost、KAN及其集成方案进行对比评估，以实现按买方-供应商对的实时稀释预测与动态额度支持。

**主要结论**：实验表明数据驱动的两阶段XGBoost/KAN与集成模型能够有效预测发票稀释，可作为确定性算法的补充用于实时动态信用限额，从而降低对IPU的依赖并提升供应链金融的可用性。

**关键词**：供应链金融, 发票稀释预测, 支付稀释风险, 买方-供应商对建模, 实时风险评分, 特征泄漏防护, 集成学习, 规则模型与机器学习融合

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15248v1) | [下载PDF](https://arxiv.org/pdf/2602.15248v1.pdf)

---

## [2. Secure and Energy-Efficient Wireless Agentic AI Networks](https://arxiv.org/abs/2602.15212v1)

**作者**：Yuanyan Song, Kezhi Wang, Xinmian Xu  
**分类**：cs.AI  
**发布时间**：2026-02-16

### 📄 论文摘要

In this paper, we introduce a secure wireless agentic AI network comprising one supervisor AI agent and multiple other AI agents to provision quality of service (QoS) for users' reasoning tasks while ensuring confidentiality of private knowledge and reasoning outcomes. Specifically, the supervisor AI agent can dynamically assign other AI agents to participate in cooperative reasoning, while the unselected AI agents act as friendly jammers to degrade the eavesdropper's interception performance. To extend the service duration of AI agents, an energy minimization problem is formulated that jointly optimizes AI agent selection, base station (BS) beamforming, and AI agent transmission power, subject to latency and reasoning accuracy constraints. To address the formulated problem, we propose two resource allocation schemes, ASC and LAW, which first decompose it into three sub-problems. Specifically, ASC optimizes each sub-problem iteratively using the proposed alternating direction method of multipliers (ADMM)-based algorithm, semi-definite relaxation (SDR), and successive convex approximation (SCA), while LAW tackles each sub-problem using the proposed large language model (LLM) optimizer within an agentic workflow. The experimental results show that the proposed solutions can reduce network energy consumption by up to 59.1% compared to other benchmark schemes. Furthermore, the proposed schemes are validated using a practical agentic AI system based on Qwen, demonstrating satisfactory reasoning accuracy across various public benchmarks.

### 🤖 AI 总结

**一句话总结**：提出一种安全且节能的无线Agentic AI网络，通过“协作推理+友军干扰”保障隐私与QoS，并联合优化资源分配以显著降低能耗。

**研究动机**：无线多智能体协作推理在提升用户任务QoS的同时面临窃听威胁与终端能量受限问题，需要在保密性、时延/准确率约束与能耗之间取得平衡。

**核心方法**：构建含监督Agent与多协作Agent的网络：被选中Agent参与协作推理，未选中Agent作为友军干扰器抑制窃听；建立联合优化问题（Agent选择、BS波束成形、Agent发射功率）并提出ASC（ADMM+SDR+SCA迭代分解求解）与LAW（在Agentic workflow中用LLM优化器求解各子问题）两种方案。

**主要结论**：实验表明ASC/LAW相比基线最高可降低59.1%网络能耗，并在基于Qwen的真实Agentic系统验证中保持多项公开基准上令人满意的推理准确率与约束满足。

**关键词**：无线多智能体网络, 安全推理, 物理层安全, 友好干扰, 协同推理, 资源分配优化, 能耗最小化, 波束成形, 功率控制

**评分**：43

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15212v1) | [下载PDF](https://arxiv.org/pdf/2602.15212v1.pdf)

---

## [3. Mind the (DH) Gap! A Contrast in Risky Choices Between Reasoning and Conversational LLMs](https://arxiv.org/abs/2602.15173v1)

**作者**：Luise Ge, Yongyan Zhang, Yevgeniy Vorobeychik  
**分类**：cs.AI  
**发布时间**：2026-02-16

### 📄 论文摘要

The use of large language models either as decision support systems, or in agentic workflows, is rapidly transforming the digital ecosystem. However, the understanding of LLM decision-making under uncertainty remains limited. We initiate a comparative study of LLM risky choices along two dimensions: (1) prospect representation (explicit vs. experience based) and (2) decision rationale (explanation). Our study, which involves 20 frontier and open LLMs, is complemented by a matched human subjects experiment, which provides one reference point, while an expected payoff maximizing rational agent model provides another. We find that LLMs cluster into two categories: reasoning models (RMs) and conversational models (CMs). RMs tend towards rational behavior, are insensitive to the order of prospects, gain/loss framing, and explanations, and behave similarly whether prospects are explicit or presented via experience history. CMs are significantly less rational, slightly more human-like, sensitive to prospect ordering, framing, and explanation, and exhibit a large description-history gap. Paired comparisons of open LLMs suggest that a key factor differentiating RMs and CMs is training for mathematical reasoning.

### 🤖 AI 总结

**一句话总结**：论文比较了推理型与对话型LLM在不确定风险决策中的差异，发现推理型更接近理性期望收益最大化，而对话型更受呈现方式与解释影响且存在显著“描述-经验”差距。

**研究动机**：LLM正被用于决策支持与代理式工作流，但其在不确定性下的决策规律与偏差（如框架效应、顺序效应）尚缺乏系统理解。作者希望明确不同类型LLM在风险选择上的行为特征，并与人类与理性基线对照。

**核心方法**：在20个前沿与开源LLM上，沿两维度操控实验：前景呈现（显式描述vs基于经验历史）与是否要求决策解释，并加入前景顺序与得失框架等因素；同时进行匹配的人类受试实验，并用期望收益最大化模型作理性参照。

**主要结论**：LLM呈现两类聚类：推理模型对顺序、框架与解释不敏感，且在显式与经验呈现下表现一致、更加理性；对话模型更不理性但略更像人类，显著受顺序/框架/解释影响并出现大的描述-历史差距，开源模型对比表明数学推理训练可能是区分两类的关键因素。

**关键词**：LLM决策不确定性, 风险选择, 前景理论, 描述-经验差距, 框架效应, 选项顺序效应, 解释对决策影响, 推理模型, 数学推理训练, 人类对照实验, 期望收益最大化

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15173v1) | [下载PDF](https://arxiv.org/pdf/2602.15173v1.pdf)

---

## cs.CL

## [4. AIC CTU@AVerImaTeC: dual-retriever RAG for image-text fact checking](https://arxiv.org/abs/2602.15190v1)

**作者**：Herbert Ullrich, Jan Drchal  
**分类**：cs.CL  
**发布时间**：2026-02-16

### 📄 论文摘要

In this paper, we present our 3rd place system in the AVerImaTeC shared task, which combines our last year's retrieval-augmented generation (RAG) pipeline with a reverse image search (RIS) module. Despite its simplicity, our system delivers competitive performance with a single multimodal LLM call per fact-check at just $0.013 on average using GPT5.1 via OpenAI Batch API. Our system is also easy to reproduce and tweak, consisting of only three decoupled modules - a textual retrieval module based on similarity search, an image retrieval module based on API-accessed RIS, and a generation module using GPT5.1 - which is why we suggest it as an accesible starting point for further experimentation. We publish its code and prompts, as well as our vector stores and insights into the scheme's running costs and directions for further improvement.

### 🤖 AI 总结

**一句话总结**：提出一种“双检索器”RAG事实核查系统，将文本相似检索与反向图片搜索结合，并用一次多模态LLM调用完成判定，成本低且效果名列前茅。

**研究动机**：现有图文事实核查需要同时覆盖文本证据与图像溯源，但常见方案要么成本高、要么流水线复杂难复现。作者希望用更简单、低成本、模块化的方案获得有竞争力的共享任务成绩。

**核心方法**：系统由三个解耦模块组成：文本端用向量相似检索召回候选证据，图像端通过API反向图片搜索获取相关来源，再把两路证据交给GPT5.1进行检索增强生成式核查（每次核查仅一次多模态LLM调用）。同时公开代码、提示词、向量库，并分析运行成本。

**主要结论**：该方法在AVerImaTeC共享任务中获得第3名，证明“文本检索+反向图搜+单次LLM生成”的简化RAG框架即可取得强基线表现。系统平均成本约$0.013/条且易复现，可作为后续改进与扩展的起点。

**关键词**：图文事实核查, 双检索器, 反向图像搜索, 文本相似度检索, 图像检索, 多模态LLM推理, 推理成本优化, 共享任务评测

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15190v1) | [下载PDF](https://arxiv.org/pdf/2602.15190v1.pdf)

---

## cs.CV

## [5. Time-Archival Camera Virtualization for Sports and Visual Performances](https://arxiv.org/abs/2602.15181v1)

**作者**：Yunxiao Zhang, William Stone, Suryansh Kumar  
**分类**：cs.CV, cs.LG, cs.RO  
**发布时间**：2026-02-16

### 📄 论文摘要

Camera virtualization -- an emerging solution to novel view synthesis -- holds transformative potential for visual entertainment, live performances, and sports broadcasting by enabling the generation of photorealistic images from novel viewpoints using images from a limited set of calibrated multiple static physical cameras. Despite recent advances, achieving spatially and temporally coherent and photorealistic rendering of dynamic scenes with efficient time-archival capabilities, particularly in fast-paced sports and stage performances, remains challenging for existing approaches. Recent methods based on 3D Gaussian Splatting (3DGS) for dynamic scenes could offer real-time view-synthesis results. Yet, they are hindered by their dependence on accurate 3D point clouds from the structure-from-motion method and their inability to handle large, non-rigid, rapid motions of different subjects (e.g., flips, jumps, articulations, sudden player-to-player transitions). Moreover, independent motions of multiple subjects can break the Gaussian-tracking assumptions commonly used in 4DGS, ST-GS, and other dynamic splatting variants. This paper advocates reconsidering a neural volume rendering formulation for camera virtualization and efficient time-archival capabilities, making it useful for sports broadcasting and related applications. By modeling a dynamic scene as rigid transformations across multiple synchronized camera views at a given time, our method performs neural representation learning, providing enhanced visual rendering quality at test time. A key contribution of our approach is its support for time-archival, i.e., users can revisit any past temporal instance of a dynamic scene and can perform novel view synthesis, enabling retrospective rendering for replay, analysis, and archival of live events, a functionality absent in existing neural rendering approaches and novel view synthesis...

### 🤖 AI 总结

**一句话总结**：提出一种面向体育与舞台表演的“时间可归档”相机虚拟化神经渲染方法，在动态快速运动场景中实现更时空一致、逼真的新视角合成，并支持回看任意历史时刻重渲染。

**研究动机**：现有动态3DGS/4DGS等方法依赖高质量SfM点云且难以应对大幅非刚体快速运动与多主体独立运动，导致跟踪假设被破坏、渲染不稳定；同时缺乏对过去时间点的可检索重放（time-archival）能力。

**核心方法**：回到神经体渲染框架，将每个时间点的动态场景建模为跨多路同步相机视图的刚体变换组合，并在此表示上进行神经表示学习，以提升测试时的新视角渲染质量与时空一致性；同时将不同时间实例显式纳入表示以实现可归档查询与回放渲染。

**主要结论**：该方法在快节奏体育/演出等复杂动态场景下，相比基于高斯溅射的动态方案更稳健且具更高视觉质量，并首次（相对既有神经渲染/新视角合成工作）提供可回到任意历史时刻进行新视角重建的time-archival能力，适用于转播回放与分析归档。

**关键词**：相机虚拟化, 新视角合成, 神经体渲染, 动态场景渲染, 时空一致性, 时间归档渲染, 体育赛事转播, 多视角同步相机, 刚体变换建模, 三维高斯泼溅, 非刚体快速运动

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15181v1) | [下载PDF](https://arxiv.org/pdf/2602.15181v1.pdf)

---

## [6. Distributional Deep Learning for Super-Resolution of 4D Flow MRI under Domain Shift](https://arxiv.org/abs/2602.15167v1)

**作者**：Xiaoyi Wen, Fei Jiang  
**分类**：cs.CV, stat.AP, stat.ML  
**发布时间**：2026-02-16

### 📄 论文摘要

Super-resolution is widely used in medical imaging to enhance low-quality data, reducing scan time and improving abnormality detection. Conventional super-resolution approaches typically rely on paired datasets of downsampled and original high resolution images, training models to reconstruct high resolution images from their artificially degraded counterparts. However, in real-world clinical settings, low resolution data often arise from acquisition mechanisms that differ significantly from simple downsampling. As a result, these inputs may lie outside the domain of the training data, leading to poor model generalization due to domain shift. To address this limitation, we propose a distributional deep learning framework that improves model robustness and domain generalization. We develop this approch for enhancing the resolution of 4D Flow MRI (4DF). This is a novel imaging modality that captures hemodynamic flow velocity and clinically relevant metrics such as vessel wall stress. These metrics are critical for assessing aneurysm rupture risk. Our model is initially trained on high resolution computational fluid dynamics (CFD) simulations and their downsampled counterparts. It is then fine-tuned on a small, harmonized dataset of paired 4D Flow MRI and CFD samples. We derive the theoretical properties of our distributional estimators and demonstrate that our framework significantly outperforms traditional deep learning approaches through real data applications. This highlights the effectiveness of distributional learning in addressing domain shift and improving super-resolution performance in clinically realistic scenarios.

### 🤖 AI 总结

**一句话总结**：提出一种分布式（distributional）深度学习超分辨框架，以提升4D Flow MRI在真实采集域偏移下的重建鲁棒性与泛化能力。

**研究动机**：传统超分模型依赖“人工下采样-高分”配对数据训练，但临床低分数据的退化机制与下采样不同，导致域偏移下性能显著下降。4D Flow MRI对血流速度及壁面应力等指标敏感，需在低质输入下仍能可靠超分。

**核心方法**：先用高分辨CFD模拟及其下采样数据预训练模型，再用少量“配对且协调(harmonized)”的4D Flow MRI–CFD样本微调；同时引入分布式学习/估计来对齐训练与测试分布，并给出分布估计器的理论性质。

**主要结论**：在真实数据应用中，该分布式学习框架相较传统深度学习超分方法显著提升了域偏移下的重建效果与泛化鲁棒性，证明其更适合临床真实退化场景的4D Flow MRI超分。

**关键词**：超分辨率重建, 医学影像超分, 域偏移, 域泛化, 分布式深度学习, 分布估计器, 鲁棒性学习, 计算流体力学模拟（CFD）, 仿真到真实迁移, 小样本微调, 血流动力学指标

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15167v1) | [下载PDF](https://arxiv.org/pdf/2602.15167v1.pdf)

---

## [7. Loss Knows Best: Detecting Annotation Errors in Videos via Loss Trajectories](https://arxiv.org/abs/2602.15154v1)

**作者**：Praditha Alwis, Soumyadeep Chandra, Deepak Ravikumar 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-02-16

### 📄 论文摘要

High-quality video datasets are foundational for training robust models in tasks like action recognition, phase detection, and event segmentation. However, many real-world video datasets suffer from annotation errors such as *mislabeling*, where segments are assigned incorrect class labels, and *disordering*, where the temporal sequence does not follow the correct progression. These errors are particularly harmful in phase-annotated tasks, where temporal consistency is critical. We propose a novel, model-agnostic method for detecting annotation errors by analyzing the Cumulative Sample Loss (CSL)--defined as the average loss a frame incurs when passing through model checkpoints saved across training epochs. This per-frame loss trajectory acts as a dynamic fingerprint of frame-level learnability. Mislabeled or disordered frames tend to show consistently high or irregular loss patterns, as they remain difficult for the model to learn throughout training, while correctly labeled frames typically converge to low loss early. To compute CSL, we train a video segmentation model and store its weights at each epoch. These checkpoints are then used to evaluate the loss of each frame in a test video. Frames with persistently high CSL are flagged as likely candidates for annotation errors, including mislabeling or temporal misalignment. Our method does not require ground truth on annotation errors and is generalizable across datasets. Experiments on EgoPER and Cholec80 demonstrate strong detection performance, effectively identifying subtle inconsistencies such as mislabeling and frame disordering. The proposed approach provides a powerful tool for dataset auditing and improving training reliability in video-based machine learning.

### 🤖 AI 总结

**一句话总结**：提出一种通过训练过程中“累计样本损失（CSL）”轨迹来自动发现视频逐帧标注错误（错标与时序错乱）的通用审计方法。

**研究动机**：真实视频数据常含错标与时序不一致等标注噪声，尤其在阶段/流程类任务中会破坏时间一致性并显著影响模型训练与评估。现有发现错误往往依赖人工或额外监督，缺乏可泛化的自动化手段。

**核心方法**：在训练视频分割模型时保存各epoch的checkpoint，并用这些checkpoint对每一帧计算跨epoch平均损失形成CSL（损失轨迹指纹）。持续高损失或不规则损失轨迹的帧被判为难以学习样本，从而作为潜在错标或时间错位（disordering）候选被标记。

**主要结论**：在EgoPER与Cholec80上，CSL能有效定位细微的错标与帧顺序异常，且不需要错误标注的真值监督、对模型相对无关。该方法可作为数据集审计工具提升视频数据质量与训练可靠性。

**关键词**：视频数据集, 注释错误, 损失轨迹, 累积样本损失, 模型无关, 误标记, 时间错位, 数据集审计, 训练可靠性, 动作识别

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15154v1) | [下载PDF](https://arxiv.org/pdf/2602.15154v1.pdf)

---

## cs.LG

## [8. Size Transferability of Graph Transformers with Convolutional Positional Encodings](https://arxiv.org/abs/2602.15239v1)

**作者**：Javier Porras-Valenzuela, Zhiyang Wang, Alejandro Ribeiro  
**分类**：cs.LG  
**发布时间**：2026-02-16

### 📄 论文摘要

Transformers have achieved remarkable success across domains, motivating the rise of Graph Transformers (GTs) as attention-based architectures for graph-structured data. A key design choice in GTs is the use of Graph Neural Network (GNN)-based positional encodings to incorporate structural information. In this work, we study GTs through the lens of manifold limit models for graph sequences and establish a theoretical connection between GTs with GNN positional encodings and Manifold Neural Networks (MNNs). Building on transferability results for GNNs under manifold convergence, we show that GTs inherit transferability guarantees from their positional encodings. In particular, GTs trained on small graphs provably generalize to larger graphs under mild assumptions. We complement our theory with extensive experiments on standard graph benchmarks, demonstrating that GTs exhibit scalable behavior on par with GNNs. To further show the efficiency in a real-world scenario, we implement GTs for shortest path distance estimation over terrains to better illustrate the efficiency of the transferable GTs. Our results provide new insights into the understanding of GTs and suggest practical directions for efficient training of GTs in large-scale settings.

### 🤖 AI 总结

**一句话总结**：本文从流形极限模型角度建立带GNN卷积式位置编码的图Transformer与流形神经网络的理论联系，证明其可从小图训练迁移到大图推理并在实验中验证可扩展性。

**研究动机**：现有图Transformer依赖位置编码注入结构信息，但其“训练于小规模图、泛化到更大规模图”的尺寸可迁移性缺乏系统理论解释与保证。

**核心方法**：基于图序列的流形收敛与流形极限模型，将使用GNN/卷积位置编码的图Transformer刻画为与流形神经网络相关的形式，并利用GNN在流形收敛下的可迁移性结果，推出图Transformer的可迁移性来源于其位置编码；同时在标准基准与地形最短路距离估计任务上做验证。

**主要结论**：在温和假设下，带GNN卷积位置编码的图Transformer可继承位置编码的理论迁移保证，因而能从小图训练推广到大图；实验显示其可扩展性与GNN相当，并在真实场景中体现出更高效的大规模训练与部署潜力。

**关键词**：图变换器, 图神经网络, 位置编码, 可转移性, 流形神经网络, 图序列, 短路径估计, 大规模训练

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15239v1) | [下载PDF](https://arxiv.org/pdf/2602.15239v1.pdf)

---

## [9. Closing the Distribution Gap in Adversarial Training for LLMs](https://arxiv.org/abs/2602.15238v2)

**作者**：Chengzhi Hu, Jonas Dornbusch, David Lüdke 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CR  
**发布时间**：2026-02-16

### 📄 论文摘要

Adversarial training for LLMs is one of the most promising methods to reliably improve robustness against adversaries. However, despite significant progress, models remain vulnerable to simple in-distribution exploits, such as rewriting prompts in the past tense or translating them into other languages. We argue that this persistent fragility stems from a fundamental limitation in current adversarial training algorithms: they minimize adversarial loss on their training set but inadequately cover the data distribution, resulting in vulnerability to seemingly simple attacks. To bridge this gap, we propose Distributional Adversarial Training, DAT. We leverage Diffusion LLMs to approximate the true joint distribution of prompts and responses, enabling generation of diverse, high-likelihood samples that address generalization failures. By combining optimization over the data distribution provided by the diffusion model with continuous adversarial training, DAT achieves substantially higher adversarial robustness than previous methods.

### 🤖 AI 总结

**一句话总结**：提出分布式对抗训练（DAT），用扩散式LLM近似真实提示-回答分布来生成高似然多样样本，从而显著提升LLM对简单改写/翻译等同分布攻击的鲁棒性。

**研究动机**：现有LLM对抗训练主要在训练集上最小化对抗损失，但对整体数据分布覆盖不足，导致对看似简单的同分布变体（如时态改写、跨语言翻译）仍然脆弱。

**核心方法**：DAT利用扩散LLM建模并采样提示与回复的联合分布，生成多样且高概率的训练样本以补齐分布覆盖；再将基于该分布的优化与持续对抗训练结合，形成更强的泛化鲁棒性。

**主要结论**：通过缩小“训练集对抗优化”与“真实数据分布覆盖”之间的差距，DAT相比以往方法取得更高的对抗鲁棒性，能更好抵御同分布的简单提示变形攻击。

**关键词**：分布差距, 分布式对抗训练（DAT）, 数据分布覆盖, 扩散模型LLM, 联合分布建模, 高似然采样, 分布内攻击, 提示改写攻击, 跨语言攻击, 连续对抗训练

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15238v2) | [下载PDF](https://arxiv.org/pdf/2602.15238v2.pdf)

---

## [10. BindCLIP: A Unified Contrastive-Generative Representation Learning Framework for Virtual Screening](https://arxiv.org/abs/2602.15236v1)

**作者**：Anjie Qiao, Zhen Wang, Yaliang Li 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-16

### 📄 论文摘要

Virtual screening aims to efficiently identify active ligands from massive chemical libraries for a given target pocket. Recent CLIP-style models such as DrugCLIP enable scalable virtual screening by embedding pockets and ligands into a shared space. However, our analyses indicate that such representations can be insensitive to fine-grained binding interactions and may rely on shortcut correlations in training data, limiting their ability to rank ligands by true binding compatibility. To address these issues, we propose BindCLIP, a unified contrastive-generative representation learning framework for virtual screening. BindCLIP jointly trains pocket and ligand encoders using CLIP-style contrastive learning together with a pocket-conditioned diffusion objective for binding pose generation, so that pose-level supervision directly shapes the retrieval embedding space toward interaction-relevant features. To further mitigate shortcut reliance, we introduce hard-negative augmentation and a ligand-ligand anchoring regularizer that prevents representation collapse. Experiments on two public benchmarks demonstrate consistent improvements over strong baselines. BindCLIP achieves substantial gains on challenging out-of-distribution virtual screening and improves ligand-analogue ranking on the FEP+ benchmark. Together, these results indicate that integrating generative, pose-level supervision with contrastive learning yields more interaction-aware embeddings and improves generalization in realistic screening settings, bringing virtual screening closer to real-world applicability.

### 🤖 AI 总结

**一句话总结**：BindCLIP 将CLIP式对比学习与口袋条件扩散生成的姿态监督统一训练，学习更“交互感知”的口袋-配体嵌入，从而提升虚拟筛选排序与OOD泛化。

**研究动机**：现有DrugCLIP等检索嵌入可能对细粒度结合相互作用不敏感，并容易利用数据中的“捷径相关性”，导致无法按真实结合兼容性可靠排名配体。为此需要引入能直接约束相互作用的姿态级监督，并降低对捷径的依赖。

**核心方法**：联合训练口袋/配体编码器：一方面用CLIP式对比学习对齐口袋-配体表征，另一方面加入口袋条件扩散目标生成结合姿态，使姿态监督反向塑造检索嵌入空间。另通过hard-negative增强与配体-配体锚定正则防止表征塌缩并缓解捷径学习。

**主要结论**：在两项公开基准上相对强基线稳定提升，尤其在具有挑战的分布外虚拟筛选与FEP+配体类似物排序上获得显著增益。结果表明将生成式姿态监督与对比学习结合可提升交互相关性与真实场景下的泛化能力。

**关键词**：虚拟筛选, 蛋白口袋-配体联合表征, Diffusion, 结合构象生成, 构象级监督, 硬负样本挖掘, 配体-配体对齐正则化, 表示坍塌防护, 分布外泛化, FEP+基准评测

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15236v1) | [下载PDF](https://arxiv.org/pdf/2602.15236v1.pdf)

---

## [11. Automatically Finding Reward Model Biases](https://arxiv.org/abs/2602.15222v1)

**作者**：Atticus Wang, Iván Arcuschin, Arthur Conmy  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-16

### 📄 论文摘要

Reward models are central to large language model (LLM) post-training. However, past work has shown that they can reward spurious or undesirable attributes such as length, format, hallucinations, and sycophancy. In this work, we introduce and study the research problem of automatically finding reward model biases in natural language. We offer a simple approach of using an LLM to iteratively propose and refine candidate biases. Our method can recover known biases and surface novel ones: for example, we found that Skywork-V2-8B, a leading open-weight reward model, often mistakenly favors responses with redundant spacing and responses with hallucinated content. In addition, we show evidence that evolutionary iteration outperforms flat best-of-N search, and we validate the recall of our pipeline using synthetically injected biases. We hope our work contributes to further research on improving RMs through automated interpretability methods.

### 🤖 AI 总结

**一句话总结**：提出一种用LLM自动发现奖励模型（RM）偏置的迭代搜索框架，能复现已知偏置并挖掘如“偏好冗余空格/幻觉内容”等新偏置。

**研究动机**：奖励模型在LLM后训练中至关重要，但常会奖励长度、格式、幻觉、迎合等“伪特征”，需要一种可扩展、自动化的方法来系统定位这些偏置。

**核心方法**：用LLM生成“候选偏置描述+触发示例”，并通过进化式迭代（基于RM反馈不断改写/变异/筛选）来强化能稳定提高RM评分的偏置；同时用合成注入偏置来评估管线的召回率，并对比平铺的best-of-N搜索。

**主要结论**：该方法能够找回已知RM偏置并发现新偏置（如Skywork-V2-8B偏好冗余空格与幻觉内容），且进化迭代优于简单best-of-N；合成偏置实验表明管线具备较好的召回与有效性，有助于RM自动化可解释性与改进。

**关键词**：奖励模型偏差检测, 奖励模型可解释性, LLM引导搜索, 进化迭代搜索, 合成偏差注入, 长度偏好偏差, 格式偏好偏差, 幻觉偏好偏差, 奉承偏好偏差, 后训练评估

**评分**：44

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15222v1) | [下载PDF](https://arxiv.org/pdf/2602.15222v1.pdf)

---

## [12. MAVRL: Learning Reward Functions from Multiple Feedback Types with Amortized Variational Inference](https://arxiv.org/abs/2602.15206v1)

**作者**：Raphaël Baur, Yannick Metz, Maria Gkoulta 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-16

### 📄 论文摘要

Reward learning typically relies on a single feedback type or combines multiple feedback types using manually weighted loss terms. Currently, it remains unclear how to jointly learn reward functions from heterogeneous feedback types such as demonstrations, comparisons, ratings, and stops that provide qualitatively different signals. We address this challenge by formulating reward learning from multiple feedback types as Bayesian inference over a shared latent reward function, where each feedback type contributes information through an explicit likelihood. We introduce a scalable amortized variational inference approach that learns a shared reward encoder and feedback-specific likelihood decoders and is trained by optimizing a single evidence lower bound. Our approach avoids reducing feedback to a common intermediate representation and eliminates the need for manual loss balancing. Across discrete and continuous-control benchmarks, we show that jointly inferred reward posteriors outperform single-type baselines, exploit complementary information across feedback types, and yield policies that are more robust to environment perturbations. The inferred reward uncertainty further provides interpretable signals for analyzing model confidence and consistency across feedback types.

### 🤖 AI 总结

**一句话总结**：MAVRL将多种异质人类反馈统一为对共享潜在奖励函数的贝叶斯推断，并用摊销变分推断端到端联合学习，从而得到更准确且更鲁棒的奖励与策略。

**研究动机**：现有奖励学习通常只用单一反馈或靠手工加权融合多种反馈，但不同反馈（演示、偏好比较、打分、停止等）信号性质差异大，难以一致且可扩展地联合建模与训练。

**核心方法**：把“多反馈奖励学习”表述为对同一潜在奖励函数的贝叶斯后验推断：每种反馈类型通过各自显式似然函数提供约束；提出可扩展的摊销变分推断框架，学习共享的reward encoder与反馈类型特定的likelihood decoder，并用单一ELBO目标联合优化，避免中间统一表示与手动loss平衡。

**主要结论**：在离散与连续控制基准上，联合推断的奖励后验优于单反馈基线，能利用不同反馈的互补信息并在环境扰动下产生更鲁棒的策略；同时后验不确定性可作为可解释信号，用于评估模型置信度与不同反馈间一致性。

**关键词**：多反馈奖励学习, 异构人类反馈, 贝叶斯推断, 潜在奖励函数, 摊销变分推断, 证据下界（ELBO）, 奖励编码器, 反馈特定似然建模, 奖励后验分布, 奖励不确定性估计, 鲁棒强化学习

**评分**：42

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15206v1) | [下载PDF](https://arxiv.org/pdf/2602.15206v1.pdf)

---

## [13. COMPOT: Calibration-Optimized Matrix Procrustes Orthogonalization for Transformers Compression](https://arxiv.org/abs/2602.15200v1)

**作者**：Denis Makhov, Dmitriy Shopkhoev, Magauiya Zhussip 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-16

### 📄 论文摘要

Post-training compression of Transformer models commonly relies on truncated singular value decomposition (SVD). However, enforcing a single shared subspace can degrade accuracy even at moderate compression. Sparse dictionary learning provides a more flexible union-of-subspaces representation, but existing approaches often suffer from iterative dictionary and coefficient updates. We propose COMPOT (Calibration-Optimized Matrix Procrustes Orthogonalization for Transformers), a training-free compression framework that uses a small calibration dataset to estimate a sparse weight factorization. COMPOT employs orthogonal dictionaries that enable closed-form Procrustes updates for the dictionary and analytical single-step sparse coding for the coefficients, eliminating iterative optimization. To handle heterogeneous layer sensitivity under a global compression budget, COMPOT further introduces a one-shot dynamic allocation strategy that adaptively redistributes layer-wise compression rates. Extensive experiments across diverse architectures and tasks show that COMPOT consistently delivers a superior quality-compression trade-off over strong low-rank and sparse baselines, while remaining fully compatible with post-training quantization for extreme compression. Code is available $\href{https://github.com/mts-ai/COMPOT}{here}$.

### 🤖 AI 总结

**一句话总结**：COMPOT提出一种无需再训练、仅用少量校准数据的Transformer后训练压缩框架，通过正交字典的闭式更新与一次性稀疏编码实现更优的压缩-精度权衡。

**研究动机**：传统截断SVD要求所有权重共享单一低秩子空间，导致中等压缩率下精度明显下降；而稀疏字典学习虽更灵活，但通常需要迭代优化字典与系数，成本高且复杂。

**核心方法**：COMPOT用校准数据估计稀疏权重分解：采用正交字典使字典更新可用Procrustes闭式解，系数可解析单步稀疏编码，从而避免迭代；同时提出一次性动态分配策略，在全局压缩预算下按层敏感度自适应分配压缩率，并与PTQ兼容。

**主要结论**：在多种架构与任务上，COMPOT相较强低秩/稀疏基线取得更好的质量-压缩折中，并能与后训练量化结合实现更极端压缩而保持较高精度。

**关键词**：后训练压缩, 低秩分解, 稀疏字典学习, 正交字典, 校准数据集, 一阶段稀疏编码, 层级压缩率动态分配, 后训练量化

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15200v1) | [下载PDF](https://arxiv.org/pdf/2602.15200v1.pdf)

---

## [14. Learning Data-Efficient and Generalizable Neural Operators via Fundamental Physics Knowledge](https://arxiv.org/abs/2602.15184v1)

**作者**：Siying Ma, Mehrdad M. Zadeh, Mauricio Soroco 等 6 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-02-16

### 📄 论文摘要

Recent advances in scientific machine learning (SciML) have enabled neural operators (NOs) to serve as powerful surrogates for modeling the dynamic evolution of physical systems governed by partial differential equations (PDEs). While existing approaches focus primarily on learning simulations from the target PDE, they often overlook more fundamental physical principles underlying these equations. Inspired by how numerical solvers are compatible with simulations of different settings of PDEs, we propose a multiphysics training framework that jointly learns from both the original PDEs and their simplified basic forms. Our framework enhances data efficiency, reduces predictive errors, and improves out-of-distribution (OOD) generalization, particularly in scenarios involving shifts of physical parameters and synthetic-to-real transfer. Our method is architecture-agnostic and demonstrates consistent improvements in normalized root mean square error (nRMSE) across a wide range of 1D/2D/3D PDE problems. Through extensive experiments, we show that explicit incorporation of fundamental physics knowledge significantly strengthens the generalization ability of neural operators. We will release models and codes at https://sites.google.com/view/sciml-fundemental-pde.

### 🤖 AI 总结

**一句话总结**：提出一种将目标PDE与其更基本简化形式联合训练的多物理框架，从而让神经算子更省数据且具更强OOD泛化能力。

**研究动机**：现有神经算子多仅拟合目标PDE的模拟数据，忽视支撑这些方程的更基础物理原则，导致数据需求高且对参数变化/仿真到真实迁移的泛化不足。

**核心方法**：设计多物理联合训练：同时用原始PDE与其简化“基本形式”数据进行训练，把基础物理知识显式注入学习过程；方法与具体神经算子架构无关，可直接套用在多种1D/2D/3D PDE任务上。

**主要结论**：联合学习基础物理与目标PDE可显著提升数据效率、降低预测nRMSE，并在物理参数分布偏移与synthetic-to-real等OOD场景下获得更稳健的泛化表现。

**关键词**：神经算子, 科学机器学习, 偏微分方程, 物理先验, 多物理训练, 数据效率, 分布外泛化, 参数漂移鲁棒性, 仿真到真实迁移, 归一化均方根误差（nRMSE）, 架构无关方法

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15184v1) | [下载PDF](https://arxiv.org/pdf/2602.15184v1.pdf)

---

## [15. Refine Now, Query Fast: A Decoupled Refinement Paradigm for Implicit Neural Fields](https://arxiv.org/abs/2602.15155v2)

**作者**：Tianyu Xiong, Skylar Wurster, Han-Wei Shen  
**分类**：cs.LG, cs.CE, cs.CV, cs.GR  
**发布时间**：2026-02-16

### 📄 论文摘要

Implicit Neural Representations (INRs) have emerged as promising surrogates for large 3D scientific simulations due to their ability to continuously model spatial and conditional fields, yet they face a critical fidelity-speed dilemma: deep MLPs suffer from high inference cost, while efficient embedding-based models lack sufficient expressiveness. To resolve this, we propose the Decoupled Representation Refinement (DRR) architectural paradigm. DRR leverages a deep refiner network, alongside non-parametric transformations, in a one-time offline process to encode rich representations into a compact and efficient embedding structure. This approach decouples slow neural networks with high representational capacity from the fast inference path. We introduce DRR-Net, a simple network that validates this paradigm, and a novel data augmentation strategy, Variational Pairs (VP) for improving INRs under complex tasks like high-dimensional surrogate modeling. Experiments on several ensemble simulation datasets demonstrate that our approach achieves state-of-the-art fidelity, while being up to 27$\times$ faster at inference than high-fidelity baselines and remaining competitive with the fastest models. The DRR paradigm offers an effective strategy for building powerful and practical neural field surrogates and \rev{INRs in broader applications}, with a minimal compromise between speed and quality.

### 🤖 AI 总结

**一句话总结**：提出DRR解耦式精炼范式：用一次离线深度精炼把高表达能力“压缩”进轻量嵌入结构，实现隐式神经场高保真且快速推理。

**研究动机**：INR在3D科学仿真替代建模中面临“质量-速度”矛盾：深MLP推理慢但精度高，嵌入式高效模型快但表达力不足。需要一种能保留高保真同时将推理路径变快的结构性方案。

**核心方法**：DRR在离线阶段使用深refiner网络+非参数变换对表示进行一次性精炼，将复杂信息编码到紧凑的embedding结构中；在线推理只走轻量快速路径。作者实现DRR-Net验证该范式，并提出Variational Pairs数据增强以提升高维代理建模等复杂任务下的INR效果。

**主要结论**：在多个集合仿真数据集上，方法达到SOTA保真度，同时相对高保真基线推理最高提速27×，且速度上仍与最快模型具竞争力，证明DRR能以很小质量代价兼顾实用速度与精度。

**关键词**：隐式神经表示, 隐式神经场, 3D 科学仿真代理建模, 高维代理建模, 推理加速, 表示精炼, 解耦架构, 离线预计算, 嵌入式表示, 非参数变换, 数据增强

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15155v2) | [下载PDF](https://arxiv.org/pdf/2602.15155v2.pdf)

---

