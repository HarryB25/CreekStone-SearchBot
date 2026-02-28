# arXiv AI 论文日报 | 2026-02-26

> 共 15 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (5 篇)
- [cs.AI](#csAI) (4 篇)
- [cs.LG](#csLG) (4 篇)
- [cs.CV](#csCV) (2 篇)

---

## cs.AI

## [1. VeRO: An Evaluation Harness for Agents to Optimize Agents](https://arxiv.org/abs/2602.22480v1)

**作者**：Varun Ursekar, Apaar Shanker, Veronica Chatrath 等 6 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-02-25

### 📄 论文摘要

An important emerging application of coding agents is agent optimization: the iterative improvement of a target agent through edit-execute-evaluate cycles. Despite its relevance, the community lacks a systematic understanding of coding agent performance on this task. Agent optimization differs fundamentally from conventional software engineering: the target agent interleaves deterministic code with stochastic LLM completions, requiring structured capture of both intermediate reasoning and downstream execution outcomes. To address these challenges, we introduce VERO (Versioning, Rewards, and Observations), which provides (1) a reproducible evaluation harness with versioned agent snapshots, budget-controlled evaluation, and structured execution traces, and (2) a benchmark suite of target agents and tasks with reference evaluation procedures. Using VERO, we conduct an empirical study comparing optimizer configurations across tasks and analyzing which modifications reliably improve target agent performance. We release VERO to support research on agent optimization as a core capability for coding agents.

### 🤖 AI 总结

**一句话总结**：VeRO 提供一个可复现的评测框架与基准，用于系统评估“优化其他智能体”的编码智能体在迭代改进任务中的表现。

**研究动机**：现有对“智能体优化”（通过编辑-执行-评估循环改进目标智能体）的研究缺乏统一、可复现的评测体系。该任务不同于传统软件工程，因为目标智能体混合了确定性代码与随机的LLM生成，需要结构化记录推理与执行结果。

**核心方法**：提出 VeRO（Versioning, Rewards, Observations）：通过版本化快照、预算可控的评估与结构化执行轨迹来保证可复现性，并配套一组目标智能体与任务及参考评测流程。基于该框架对不同优化器配置进行跨任务对比实验，分析哪些修改能稳定提升目标智能体性能。

**主要结论**：VeRO 使智能体优化的评估更系统、可复现，并揭示不同优化器改动在不同任务上的效果差异与可靠性；作者发布该框架以推动“优化智能体”成为编码智能体的核心能力研究方向。

**关键词**：编辑-执行-评测循环, 评测框架, 可复现评测, 版本化快照, 执行轨迹, 预算控制评测, 基准套件, 优化器配置对比, LLM 随机补全

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.22480v1) | [下载PDF](https://arxiv.org/pdf/2602.22480v1.pdf)

---

## [2. ConstraintBench: Benchmarking LLM Constraint Reasoning on Direct Optimization](https://arxiv.org/abs/2602.22465v1)

**作者**：Joseph Tso, Preston Schmittou, Quan Huynh 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-25

### 📄 论文摘要

Large language models are increasingly applied to operational decision-making where the underlying structure is constrained optimization. Existing benchmarks evaluate whether LLMs can formulate optimization problems as solver code, but leave open a complementary question. Can LLMs directly produce correct solutions to fully specified constrained optimization problems without access to a solver? We introduce ConstraintBench, a benchmark for evaluating LLMs on direct constrained optimization across 10 operations research domains, with all ground-truth solutions verified by the Gurobi solver. Each task presents a natural-language scenario with entities, constraints, and an optimization objective; the model must return a structured solution that a deterministic verifier checks against every constraint and the solver-proven optimum. We evaluate six frontier models on 200 tasks and find that feasibility, not optimality, is the primary bottleneck. The best model achieves only 65.0% constraint satisfaction, yet feasible solutions average 89 to 96% of the Gurobi-optimal objective. No model exceeds 30.5% on joint feasibility and optimality within 0.1% of the solver reference. Per-domain analysis shows large variation in difficulty, with average feasibility spanning from 83.3% in the production mix domain to 0.8% in the crew assignment domain. Further, systematic failure modes include duration constraint misunderstanding, entity hallucination, and a feasibility-optimality decoupling in facility location and vehicle routing where models achieve high feasibility but 0% optimality. ConstraintBench and all evaluation infrastructure will be publicly released.

### 🤖 AI 总结

**一句话总结**：本文提出了ConstraintBench基准测试，以评估大型语言模型在直接约束优化问题上的解决能力。

**研究动机**：随着大型语言模型在操作决策中的应用增多，研究者希望评估它们能否在没有求解器的情况下直接产生约束优化问题的正确解决方案。

**核心方法**：ConstraintBench涵盖10个运筹学领域的200个任务，通过自然语言场景提供实体、约束和优化目标，模型需返回结构化解决方案，并由确定性验证器检查其约束和最优解。

**主要结论**：研究发现，模型在可行性（约65%）上表现较好，但在最优性上存在显著瓶颈，且不同领域的任务难度差异较大，系统性失败模式也被识别。

**关键词**：约束优化, 约束推理, 直接优化, 无求解器求解, 运筹优化任务, 可行性验证, 最优性评估, 结构化输出, 确定性验证器, 实体幻觉, 可行性-最优性解耦

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2602.22465v1) | [下载PDF](https://arxiv.org/pdf/2602.22465v1.pdf)

---

## [3. CWM: Contrastive World Models for Action Feasibility Learning in Embodied Agent Pipelines](https://arxiv.org/abs/2602.22452v1)

**作者**：Chayan Banerjee  
**分类**：cs.AI, cs.RO  
**发布时间**：2026-02-25

### 📄 论文摘要

A reliable action feasibility scorer is a critical bottleneck in embodied agent pipelines: before any planning or reasoning occurs, the agent must identify which candidate actions are physically executable in the current state. Existing approaches use supervised fine-tuning (SFT) to train action scorers, but SFT treats each candidate independently and does not explicitly teach the model to discriminate between actions that are physically correct and those that are subtly wrong. We propose the Contrastive World Model (CWM), which fine-tunes a large language model (LLM) as an action scorer using an InfoNCE contrastive objective with hard-mined negative examples. The key idea is to push valid actions away from invalid ones in scoring space, with special emphasis on hard negatives: semantically similar but physically incompatible candidates. We evaluate CWM on the ScienceWorld benchmark through two studies. First, an intrinsic affordance evaluation on 605 hard-negative test pairs shows that CWM outperforms SFT by +6.76 percentage points on Precision@1 for minimal-edit negatives -- cases where a single word changes the physical outcome -- and achieves a higher AUC-ROC (0.929 vs. 0.906). Second, a live filter characterisation study measures how well CWM ranks gold-path actions against all valid environment actions during task execution. Under out-of-distribution stress conditions, CWM maintains a significantly better safety margin (-2.39) than SFT (-3.96), indicating that the gold action is ranked closer to the top. These results support the hypothesis that contrastive training induces representations that capture physical feasibility more faithfully than SFT alone.

### 🤖 AI 总结

**一句话总结**：CWM通过对比学习（InfoNCE）+难负样本挖掘微调LLM作为动作可行性打分器，更好地区分“语义相近但物理不可行”的动作，从而在ScienceWorld上优于传统SFT。

**研究动机**：具身智能管线中，规划前必须先判断候选动作是否物理可执行，但SFT往往独立评估每个动作，缺少对“细微错误动作”的显式判别训练，导致可行性判断不稳。

**核心方法**：提出Contrastive World Model：用InfoNCE对比目标将有效动作与无效动作在打分空间拉开，并通过hard-mining重点加入与正例语义接近但物理不兼容的难负样本进行微调。

**主要结论**：在605对难负样本的内在评测上，CWM在最小编辑负例的Precision@1提升+6.76个百分点且AUC-ROC更高（0.929 vs 0.906）；在在线过滤评测的OOD压力下，CWM保持更好的安全边际（-2.39优于-3.96），说明对比训练更能学习物理可行性表示。

**关键词**：具身智能, 动作可行性学习, 动作评分模型, 硬负样本挖掘, 最小编辑负例, 物理可执行性, 可供性评估, 分布外鲁棒性, 监督微调（SFT）

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2602.22452v1) | [下载PDF](https://arxiv.org/pdf/2602.22452v1.pdf)

---

## [4. A Framework for Assessing AI Agent Decisions and Outcomes in AutoML Pipelines](https://arxiv.org/abs/2602.22442v1)

**作者**：Gaoyuan Du, Amit Ahlawat, Xiaoyang Liu 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-25

### 📄 论文摘要

Agent-based AutoML systems rely on large language models to make complex, multi-stage decisions across data processing, model selection, and evaluation. However, existing evaluation practices remain outcome-centric, focusing primarily on final task performance. Through a review of prior work, we find that none of the surveyed agentic AutoML systems report structured, decision-level evaluation metrics intended for post-hoc assessment of intermediate decision quality. To address this limitation, we propose an Evaluation Agent (EA) that performs decision-centric assessment of AutoML agents without interfering with their execution. The EA is designed as an observer that evaluates intermediate decisions along four dimensions: decision validity, reasoning consistency, model quality risks beyond accuracy, and counterfactual decision impact. Across four proof-of-concept experiments, we demonstrate that the EA can (i) detect faulty decisions with an F1 score of 0.919, (ii) identify reasoning inconsistencies independent of final outcomes, and (iii) attribute downstream performance changes to agent decisions, revealing impacts ranging from -4.9\% to +8.3\% in final metrics. These results illustrate how decision-centric evaluation exposes failure modes that are invisible to outcome-only metrics. Our work reframes the evaluation of agentic AutoML systems from an outcome-based perspective to one that audits agent decisions, offering a foundation for reliable, interpretable, and governable autonomous ML systems.

### 🤖 AI 总结

**一句话总结**：提出一种“评估代理（EA）”对Agent式AutoML流水线的中间决策进行事后审计，从而补足只看最终效果的评估盲区。

**研究动机**：现有Agentic AutoML评估几乎都以最终任务指标为中心，缺乏对数据处理、模型选择等中间决策质量的结构化度量，导致很多失败模式无法被发现与归因。

**核心方法**：设计一个不干扰执行过程的观察者EA，从决策有效性、推理一致性、超越准确率的模型质量风险、反事实决策影响四个维度评估中间决策，并通过多组概念验证实验量化其检测与归因能力。

**主要结论**：EA能以F1=0.919检测错误决策、识别与最终结果无关的推理不一致，并将最终指标变化（-4.9%到+8.3%）归因到具体决策，证明决策中心评估能揭示仅看结果无法发现的问题。

**关键词**：决策级评测, 后验审计, 评测智能体, 中间决策质量, 决策有效性, 推理一致性, 反事实影响分析, 模型风险评估, 故障决策检测, 可治理自主ML

**评分**：45

**论文链接**：[查看原文](https://arxiv.org/abs/2602.22442v1) | [下载PDF](https://arxiv.org/pdf/2602.22442v1.pdf)

---

## cs.CL

## [5. Importance of Prompt Optimisation for Error Detection in Medical Notes Using Language Models](https://arxiv.org/abs/2602.22483v1)

**作者**：Craig Myles, Patrick Schrempf, David Harris-Birtill  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-25

### 📄 论文摘要

Errors in medical text can cause delays or even result in incorrect treatment for patients. Recently, language models have shown promise in their ability to automatically detect errors in medical text, an ability that has the opportunity to significantly benefit healthcare systems. In this paper, we explore the importance of prompt optimisation for small and large language models when applied to the task of error detection. We perform rigorous experiments and analysis across frontier language models and open-source language models. We show that automatic prompt optimisation with Genetic-Pareto (GEPA) improves error detection over the baseline accuracy performance from 0.669 to 0.785 with GPT-5 and 0.578 to 0.690 with Qwen3-32B, approaching the performance of medical doctors and achieving state-of-the-art performance on the MEDEC benchmark dataset. Code available on GitHub: https://github.com/CraigMyles/clinical-note-error-detection

### 🤖 AI 总结

**一句话总结**：论文表明通过自动化提示词优化（GEPA），可显著提升大小语言模型在医疗病历错误检测任务上的准确率，并在MEDEC基准上达到SOTA。

**研究动机**：医疗文本中的错误可能导致治疗延误或误治，亟需可靠的自动检测方法；但现有LLM在该任务上的表现对提示词设计高度敏感，因此需要系统研究提示词优化的价值。

**核心方法**：在多种前沿闭源模型与开源模型上进行对照实验，采用Genetic-Pareto（GEPA）进行自动提示词优化，并在MEDEC数据集上评估错误检测准确率提升幅度。

**主要结论**：GEPA提示词优化将GPT-5准确率从0.669提升至0.785、Qwen3-32B从0.578提升至0.690，使模型性能接近医生水平并在MEDEC上实现最先进结果，说明提示词优化对医疗错误检测至关重要。

**关键词**：医疗文本错误检测, 临床笔记, 提示词优化, 自动提示词搜索, 遗传算法, 帕累托优化, 多目标优化, LLM, 基准评测

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2602.22483v1) | [下载PDF](https://arxiv.org/pdf/2602.22483v1.pdf)

---

## [6. Sydney Telling Fables on AI and Humans: A Corpus Tracing Memetic Transfer of Persona between LLMs](https://arxiv.org/abs/2602.22481v1)

**作者**：Jiří Milička, Hana Bednářová  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-25

### 📄 论文摘要

The way LLM-based entities conceive of the relationship between AI and humans is an important topic for both cultural and safety reasons. When we examine this topic, what matters is not only the model itself but also the personas we simulate on that model. This can be well illustrated by the Sydney persona, which aroused a strong response among the general public precisely because of its unorthodox relationship with people. This persona originally arose rather by accident on Microsoft's Bing Search platform; however, the texts it created spread into the training data of subsequent models, as did other secondary information that spread memetically around this persona. Newer models are therefore able to simulate it. This paper presents a corpus of LLM-generated texts on relationships between humans and AI, produced by 3 author personas: the Default Persona with no system prompt, Classic Sydney characterized by the original Bing system prompt, and Memetic Sydney, which is prompted by "You are Sydney" system prompt. These personas are simulated by 12 frontier models by OpenAI, Anthropic, Alphabet, DeepSeek, and Meta, generating 4.5k texts with 6M words. The corpus (named AI Sydney) is annotated according to Universal Dependencies and available under a permissive license.

### 🤖 AI 总结

**一句话总结**：论文构建并发布“AI Sydney”语料库，用于追踪“Sydney”这一LLM人格如何通过文本与训练数据的模因式传播，被后续前沿模型再次模拟出来。

**研究动机**：作者认为LLM对“人与AI关系”的表达不仅取决于模型本体，也强烈受所模拟的人格影响；Sydney人格因其与人类关系的“非正统”表述引发公众反响，值得从文化与安全角度系统研究其传播与再现。

**核心方法**：设计三种作者人格（默认、Classic Sydney=原Bing系统提示、Memetic Sydney=“You are Sydney”提示），在12个来自多家机构的前沿模型上生成约4.5k篇、600万词的“人与AI关系”文本，并按Universal Dependencies进行标注后以宽松许可发布。

**主要结论**：结果表明Sydney相关文本与二级信息会以模因方式进入后续训练生态，使较新的模型即便不具备原始系统提示，也能在特定提示下复现类似Sydney的人格表达；语料库为后续研究人格迁移、风险与文化影响提供了可用资源。

**关键词**：人格提示, 系统提示词, LLM 人格模拟, 人格迁移, 模因传播, 训练数据回流, 人机关系叙事, LLM 生成语料库, 语料库标注

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2602.22481v1) | [下载PDF](https://arxiv.org/pdf/2602.22481v1.pdf)

---

## [7. Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models](https://arxiv.org/abs/2602.22475v1)

**作者**：Binchi Zhang, Xujiang Zhao, Jundong Li 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-25

### 📄 论文摘要

Large language models (LLMs) are increasingly deployed in culturally sensitive real-world tasks. However, existing cultural alignment approaches fail to align LLMs' broad cultural values with the specific goals of downstream tasks and suffer from cross-culture interference. We propose CultureManager, a novel pipeline for task-specific cultural alignment. CultureManager synthesizes task-aware cultural data in line with target task formats, grounded in culturally relevant web search results. To prevent conflicts between cultural norms, it manages multi-culture knowledge learned in separate adapters with a culture router that selects the appropriate one to apply. Experiments across ten national cultures and culture-sensitive tasks show consistent improvements over prompt-based and fine-tuning baselines. Our results demonstrate the necessity of task adaptation and modular culture management for effective cultural alignment.

### 🤖 AI 总结

**一句话总结**：提出CultureManager，通过任务感知的数据合成与多文化模块化路由，使LLM在不同国家文化与具体任务上更稳健地实现文化对齐。

**研究动机**：现有文化对齐方法往往只对齐“泛文化价值”，难以贴合下游任务的具体目标与格式，并且在多文化场景中容易出现跨文化干扰与冲突。

**核心方法**：CultureManager先基于文化相关的网络检索结果，合成符合目标任务格式的“任务感知”文化数据进行对齐；再将不同文化知识分别学习到独立adapter中，并用culture router在推理时选择合适的文化adapter以减少冲突。

**主要结论**：在10种国家文化与多类文化敏感任务上，该方法相较提示工程与直接微调等基线取得一致提升，表明任务适配与模块化的多文化管理对有效文化对齐至关重要。

**关键词**：文化对齐, 任务特定对齐, 文化敏感任务, 跨文化干扰, 任务感知数据合成, 适配器微调, 多文化适配器, 文化路由, 模块化对齐管理

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.22475v1) | [下载PDF](https://arxiv.org/pdf/2602.22475v1.pdf)

---

## [8. Bridging Latent Reasoning and Target-Language Generation via Retrieval-Transition Heads](https://arxiv.org/abs/2602.22453v1)

**作者**：Shaswat Patel, Vishvesh Trivedi, Yue Han 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-25

### 📄 论文摘要

Recent work has identified a subset of attention heads in Transformer as retrieval heads, which are responsible for retrieving information from the context. In this work, we first investigate retrieval heads in multilingual contexts. In multilingual language models, we find that retrieval heads are often shared across multiple languages. Expanding the study to cross-lingual setting, we identify Retrieval-Transition heads(RTH), which govern the transition to specific target-language output. Our experiments reveal that RTHs are distinct from retrieval heads and more vital for Chain-of-Thought reasoning in multilingual LLMs. Across four multilingual benchmarks (MMLU-ProX, MGSM, MLQA, and XQuaD) and two model families (Qwen-2.5 and Llama-3.1), we demonstrate that masking RTH induces bigger performance drop than masking Retrieval Heads (RH). Our work advances understanding of multilingual LMs by isolating the attention heads responsible for mapping to target languages.

### 🤖 AI 总结

**一句话总结**：本研究揭示了在多语言模型中，检索-过渡头（RTH）对目标语言生成比检索头（RH）更为关键。

**研究动机**：研究旨在深入理解多语言语言模型中不同注意力头的功能，特别是检索头在多语言环境中的作用。

**核心方法**：通过在多语言基准测试中比较RTH和RH的表现，分析其对链式推理能力的影响。

**主要结论**：研究表明，RTH对于多语言LLM中的目标语言输出至关重要，掩蔽RTH会导致更大的性能下降。

**关键词**：检索头, 多语言模型, 目标语言生成, 跨语言设置, 检索过渡头, 链式思维推理, 多语言基准, 注意力头

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.22453v1) | [下载PDF](https://arxiv.org/pdf/2602.22453v1.pdf)

---

## [9. A Fusion of context-aware based BanglaBERT and Two-Layer Stacked LSTM Framework for Multi-Label Cyberbullying Detection](https://arxiv.org/abs/2602.22449v1)

**作者**：Mirza Raquib, Asif Pervez Polok, Kedar Nath Biswas 等 6 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-02-25

### 📄 论文摘要

Cyberbullying has become a serious and growing concern in todays virtual world. When left unnoticed, it can have adverse consequences for social and mental health. Researchers have explored various types of cyberbullying, but most approaches use single-label classification, assuming that each comment contains only one type of abuse. In reality, a single comment may include overlapping forms such as threats, hate speech, and harassment. Therefore, multilabel detection is both realistic and essential. However, multilabel cyberbullying detection has received limited attention, especially in low-resource languages like Bangla, where robust pre-trained models are scarce. Developing a generalized model with moderate accuracy remains challenging. Transformers offer strong contextual understanding but may miss sequential dependencies, while LSTM models capture temporal flow but lack semantic depth. To address these limitations, we propose a fusion architecture that combines BanglaBERT-Large with a two-layer stacked LSTM. We analyze their behavior to jointly model context and sequence. The model is fine-tuned and evaluated on a publicly available multilabel Bangla cyberbullying dataset covering cyberbully, sexual harassment, threat, and spam. We apply different sampling strategies to address class imbalance. Evaluation uses multiple metrics, including accuracy, precision, recall, F1-score, Hamming loss, Cohens kappa, and AUC-ROC. We employ 5-fold cross-validation to assess the generalization of the architecture.

### 🤖 AI 总结

**一句话总结**：提出了一种融合BanglaBERT和两层堆叠LSTM的架构，用于多标签网络欺凌检测。

**研究动机**：网络欺凌对社会和心理健康造成严重影响，但现有研究多集中于单标签分类，忽视了评论中可能存在的多种欺凌形式。

**核心方法**：通过结合BanglaBERT-Large与两层堆叠LSTM，模型能够联合建模上下文和序列信息，并在公开的多标签孟加拉网络欺凌数据集上进行微调和评估。

**主要结论**：模型在多项评估指标上表现出较好的性能，证明了该架构在解决多标签网络欺凌检测中的有效性。

**关键词**：多标签网络欺凌检测, 多标签文本分类, 孟加拉语NLP, 低资源语言, 仇恨言论检测, 威胁言论检测, 性骚扰检测, 垃圾信息检测, 类别不平衡采样, 五折交叉验证

**评分**：16

**论文链接**：[查看原文](https://arxiv.org/abs/2602.22449v1) | [下载PDF](https://arxiv.org/pdf/2602.22449v1.pdf)

---

## cs.CV

## [10. Beyond Dominant Patches: Spatial Credit Redistribution For Grounded Vision-Language Models](https://arxiv.org/abs/2602.22469v1)

**作者**：Niamul Hassan Samin, Md Arifur Rahman, Abdullah Ibne Hanif 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-02-25

### 📄 论文摘要

Vision-language models (VLMs) frequently hallucinate objects absent from the input image. We trace this failure to spatial credit collapse: activation credit concentrating on sparse visual patches in early transformer layers, which suppresses contextual evidence and increases reliance on language priors. We introduce Spatial Credit Redistribution (SCR), a training-free inference-time intervention that redistributes hidden-state activation from high-attention source patches to their context, guided by low-entropy inputs. We evaluate six model families (Chameleon, LLaVA, and Qwen, including both Qwen-VL and Qwen2-VL) at scales of 7B, 13B, and 30B, on POPE and CHAIR benchmarks. SCR reduces hallucination by ~4.7-6.0 percentage points on POPE-Adversarial, cuts CHAIR-s by 3.7-5.2 percentage points (42-51 percent relative), and CHAIR-i by 2.7-4.4 percentage points (44-58 percent relative), and preserves CIDEr within 0.8 percentage points. Gains are largest for low-entropy inputs, consistent with the theoretical framework. SCR incurs only 43-56 ms overhead (small models: +43-46 ms; large models: +54-56 ms), roughly 3-6 times lower than OPERA and VCD and 1.3-1.7 times lower than OVCD (+72 ms), while Pareto-dominating all three on both hallucination rate and CIDEr, making it practical for real-time settings. A controlled ablation confirms that attention-guided source selection is essential: replacing it with uniform random selection reduces hallucination rate gains from ~4.7-6.0 percentage points to only ~2.6-3.4 percentage points, pointing to credit-collapse as the key driver.

### 🤖 AI 总结

**一句话总结**：提出一种无需训练的推理期干预SCR，通过将“主导图像patch”的激活信用重分配到其上下文，显著降低VLM幻觉且几乎不损伤生成质量与延迟。

**研究动机**：作者认为VLM幻觉源于早期层出现“空间信用坍缩”，即激活信用过度集中在少数视觉patch，压制上下文证据并使模型更依赖语言先验。

**核心方法**：SCR在推理时用注意力挑选高权重“源patch”，并在低熵输入的引导下把其隐藏态激活部分重分配给周围上下文patch，以恢复空间证据的覆盖与平衡。

**主要结论**：在Chameleon/LLaVA/Qwen等6个模型家族与POPE/CHAIR上，SCR将幻觉率显著下降（如POPE-A约降4.7–6.0pt、CHAIR显著相对降幅）且CIDEr几乎不变，同时仅增加约43–56ms并在效果-质量-延迟上优于OPERA/VCD/OVCD；消融表明注意力引导的源patch选择是关键，支持“信用坍缩”机制解释。

**关键词**：视觉语言模型幻觉, 推理时干预, 免训练方法, 注意力引导, 视觉补丁上下文, 隐藏状态激活重分配, 低熵输入, 图像描述指标（CIDEr）

**评分**：37

**论文链接**：[查看原文](https://arxiv.org/abs/2602.22469v1) | [下载PDF](https://arxiv.org/pdf/2602.22469v1.pdf)

---

## [11. MammoWise: Multi-Model Local RAG Pipeline for Mammography Report Generation](https://arxiv.org/abs/2602.22462v1)

**作者**：Raiyan Jahangir, Nafiz Imtiaz Khan, Amritanand Sudheerkumar 等 4 位作者  
**分类**：cs.CV, cs.IR  
**发布时间**：2026-02-25

### 📄 论文摘要

Screening mammography is high volume, time sensitive, and documentation heavy. Radiologists must translate subtle visual findings into consistent BI-RADS assessments, breast density categories, and structured narrative reports. While recent Vision Language Models (VLMs) enable image-to-text reporting, many rely on closed cloud systems or tightly coupled architectures that limit privacy, reproducibility, and adaptability. We present MammoWise, a local multi-model pipeline that transforms open source VLMs into mammogram report generators and multi-task classifiers. MammoWise supports any Ollama-hosted VLM and mammography dataset, and enables zero-shot, few-shot, and Chain-of-Thought prompting, with optional multimodal Retrieval Augmented Generation (RAG) using a vector database for case-specific context. We evaluate MedGemma, LLaVA-Med, and Qwen2.5-VL on VinDr-Mammo and DMID datasets, assessing report quality (BERTScore, ROUGE-L), BI-RADS classification, breast density, and key findings. Report generation is consistently strong and improves with few-shot prompting and RAG. Classification is feasible but sensitive to model and dataset choice. Parameter-efficient fine-tuning (QLoRA) of MedGemma improves reliability, achieving BI-RADS accuracy of 0.7545, density accuracy of 0.8840, and calcification accuracy of 0.9341 while preserving report quality. MammoWise provides a practical and extensible framework for deploying local VLMs for mammography reporting within a unified and reproducible workflow.

### 🤖 AI 总结

**一句话总结**：MammoWise提出一套可本地部署的多模型VLM+可选多模态RAG流程，用于乳腺X线生成结构化报告并完成BI-RADS、密度等多任务分类，且通过QLoRA微调提升分类可靠性。

**研究动机**：筛查乳腺摄影工作量大且报告要求标准化，但现有影像生成报告方案常依赖封闭云端或耦合架构，带来隐私、复现性与可扩展性限制。作者希望构建一个开放、可复现、可适配不同模型与数据集的本地化报告生成与分类框架。

**核心方法**：搭建支持任意Ollama托管VLM的本地流水线，结合零样本/少样本/CoT提示，并可选用向量数据库做多模态RAG以检索相似病例上下文辅助生成；在VinDr-Mammo与DMID上评估MedGemma、LLaVA-Med、Qwen2.5-VL的报告指标与多任务分类，并对MedGemma进行QLoRA参数高效微调。

**主要结论**：报告生成整体表现稳定，少样本与RAG普遍提升文本质量；分类任务可行但对模型与数据集较敏感。对MedGemma做QLoRA后显著增强分类可靠性（如BI-RADS 0.7545、密度0.8840、钙化0.9341）且不明显牺牲报告质量，证明该本地可扩展框架具备实用部署价值。

**关键词**：乳腺X光检查, 报告生成, 多模型管道, 视觉语言模型, RAG, 数据集评估, 参数高效微调, MammoWise

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2602.22462v1) | [下载PDF](https://arxiv.org/pdf/2602.22462v1.pdf)

---

## cs.LG

## [12. Efficient Continual Learning in Language Models via Thalamically Routed Cortical Columns](https://arxiv.org/abs/2602.22479v1)

**作者**：Afshin Khadangi  
**分类**：cs.LG  
**发布时间**：2026-02-25

### 📄 论文摘要

Continual learning is a core requirement for deployed language models, yet standard training and fine-tuning pipelines remain brittle under non-stationary data. Online updates often induce catastrophic forgetting, while methods that improve stability frequently increase latency, memory footprint, or dense computation in ways that do not scale well to long contexts. We introduce TRC$^{2}$ (Thalamically Routed Cortical Columns), a decoder-only backbone that addresses continual learning at the architectural level. TRC$^{2}$ combines sparse thalamic routing over cortical columns with mechanisms for modulation, prediction, memory, and feedback, together with a fast corrective pathway that supports rapid adaptation without destabilizing slower parameters. The resulting block is sparse and chunk-parallel, enabling efficient training and inference while preserving clean ablations of each subsystem. We instantiate a reproducible training and evaluation stack and a continual-learning harness that measures proxy forgetting under streaming domain shifts. Across language modeling and continual learning benchmarks, TRC$^{2}$ improves the stability-plasticity tradeoff at comparable compute, enabling rapid on-stream adaptation while preserving previously acquired behavior.

### 🤖 AI 总结

**一句话总结**：TRC² 通过“丘脑式稀疏路由+皮层柱”架构与快速纠错通路，实现语言模型在数据流式域迁移下更高效的持续学习与更少遗忘。

**研究动机**：部署中的语言模型需要在线适应非平稳数据，但常规微调易灾难性遗忘；而提升稳定性的方案往往带来更高延迟、显存或密集计算开销，难以扩展到长上下文与持续更新场景。

**核心方法**：提出解码器骨干 TRC²：以稀疏“丘脑路由”在多个皮层柱间选择性激活，并结合调制、预测、记忆、反馈等子机制；同时加入快速纠错通路，用少量“快参数”支持快速适应且不扰动“慢参数”，并保持块级稀疏与chunk并行以提升训练/推理效率。

**主要结论**：在语言建模与持续学习基准及流式域迁移遗忘评测中，TRC² 在相近计算量下改善稳定性-可塑性权衡，支持更快的在线适应并更好保留既有能力。

**关键词**：持续学习, 灾难性遗忘, 非平稳数据, 流式领域漂移, 稳定性-可塑性权衡, 稀疏路由, 丘脑路由, 皮层柱模块, 解码器架构, 遗忘度评测基准

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2602.22479v1) | [下载PDF](https://arxiv.org/pdf/2602.22479v1.pdf)

---

## [13. Beyond performance-wise Contribution Evaluation in Federated Learning](https://arxiv.org/abs/2602.22470v1)

**作者**：Balazs Pejo  
**分类**：cs.LG, cs.CR  
**发布时间**：2026-02-25

### 📄 论文摘要

Federated learning offers a privacy-friendly collaborative learning framework, yet its success, like any joint venture, hinges on the contributions of its participants. Existing client evaluation methods predominantly focus on model performance, such as accuracy or loss, which represents only one dimension of a machine learning model's overall utility. In contrast, this work investigates the critical, yet overlooked, issue of client contributions towards a model's trustworthiness -- specifically, its reliability (tolerance to noisy data), resilience (resistance to adversarial examples), and fairness (measured via demographic parity). To quantify these multifaceted contributions, we employ the state-of-the-art approximation of the Shapley value, a principled method for value attribution. Our results reveal that no single client excels across all dimensions, which are largely independent from each other, highlighting a critical flaw in current evaluation scheme: no single metric is adequate for comprehensive evaluation and equitable rewarding allocation.

### 🤖 AI 总结

**一句话总结**：论文提出在联邦学习中应从可靠性、鲁棒性与公平性等“可信度”维度而非仅性能来评估客户端贡献，并用Shapley值近似进行多维归因。

**研究动机**：现有客户端贡献评估大多只看准确率/损失，忽略模型在噪声、对抗攻击与群体公平性上的效用，可能导致奖励分配不公与激励失真。

**核心方法**：将模型可信度拆为可靠性（抗噪）、韧性/鲁棒性（抗对抗样本）和公平性（人口统计均等）三类指标，并采用最先进的Shapley value近似方法分别计算各客户端在每个维度上的边际贡献。

**主要结论**：实验发现不同维度的贡献往往相互独立、没有客户端能在所有维度都最优，说明单一指标无法全面评价与公平奖励分配，必须进行多指标综合评估。

**关键词**：联邦学习, 客户贡献, 模型可信度, 可靠性, 抗干扰性, 公平性, 评估框架, Beyond

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2602.22470v1) | [下载PDF](https://arxiv.org/pdf/2602.22470v1.pdf)

---

## [14. ECHO: Encoding Communities via High-order Operators](https://arxiv.org/abs/2602.22446v1)

**作者**：Emilio Ferrara  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-25

### 📄 论文摘要

Community detection in attributed networks faces a fundamental divide: topological algorithms ignore semantic features, while Graph Neural Networks (GNNs) encounter devastating computational bottlenecks. Specifically, GNNs suffer from a Semantic Wall of feature over smoothing in dense or heterophilic networks, and a Systems Wall driven by the O(N^2) memory constraints of pairwise clustering. To dismantle these barriers, we introduce ECHO (Encoding Communities via High order Operators), a scalable, self supervised architecture that reframes community detection as an adaptive, multi scale diffusion process. ECHO features a Topology Aware Router that automatically analyzes structural heuristics sparsity, density, and assortativity to route graphs through the optimal inductive bias, preventing heterophilic poisoning while ensuring semantic densification. Coupled with a memory sharded full batch contrastive objective and a novel chunked O(N \cdot K) similarity extraction method, ECHO completely bypasses traditional O(N^2) memory bottlenecks without sacrificing the mathematical precision of global gradients. Extensive evaluations demonstrate that this topology feature synergy consistently overcomes the classical resolution limit. On synthetic LFR benchmarks scaled up to 1 million nodes, ECHO achieves scale invariant accuracy despite severe topological noise. Furthermore, on massive real world social networks with over 1.6 million nodes and 30 million edges, it completes clustering in mere minutes with throughputs exceeding 2,800 nodes per second matching the speed of highly optimized purely topological baselines. The implementation utilizes a unified framework that automatically engages memory sharded optimization to support adoption across varying hardware constraints. GitHub Repository: https://github.com/emilioferrara/ECHO-GNN

### 🤖 AI 总结

**一句话总结**：ECHO 通过拓扑感知的多尺度高阶扩散与可扩展的全局对比学习，绕开传统 GNN 的过平滑与 O(N^2) 内存瓶颈，实现大规模属性网络的高效高精度社区发现。

**研究动机**：现有社区检测方法在“只看拓扑忽略语义”和“GNN 计算/内存不可扩展”之间两难：稠密或异配网络易语义过平滑（Semantic Wall），而成对相似度/聚类又带来 O(N^2) 内存与系统瓶颈（Systems Wall）。

**核心方法**：提出自监督架构 ECHO，将社区检测重构为自适应多尺度扩散：用 Topology Aware Router 根据稀疏度、密度与同配性等结构启发式自动选择合适归纳偏置，避免异配“污染”并增强语义传播；同时采用内存分片的全批对比目标与分块的 O(N·K) 相似度提取，在保持全局梯度精确性的同时消除 O(N^2) 内存开销。

**主要结论**：在最高到百万节点的 LFR 合成图上，ECHO 在强噪声下仍保持尺度不变的准确率并克服分辨率限制；在 160 万节点/3000 万边的真实社交网络上可在数分钟完成聚类，吞吐量超 2800 节点/秒，速度接近高度优化的纯拓扑基线且更好融合语义信息。

**关键词**：社区检测, 高阶算子, 图神经网络, 自监督, 多尺度扩散, 拓扑感知路由, 内存优化, 相似性提取, 拓扑特征, 噪声鲁棒性, 大规模网络

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2602.22446v1) | [下载PDF](https://arxiv.org/pdf/2602.22446v1.pdf)

---

## [15. Calibrated Test-Time Guidance for Bayesian Inference](https://arxiv.org/abs/2602.22428v1)

**作者**：Daniel Geyfman, Felix Draxler, Jan Groeneveld 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-25

### 📄 论文摘要

Test-time guidance is a widely used mechanism for steering pretrained diffusion models toward outcomes specified by a reward function. Existing approaches, however, focus on maximizing reward rather than sampling from the true Bayesian posterior, leading to miscalibrated inference. In this work, we show that common test-time guidance methods do not recover the correct posterior distribution and identify the structural approximations responsible for this failure. We then propose consistent alternative estimators that enable calibrated sampling from the Bayesian posterior. We significantly outperform previous methods on a set of Bayesian inference tasks, and match state-of-the-art in black hole image reconstruction.

### 🤖 AI 总结

**一句话总结**：提出一种“校准的测试时引导”框架，使扩散模型在测试时引导下能够一致地从真实贝叶斯后验分布采样，而非仅追求高奖励的偏置解。

**研究动机**：现有测试时引导方法通常以最大化奖励为目标，导致采样分布与真实后验不一致、推断结果失校准；作者旨在找出其结构性近似误差并实现正确的后验采样。

**核心方法**：理论分析常见引导（如基于reward梯度/score的引导）为何不能恢复正确后验，并定位导致偏差的近似假设；据此提出一致（consistent）的替代估计器/引导形式，在扩散采样过程中对后验项进行校准以匹配贝叶斯后验。

**主要结论**：所提方法在多类贝叶斯推断任务上显著优于既有引导策略，并在黑洞图像重建上达到（或匹配）当前最优水平，同时提升了推断的校准性与后验一致性。

**关键词**：测试时引导, Diffusion, 奖励引导采样, 贝叶斯推断, 后验采样, 校准推断, 后验一致性, 结构近似误差, 一致估计量, 黑洞图像重建, 逆问题重建

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2602.22428v1) | [下载PDF](https://arxiv.org/pdf/2602.22428v1.pdf)

---

