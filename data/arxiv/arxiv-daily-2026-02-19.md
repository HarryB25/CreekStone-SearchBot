# arXiv AI 论文日报 | 2026-02-19

> 共 15 篇论文，由AI自动总结

## 📑 目录

- [cs.AI](#csAI) (1 篇)
- [cs.LG](#csLG) (10 篇)
- [cs.CL](#csCL) (1 篇)
- [cs.CV](#csCV) (3 篇)

---

## cs.AI

## [1. El Agente Gráfico: Structured Execution Graphs for Scientific Agents](https://arxiv.org/abs/2602.17902v1)

**作者**：Jiaru Bai, Abdulrahman Aldossary, Thomas Swanick 等 11 位作者  
**分类**：cs.AI, cs.MA, cs.SE, physics.chem-ph  
**发布时间**：2026-02-19

### 📄 论文摘要

Large language models (LLMs) are increasingly used to automate scientific workflows, yet their integration with heterogeneous computational tools remains ad hoc and fragile. Current agentic approaches often rely on unstructured text to manage context and coordinate execution, generating often overwhelming volumes of information that may obscure decision provenance and hinder auditability. In this work, we present El Agente Gráfico, a single-agent framework that embeds LLM-driven decision-making within a type-safe execution environment and dynamic knowledge graphs for external persistence. Central to our approach is a structured abstraction of scientific concepts and an object-graph mapper that represents computational state as typed Python objects, stored either in memory or persisted in an external knowledge graph. This design enables context management through typed symbolic identifiers rather than raw text, thereby ensuring consistency, supporting provenance tracking, and enabling efficient tool orchestration. We evaluate the system by developing an automated benchmarking framework across a suite of university-level quantum chemistry tasks previously evaluated on a multi-agent system, demonstrating that a single agent, when coupled to a reliable execution engine, can robustly perform complex, multi-step, and parallel computations. We further extend this paradigm to two other large classes of applications: conformer ensemble generation and metal-organic framework design, where knowledge graphs serve as both memory and reasoning substrates. Together, these results illustrate how abstraction and type safety can provide a scalable foundation for agentic scientific automation beyond prompt-centric designs.

### 🤖 AI 总结

**一句话总结**：提出“El Agente Gráfico”单智能体框架，用类型安全的执行图与知识图谱持久化来替代基于非结构化文本的科学智能体编排，实现更可靠可审计的科学工作流自动化。

**研究动机**：现有LLM科学智能体常用非结构化文本管理上下文与工具协调，信息冗余且难以追踪决策来源，导致执行脆弱、难以审计与复现。作者希望用结构化与类型安全机制提升一致性、可追溯性与工具编排的鲁棒性。

**核心方法**：将LLM决策嵌入类型安全的执行环境：以结构化科学概念抽象+对象-图映射器将计算状态表示为带类型的Python对象，并可持久化到外部知识图谱；上下文通过符号化的typed标识符管理而非原始文本，从而支持并行与多步工具调用。

**主要结论**：在量子化学任务基准上，配合可靠执行引擎的单智能体即可稳定完成复杂多步与并行计算，效果可替代先前多智能体方案；在构象集生成与MOF设计中，知识图谱同时作为记忆与推理底座，证明类型安全与抽象可为可扩展的科学智能体自动化提供更稳健基础。

**关键词**：科学工作流自动化, 科学智能体, 结构化执行图, 类型安全执行环境, 知识图谱记忆, 符号化上下文管理, 工具编排, 自动化基准评测, 量子化学任务

**评分**：54

**论文链接**：[查看原文](https://arxiv.org/abs/2602.17902v1) | [下载PDF](https://arxiv.org/pdf/2602.17902v1.pdf)

---

## cs.CL

## [2. Understanding Unreliability of Steering Vectors in Language Models: Geometric Predictors and the Limits of Linear Approximations](https://arxiv.org/abs/2602.17881v1)

**作者**：Joschka Braun  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-02-19

### 📄 论文摘要

Steering vectors are a lightweight method for controlling language model behavior by adding a learned bias to the activations at inference time. Although effective on average, steering effect sizes vary across samples and are unreliable for many target behaviors. In my thesis, I investigate why steering reliability differs across behaviors and how it is impacted by steering vector training data. First, I find that higher cosine similarity between training activation differences predicts more reliable steering. Second, I observe that behavior datasets where positive and negative activations are better separated along the steering direction are more reliably steerable. Finally, steering vectors trained on different prompt variations are directionally distinct, yet perform similarly well and exhibit correlated efficacy across datasets. My findings suggest that steering vectors are unreliable when the latent target behavior representation is not effectively approximated by the linear steering direction. Taken together, these insights offer a practical diagnostic for steering unreliability and motivate the development of more robust steering methods that explicitly account for non-linear latent behavior representations.

### 🤖 AI 总结

**一句话总结**：研究表明，语言模型中的引导向量在不同目标行为上的可靠性差异与训练数据的相似性和分离程度有关。

**研究动机**：探讨引导向量在控制语言模型行为时的可靠性问题，旨在理解其变异性及影响因素。

**核心方法**：通过分析训练激活差异的余弦相似性和行为数据集中正负激活的分离程度，评估引导向量的可靠性。

**主要结论**：引导向量在目标行为表示无法有效线性近似时表现不可靠，提示需要开发更稳健的引导方法以处理非线性行为表示。

**关键词**：LLM 行为控制, 激活偏置注入, 推理时干预, 可控性可靠性, 行为表示线性近似, 余弦相似度预测, 激活差分一致性, 投影可分性, 提示变体鲁棒性, 非线性潜在表示

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2602.17881v1) | [下载PDF](https://arxiv.org/pdf/2602.17881v1.pdf)

---

## cs.CV

## [3. Understanding the Fine-Grained Knowledge Capabilities of Vision-Language Models](https://arxiv.org/abs/2602.17871v1)

**作者**：Dhruba Ghosh, Yuhui Zhang, Ludwig Schmidt  
**分类**：cs.CV, cs.AI, cs.LG, cs.MM  
**发布时间**：2026-02-19

### 📄 论文摘要

Vision-language models (VLMs) have made substantial progress across a wide range of visual question answering benchmarks, spanning visual reasoning, document understanding, and multimodal dialogue. These improvements are evident in a wide range of VLMs built on a variety of base models, alignment architectures, and training data. However, recent works show that these models trail behind in traditional image classification benchmarks, which test fine-grained visual knowledge. We test a large number of recent VLMs on fine-grained classification benchmarks and identify potential factors in the disconnect between fine-grained knowledge and other vision benchmarks. Through a series of ablation experiments, we find that using a better LLM improves all benchmark scores equally, while a better vision encoder disproportionately improves fine-grained classification performance. Furthermore, we find that the pretraining stage is also vital to fine-grained performance, particularly when the language model weights are unfrozen during pretraining. These insights pave the way for enhancing fine-grained visual understanding and vision-centric capabilities in VLMs.

### 🤖 AI 总结

**一句话总结**：论文系统评测多种视觉-语言模型在细粒度分类上的能力，发现提升视觉编码器与预训练策略（尤其解冻语言模型权重）对细粒度知识最关键。

**研究动机**：尽管VLM在VQA、文档理解等基准上表现显著提升，但在传统细粒度图像分类上落后，说明其“细粒度视觉知识”与其他视觉能力存在脱节，需要找出原因与改进路径。

**核心方法**：作者对大量近期VLM在细粒度分类基准上进行对比评测，并通过消融实验分别替换/增强LLM、视觉编码器与预训练设置（含是否在预训练阶段解冻语言模型权重）来定位影响因素。

**主要结论**：更强的LLM会较为均衡地提升各类基准，而更强的视觉编码器会对细粒度分类带来更显著的增益；此外预训练阶段对细粒度性能至关重要，尤其当预训练时解冻语言模型权重时细粒度表现提升更明显。

**关键词**：视觉语言模型, 细粒度图像分类, 细粒度视觉知识, 视觉问答评测, 细粒度分类基准, 消融实验, 视觉编码器, LLM, 跨模态对齐架构, 预训练策略

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2602.17871v1) | [下载PDF](https://arxiv.org/pdf/2602.17871v1.pdf)

---

## [4. Learning Compact Video Representations for Efficient Long-form Video Understanding in Large Multimodal Models](https://arxiv.org/abs/2602.17869v1)

**作者**：Yuxiao Chen, Jue Wang, Zhikang Zhang 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-19

### 📄 论文摘要

With recent advancements in video backbone architectures, combined with the remarkable achievements of large language models (LLMs), the analysis of long-form videos spanning tens of minutes has become both feasible and increasingly prevalent. However, the inherently redundant nature of video sequences poses significant challenges for contemporary state-of-the-art models. These challenges stem from two primary aspects: 1) efficiently incorporating a larger number of frames within memory constraints, and 2) extracting discriminative information from the vast volume of input data. In this paper, we introduce a novel end-to-end schema for long-form video understanding, which includes an information-density-based adaptive video sampler (AVS) and an autoencoder-based spatiotemporal video compressor (SVC) integrated with a multimodal large language model (MLLM). Our proposed system offers two major advantages: it adaptively and effectively captures essential information from video sequences of varying durations, and it achieves high compression rates while preserving crucial discriminative information. The proposed framework demonstrates promising performance across various benchmarks, excelling in both long-form video understanding tasks and standard video understanding benchmarks. These results underscore the versatility and efficacy of our approach, particularly in managing the complexities of prolonged video sequences.

### 🤖 AI 总结

**一句话总结**：本文提出了一种新颖的端到端架构，通过信息密度自适应视频采样器和基于自编码器的时空视频压缩器，实现了高效的长格式视频理解。

**研究动机**：随着视频架构的进步和大型语言模型的发展，分析长时间视频成为可能。然而，视频序列的冗余特性给现有模型带来了内存和信息提取的挑战。

**核心方法**：提出了一种集成多模态大型语言模型的自适应视频采样器和时空视频压缩器，能够在保持重要信息的同时高效压缩视频数据。

**主要结论**：该框架在长格式视频理解任务和标准视频理解基准测试中表现出色，展示了其在处理复杂视频序列中的灵活性和有效性。

**关键词**：紧凑视频表征, 自适应视频采样, 信息密度建模, 帧选择, 时空视频压缩, 视频自编码器, 多模态大语言模型（MLLM）, 视频冗余消除, 内存受限推理, 高压缩率表征

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.17869v1) | [下载PDF](https://arxiv.org/pdf/2602.17869v1.pdf)

---

## [5. On the Evaluation Protocol of Gesture Recognition for UAV-based Rescue Operation based on Deep Learning: A Subject-Independence Perspective](https://arxiv.org/abs/2602.17854v1)

**作者**：Domonkos Varga  
**分类**：cs.CV  
**发布时间**：2026-02-19

### 📄 论文摘要

This paper presents a methodological analysis of the gesture-recognition approach proposed by Liu and Szirányi, with a particular focus on the validity of their evaluation protocol. We show that the reported near-perfect accuracy metrics result from a frame-level random train-test split that inevitably mixes samples from the same subjects across both sets, causing severe data leakage. By examining the published confusion matrix, learning curves, and dataset construction, we demonstrate that the evaluation does not measure generalization to unseen individuals. Our findings underscore the importance of subject-independent data partitioning in vision-based gesture-recognition research, especially for applications - such as UAV-human interaction - that require reliable recognition of gestures performed by previously unseen people.

### 🤖 AI 总结

**一句话总结**：本文分析了基于深度学习的手势识别评估协议，揭示数据泄漏问题影响了准确性评估。

**研究动机**：研究旨在揭示现有手势识别评估方法的缺陷，以提高其在无人机救援操作中的可靠性。

**核心方法**：通过分析混淆矩阵、学习曲线及数据集构建，指出现有评估方法未能有效测量对未见个体的泛化能力。

**主要结论**：强调在视觉手势识别研究中采用独立于主体的数据划分的重要性，以确保对新用户的手势识别准确性。

**关键词**：手势识别, 无人机救援, 无人机-人交互, 评测协议, 受试者独立划分, 跨主体泛化, 数据泄漏, 帧级随机划分, 训练-测试划分, 混淆矩阵分析, 学习曲线分析

**评分**：15

**论文链接**：[查看原文](https://arxiv.org/abs/2602.17854v1) | [下载PDF](https://arxiv.org/pdf/2602.17854v1.pdf)

---

## cs.LG

## [6. Breaking the Correlation Plateau: On the Optimization and Capacity Limits of Attention-Based Regressors](https://arxiv.org/abs/2602.17898v1)

**作者**：Jingquan Yan, Yuwei Miao, Peiran Yu 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-19

### 📄 论文摘要

Attention-based regression models are often trained by jointly optimizing Mean Squared Error (MSE) loss and Pearson correlation coefficient (PCC) loss, emphasizing the magnitude of errors and the order or shape of targets, respectively. A common but poorly understood phenomenon during training is the PCC plateau: PCC stops improving early in training, even as MSE continues to decrease. We provide the first rigorous theoretical analysis of this behavior, revealing fundamental limitations in both optimization dynamics and model capacity. First, in regard to the flattened PCC curve, we uncover a critical conflict where lowering MSE (magnitude matching) can paradoxically suppress the PCC gradient (shape matching). This issue is exacerbated by the softmax attention mechanism, particularly when the data to be aggregated is highly homogeneous. Second, we identify a limitation in the model capacity: we derived a PCC improvement limit for any convex aggregator (including the softmax attention), showing that the convex hull of the inputs strictly bounds the achievable PCC gain. We demonstrate that data homogeneity intensifies both limitations. Motivated by these insights, we propose the Extrapolative Correlation Attention (ECA), which incorporates novel, theoretically-motivated mechanisms to improve the PCC optimization and extrapolate beyond the convex hull. Across diverse benchmarks, including challenging homogeneous data setting, ECA consistently breaks the PCC plateau, achieving significant improvements in correlation without compromising MSE performance.

### 🤖 AI 总结

**一句话总结**：论文从理论上解释了注意力回归训练中“PCC（皮尔逊相关）早早停滞而MSE继续下降”的原因，并提出ECA机制突破该相关性平台。

**研究动机**：现有注意力回归常联合优化MSE与PCC，但训练中PCC很快进入平台期、难以继续提升，现象普遍却缺乏严谨解释与有效改进手段。作者希望厘清其优化动力学与模型容量上的根本限制，并给出可突破限制的方法。

**核心方法**：理论上分析联合损失下的梯度冲突：MSE下降会抑制PCC的梯度更新，且在输入同质、softmax注意力趋于平均/塌缩时问题更严重；进一步证明任何“凸聚合器”（含softmax注意力）的PCC提升受输入凸包严格约束。基于上述结论提出Extrapolative Correlation Attention（ECA），通过可“外推”超出凸包的机制与改进的相关性优化设计来提升PCC且不牺牲MSE。

**主要结论**：PCC平台期来自两类根因：优化层面的MSE↔PCC梯度冲突与softmax在同质数据下的放大效应，以及容量层面的凸聚合器凸包上界导致的PCC提升极限；数据同质性会同时加剧两者。实验表明ECA能稳定打破PCC平台，在多种基准（含高度同质场景）显著提升相关性并保持MSE性能。

**关键词**：注意力回归, MSE-PCC 联合损失, 相关系数平台期, 相关系数梯度抑制, 优化动力学, 模型容量上限, 凸聚合器, 凸包约束, 数据同质性, 外推相关注意力（ECA）, 凸包外推

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2602.17898v1) | [下载PDF](https://arxiv.org/pdf/2602.17898v1.pdf)

---

## [7. COMBA: Cross Batch Aggregation for Learning Large Graphs with Context Gating State Space Models](https://arxiv.org/abs/2602.17893v1)

**作者**：Jiajun Shen, Yufei Jin, Yi He 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-19

### 📄 论文摘要

State space models (SSMs) have recently emerged for modeling long-range dependency in sequence data, with much simplified computational costs than modern alternatives, such as transformers. Advancing SMMs to graph structured data, especially for large graphs, is a significant challenge because SSMs are sequence models and the shear graph volumes make it very expensive to convert graphs as sequences for effective learning. In this paper, we propose COMBA to tackle large graph learning using state space models, with two key innovations: graph context gating and cross batch aggregation. Graph context refers to different hops of neighborhood for each node, and graph context gating allows COMBA to use such context to learn best control of neighbor aggregation. For each graph context, COMBA samples nodes as batches, and train a graph neural network (GNN), with information being aggregated cross batches, allowing COMBA to scale to large graphs. Our theoretical study asserts that cross-batch aggregation guarantees lower error than training GNN without aggregation. Experiments on benchmark networks demonstrate significant performance gains compared to baseline approaches. Code and benchmark datasets will be released for public access.

### 🤖 AI 总结

**一句话总结**：COMBA是一种针对大规模图学习的状态空间模型，通过图上下文门控和跨批次聚合来提升性能。

**研究动机**：在处理大型图数据时，传统的状态空间模型面临转换图为序列的高成本问题，因此需要一种有效的方法来学习图结构数据。

**核心方法**：COMBA通过引入图上下文门控和跨批次聚合的技术，使模型能够更有效地学习节点的邻居信息，并在训练过程中进行信息的跨批次聚合。

**主要结论**：研究表明，跨批次聚合能够显著降低误差，并在标准网络上实现了相较于基线方法的显著性能提升。

**关键词**：大规模图学习, 状态空间模型（SSM）, 图神经网络（GNN）, 长程依赖建模, 图上下文门控, 跨批次聚合, 邻居聚合控制, 多跳邻域建模, 节点批采样, 可扩展训练, 误差界理论分析, 基准图数据集评测

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.17893v1) | [下载PDF](https://arxiv.org/pdf/2602.17893v1.pdf)

---

## [8. Machine Learning Based Prediction of Surgical Outcomes in Chronic Rhinosinusitis from Clinical Data](https://arxiv.org/abs/2602.17888v1)

**作者**：Sayeed Shafayet Chowdhury, Karen D'Souza, V. Siva Kakumani 等 12 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-19

### 📄 论文摘要

Artificial intelligence (AI) has increasingly transformed medical prognostics by enabling rapid and accurate analysis across imaging and pathology. However, the investigation of machine learning predictions applied to prospectively collected, standardized data from observational clinical intervention trials remains underexplored, despite its potential to reduce costs and improve patient outcomes. Chronic rhinosinusitis (CRS), a persistent inflammatory disease of the paranasal sinuses lasting more than three months, imposes a substantial burden on quality of life (QoL) and societal cost. Although many patients respond to medical therapy, others with refractory symptoms often pursue surgical intervention. Surgical decision-making in CRS is complex, as it must weigh known procedural risks against uncertain individualized outcomes. In this study, we evaluated supervised machine learning models for predicting surgical benefit in CRS, using the Sino-Nasal Outcome Test-22 (SNOT-22) as the primary patient-reported outcome. Our prospectively collected cohort from an observational intervention trial comprised patients who all underwent surgery; we investigated whether models trained only on preoperative data could identify patients who might not have been recommended surgery prior to the procedure. Across multiple algorithms, including an ensemble approach, our best model achieved approximately 85% classification accuracy, providing accurate and interpretable predictions of surgical candidacy. Moreover, on a held-out set of 30 cases spanning mixed difficulty, our model achieved 80% accuracy, exceeding the average prediction accuracy of expert clinicians (75.6%), demonstrating its potential to augment clinical decision-making and support personalized CRS care.

### 🤖 AI 总结

**一句话总结**：本文用术前临床数据训练监督式机器学习模型，预测慢性鼻窦炎（CRS）患者是否能从手术中获益，并在准确率上达到或超过专家临床判断。

**研究动机**：CRS手术决策需要在已知手术风险与个体化疗效不确定性间权衡，而针对前瞻性、标准化临床试验数据的机器学习预后预测研究仍相对不足。

**核心方法**：基于前瞻性观察性干预试验队列（均接受手术），以SNOT-22作为主要结局标签，仅使用术前特征训练多种监督学习算法及集成模型，评估其对“手术获益/候选性”的分类预测，并与专家在独立留出样本上的表现对比。

**主要结论**：最佳模型在整体上约达85%分类准确率，且在30例混合难度留出集上达80%，优于专家平均75.6%，显示其可提供可解释的候选性预测并辅助个体化手术决策。

**关键词**：慢性鼻窦炎, 手术结局预测, 手术获益预测, 术前临床数据, 患者报告结局, 监督学习, 集成学习, 可解释性预测模型, 观察性干预试验数据, 手术适应证判别

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.17888v1) | [下载PDF](https://arxiv.org/pdf/2602.17888v1.pdf)

---

## [9. The Geometry of Multi-Task Grokking: Transverse Instability, Superposition, and Weight Decay Phase Structure](https://arxiv.org/abs/2602.18523v1)

**作者**：Yongzhong Xu  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-19

### 📄 论文摘要

Grokking -- the abrupt transition from memorization to generalization long after near-zero training loss -- has been studied mainly in single-task settings. We extend geometric analysis to multi-task modular arithmetic, training shared-trunk Transformers on dual-task (mod-add + mod-mul) and tri-task (mod-add + mod-mul + mod-sq) objectives across a systematic weight decay sweep. Five consistent phenomena emerge. (1) Staggered grokking order: multiplication generalizes first, followed by squaring, then addition, with consistent delays across seeds. (2) Universal integrability: optimization trajectories remain confined to an empirically invariant low-dimensional execution manifold; commutator defects orthogonal to this manifold reliably precede generalization. (3) Weight decay phase structure: grokking timescale, curvature depth, reconstruction threshold, and defect lead covary systematically with weight decay, revealing distinct dynamical regimes and a sharp no-decay failure mode. (4) Holographic incompressibility: final solutions occupy only 4--8 principal trajectory directions yet are distributed across full-rank weights and destroyed by minimal perturbations; SVD truncation, magnitude pruning, and uniform scaling all fail to preserve performance. (5) Transverse fragility and redundancy: removing less than 10% of orthogonal gradient components eliminates grokking, yet dual-task models exhibit partial recovery under extreme deletion, suggesting redundant center manifolds enabled by overparameterization. Together, these results support a dynamical picture in which multi-task grokking constructs a compact superposition subspace in parameter space, with weight decay acting as compression pressure and excess parameters supplying geometric redundancy in optimization pathways.

### 🤖 AI 总结

**一句话总结**：在多任务模块算术上，作者用几何视角揭示多任务grokking存在稳定的低维执行流形与可预测的“横向缺陷”前兆，并呈现随weight decay变化的清晰相结构与脆弱/冗余并存的优化动力学。

**研究动机**：以往grokking研究多聚焦单任务，尚不清楚多任务共享参数下的泛化跃迁顺序、几何机制以及正则化（weight decay）如何塑造其动力学与可达性。

**核心方法**：训练共享trunk的Transformer同时学习mod-add/mod-mul（及加上mod-sq）的多任务目标，系统扫weight decay；用轨迹几何分析（低维流形/主方向、曲率与“对易子缺陷”等横向量）、以及删减正交梯度分量与SVD截断/剪枝/缩放等扰动实验评估稳定性与可压缩性。

**主要结论**：观察到稳定的分阶段grokking顺序（乘法→平方→加法）与“普适可积”低维执行流形，且正交于流形的缺陷信号可领先预测泛化；weight decay引入不同动力学相并在无衰减时出现失败模式；最终解在少数轨迹主方向上“不可压缩”且对微小扰动极脆弱，同时过参数化带来一定冗余中心流形使极端删除下仍可能部分恢复。

**关键词**：模块化算术任务, 权重衰减, 相结构, 优化轨迹几何, 低维执行流形, 参数空间叠加子空间, 中心流形冗余, 横向不稳定性, 不可压缩性

**评分**：19

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18523v1) | [下载PDF](https://arxiv.org/pdf/2602.18523v1.pdf)

---

## [10. ADAPT: Hybrid Prompt Optimization for LLM Feature Visualization](https://arxiv.org/abs/2602.17867v1)

**作者**：João N. Cardoso, Arlindo L. Oliveira, Bruno Martins  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-02-19

### 📄 论文摘要

Understanding what features are encoded by learned directions in LLM activation space requires identifying inputs that strongly activate them. Feature visualization, which optimizes inputs to maximally activate a target direction, offers an alternative to costly dataset search approaches, but remains underexplored for LLMs due to the discrete nature of text. Furthermore, existing prompt optimization techniques are poorly suited to this domain, which is highly prone to local minima. To overcome these limitations, we introduce ADAPT, a hybrid method combining beam search initialization with adaptive gradient-guided mutation, designed around these failure modes. We evaluate on Sparse Autoencoder latents from Gemma 2 2B, proposing metrics grounded in dataset activation statistics to enable rigorous comparison, and show that ADAPT consistently outperforms prior methods across layers and latent types. Our results establish that feature visualization for LLMs is tractable, but requires design assumptions tailored to the domain.

### 🤖 AI 总结

**一句话总结**：ADAPT 通过“束搜索初始化 + 自适应梯度引导变异”的混合提示优化，使在LLM激活空间中对特征方向的可解释输入搜索更稳定、更有效。

**研究动机**：为理解LLM激活空间中学习到的方向（如SAE隐变量）编码了什么，需要找到能强激活该方向的文本输入；但文本离散性与提示优化易陷入局部最优，使现有特征可视化方法效果不佳且对比不够严谨。

**核心方法**：提出ADAPT：先用beam search生成高激活的初始prompt以缓解局部极小值问题，再用自适应的、由梯度信号引导的离散“变异/编辑”迭代优化文本；并在Gemma 2 2B的稀疏自编码器(latents)上评估，使用基于数据集激活统计的指标进行可比性衡量。

**主要结论**：ADAPT在不同层与不同latent类型上稳定优于既有提示优化/特征可视化方法，表明LLM特征可视化是可行的，但需要针对离散文本与局部最优等领域失效模式做专门设计。

**关键词**：特征可视化, LLM, 提示优化, 混合方法, 自适应梯度, 局部最优, 稀疏自编码器, 激活统计, 性能评估

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2602.17867v1) | [下载PDF](https://arxiv.org/pdf/2602.17867v1.pdf)

---

## [11. Financial time series augmentation using transformer based GAN architecture](https://arxiv.org/abs/2602.17865v1)

**作者**：Andrzej Podobiński, Jarosław A. Chudziak  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-19

### 📄 论文摘要

Time-series forecasting is a critical task across many domains, from engineering to economics, where accurate predictions drive strategic decisions. However, applying advanced deep learning models in challenging, volatile domains like finance is difficult due to the inherent limitation and dynamic nature of financial time series data. This scarcity often results in sub-optimal model training and poor generalization. The fundamental challenge lies in determining how to reliably augment scarce financial time series data to enhance the predictive accuracy of deep learning forecasting models. Our main contribution is a demonstration of how Generative Adversarial Networks (GANs) can effectively serve as a data augmentation tool to overcome data scarcity in the financial domain. Specifically, we show that training a Long Short-Term Memory (LSTM) forecasting model on a dataset augmented with synthetic data generated by a transformer-based GAN (TTS-GAN) significantly improves the forecasting accuracy compared to using real data alone. We confirm these results across different financial time series (Bitcoin and S\&P500 price data) and various forecasting horizons. Furthermore, we propose a novel, time series specific quality metric that combines Dynamic Time Warping (DTW) and a modified Deep Dataset Dissimilarity Measure (DeD-iMs) to reliably monitor the training progress and evaluate the quality of the generated data. These findings provide compelling evidence for the benefits of GAN-based data augmentation in enhancing financial predictive capabilities.

### 🤖 AI 总结

**一句话总结**：N/A

**研究动机**：N/A

**核心方法**：N/A

**主要结论**：N/A

**关键词**：金融时间序列, 时间序列预测, 数据增强, 生成对抗网络（GAN）, 合成时间序列数据, 数据稀缺, 生成数据质量评估, 动态时间规整（DTW）, 数据集差异度量（DeD-iMs）, 多预测步长

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2602.17865v1) | [下载PDF](https://arxiv.org/pdf/2602.17865v1.pdf)

---

## [12. JAX-Privacy: A library for differentially private machine learning](https://arxiv.org/abs/2602.17861v1)

**作者**：Ryan McKenna, Galen Andrew, Borja Balle 等 9 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-19

### 📄 论文摘要

JAX-Privacy is a library designed to simplify the deployment of robust and performant mechanisms for differentially private machine learning. Guided by design principles of usability, flexibility, and efficiency, JAX-Privacy serves both researchers requiring deep customization and practitioners who want a more out-of-the-box experience. The library provides verified, modular primitives for critical components for all aspects of the mechanism design including batch selection, gradient clipping, noise addition, accounting, and auditing, and brings together a large body of recent research on differentially private ML.

### 🤖 AI 总结

**一句话总结**：JAX-Privacy 是一个面向差分隐私机器学习的 JAX 库，提供可验证且模块化的隐私机制组件，兼顾易用性、灵活性与效率。

**研究动机**：差分隐私训练涉及批次采样、梯度裁剪、加噪、隐私会计与审计等复杂环节，实践中容易出错且难以兼顾性能与可复现。作者希望用统一的库降低部署门槛，同时支持研究者深度定制与工程落地。

**核心方法**：库以“可用、灵活、高效”为设计原则，提供经过验证的模块化原语覆盖 DP 机制设计全链路：batch selection、gradient clipping、noise addition、accounting、auditing，并整合近期 DP-ML 研究成果以便组合与扩展。

**主要结论**：JAX-Privacy 通过标准化且可组合的 DP 组件，使差分隐私机器学习更容易正确实现并保持较高性能；同时既能开箱即用，也能支持研究级别的机制探索与自定义。

**关键词**：差分隐私, 隐私保护机器学习, 梯度裁剪, 噪声注入, 隐私审计, 批量采样, 模块化隐私机制, JAX-Privacy

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.17861v1) | [下载PDF](https://arxiv.org/pdf/2602.17861v1.pdf)

---

## [13. Neural Prior Estimation: Learning Class Priors from Latent Representations](https://arxiv.org/abs/2602.17853v1)

**作者**：Masoud Yavari, Payman Moallem  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-02-19

### 📄 论文摘要

Class imbalance induces systematic bias in deep neural networks by imposing a skewed effective class prior. This work introduces the Neural Prior Estimator (NPE), a framework that learns feature-conditioned log-prior estimates from latent representations. NPE employs one or more Prior Estimation Modules trained jointly with the backbone via a one-way logistic loss. Under the Neural Collapse regime, NPE is analytically shown to recover the class log-prior up to an additive constant, providing a theoretically grounded adaptive signal without requiring explicit class counts or distribution-specific hyperparameters. The learned estimate is incorporated into logit adjustment, forming NPE-LA, a principled mechanism for bias-aware prediction. Experiments on long-tailed CIFAR and imbalanced semantic segmentation benchmarks (STARE, ADE20K) demonstrate consistent improvements, particularly for underrepresented classes. NPE thus offers a lightweight and theoretically justified approach to learned prior estimation and imbalance-aware prediction.

### 🤖 AI 总结

**一句话总结**：提出NPE从网络潜表示中学习类别先验并用于logit调整，在不依赖显式类频统计的情况下提升长尾与不均衡任务表现。

**研究动机**：类别不均衡会在训练中引入偏斜的有效类先验，导致模型对少数类系统性偏置；现有先验修正常依赖类计数或手工超参，适应性与可用性受限。

**核心方法**：设计Neural Prior Estimator（NPE），通过一个或多个Prior Estimation Module从潜特征中预测特征条件的log-prior，并与主干网络用单向logistic损失联合训练；将学到的先验估计注入logit adjustment形成NPE-LA进行偏置感知预测。

**主要结论**：理论上在Neural Collapse条件下，NPE可恢复类别log-prior（差一个加性常数），提供有依据的自适应先验信号；在长尾CIFAR与不均衡语义分割（STARE、ADE20K）上稳定提升，尤其改善少数类性能，且方法轻量无需显式类频或分布特定超参。

**关键词**：类别不平衡, 类别先验估计, 特征条件先验, 潜在表征, 长尾识别, 偏置校正预测, 语义分割不平衡, 联合训练模块

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.17853v1) | [下载PDF](https://arxiv.org/pdf/2602.17853v1.pdf)

---

## [14. Quad Length Codes for Lossless Compression of e4m3](https://arxiv.org/abs/2602.17849v2)

**作者**：Aditya Agrawal, Albert Magyar, Hiteshwar Eswaraiah 等 8 位作者  
**分类**：cs.LG, cs.IT  
**发布时间**：2026-02-19

### 📄 论文摘要

Training and serving Large Language Models (LLMs) relies heavily on parallelization and collective operations, which are frequently bottlenecked by network bandwidth. Lossless compression using e.g., Huffman codes can alleviate the issue, however, Huffman codes suffer from slow, bit-sequential decoding and high hardware complexity due to deep tree traversals. Universal codes e.g., Exponential-Golomb codes are faster to decode but do not exploit the symbol frequency distributions. To address these limitations, this paper introduces Quad Length Codes, a hybrid approach designed to balance compression efficiency with decoding speed. The coding scheme uses 3 prefix bits to divide the 256 symbols into 8 areas. Each area has a different code length and encodes a different number of symbols. The scheme uses a Look Up Table with 256 entries, significantly simplifying the hardware implementation compared to Huffman trees. The coding scheme can be adapted for different distributions. For the e4m3 data type, the scheme achieves a compressibility of 13.9% in comparison to 15.9% achieved by Huffman codes, but it significantly speeds up the decoding and simplifies the hardware complexity.

### 🤖 AI 总结

**一句话总结**：提出Quad Length Codes，用固定前缀分区+查表的方式对e4m3进行无损压缩，在接近Huffman压缩率的同时显著提升解码速度并降低硬件复杂度。

**研究动机**：LLM训练/推理中的集体通信受网络带宽限制，需要无损压缩缓解；但Huffman解码需深树遍历、位串行且硬件复杂，通用码虽快却难以利用真实符号分布。

**核心方法**：用3个前缀位将256个符号划分为8个区域，每区采用不同码长并覆盖不同数量符号，以适配分布；解码通过256项LUT直接映射，避免Huffman树遍历并便于硬件实现。

**主要结论**：在e4m3数据上，该方法压缩率约13.9%（Huffman约15.9%），虽略逊但显著加速解码并简化硬件实现，且可针对不同分布进行调整。

**关键词**：无损压缩, 四长度编码, 解码速度, 硬件复杂性, 符号频率分布, 查找表, e4m3数据类型, Quad

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2602.17849v2) | [下载PDF](https://arxiv.org/pdf/2602.17849v2.pdf)

---

## [15. Two Calm Ends and the Wild Middle: A Geometric Picture of Memorization in Diffusion Models](https://arxiv.org/abs/2602.17846v1)

**作者**：Nick Dodson, Xinyu Gao, Qingsong Wang 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-19

### 📄 论文摘要

Diffusion models generate high-quality samples but can also memorize training data, raising serious privacy concerns. Understanding the mechanisms governing when memorization versus generalization occurs remains an active area of research. In particular, it is unclear where along the noise schedule memorization is induced, how data geometry influences it, and how phenomena at different noise scales interact. We introduce a geometric framework that partitions the noise schedule into three regimes based on the coverage properties of training data by Gaussian shells and the concentration behavior of the posterior, which we argue are two fundamental objects governing memorization and generalization in diffusion models. This perspective reveals that memorization risk is highly non-uniform across noise levels. We further identify a danger zone at medium noise levels where memorization is most pronounced. In contrast, both the small and large noise regimes resist memorization, but through fundamentally different mechanisms: small noise avoids memorization due to limited training coverage, while large noise exhibits low posterior concentration and admits a provably near linear Gaussian denoising behavior. For the medium noise regime, we identify geometric conditions through which we propose a geometry-informed targeted intervention that mitigates memorization.

### 🤖 AI 总结

**一句话总结**：论文提出一个几何框架把扩散模型的噪声日程分为“小/中/大噪声”三段，指出记忆化风险主要集中在中等噪声段，并给出针对性的几何干预来缓解。

**研究动机**：扩散模型可能记忆训练样本带来隐私风险，但现有理解不清楚“记忆化在噪声日程的哪个阶段发生”、数据几何如何影响以及不同噪声尺度现象如何相互作用。

**核心方法**：基于两类关键几何对象——训练数据被高斯壳覆盖的性质与后验分布的集中行为——将噪声日程划分为三个机制不同的区间，并据此分析各区间的记忆化倾向；在中噪声区提出满足特定几何条件的“定向干预”以抑制记忆化。

**主要结论**：记忆化风险在噪声水平上高度不均匀：中等噪声存在最危险的“记忆化区”；小噪声因训练覆盖不足而不易记忆，大噪声因后验不集中且去噪近似线性高斯而天然抗记忆，并可通过几何引导的干预降低中噪声段的记忆风险。

**关键词**：Diffusion, 训练数据记忆化, 隐私泄露风险, 噪声调度, 中等噪声危险区, 数据几何, 高斯壳覆盖, 后验分布集中, 线性高斯去噪, 定向干预缓解

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2602.17846v1) | [下载PDF](https://arxiv.org/pdf/2602.17846v1.pdf)

---

