# arXiv AI 论文日报 | 2026-02-05

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (13 篇)
- [cs.AI](#csAI) (5 篇)
- [cs.CV](#csCV) (8 篇)
- [cs.CL](#csCL) (4 篇)

---

## cs.AI

## [1. DyTopo: Dynamic Topology Routing for Multi-Agent Reasoning via Semantic Matching](https://arxiv.org/abs/2602.06039v1)

**作者**：Yuxing Lu, Yucheng Hu, Xukai Zhao 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-05

### 📄 论文摘要

Multi-agent systems built from prompted large language models can improve multi-round reasoning, yet most existing pipelines rely on fixed, trajectory-wide communication patterns that are poorly matched to the stage-dependent needs of iterative problem solving. We introduce DyTopo, a manager-guided multi-agent framework that reconstructs a sparse directed communication graph at each round. Conditioned on the manager's round goal, each agent outputs lightweight natural-language query (need) and \key (offer) descriptors; DyTopo embeds these descriptors and performs semantic matching, routing private messages only along the induced edges. Across code generation and mathematical reasoning benchmarks and four LLM backbones, DyTopo consistently outperforms over the strongest baseline (avg. +6.2). Beyond accuracy, DyTopo yields an interpretable coordination trace via the evolving graphs, enabling qualitative inspection of how communication pathways reconfigure across rounds.

### 🤖 AI 总结

**一句话总结**：DyTopo是一种动态拓扑路由框架，通过语义匹配优化多代理系统的通信效率和问题解决能力。

**研究动机**：现有的多代理系统通常依赖于固定的通信模式，难以满足迭代问题解决中阶段性需求，因此需要一种灵活的通信机制。

**核心方法**：DyTopo通过管理者指导，在每一轮重构稀疏的有向通信图，基于代理的需求和提供描述符进行语义匹配，仅在有效边上路由私密消息。

**主要结论**：DyTopo在多个基准测试中表现优越，不仅提高了准确性，还提供了可解释的协调轨迹，便于对通信路径的定性检查。

**关键词**：多智能体, 语义匹配, 深度学习, 神经网络, 代理, 自主代理, 代码生成, 数学推理, 迭代问题解决, 语义搜索, llm

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06039v1) | [下载PDF](https://arxiv.org/pdf/2602.06039v1.pdf)

---

## [2. Learning Event-Based Shooter Models from Virtual Reality Experiments](https://arxiv.org/abs/2602.06023v1)

**作者**：Christopher A. McClurg, Alan R. Wagner  
**分类**：cs.AI, cs.RO  
**发布时间**：2026-02-05

### 📄 论文摘要

Virtual reality (VR) has emerged as a powerful tool for evaluating school security measures in high-risk scenarios such as school shootings, offering experimental control and high behavioral fidelity. However, assessing new interventions in VR requires recruiting new participant cohorts for each condition, making large-scale or iterative evaluation difficult. These limitations are especially restrictive when attempting to learn effective intervention strategies, which typically require many training episodes. To address this challenge, we develop a data-driven discrete-event simulator (DES) that models shooter movement and in-region actions as stochastic processes learned from participant behavior in VR studies. We use the simulator to examine the impact of a robot-based shooter intervention strategy. Once shown to reproduce key empirical patterns, the DES enables scalable evaluation and learning of intervention strategies that are infeasible to train directly with human subjects. Overall, this work demonstrates a high-to-mid fidelity simulation workflow that provides a scalable surrogate for developing and evaluating autonomous school-security interventions.

### 🤖 AI 总结

**一句话总结**：本研究开发了一种基于虚拟现实的离散事件模拟器，用于评估学校安全干预策略的有效性。

**研究动机**：虚拟现实在高风险场景下评估学校安全措施的能力受限于需要为每个条件招募新参与者，从而影响大规模和迭代评估的可行性。

**核心方法**：研究者开发了一种数据驱动的离散事件模拟器，模拟射手的移动和行为，以从虚拟现实研究中的参与者行为中学习。

**主要结论**：该模拟器能够有效复制关键的实证模式，从而支持对干预策略的可扩展评估和学习，提供了开发和评估自主学校安全干预的可行替代方案。

**关键词**：虚拟现实, 事件驱动模拟器, 深度学习, 机器人干预, 自主系统, 学习策略, 行为模拟, 数据驱动, 评估方法, autonomous

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06023v1) | [下载PDF](https://arxiv.org/pdf/2602.06023v1.pdf)

---

## [3. AgenticPay: A Multi-Agent LLM Negotiation System for Buyer-Seller Transactions](https://arxiv.org/abs/2602.06008v1)

**作者**：Xianyang Liu, Shangding Gu, Dawn Song  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-02-05

### 📄 论文摘要

Large language model (LLM)-based agents are increasingly expected to negotiate, coordinate, and transact autonomously, yet existing benchmarks lack principled settings for evaluating language-mediated economic interaction among multiple agents. We introduce AgenticPay, a benchmark and simulation framework for multi-agent buyer-seller negotiation driven by natural language. AgenticPay models markets in which buyers and sellers possess private constraints and product-dependent valuations, and must reach agreements through multi-round linguistic negotiation rather than numeric bidding alone. The framework supports a diverse suite of over 110 tasks ranging from bilateral bargaining to many-to-many markets, with structured action extraction and metrics for feasibility, efficiency, and welfare. Benchmarking state-of-the-art proprietary and open-weight LLMs reveals substantial gaps in negotiation performance and highlights challenges in long-horizon strategic reasoning, establishing AgenticPay as a foundation for studying agentic commerce and language-based market interaction. Code and dataset are available at the link: https://github.com/SafeRL-Lab/AgenticPay.

### 🤖 AI 总结

**一句话总结**：AgenticPay是一个多代理LLM的谈判系统，专注于买卖交易中的语言驱动的经济互动评估。

**研究动机**：当前的评估基准缺乏对多代理语言中介经济互动的系统性设置，急需一个能有效评估谈判能力的框架。

**核心方法**：AgenticPay提供了一个模拟框架，支持超过110个任务，从双边谈判到多对多市场，评估谈判的可行性、效率和福利。

**主要结论**：基准测试揭示了现有LLM在谈判表现上的显著差距，并突出了在长期战略推理中的挑战，为代理商业和基于语言的市场互动研究奠定了基础。

**关键词**：多代理, LLM, 语言模型, 协商, 交易, 自动化, 经济交互, 多轮谈判, 市场模拟, 行动提取

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06008v1) | [下载PDF](https://arxiv.org/pdf/2602.06008v1.pdf)

---

## [4. Speech Emotion Recognition Leveraging OpenAI's Whisper Representations and Attentive Pooling Methods](https://arxiv.org/abs/2602.06000v1)

**作者**：Ali Shendabadi, Parnia Izadirad, Mostafa Salehi 等 4 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-02-05

### 📄 论文摘要

Speech Emotion Recognition (SER) research has faced limitations due to the lack of standard and sufficiently large datasets. Recent studies have leveraged pre-trained models to extract features for downstream tasks such as SER. This work explores the capabilities of Whisper, a pre-trained ASR system, in speech emotion recognition by proposing two attention-based pooling methods, Multi-head Attentive Average Pooling and QKV Pooling, designed to efficiently reduce the dimensionality of Whisper representations while preserving emotional features. We experiment on English and Persian, using the IEMOCAP and ShEMO datasets respectively, with Whisper Tiny and Small. Our multi-head QKV architecture achieves state-of-the-art results on the ShEMO dataset, with a 2.47% improvement in unweighted accuracy. We further compare the performance of different Whisper encoder layers and find that intermediate layers often perform better for SER on the Persian dataset, providing a lightweight and efficient alternative to much larger models such as HuBERT X-Large. Our findings highlight the potential of Whisper as a representation extractor for SER and demonstrate the effectiveness of attention-based pooling for dimension reduction.

### 🤖 AI 总结

**一句话总结**：本文探讨利用OpenAI的Whisper模型及注意力池化方法进行语音情感识别，取得了在ShEMO数据集上的最佳结果。

**研究动机**：语音情感识别研究面临标准化和大规模数据集不足的问题，现有研究已开始利用预训练模型提取特征。

**核心方法**：提出两种基于注意力的池化方法：多头注意力平均池化和QKV池化，以有效降低Whisper表征的维度并保留情感特征。

**主要结论**：Whisper作为情感识别的表征提取器具有潜力，且注意力池化方法在降维方面表现出色。

**关键词**：情感识别, 语音处理, 预训练模型, Whisper, 多头注意力, 特征提取, 维度减少, ASR系统, 机器学习, 深度学习, rag

**评分**：67

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06000v1) | [下载PDF](https://arxiv.org/pdf/2602.06000v1.pdf)

---

## [5. Geographically-aware Transformer-based Traffic Forecasting for Urban Motorway Digital Twins](https://arxiv.org/abs/2602.05983v1)

**作者**：Krešimir Kušić, Vinny Cahill, Ivana Dusparic  
**分类**：cs.AI  
**发布时间**：2026-02-05

### 📄 论文摘要

The operational effectiveness of digital-twin technology in motorway traffic management depends on the availability of a continuous flow of high-resolution real-time traffic data. To function as a proactive decision-making support layer within traffic management, a digital twin must also incorporate predicted traffic conditions in addition to real-time observations. Due to the spatio-temporal complexity and the time-variant, non-linear nature of traffic dynamics, predicting motorway traffic remains a difficult problem. Sequence-based deep-learning models offer clear advantages over classical machine learning and statistical models in capturing long-range, temporal dependencies in time-series traffic data, yet limitations in forecasting accuracy and model complexity point to the need for further improvements. To improve motorway traffic forecasting, this paper introduces a Geographically-aware Transformer-based Traffic Forecasting GATTF model, which exploits the geographical relationships between distributed sensors using their mutual information (MI). The model has been evaluated using real-time data from the Geneva motorway network in Switzerland and results confirm that incorporating geographical awareness through MI enhances the accuracy of GATTF forecasting compared to a standard Transformer, without increasing model complexity.

### 🤖 AI 总结

**一句话总结**：本研究提出了一种地理感知的基于Transformer的交通预测模型，以提高城市高速公路的交通预测准确性。

**研究动机**：高速公路数字双胞胎技术的有效性依赖于高分辨率实时交通数据的持续流动，同时需结合预测的交通状况以支持决策。

**核心方法**：提出的GATTF模型利用分布式传感器之间的互信息来捕捉地理关系，改善交通预测性能。

**主要结论**：实验结果表明，使用互信息增强地理感知可以提高GATTF模型的预测准确性，相较于标准Transformer模型，复杂度未增加。

**关键词**：深度学习, Transformer, 交通预测, 数字双胞胎, 时序数据, 地理信息, 实时数据, 机器学习, 预测模型

**评分**：65

**论文链接**：[查看原文](https://arxiv.org/abs/2602.05983v1) | [下载PDF](https://arxiv.org/pdf/2602.05983v1.pdf)

---

## cs.CL

## [6. Learning Query-Aware Budget-Tier Routing for Runtime Agent Memory](https://arxiv.org/abs/2602.06025v1)

**作者**：Haozhen Zhang, Haodong Yue, Tao Feng 等 11 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-02-05

### 📄 论文摘要

Memory is increasingly central to Large Language Model (LLM) agents operating beyond a single context window, yet most existing systems rely on offline, query-agnostic memory construction that can be inefficient and may discard query-critical information. Although runtime memory utilization is a natural alternative, prior work often incurs substantial overhead and offers limited explicit control over the performance-cost trade-off. In this work, we present \textbf{BudgetMem}, a runtime agent memory framework for explicit, query-aware performance-cost control. BudgetMem structures memory processing as a set of memory modules, each offered in three budget tiers (i.e., \textsc{Low}/\textsc{Mid}/\textsc{High}). A lightweight router performs budget-tier routing across modules to balance task performance and memory construction cost, which is implemented as a compact neural policy trained with reinforcement learning. Using BudgetMem as a unified testbed, we study three complementary strategies for realizing budget tiers: implementation (method complexity), reasoning (inference behavior), and capacity (module model size). Across LoCoMo, LongMemEval, and HotpotQA, BudgetMem surpasses strong baselines when performance is prioritized (i.e., high-budget setting), and delivers better accuracy-cost frontiers under tighter budgets. Moreover, our analysis disentangles the strengths and weaknesses of different tiering strategies, clarifying when each axis delivers the most favorable trade-offs under varying budget regimes.

### 🤖 AI 总结

**一句话总结**：提出了一种名为BudgetMem的运行时代理内存框架，通过查询感知的预算分层路由来优化内存使用和性能成本的平衡。

**研究动机**：当前大语言模型代理的内存构建多为离线且不考虑查询，导致信息丢失和效率低下，因此需要一种更灵活的内存管理方法。

**核心方法**：BudgetMem将内存处理结构化为多种预算层次的内存模块，并利用轻量级路由器在模块间进行预算层路由，以平衡任务性能和内存成本。

**主要结论**：在多项测试中，BudgetMem在高预算设置下优于基线表现，并在紧预算下提供更好的准确性和成本平衡，同时揭示了不同层次策略的优势和劣势。

**关键词**：查询感知, 预算分层, 运行时代理, 记忆框架, 强化学习, 神经网络, LLM, 性能控制, 任务性能, 记忆构建成本

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06025v1) | [下载PDF](https://arxiv.org/pdf/2602.06025v1.pdf)

---

## [7. A Systematic Evaluation of Large Language Models for PTSD Severity Estimation: The Role of Contextual Knowledge and Modeling Strategies](https://arxiv.org/abs/2602.06015v1)

**作者**：Panagiotis Kaliosis, Adithya V Ganesan, Oscar N. E. Kjell 等 11 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-05

### 📄 论文摘要

Large language models (LLMs) are increasingly being used in a zero-shot fashion to assess mental health conditions, yet we have limited knowledge on what factors affect their accuracy. In this study, we utilize a clinical dataset of natural language narratives and self-reported PTSD severity scores from 1,437 individuals to comprehensively evaluate the performance of 11 state-of-the-art LLMs. To understand the factors affecting accuracy, we systematically varied (i) contextual knowledge like subscale definitions, distribution summary, and interview questions, and (ii) modeling strategies including zero-shot vs few shot, amount of reasoning effort, model sizes, structured subscales vs direct scalar prediction, output rescaling and nine ensemble methods. Our findings indicate that (a) LLMs are most accurate when provided with detailed construct definitions and context of the narrative; (b) increased reasoning effort leads to better estimation accuracy; (c) performance of open-weight models (Llama, Deepseek), plateau beyond 70B parameters while closed-weight (o3-mini, gpt-5) models improve with newer generations; and (d) best performance is achieved when ensembling a supervised model with the zero-shot LLMs. Taken together, the results suggest choice of contextual knowledge and modeling strategies is important for deploying LLMs to accurately assess mental health.

### 🤖 AI 总结

**一句话总结**：本研究评估了11种大型语言模型在PTSD严重程度评估中的表现，强调了上下文知识和建模策略的重要性。

**研究动机**：随着大型语言模型在心理健康评估中的应用增加，了解影响其准确性的因素变得尤为重要。

**核心方法**：使用1437个个体的临床数据集，通过系统性变化上下文知识和建模策略来评估模型性能。

**主要结论**：选择合适的上下文知识和建模策略对于准确评估心理健康至关重要，模型性能受多种因素影响。

**关键词**：大语言模型, PTSD, 评估, 上下文知识, 建模策略, 机器学习, 生成模型, 语义搜索, 零-shot, 多模型集成, llm

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06015v1) | [下载PDF](https://arxiv.org/pdf/2602.06015v1.pdf)

---

## [8. DSB: Dynamic Sliding Block Scheduling for Diffusion LLMs](https://arxiv.org/abs/2602.05992v1)

**作者**：Lizhuo Luo, Shenggui Li, Yonggang Wen 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-05

### 📄 论文摘要

Diffusion large language models (dLLMs) have emerged as a promising alternative for text generation, distinguished by their native support for parallel decoding. In practice, block inference is crucial for avoiding order misalignment in global bidirectional decoding and improving output quality. However, the widely-used fixed, predefined block (naive) schedule is agnostic to semantic difficulty, making it a suboptimal strategy for both quality and efficiency: it can force premature commitments to uncertain positions while delaying easy positions near block boundaries. In this work, we analyze the limitations of naive block scheduling and disclose the importance of dynamically adapting the schedule to semantic difficulty for reliable and efficient inference. Motivated by this, we propose Dynamic Sliding Block (DSB), a training-free block scheduling method that uses a sliding block with a dynamic size to overcome the rigidity of the naive block. To further improve efficiency, we introduce DSB Cache, a training-free KV-cache mechanism tailored to DSB. Extensive experiments across multiple models and benchmarks demonstrate that DSB, together with DSB Cache, consistently improves both generation quality and inference efficiency for dLLMs. Code is released at https://github.com/lizhuo-luo/DSB.

### 🤖 AI 总结

**一句话总结**：提出了一种动态滑动块调度方法DSB，以提高扩散大型语言模型的生成质量和推理效率。

**研究动机**：传统的固定块调度忽视语义难度，导致生成质量和效率的下降，因此需要动态调整调度策略。

**核心方法**：DSB是一种训练无关的滑动块调度方法，结合了动态大小的滑动块和DSB Cache机制以优化性能。

**主要结论**：实验表明，DSB及其缓存机制在多个模型和基准测试中均显著提升了生成质量和推理效率。

**关键词**：动态滑块调度, 扩散大语言模型, 块推理, 语义难度, KV-cache机制, 生成质量, 推理效率, 无需训练, 自适应调度, llm

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.05992v1) | [下载PDF](https://arxiv.org/pdf/2602.05992v1.pdf)

---

## [9. Characterizing Human Semantic Navigation in Concept Production as Trajectories in Embedding Space](https://arxiv.org/abs/2602.05971v1)

**作者**：Felipe D. Toro-Hernández, Jesuino Vieira Filho, Rodrigo M. Cabral-Carvalho  
**分类**：cs.CL, cs.LG, q-bio.NC  
**发布时间**：2026-02-05

### 📄 论文摘要

Semantic representations can be framed as a structured, dynamic knowledge space through which humans navigate to retrieve and manipulate meaning. To investigate how humans traverse this geometry, we introduce a framework that represents concept production as navigation through embedding space. Using different transformer text embedding models, we construct participant-specific semantic trajectories based on cumulative embeddings and extract geometric and dynamical metrics, including distance to next, distance to centroid, entropy, velocity, and acceleration. These measures capture both scalar and directional aspects of semantic navigation, providing a computationally grounded view of semantic representation search as movement in a geometric space. We evaluate the framework on four datasets across different languages, spanning different property generation tasks: Neurodegenerative, Swear verbal fluency, Property listing task in Italian, and in German. Across these contexts, our approach distinguishes between clinical groups and concept types, offering a mathematical framework that requires minimal human intervention compared to typical labor-intensive linguistic pre-processing methods. Comparison with a non-cumulative approach reveals that cumulative embeddings work best for longer trajectories, whereas shorter ones may provide too little context, favoring the non-cumulative alternative. Critically, different embedding models yielded similar results, highlighting similarities between different learned representations despite different training pipelines. By framing semantic navigation as a structured trajectory through embedding space, bridging cognitive modeling with learned representation, thereby establishing a pipeline for quantifying semantic representation dynamics with applications in clinical research, cross-linguistic analysis, and the assessment of artificial cognition.

### 🤖 AI 总结

**一句话总结**：本研究通过构建嵌入空间中的语义轨迹，揭示人类在概念生产中的语义导航过程。

**研究动机**：研究人类如何在结构化和动态的知识空间中检索和操作意义，以深入理解语义表示的导航机制。

**核心方法**：利用不同的变换器文本嵌入模型，构建参与者特定的语义轨迹，并提取几何和动态指标来分析这些轨迹。

**主要结论**：该框架有效区分临床组和概念类型，提供了一种数学方法以量化语义表示动态，适用于临床研究和跨语言分析。

**关键词**：语义导航, 嵌入空间, 变换器, 语义表示, 语义轨迹, 语义检索, 多语言分析, 临床研究, 人机协作, 认知建模, generative

**评分**：52

**论文链接**：[查看原文](https://arxiv.org/abs/2602.05971v1) | [下载PDF](https://arxiv.org/pdf/2602.05971v1.pdf)

---

## cs.CV

## [10. Thinking with Geometry: Active Geometry Integration for Spatial Reasoning](https://arxiv.org/abs/2602.06037v1)

**作者**：Haoyuan Li, Qihang Cao, Tao Tang 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-05

### 📄 论文摘要

Recent progress in spatial reasoning with Multimodal Large Language Models (MLLMs) increasingly leverages geometric priors from 3D encoders. However, most existing integration strategies remain passive: geometry is exposed as a global stream and fused in an indiscriminate manner, which often induces semantic-geometry misalignment and redundant signals. We propose GeoThinker, a framework that shifts the paradigm from passive fusion to active perception. Instead of feature mixing, GeoThinker enables the model to selectively retrieve geometric evidence conditioned on its internal reasoning demands. GeoThinker achieves this through Spatial-Grounded Fusion applied at carefully selected VLM layers, where semantic visual priors selectively query and integrate task-relevant geometry via frame-strict cross-attention, further calibrated by Importance Gating that biases per-frame attention toward task-relevant structures. Comprehensive evaluation results show that GeoThinker sets a new state-of-the-art in spatial intelligence, achieving a peak score of 72.6 on the VSI-Bench. Furthermore, GeoThinker demonstrates robust generalization and significantly improved spatial perception across complex downstream scenarios, including embodied referring and autonomous driving. Our results indicate that the ability to actively integrate spatial structures is essential for next-generation spatial intelligence. Code can be found at https://github.com/Li-Hao-yuan/GeoThinker.

### 🤖 AI 总结

**一句话总结**：GeoThinker提出了一种主动几何集成框架，通过选择性检索几何证据来提升空间推理能力。

**研究动机**：现有的几何集成策略多为被动融合，导致语义与几何的不匹配，影响空间推理效果。

**核心方法**：GeoThinker通过在特定的视觉语言模型层应用空间基础融合，使语义视觉先验有选择地查询和整合任务相关的几何信息，并通过重要性门控进一步优化注意力分配。

**主要结论**：GeoThinker在空间智能方面取得了新的最佳成绩，表明主动集成空间结构对下一代空间智能至关重要。

**关键词**：几何思维, 空间推理, 多模态大型语言模型, 3D编码器, 主动感知, 空间融合, 视觉先验, 任务相关几何, 自主驾驶, 空间智能, ml

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06037v1) | [下载PDF](https://arxiv.org/pdf/2602.06037v1.pdf)

---

## [11. InterPrior: Scaling Generative Control for Physics-Based Human-Object Interactions](https://arxiv.org/abs/2602.06035v1)

**作者**：Sirui Xu, Samuel Schulter, Morteza Ziyadi 等 7 位作者  
**分类**：cs.CV, cs.GR, cs.RO  
**发布时间**：2026-02-05

### 📄 论文摘要

Humans rarely plan whole-body interactions with objects at the level of explicit whole-body movements. High-level intentions, such as affordance, define the goal, while coordinated balance, contact, and manipulation can emerge naturally from underlying physical and motor priors. Scaling such priors is key to enabling humanoids to compose and generalize loco-manipulation skills across diverse contexts while maintaining physically coherent whole-body coordination. To this end, we introduce InterPrior, a scalable framework that learns a unified generative controller through large-scale imitation pretraining and post-training by reinforcement learning. InterPrior first distills a full-reference imitation expert into a versatile, goal-conditioned variational policy that reconstructs motion from multimodal observations and high-level intent. While the distilled policy reconstructs training behaviors, it does not generalize reliably due to the vast configuration space of large-scale human-object interactions. To address this, we apply data augmentation with physical perturbations, and then perform reinforcement learning finetuning to improve competence on unseen goals and initializations. Together, these steps consolidate the reconstructed latent skills into a valid manifold, yielding a motion prior that generalizes beyond the training data, e.g., it can incorporate new behaviors such as interactions with unseen objects. We further demonstrate its effectiveness for user-interactive control and its potential for real robot deployment.

### 🤖 AI 总结

**一句话总结**：InterPrior是一个可扩展的生成控制框架，旨在通过模仿预训练和强化学习提升人类-物体交互中的运动协调能力。

**研究动机**：人类在与物体的交互中往往依赖于高层次的意图和自然的运动协调，而不是明确的全身动作规划。

**核心方法**：InterPrior通过大规模模仿预训练和后续的强化学习微调，学习一个统一的目标条件变分策略，以重构来自多模态观察和高层意图的运动。

**主要结论**：该方法在用户交互控制中表现出色，并展示了其在真实机器人部署中的潜力，能够超越训练数据生成新的交互行为。

**关键词**：生成控制, 物理交互, 生成模型, 强化学习, 运动重建, 目标导向, 多模态观察, 机器人部署, humanoid, 运动先验, generative

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06035v1) | [下载PDF](https://arxiv.org/pdf/2602.06035v1.pdf)

---

## [12. V-Retrver: Evidence-Driven Agentic Reasoning for Universal Multimodal Retrieval](https://arxiv.org/abs/2602.06034v1)

**作者**：Dongyang Chen, Chaoyang Wang, Dezhao SU 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-05

### 📄 论文摘要

Multimodal Large Language Models (MLLMs) have recently been applied to universal multimodal retrieval, where Chain-of-Thought (CoT) reasoning improves candidate reranking. However, existing approaches remain largely language-driven, relying on static visual encodings and lacking the ability to actively verify fine-grained visual evidence, which often leads to speculative reasoning in visually ambiguous cases. We propose V-Retrver, an evidence-driven retrieval framework that reformulates multimodal retrieval as an agentic reasoning process grounded in visual inspection. V-Retrver enables an MLLM to selectively acquire visual evidence during reasoning via external visual tools, performing a multimodal interleaved reasoning process that alternates between hypothesis generation and targeted visual verification.To train such an evidence-gathering retrieval agent, we adopt a curriculum-based learning strategy combining supervised reasoning activation, rejection-based refinement, and reinforcement learning with an evidence-aligned objective. Experiments across multiple multimodal retrieval benchmarks demonstrate consistent improvements in retrieval accuracy (with 23.0% improvements on average), perception-driven reasoning reliability, and generalization.

### 🤖 AI 总结

**一句话总结**：V-Retrver提出了一种基于证据驱动的多模态检索框架，通过视觉检查增强推理过程。

**研究动机**：现有多模态大型语言模型在检索中主要依赖语言驱动，缺乏有效的视觉证据验证，导致推理不准确。

**核心方法**：V-Retrver将多模态检索重构为一种代理推理过程，结合课程学习策略，允许模型在推理过程中选择性获取视觉证据。

**主要结论**：实验表明V-Retrver在检索准确性、推理可靠性和泛化能力上都有显著提升，平均提高23.0%。

**关键词**：多模态, 大语言模型, 代理推理, 视觉检索, 证据驱动, 强化学习, 监督学习, 目标视觉验证, 交替推理, ml

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06034v1) | [下载PDF](https://arxiv.org/pdf/2602.06034v1.pdf)

---

## [13. Splat and Distill: Augmenting Teachers with Feed-Forward 3D Reconstruction For 3D-Aware Distillation](https://arxiv.org/abs/2602.06032v1)

**作者**：David Shavin, Sagie Benaim  
**分类**：cs.CV  
**发布时间**：2026-02-05

### 📄 论文摘要

Vision Foundation Models (VFMs) have achieved remarkable success when applied to various downstream 2D tasks. Despite their effectiveness, they often exhibit a critical lack of 3D awareness. To this end, we introduce Splat and Distill, a framework that instills robust 3D awareness into 2D VFMs by augmenting the teacher model with a fast, feed-forward 3D reconstruction pipeline. Given 2D features produced by a teacher model, our method first lifts these features into an explicit 3D Gaussian representation, in a feedforward manner. These 3D features are then ``splatted" onto novel viewpoints, producing a set of novel 2D feature maps used to supervise the student model, ``distilling" geometrically grounded knowledge. By replacing slow per-scene optimization of prior work with our feed-forward lifting approach, our framework avoids feature-averaging artifacts, creating a dynamic learning process where the teacher's consistency improves alongside that of the student. We conduct a comprehensive evaluation on a suite of downstream tasks, including monocular depth estimation, surface normal estimation, multi-view correspondence, and semantic segmentation. Our method significantly outperforms prior works, not only achieving substantial gains in 3D awareness but also enhancing the underlying semantic richness of 2D features. Project page is available at https://davidshavin4.github.io/Splat-and-Distill/

### 🤖 AI 总结

**一句话总结**：提出了一种新框架Splat and Distill，通过快速的前馈3D重建增强2D视觉基础模型的3D意识。

**研究动机**：尽管视觉基础模型在2D任务中表现出色，但它们在3D意识方面存在显著不足。

**核心方法**：该方法通过将2D特征提升为显式的3D高斯表示，并将其投影到新视角生成新的2D特征图，以监督学生模型并提炼几何知识。

**主要结论**：实验结果表明，该方法在多个下游任务中显著优于先前的工作，提升了3D意识和2D特征的语义丰富性。

**关键词**：3D重建, 视觉基础模型, 2D特征, 教师模型, 学生模型, 知识蒸馏, 语义分割, 深度学习, feed-forward, rag

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06032v1) | [下载PDF](https://arxiv.org/pdf/2602.06032v1.pdf)

---

## [14. Context Forcing: Consistent Autoregressive Video Generation with Long Context](https://arxiv.org/abs/2602.06028v1)

**作者**：Shuo Chen, Cong Wei, Sun Sun 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-05

### 📄 论文摘要

Recent approaches to real-time long video generation typically employ streaming tuning strategies, attempting to train a long-context student using a short-context (memoryless) teacher. In these frameworks, the student performs long rollouts but receives supervision from a teacher limited to short 5-second windows. This structural discrepancy creates a critical \textbf{student-teacher mismatch}: the teacher's inability to access long-term history prevents it from guiding the student on global temporal dependencies, effectively capping the student's context length. To resolve this, we propose \textbf{Context Forcing}, a novel framework that trains a long-context student via a long-context teacher. By ensuring the teacher is aware of the full generation history, we eliminate the supervision mismatch, enabling the robust training of models capable of long-term consistency. To make this computationally feasible for extreme durations (e.g., 2 minutes), we introduce a context management system that transforms the linearly growing context into a \textbf{Slow-Fast Memory} architecture, significantly reducing visual redundancy. Extensive results demonstrate that our method enables effective context lengths exceeding 20 seconds -- 2 to 10 times longer than state-of-the-art methods like LongLive and Infinite-RoPE. By leveraging this extended context, Context Forcing preserves superior consistency across long durations, surpassing state-of-the-art baselines on various long video evaluation metrics.

### 🤖 AI 总结

**一句话总结**：本文提出了一种名为Context Forcing的新框架，通过长上下文教师训练长上下文学生，从而提升视频生成的一致性和有效性。

**研究动机**：现有视频生成方法存在学生与教师之间的短期和长期上下文不匹配问题，限制了模型的生成能力。

**核心方法**：Context Forcing框架通过引入长上下文教师，消除监督不匹配，并使用Slow-Fast Memory架构来管理和优化上下文处理。

**主要结论**：实验结果显示，该方法在生成超过20秒的长视频时，显著超越了现有技术，提升了长时间一致性。

**关键词**：视频生成, 长期一致性, 上下文管理, 深度学习, 生成模型, 长期依赖, Slow-Fast Memory, 训练框架, 监督匹配, rag

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06028v1) | [下载PDF](https://arxiv.org/pdf/2602.06028v1.pdf)

---

## [15. GenArena: How Can We Achieve Human-Aligned Evaluation for Visual Generation Tasks?](https://arxiv.org/abs/2602.06013v1)

**作者**：Ruihang Li, Leigang Qu, Jingxu Zhang 等 9 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-02-05

### 📄 论文摘要

The rapid advancement of visual generation models has outpaced traditional evaluation approaches, necessitating the adoption of Vision-Language Models as surrogate judges. In this work, we systematically investigate the reliability of the prevailing absolute pointwise scoring standard, across a wide spectrum of visual generation tasks. Our analysis reveals that this paradigm is limited due to stochastic inconsistency and poor alignment with human perception. To resolve these limitations, we introduce GenArena, a unified evaluation framework that leverages a pairwise comparison paradigm to ensure stable and human-aligned evaluation. Crucially, our experiments uncover a transformative finding that simply adopting this pairwise protocol enables off-the-shelf open-source models to outperform top-tier proprietary models. Notably, our method boosts evaluation accuracy by over 20% and achieves a Spearman correlation of 0.86 with the authoritative LMArena leaderboard, drastically surpassing the 0.36 correlation of pointwise methods. Based on GenArena, we benchmark state-of-the-art visual generation models across diverse tasks, providing the community with a rigorous and automated evaluation standard for visual generation.

### 🤖 AI 总结

**一句话总结**：本文提出了GenArena框架，通过对比评估提高视觉生成任务的人类对齐评估的可靠性和准确性。

**研究动机**：随着视觉生成模型的快速发展，传统评估方法已无法满足需求，因此需要寻求更符合人类感知的评估标准。

**核心方法**：引入GenArena作为统一的评估框架，采用成对比较的方法，克服现有绝对评分标准的不足。

**主要结论**：GenArena显著提高了评估准确性，且通过基准测试为视觉生成模型提供了严格的自动化评估标准。

**关键词**：视觉生成, 评估框架, 人类对齐, Vision-Language Models, pairwise comparison, 生成模型, 评价准确性, LMArena, 视觉任务

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06013v1) | [下载PDF](https://arxiv.org/pdf/2602.06013v1.pdf)

---

## [16. RISE-Video: Can Video Generators Decode Implicit World Rules?](https://arxiv.org/abs/2602.05986v1)

**作者**：Mingxin Liu, Shuran Ma, Shibei Meng 等 12 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-02-05

### 📄 论文摘要

While generative video models have achieved remarkable visual fidelity, their capacity to internalize and reason over implicit world rules remains a critical yet under-explored frontier. To bridge this gap, we present RISE-Video, a pioneering reasoning-oriented benchmark for Text-Image-to-Video (TI2V) synthesis that shifts the evaluative focus from surface-level aesthetics to deep cognitive reasoning. RISE-Video comprises 467 meticulously human-annotated samples spanning eight rigorous categories, providing a structured testbed for probing model intelligence across diverse dimensions, ranging from commonsense and spatial dynamics to specialized subject domains. Our framework introduces a multi-dimensional evaluation protocol consisting of four metrics: \textit{Reasoning Alignment}, \textit{Temporal Consistency}, \textit{Physical Rationality}, and \textit{Visual Quality}. To further support scalable evaluation, we propose an automated pipeline leveraging Large Multimodal Models (LMMs) to emulate human-centric assessment. Extensive experiments on 11 state-of-the-art TI2V models reveal pervasive deficiencies in simulating complex scenarios under implicit constraints, offering critical insights for the advancement of future world-simulating generative models.

### 🤖 AI 总结

**一句话总结**：RISE-Video是一个旨在评估视频生成模型理解隐含世界规则能力的基准，强调认知推理而非仅仅视觉美感。

**研究动机**：尽管生成视频模型在视觉效果上取得了显著进展，但它们在内化和推理隐含世界规则方面仍存在不足，因此需要一个新的评估框架。

**核心方法**：RISE-Video包含467个经过人工注释的样本，设定了多维度的评估协议，采用四个指标来测试模型的智能，包括推理一致性、时间一致性、物理合理性和视觉质量。

**主要结论**：对11个最先进的TI2V模型的广泛实验显示，在复杂场景下的隐含约束模拟中存在普遍缺陷，为未来生成模型的发展提供了重要见解。

**关键词**：视频生成, 生成模型, 认知推理, 多模态模型, 评估协议, 深度学习, 语义搜索, 代理工作流, 自动化评估, generative

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.05986v1) | [下载PDF](https://arxiv.org/pdf/2602.05986v1.pdf)

---

## [17. LSA: Localized Semantic Alignment for Enhancing Temporal Consistency in Traffic Video Generation](https://arxiv.org/abs/2602.05966v1)

**作者**：Mirlan Karimov, Teodora Spasojevic, Markus Braun 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-02-05

### 📄 论文摘要

Controllable video generation has emerged as a versatile tool for autonomous driving, enabling realistic synthesis of traffic scenarios. However, existing methods depend on control signals at inference time to guide the generative model towards temporally consistent generation of dynamic objects, limiting their utility as scalable and generalizable data engines. In this work, we propose Localized Semantic Alignment (LSA), a simple yet effective framework for fine-tuning pre-trained video generation models. LSA enhances temporal consistency by aligning semantic features between ground-truth and generated video clips. Specifically, we compare the output of an off-the-shelf feature extraction model between the ground-truth and generated video clips localized around dynamic objects inducing a semantic feature consistency loss. We fine-tune the base model by combining this loss with the standard diffusion loss. The model fine-tuned for a single epoch with our novel loss outperforms the baselines in common video generation evaluation metrics. To further test the temporal consistency in generated videos we adapt two additional metrics from object detection task, namely mAP and mIoU. Extensive experiments on nuScenes and KITTI datasets show the effectiveness of our approach in enhancing temporal consistency in video generation without the need for external control signals during inference and any computational overheads.

### 🤖 AI 总结

**一句话总结**：提出了一种局部语义对齐框架，用于增强交通视频生成的时间一致性。

**研究动机**：现有视频生成方法依赖推理时的控制信号，限制了其作为可扩展数据引擎的实用性。

**核心方法**：通过对比真实视频与生成视频的语义特征，结合标准扩散损失来微调预训练的视频生成模型。

**主要结论**：在nuScenes和KITTI数据集上的实验表明，该方法有效提升了视频生成的时间一致性，无需外部控制信号且没有额外计算开销。

**关键词**：视频生成, 交通场景, 语义对齐, 时序一致性, 深度学习, 生成模型, 特征提取, 控制信号, 基础模型, mAP, mIoU, autonomous

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.05966v1) | [下载PDF](https://arxiv.org/pdf/2602.05966v1.pdf)

---

## cs.LG

## [18. Shared LoRA Subspaces for almost Strict Continual Learning](https://arxiv.org/abs/2602.06043v1)

**作者**：Prakhar Kaushik, Ankit Vaidya, Shravan Chaudhari 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CV  
**发布时间**：2026-02-05

### 📄 论文摘要

Adapting large pretrained models to new tasks efficiently and continually is crucial for real-world deployment but remains challenging due to catastrophic forgetting and the high cost of retraining. While parameter-efficient tuning methods like low rank adaptation (LoRA) reduce computational demands, they lack mechanisms for strict continual learning and knowledge integration, without relying on data replay, or multiple adapters. We propose Share, a novel approach to parameter efficient continual finetuning that learns and dynamically updates a single, shared low-rank subspace, enabling seamless adaptation across multiple tasks and modalities. Share constructs a foundational subspace that extracts core knowledge from past tasks and incrementally integrates new information by identifying essential subspace directions. Knowledge from each new task is incorporated into this evolving subspace, facilitating forward knowledge transfer, while minimizing catastrophic interference. This approach achieves up to 100x parameter reduction and 281x memory savings over traditional LoRA methods, maintaining performance comparable to jointly trained models. A single Share model can replace hundreds of task-specific LoRA adapters, supporting scalable, asynchronous continual learning. Experiments across image classification, natural language understanding, 3D pose estimation, and text-to-image generation validate its effectiveness, making Share a practical and scalable solution for lifelong learning in large-scale AI systems.

### 🤖 AI 总结

**一句话总结**：Share是一种新颖的低秩子空间共享方法，旨在实现高效的持续学习，减少灾难性遗忘并支持多任务适应。

**研究动机**：有效且持续地将大型预训练模型适应新任务是现实部署中的关键挑战，尤其是灾难性遗忘和重训练成本高昂的问题。

**核心方法**：Share通过学习和动态更新一个共享的低秩子空间，提取过去任务的核心知识，并逐步整合新信息，从而实现任务之间的无缝适应。

**主要结论**：该方法在多个任务上验证了其有效性，实现了高达100倍的参数减少和281倍的内存节省，支持可扩展的异步持续学习。

**关键词**：共享LoRA子空间, 低秩适应, 持续学习, 知识集成, 参数高效, 多任务适应, 图像分类, 自然语言理解, 3D姿态估计, 文本生成, ml

**评分**：75

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06043v1) | [下载PDF](https://arxiv.org/pdf/2602.06043v1.pdf)

---

## [19. Pseudo-Invertible Neural Networks](https://arxiv.org/abs/2602.06042v1)

**作者**：Yamit Ehrlich, Nimrod Berman, Assaf Shocher  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-02-05

### 📄 论文摘要

The Moore-Penrose Pseudo-inverse (PInv) serves as the fundamental solution for linear systems. In this paper, we propose a natural generalization of PInv to the nonlinear regime in general and to neural networks in particular. We introduce Surjective Pseudo-invertible Neural Networks (SPNN), a class of architectures explicitly designed to admit a tractable non-linear PInv. The proposed non-linear PInv and its implementation in SPNN satisfy fundamental geometric properties. One such property is null-space projection or "Back-Projection", $x' = x + A^\dagger(y-Ax)$, which moves a sample $x$ to its closest consistent state $x'$ satisfying $Ax=y$. We formalize Non-Linear Back-Projection (NLBP), a method that guarantees the same consistency constraint for non-linear mappings $f(x)=y$ via our defined PInv. We leverage SPNNs to expand the scope of zero-shot inverse problems. Diffusion-based null-space projection has revolutionized zero-shot solving for linear inverse problems by exploiting closed-form back-projection. We extend this method to non-linear degradations. Here, "degradation" is broadly generalized to include any non-linear loss of information, spanning from optical distortions to semantic abstractions like classification. This approach enables zero-shot inversion of complex degradations and allows precise semantic control over generative outputs without retraining the diffusion prior.

### 🤖 AI 总结

**一句话总结**：本文提出了一种新的伪可逆神经网络架构，扩展了伪逆的应用于非线性系统，特别是在零-shot 逆问题中的应用。

**研究动机**：研究的动机在于将经典的线性伪逆方法推广到非线性领域，以解决复杂的逆问题并保持一致性约束。

**核心方法**：提出了可映射伪可逆神经网络（SPNN）和非线性回投影（NLBP）方法，以实现非线性系统的有效逆投影。

**主要结论**：该研究表明，SPNN能够在不需要重训练的情况下，对复杂的非线性退化进行零-shot 逆转，并实现对生成输出的精确语义控制。

**关键词**：伪可逆神经网络, 非线性, 反投影, 深度学习, 神经网络, 零-shot, 生成控制, 反向投影, PInv, SPNN, neural network

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06042v1) | [下载PDF](https://arxiv.org/pdf/2602.06042v1.pdf)

---

## [20. Can vision language models learn intuitive physics from interaction?](https://arxiv.org/abs/2602.06033v1)

**作者**：Luca M. Schulze Buschoff, Konstantinos Voudouris, Can Demircan 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-05

### 📄 论文摘要

Pre-trained vision language models do not have good intuitions about the physical world. Recent work has shown that supervised fine-tuning can improve model performance on simple physical tasks. However, fine-tuned models do not appear to learn robust physical rules that can generalize to new contexts. Based on research in cognitive science, we hypothesize that models need to interact with an environment to properly learn its physical dynamics. We train models that learn through interaction with the environment using reinforcement learning. While learning from interaction allows models to improve their within-task performance, it fails to produce models with generalizable physical intuitions. We find that models trained on one task do not reliably generalize to related tasks, even if the tasks share visual statistics and physical principles, and regardless of whether the models are trained through interaction.

### 🤖 AI 总结

**一句话总结**：研究表明，基于交互学习的视觉语言模型在物理直觉上未能实现良好的泛化能力。

**研究动机**：预训练的视觉语言模型缺乏对物理世界的直觉，而监督微调虽能提升简单物理任务的表现，但模型的泛化能力仍然不足。

**核心方法**：通过强化学习训练模型，使其通过与环境的交互学习物理动态。

**主要结论**：尽管交互学习提高了模型在特定任务内的表现，但模型仍无法在相关任务之间可靠地泛化。

**关键词**：视觉语言模型, 物理直觉, 强化学习, 交互学习, 深度学习, 语义搜索, 生成模型, 多智能体, 任务泛化, context

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06033v1) | [下载PDF](https://arxiv.org/pdf/2602.06033v1.pdf)

---

## [21. Curiosity is Knowledge: Self-Consistent Learning and No-Regret Optimization with Active Inference](https://arxiv.org/abs/2602.06029v1)

**作者**：Yingke Li, Anjali Parashar, Enlu Zhou 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-05

### 📄 论文摘要

Active inference (AIF) unifies exploration and exploitation by minimizing the Expected Free Energy (EFE), balancing epistemic value (information gain) and pragmatic value (task performance) through a curiosity coefficient. Yet it has been unclear when this balance yields both coherent learning and efficient decision-making: insufficient curiosity can drive myopic exploitation and prevent uncertainty resolution, while excessive curiosity can induce unnecessary exploration and regret. We establish the first theoretical guarantee for EFE-minimizing agents, showing that a single requirement--sufficient curiosity--simultaneously ensures self-consistent learning (Bayesian posterior consistency) and no-regret optimization (bounded cumulative regret). Our analysis characterizes how this mechanism depends on initial uncertainty, identifiability, and objective alignment, thereby connecting AIF to classical Bayesian experimental design and Bayesian optimization within one theoretical framework. We further translate these theories into practical design guidelines for tuning the epistemic-pragmatic trade-off in hybrid learning-optimization problems, validated through real-world experiments.

### 🤖 AI 总结

**一句话总结**：本文提出了一种新的理论框架，确保主动推理中的足够好奇心可以实现自洽学习和无悔优化。

**研究动机**：研究旨在解决在主动推理中，如何平衡探索与利用，从而实现有效的决策和学习。

**核心方法**：通过建立理论保证，提出足够的好奇心是实现贝叶斯后验一致性和有界累积悔恨的单一要求。

**主要结论**：结果表明，初始不确定性、可识别性和目标对齐对机制的影响，为混合学习-优化问题中的知识与实用性权衡提供了实际设计指导。

**关键词**：自我一致学习, 主动推理, 期望自由能, 好奇心系数, 贝叶斯优化, 任务性能, 信息增益, 高效决策, agent

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06029v1) | [下载PDF](https://arxiv.org/pdf/2602.06029v1.pdf)

---

## [22. Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering](https://arxiv.org/abs/2602.06022v1)

**作者**：Miranda Muqing Miao, Young-Min Cho, Lyle Ungar  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-05

### 📄 论文摘要

Large language models (LLMs) exhibit persistent miscalibration, especially after instruction tuning and preference alignment. Modified training objectives can improve calibration, but retraining is expensive. Inference-time steering offers a lightweight alternative, yet most existing methods optimize proxies for correctness rather than correctness itself. We introduce CORAL (Correctness-Optimized Residual Activation Lens), a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes. We evaluate CORAL across three 7B-parameter models and find that it consistently improves accuracy by 10\% and expected calibration error (ECE) by 50\% on average. We additionally demonstrate that these gains transfer without retraining to the complete published test sets of four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA), averaging 14\% accuracy improvements and 49\% ECE improvements. Our results support the hypothesis that distributed information in model internals can be extracted using regularized probes when individual neurons are insufficient. CORAL thus provides a compute-efficient, transferable, and calibration-aware approach to improve MCQA performance during inference.

### 🤖 AI 总结

**一句话总结**：CORAL是一种优化推理时校准和准确性的轻量级方法，通过模型内部激活的分布式信号提升大型语言模型的表现。

**研究动机**：大型语言模型在指令调优和偏好对齐后常常出现误校准，重新训练成本高昂，因此需要一种有效的推理时调整方法。

**核心方法**：CORAL通过使用权重衰减的多层感知机探针来捕捉模型内部激活的分布式正确性信号，进行正则化推理时调整。

**主要结论**：CORAL显著提升了三种7B参数模型的准确性和期望校准误差，并且这些提升在不重新训练的情况下能够转移到其他测试集。

**关键词**：深度学习, 大语言模型, 校准, 推理, 代理, 迁移学习, CORAL, 正确性优化, 激活信号, 多模型评估, ml

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06022v1) | [下载PDF](https://arxiv.org/pdf/2602.06022v1.pdf)

---

## [23. Mechanisms of AI Protein Folding in ESMFold](https://arxiv.org/abs/2602.06020v1)

**作者**：Kevin Lu, Jannik Brinkmann, Stefan Huber 等 7 位作者  
**分类**：cs.LG, q-bio.BM  
**发布时间**：2026-02-05

### 📄 论文摘要

How do protein structure prediction models fold proteins? We investigate this question by tracing how ESMFold folds a beta hairpin, a prevalent structural motif. Through counterfactual interventions on model latents, we identify two computational stages in the folding trunk. In the first stage, early blocks initialize pairwise biochemical signals: residue identities and associated biochemical features such as charge flow from sequence representations into pairwise representations. In the second stage, late blocks develop pairwise spatial features: distance and contact information accumulate in the pairwise representation. We demonstrate that the mechanisms underlying structural decisions of ESMFold can be localized, traced through interpretable representations, and manipulated with strong causal effects.

### 🤖 AI 总结

**一句话总结**：本研究探讨了ESMFold在折叠蛋白质时的两个计算阶段及其机制。

**研究动机**：研究蛋白质结构预测模型如何折叠蛋白质，以提高对其决策机制的理解。

**核心方法**：通过对模型潜变量的反事实干预，识别ESMFold折叠过程中的早期和晚期计算阶段。

**主要结论**：ESMFold的结构决策机制可以被局部化、追踪并通过可解释的表示进行操控，具有显著的因果效应。

**关键词**：蛋白质折叠, 结构预测模型, ESMFold, 深度学习, 神经网络, 计算阶段, 语义表示, 嵌入, 生成模型, 反事实干预, agent

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06020v1) | [下载PDF](https://arxiv.org/pdf/2602.06020v1.pdf)

---

## [24. Optimism Stabilizes Thompson Sampling for Adaptive Inference](https://arxiv.org/abs/2602.06014v1)

**作者**：Shunxing Yan, Han Zhong  
**分类**：cs.LG, cs.AI, math.OC, math.ST, stat.ML  
**发布时间**：2026-02-05

### 📄 论文摘要

Thompson sampling (TS) is widely used for stochastic multi-armed bandits, yet its inferential properties under adaptive data collection are subtle. Classical asymptotic theory for sample means can fail because arm-specific sample sizes are random and coupled with the rewards through the action-selection rule. We study this phenomenon in the $K$-armed Gaussian bandit and identify \emph{optimism} as a key mechanism for restoring \emph{stability}, a sufficient condition for valid asymptotic inference requiring each arm's pull count to concentrate around a deterministic scale. First, we prove that variance-inflated TS \citep{halder2025stable} is stable for any $K \ge 2$, including the challenging regime where multiple arms are optimal. This resolves the open question raised by \citet{halder2025stable} through extending their results from the two-armed setting to the general $K$-armed setting. Second, we analyze an alternative optimistic modification that keeps the posterior variance unchanged but adds an explicit mean bonus to posterior mean, and establish the same stability conclusion. In summary, suitably implemented optimism stabilizes Thompson sampling and enables asymptotically valid inference in multi-armed bandits, while incurring only a mild additional regret cost.

### 🤖 AI 总结

**一句话总结**：乐观策略稳定了汤普森采样，从而实现了多臂赌博机中的渐近有效推断。

**研究动机**：汤普森采样在自适应数据收集下的推断性质复杂，需要找到机制恢复其稳定性以保证有效推断。

**核心方法**：研究者通过证明方差膨胀的汤普森采样在任意K臂情况下的稳定性，并分析了另一种乐观修改策略，确保后验均值增加。

**主要结论**：适当实施的乐观策略可以稳定汤普森采样，使其在多臂赌博机中实现渐近有效推断，同时仅增加轻微的额外遗憾成本。

**关键词**：关键词：采样, 自适应推断, 多臂赌博机, 稳定性, 后验均值, 变异膨胀, 优化, 强化学习, 统计推断, agent

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06014v1) | [下载PDF](https://arxiv.org/pdf/2602.06014v1.pdf)

---

## [25. On Computation and Reinforcement Learning](https://arxiv.org/abs/2602.05999v1)

**作者**：Raj Ghugare, Michał Bortkiewicz, Alicja Ziarko 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-05

### 📄 论文摘要

How does the amount of compute available to a reinforcement learning (RL) policy affect its learning? Can policies using a fixed amount of parameters, still benefit from additional compute? The standard RL framework does not provide a language to answer these questions formally. Empirically, deep RL policies are often parameterized as neural networks with static architectures, conflating the amount of compute and the number of parameters. In this paper, we formalize compute bounded policies and prove that policies which use more compute can solve problems and generalize to longer-horizon tasks that are outside the scope of policies with less compute. Building on prior work in algorithmic learning and model-free planning, we propose a minimal architecture that can use a variable amount of compute. Our experiments complement our theory. On a set 31 different tasks spanning online and offline RL, we show that $(1)$ this architecture achieves stronger performance simply by using more compute, and $(2)$ stronger generalization on longer-horizon test tasks compared to standard feedforward networks or deep residual network using up to 5 times more parameters.

### 🤖 AI 总结

**一句话总结**：本文探讨了计算资源对强化学习政策学习的影响，并提出了一种能灵活使用计算资源的最小架构。

**研究动机**：研究旨在解答计算资源与强化学习政策之间的关系，特别是如何使固定参数的政策从额外的计算中受益。

**核心方法**：提出了一种计算受限政策的形式化定义，开发了一种最小架构以灵活使用不同数量的计算资源，并通过实验证明其有效性。

**主要结论**：研究表明，使用更多计算资源的政策在多个任务上表现更强，并在长时间测试任务上具备更强的泛化能力。

**关键词**：计算, 强化学习, 深度学习, 神经网络, 算法学习, 在线学习, 模型无关规划, 计算限制政策, 长期任务, 性能提升, neural network

**评分**：65

**论文链接**：[查看原文](https://arxiv.org/abs/2602.05999v1) | [下载PDF](https://arxiv.org/pdf/2602.05999v1.pdf)

---

## [26. Orthogonal Self-Attention](https://arxiv.org/abs/2602.05996v1)

**作者**：Leo Zhang, James Martens  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-02-05

### 📄 论文摘要

Softmax Self-Attention (SSA) is a key component of Transformer architectures. However, when utilised within skipless architectures, which aim to improve representation learning, recent work has highlighted the inherent instability of SSA due to inducing rank collapse and poorly-conditioned Jacobians. In this work, we design a novel attention mechanism: Orthogonal Self-Attention (OSA), which aims to bypass these issues with SSA, in order to allow for (non-causal) Transformers without skip connections and normalisation layers to be more easily trained. In particular, OSA parametrises the attention matrix to be orthogonal via mapping a skew-symmetric matrix, formed from query-key values, through the matrix exponential. We show that this can be practically implemented, by exploiting the low-rank structure of our query-key values, resulting in the computational complexity and memory cost of OSA scaling linearly with sequence length. Furthermore, we derive an initialisation scheme for which we prove ensures that the Jacobian of OSA is well-conditioned.

### 🤖 AI 总结

**一句话总结**：本研究提出了一种新颖的正交自注意力机制，旨在解决传统自注意力的稳定性问题，以便更有效地训练无跳连接的Transformer模型。

**研究动机**：传统的Softmax自注意力在无跳连接架构中表现不稳定，导致表示学习效果不佳，因此需要一种新的注意力机制来克服这些问题。

**核心方法**：正交自注意力（OSA）通过将查询-键值形成的斜对称矩阵映射到正交矩阵，利用低秩结构实现高效计算，同时提供了一种保证雅可比矩阵良好条件的初始化方案。

**主要结论**：OSA的设计使得在不使用跳连接和归一化层的情况下，Transformer能够更容易地进行训练，且其计算复杂度和内存开销与序列长度线性相关。

**关键词**：自注意力, 变换器, 深度学习, 神经网络, 表示学习, 训练稳定性, 低秩结构, 注意力机制, Orthogonal Self-Attention, 无跳跃连接, transformer

**评分**：55

**论文链接**：[查看原文](https://arxiv.org/abs/2602.05996v1) | [下载PDF](https://arxiv.org/pdf/2602.05996v1.pdf)

---

## [27. Diamond Maps: Efficient Reward Alignment via Stochastic Flow Maps](https://arxiv.org/abs/2602.05993v1)

**作者**：Peter Holderrieth, Douglas Chen, Luca Eyring 等 10 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-05

### 📄 论文摘要

Flow and diffusion models produce high-quality samples, but adapting them to user preferences or constraints post-training remains costly and brittle, a challenge commonly called reward alignment. We argue that efficient reward alignment should be a property of the generative model itself, not an afterthought, and redesign the model for adaptability. We propose "Diamond Maps", stochastic flow map models that enable efficient and accurate alignment to arbitrary rewards at inference time. Diamond Maps amortize many simulation steps into a single-step sampler, like flow maps, while preserving the stochasticity required for optimal reward alignment. This design makes search, sequential Monte Carlo, and guidance scalable by enabling efficient and consistent estimation of the value function. Our experiments show that Diamond Maps can be learned efficiently via distillation from GLASS Flows, achieve stronger reward alignment performance, and scale better than existing methods. Our results point toward a practical route to generative models that can be rapidly adapted to arbitrary preferences and constraints at inference time.

### 🤖 AI 总结

**一句话总结**：Diamond Maps是一种高效的随机流映射模型，可以在推理时实现与任意奖励的有效对齐。

**研究动机**：现有的生成模型在训练后适应用户偏好和约束的过程既费时又脆弱，因此需要将高效的奖励对齐作为生成模型的内在属性。

**核心方法**：提出了Diamond Maps模型，通过将多个仿真步骤压缩为单步采样，保持了所需的随机性，从而实现有效的奖励对齐。

**主要结论**：实验结果表明，Diamond Maps在奖励对齐性能上优于现有方法，并能快速适应任意偏好和约束，具有良好的扩展性。

**关键词**：奖励对齐, 生成模型, 流模型, 随机流图, 价值函数, 适应性, 蒸馏, 高效学习, 模型设计, generative

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.05993v1) | [下载PDF](https://arxiv.org/pdf/2602.05993v1.pdf)

---

## [28. Clifford Kolmogorov-Arnold Networks](https://arxiv.org/abs/2602.05977v1)

**作者**：Matthias Wolff, Francesco Alesiani, Christof Duhme 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-05

### 📄 论文摘要

We introduce Clifford Kolmogorov-Arnold Network (ClKAN), a flexible and efficient architecture for function approximation in arbitrary Clifford algebra spaces. We propose the use of Randomized Quasi Monte Carlo grid generation as a solution to the exponential scaling associated with higher dimensional algebras. Our ClKAN also introduces new batch normalization strategies to deal with variable domain input. ClKAN finds application in scientific discovery and engineering, and is validated in synthetic and physics inspired tasks.

### 🤖 AI 总结

**一句话总结**：Clifford Kolmogorov-Arnold Network (ClKAN) 是一种灵活高效的架构，用于在任意Clifford代数空间中进行函数逼近。

**研究动机**：研究旨在解决高维代数相关的指数扩展问题，并推动科学发现与工程应用。

**核心方法**：提出随机准蒙特卡罗网格生成方法和新的批量归一化策略，以处理可变领域输入。

**主要结论**：ClKAN在合成和物理启发任务中得到了验证，展现出在科学与工程领域的广泛应用潜力。

**关键词**：克利福德, 科尔莫戈罗夫-阿诺德网络, 函数逼近, 随机准蒙特卡罗, 批量归一化, 深度学习, 神经网络, 代理, 自主智能, 科学发现, agent

**评分**：55

**论文链接**：[查看原文](https://arxiv.org/abs/2602.05977v1) | [下载PDF](https://arxiv.org/pdf/2602.05977v1.pdf)

---

## [29. Inverse Depth Scaling From Most Layers Being Similar](https://arxiv.org/abs/2602.05970v1)

**作者**：Yizhou Liu, Sara Kangaslahti, Ziming Liu 等 4 位作者  
**分类**：cs.LG, cs.AI, math.DS, stat.ML  
**发布时间**：2026-02-05

### 📄 论文摘要

Neural scaling laws relate loss to model size in large language models (LLMs), yet depth and width may contribute to performance differently, requiring more detailed studies. Here, we quantify how depth affects loss via analysis of LLMs and toy residual networks. We find loss scales inversely proportional to depth in LLMs, probably due to functionally similar layers reducing error through ensemble averaging rather than compositional learning or discretizing smooth dynamics. This regime is inefficient yet robust and may arise from the architectural bias of residual networks and target functions incompatible with smooth dynamics. The findings suggest that improving LLM efficiency may require architectural innovations to encourage compositional use of depth.

### 🤖 AI 总结

**一句话总结**：该研究探讨了深度对大语言模型损失的影响，发现损失与深度呈反比关系。

**研究动机**：现有的神经网络扩展规律未能充分解释深度和宽度对性能的不同贡献，需进行更深入的研究。

**核心方法**：通过分析大语言模型和简单的残差网络，量化深度对损失的影响。

**主要结论**：研究结果表明，提高大语言模型效率可能需要在架构上进行创新，以促进深度的组合使用。

**关键词**：深度学习, 神经网络, LLM, 模型规模, 逆深度缩放, 架构创新, 性能分析, 误差减少, 集成平均

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.05970v1) | [下载PDF](https://arxiv.org/pdf/2602.05970v1.pdf)

---

## [30. A Hybrid Data-Driven Algorithm for Real-Time Friction Force Estimation in Hydraulic Cylinders](https://arxiv.org/abs/2602.05967v1)

**作者**：Mohamad Amin Jamshidi, Mehrbod Zarifi, Zolfa Anvari 等 5 位作者  
**分类**：cs.LG, eess.SY  
**发布时间**：2026-02-05

### 📄 论文摘要

Hydraulic systems are widely utilized in industrial applications due to their high force generation, precise control, and ability to function in harsh environments. Hydraulic cylinders, as actuators in these systems, apply force and position through the displacement of hydraulic fluid, but their operation is significantly influenced by friction force. Achieving precision in hydraulic cylinders requires an accurate friction model under various operating conditions. Existing analytical models, often derived from experimental tests, necessitate the identification or estimation of influencing factors but are limited in adaptability and computational efficiency. This research introduces a data-driven, hybrid algorithm based on Long Short-Term Memory (LSTM) networks and Random Forests for nonlinear friction force estimation. The algorithm effectively combines feature detection and estimation processes using training data acquired from an experimental hydraulic test setup. It achieves a consistent and stable model error of less than 10% across diverse operating conditions and external load variations, ensuring robust performance in complex situations. The computational cost of the algorithm is 1.51 milliseconds per estimation, making it suitable for real-time applications. The proposed method addresses the limitations of analytical models by delivering high precision and computational efficiency. The algorithm's performance is validated through detailed analysis and experimental results, including direct comparisons with the LuGre model. The comparison highlights that while the LuGre model offers a theoretical foundation for friction modeling, its performance is limited by its inability to dynamically adjust to varying operational conditions of the hydraulic cylinder, further emphasizing the advantages of the proposed hybrid approach in real-time applications.

### 🤖 AI 总结

**一句话总结**：本研究提出了一种基于LSTM和随机森林的混合数据驱动算法，用于实时估计液压缸中的摩擦力，具有高精度和低计算成本。

**研究动机**：液压缸在工业应用中广泛使用，其性能受到摩擦力的显著影响，现有的解析模型在适应性和计算效率上存在局限，因此需要更好的摩擦模型。

**核心方法**：研究采用基于长短期记忆网络（LSTM）和随机森林的混合算法，通过实验数据进行特征检测和摩擦力估计，实现了在多种操作条件下的非线性摩擦力估计。

**主要结论**：该算法在复杂情况下表现出超过10%的稳定模型误差，计算成本仅为1.51毫秒，优于传统的LuGre模型，适合实时应用。

**关键词**：机器学习, 深度学习, 神经网络, LSTM, 随机森林, 实时估计, 摩擦力模型, 数据驱动算法, 特征检测, 复杂情况, agent

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.05967v1) | [下载PDF](https://arxiv.org/pdf/2602.05967v1.pdf)

---

