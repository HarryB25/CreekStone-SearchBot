# arXiv AI 论文日报 | 2026-02-02

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (7 篇)
- [cs.CV](#csCV) (6 篇)
- [cs.LG](#csLG) (10 篇)
- [cs.AI](#csAI) (7 篇)

---

## cs.AI

## [1. AgentRx: Diagnosing AI Agent Failures from Execution Trajectories](https://arxiv.org/abs/2602.02475v1)

**作者**：Shraddha Barke, Arnav Goyal, Alind Khare 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-02

### 📄 论文摘要

AI agents often fail in ways that are difficult to localize because executions are probabilistic, long-horizon, multi-agent, and mediated by noisy tool outputs. We address this gap by manually annotating failed agent runs and release a novel benchmark of 115 failed trajectories spanning structured API workflows, incident management, and open-ended web/file tasks. Each trajectory is annotated with a critical failure step and a category from a grounded-theory derived, cross-domain failure taxonomy. To mitigate the human cost of failure attribution, we present AGENTRX, an automated domain-agnostic diagnostic framework that pinpoints the critical failure step in a failed agent trajectory. It synthesizes constraints, evaluates them step-by-step, and produces an auditable validation log of constraint violations with associated evidence; an LLM-based judge uses this log to localize the critical step and category. Our framework improves step localization and failure attribution over existing baselines across three domains.

### 🤖 AI 总结

**一句话总结**：本文提出了一种名为AGENTRX的框架，用于自动诊断AI代理执行中的失败步骤，并通过115个失败轨迹的基准数据集进行验证。

**研究动机**：AI代理在执行过程中常常难以定位失败原因，因此需要一个有效的诊断工具来辅助识别失败步骤。

**核心方法**：AGENTRX通过手动注释失败轨迹，利用约束合成和逐步评估的方法，生成可审核的验证日志，并通过基于LLM的判断来定位关键失败步骤。

**主要结论**：AGENTRX在三个领域中相较于现有基线显著提高了失败步骤的定位和归因准确性。

**关键词**：关键词：agent, autonomous, multi-agent, 失败诊断, 执行轨迹, LLM, AGENTRX, 自动化框架, 约束评估, 关键失败步骤

**评分**：75

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02475v1) | [下载PDF](https://arxiv.org/pdf/2602.02475v1.pdf)

---

## [2. Breaking the Reversal Curse in Autoregressive Language Models via Identity Bridge](https://arxiv.org/abs/2602.02470v1)

**作者**：Xutao Ma, Yixiao Huang, Hanlin Zhu 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-02

### 📄 论文摘要

Autoregressive large language models (LLMs) have achieved remarkable success in many complex tasks, yet they can still fail in very simple logical reasoning such as the "reversal curse" -- when trained on forward knowledge data of the form "$A \rightarrow B$" (e.g., Alice's husband is Bob), the model is unable to deduce the reversal knowledge "$B \leftarrow A$" (e.g., Bob's wife is Alice) during test. Extensive prior research suggests that this failure is an inherent, fundamental limit of autoregressive causal LLMs, indicating that these models tend to memorize factual-level knowledge rather than capture higher-level rules. In this paper, we challenge this view by showing that this seemingly fundamental limit can be mitigated by slightly tweaking the training data with a simple regularization data recipe called the Identity Bridge of the form "$A \to A$" (e.g., The name of Alice is Alice). Theoretically, we prove that under this recipe, even a one-layer transformer can break the reversal curse by analyzing the implicit bias of gradient descent. Empirically, we show that a 1B pretrained language model finetuned with the proposed data recipe achieves a 40% success rate on reversal tasks, in stark contrast to a near-zero success rate when trained solely on forward-knowledge data. Our work provides a novel theoretical foundation for the reversal curse and offers a principled, low-cost path to encouraging LLMs to learn higher-level rules from data.

### 🤖 AI 总结

**一句话总结**：通过引入身份桥数据，作者提出了一种方法来缓解自回归语言模型中的反转诅咒现象，使其能够更好地进行简单的逻辑推理。

**研究动机**：自回归大型语言模型在复杂任务中表现优异，但在简单逻辑推理方面仍存在固有限制，特别是在反转知识推理上。

**核心方法**：作者提出了一种名为身份桥的正则化数据策略，通过在训练数据中添加形式为'A -> A'的示例，来改善模型的推理能力。

**主要结论**：实验表明，经过身份桥训练的语言模型在反转任务上成功率达到40%，而仅使用前向知识训练时成功率接近零，验证了该方法的有效性。

**关键词**：自回归, 语言模型, 大语言模型, LLM, 逆转诅咒, 训练数据, 身份桥, transformer, 逻辑推理, 预训练模型

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02470v1) | [下载PDF](https://arxiv.org/pdf/2602.02470v1.pdf)

---

## [3. Avenir-Web: Human-Experience-Imitating Multimodal Web Agents with Mixture of Grounding Experts](https://arxiv.org/abs/2602.02468v1)

**作者**：Aiden Yiliu Li, Xinyue Hao, Shilong Liu 等 4 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-02-02

### 📄 论文摘要

Despite advances in multimodal large language models, autonomous web agents still struggle to reliably execute long-horizon tasks on complex and dynamic web interfaces. Existing agents often suffer from inaccurate element grounding, the absence of site-specific procedural knowledge, and unstable long-term task tracking and memory, particularly when operating over complex Document Object Model structures. To address these limitations, we introduce Avenir-Web, a web agent that achieves a new open-source state of the art on the Online-Mind2Web benchmark in real-world deployment. Avenir-Web leverages a Mixture of Grounding Experts, Experience-Imitation Planning for incorporating procedural priors, and a task-tracking checklist combined with adaptive memory to enable robust and seamless interaction across diverse user interface paradigms. We evaluate Avenir-Web on Online-Mind2Web, a rigorous benchmark of live and user-centered web tasks. Our results demonstrate that Avenir-Web significantly surpasses prior open-source agents and attains performance parity with top-tier proprietary models, thereby establishing a new open-source state of the art for reliable web agents on live websites.

### 🤖 AI 总结

**一句话总结**：Avenir-Web 是一种新型的多模态网络代理，能够在复杂网站上可靠地执行长任务，超过了现有开源代理的表现。

**研究动机**：尽管多模态大语言模型有所进展，但自主网络代理在复杂动态网页界面上执行长时间任务时仍面临多种挑战。

**核心方法**：Avenir-Web 结合了多种基础专家、经验模仿规划和任务跟踪清单，以提高在不同用户界面上的交互能力。

**主要结论**：Avenir-Web 在 Online-Mind2Web 基准测试中显著超越了之前的开源代理，并与顶尖专有模型达到了性能平衡，创造了新的开源标准。

**关键词**：多模态, 网络代理, 自主代理, 任务跟踪, 经验模仿规划, 程序知识, 用户界面, 适应性记忆, 复杂模型, 生成模型, ml

**评分**：76

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02468v1) | [下载PDF](https://arxiv.org/pdf/2602.02468v1.pdf)

---

## [4. Drift-Bench: Diagnosing Cooperative Breakdowns in LLM Agents under Input Faults via Multi-Turn Interaction](https://arxiv.org/abs/2602.02455v1)

**作者**：Han Bao, Zheyuan Zhang, Pengcheng Jing 等 6 位作者  
**分类**：cs.AI, cs.CL, cs.SE  
**发布时间**：2026-02-02

### 📄 论文摘要

As Large Language Models transition to autonomous agents, user inputs frequently violate cooperative assumptions (e.g., implicit intent, missing parameters, false presuppositions, or ambiguous expressions), creating execution risks that text-only evaluations do not capture. Existing benchmarks typically assume well-specified instructions or restrict evaluation to text-only, single-turn clarification, and thus do not measure multi-turn disambiguation under grounded execution risk. We introduce \textbf{Drift-Bench}, the first diagnostic benchmark that evaluates agentic pragmatics under input faults through multi-turn clarification across state-oriented and service-oriented execution environments. Grounded in classical theories of communication, \textbf{Drift-Bench} provides a unified taxonomy of cooperative breakdowns and employs a persona-driven user simulator with the \textbf{Rise} evaluation protocol. Experiments show substantial performance drops under these faults, with clarification effectiveness varying across user personas and fault types. \MethodName bridges clarification research and agent safety evaluation, enabling systematic diagnosis of failures that can lead to unsafe executions.

### 🤖 AI 总结

**一句话总结**：Drift-Bench是一个新基准，用于评估大语言模型在输入故障下的合作性崩溃，通过多轮互动进行诊断。

**研究动机**：随着大语言模型向自主代理转型，用户输入常常违背合作假设，因此需要一个能够捕获多轮澄清的评估工具，以降低执行风险。

**核心方法**：Drift-Bench结合经典通信理论，提供了合作崩溃的统一分类，并采用基于角色的用户模拟器和Rise评估协议进行实验。

**主要结论**：实验表明，在输入故障下，模型性能显著下降，澄清效果因用户角色和故障类型而异，揭示了确保安全执行的系统性诊断需求。

**关键词**：关键词：大语言模型, 自主代理, 多轮交互, 协作失效, Drift-Bench, 代理安全评估, 语义搜索, 用户模拟器, Clarification, llm

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02455v1) | [下载PDF](https://arxiv.org/pdf/2602.02455v1.pdf)

---

## [5. Thinking with Comics: Enhancing Multimodal Reasoning through Structured Visual Storytelling](https://arxiv.org/abs/2602.02453v1)

**作者**：Andong Chen, Wenxin Zhu, Qiuyu Ding 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-02

### 📄 论文摘要

Chain-of-Thought reasoning has driven large language models to extend from thinking with text to thinking with images and videos. However, different modalities still have clear limitations: static images struggle to represent temporal structure, while videos introduce substantial redundancy and computational cost. In this work, we propose Thinking with Comics, a visual reasoning paradigm that uses comics as a high information-density medium positioned between images and videos. Comics preserve temporal structure, embedded text, and narrative coherence while requiring significantly lower reasoning cost. We systematically study two reasoning paths based on comics and evaluate them on a range of reasoning tasks and long-context understanding tasks. Experimental results show that Thinking with Comics outperforms Thinking with Images on multi-step temporal and causal reasoning tasks, while remaining substantially more efficient than Thinking with Video. Further analysis indicates that different comic narrative structures and styles consistently affect performance across tasks, suggesting that comics serve as an effective intermediate visual representation for improving multimodal reasoning.

### 🤖 AI 总结

**一句话总结**：本研究提出通过漫画增强多模态推理，称为Thinking with Comics，展示了其在推理任务中的优势。

**研究动机**：随着多模态推理的发展，现有的图像和视频在时间结构和计算效率上存在局限，因此需要一个更有效的视觉表达媒介。

**核心方法**：我们提出一种新的推理范式，利用漫画作为信息密度高的媒介，系统研究基于漫画的两种推理路径，并在多个推理任务上进行评估。

**主要结论**：实验结果表明，Thinking with Comics在多步时间和因果推理任务中优于Thinking with Images，同时在效率上显著优于Thinking with Video，且漫画叙事结构影响性能。

**关键词**：多模态推理, 视觉叙事, 思维链, 信息密度, 时间结构, 任务评估, 认知效率, 漫画, reasoning, multimodal, comics, temporal structure, narrative coherence, reasoning tasks, context

**评分**：75

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02453v1) | [下载PDF](https://arxiv.org/pdf/2602.02453v1.pdf)

---

## [6. SafeGround: Know When to Trust GUI Grounding Models via Uncertainty Calibration](https://arxiv.org/abs/2602.02419v1)

**作者**：Qingni Wang, Yue Fan, Xin Eric Wang  
**分类**：cs.AI, cs.SE  
**发布时间**：2026-02-02

### 📄 论文摘要

Graphical User Interface (GUI) grounding aims to translate natural language instructions into executable screen coordinates, enabling automated GUI interaction. Nevertheless, incorrect grounding can result in costly, hard-to-reverse actions (e.g., erroneous payment approvals), raising concerns about model reliability. In this paper, we introduce SafeGround, an uncertainty-aware framework for GUI grounding models that enables risk-aware predictions through calibrations before testing. SafeGround leverages a distribution-aware uncertainty quantification method to capture the spatial dispersion of stochastic samples from outputs of any given model. Then, through the calibration process, SafeGround derives a test-time decision threshold with statistically guaranteed false discovery rate (FDR) control. We apply SafeGround on multiple GUI grounding models for the challenging ScreenSpot-Pro benchmark. Experimental results show that our uncertainty measure consistently outperforms existing baselines in distinguishing correct from incorrect predictions, while the calibrated threshold reliably enables rigorous risk control and potentials of substantial system-level accuracy improvements. Across multiple GUI grounding models, SafeGround improves system-level accuracy by up to 5.38\% percentage points over Gemini-only inference.

### 🤖 AI 总结

**一句话总结**：SafeGround是一个不确定性意识框架，通过校准提高GUI定位模型的可靠性和风险控制能力。

**研究动机**：GUI定位将自然语言指令转化为可执行的屏幕坐标，但错误的定位可能导致严重后果，因此需要提高模型的可靠性。

**核心方法**：SafeGround利用分布感知的不确定性量化方法，通过校准过程在测试时确定具有统计保证的决策阈值，以控制虚假发现率（FDR）。

**主要结论**：实验结果表明，SafeGround在多个GUI定位模型上显著提高了系统级准确性，达到5.38%的提升，并有效区分了正确与错误的预测。

**关键词**：GUI, grounding, 不确定性校准, 风险感知, 预测模型, 自动化交互, 统计控制, 模型可靠性, ScreenSpot-Pro, rag

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02419v1) | [下载PDF](https://arxiv.org/pdf/2602.02419v1.pdf)

---

## [7. Structure Enables Effective Self-Localization of Errors in LLMs](https://arxiv.org/abs/2602.02416v1)

**作者**：Ankur Samanta, Akshayaa Magesh, Ayush Jain 等 11 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-02

### 📄 论文摘要

Self-correction in language models remains elusive. In this work, we explore whether language models can explicitly localize errors in incorrect reasoning, as a path toward building AI systems that can effectively correct themselves. We introduce a prompting method that structures reasoning as discrete, semantically coherent thought steps, and show that models are able to reliably localize errors within this structure, while failing to do so in conventional, unstructured chain-of-thought reasoning. Motivated by how the human brain monitors errors at discrete decision points and resamples alternatives, we introduce Iterative Correction Sampling of Thoughts (Thought-ICS), a self-correction framework. Thought-ICS iteratively prompts the model to generate reasoning one discrete and complete thought at a time--where each thought represents a deliberate decision by the model--creating natural boundaries for precise error localization. Upon verification, the model localizes the first erroneous step, and the system backtracks to generate alternative reasoning from the last correct point. When asked to correct reasoning verified as incorrect by an oracle, Thought-ICS achieves 20-40% self-correction lift. In a completely autonomous setting without external verification, it outperforms contemporary self-correction baselines.

### 🤖 AI 总结

**一句话总结**：本研究提出了一种结构化推理方法，帮助大型语言模型有效定位和自我纠正错误。

**研究动机**：研究旨在探索语言模型是否能够明确定位推理中的错误，以构建能够有效自我纠正的AI系统。

**核心方法**：引入迭代纠正思维（Thought-ICS）框架，通过结构化的思维步骤生成推理，以便模型在错误检测时能够更精确地定位问题。

**主要结论**：在验证错误的情况下，Thought-ICS实现了20-40%的自我纠正提升，并在无外部验证的完全自主设置中优于现有自我纠正基准。

**关键词**：自我纠错, 语言模型, 思维步骤, 结构化推理, 错误定位, Thought-ICS, 自主学习, 迭代采样, 深度学习, 神经网络, llm

**评分**：76

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02416v1) | [下载PDF](https://arxiv.org/pdf/2602.02416v1.pdf)

---

## cs.CL

## [8. Reward-free Alignment for Conflicting Objectives](https://arxiv.org/abs/2602.02495v1)

**作者**：Peter Chen, Xiaopeng Li, Xi Chen 等 4 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-02-02

### 📄 论文摘要

Direct alignment methods are increasingly used to align large language models (LLMs) with human preferences. However, many real-world alignment problems involve multiple conflicting objectives, where naive aggregation of preferences can lead to unstable training and poor trade-offs. In particular, weighted loss methods may fail to identify update directions that simultaneously improve all objectives, and existing multi-objective approaches often rely on explicit reward models, introducing additional complexity and distorting user-specified preferences. The contributions of this paper are two-fold. First, we propose a Reward-free Alignment framework for Conflicted Objectives (RACO) that directly leverages pairwise preference data and resolves gradient conflicts via a novel clipped variant of conflict-averse gradient descent. We provide convergence guarantees to Pareto-critical points that respect user-specified objective weights, and further show that clipping can strictly improve convergence rate in the two-objective setting. Second, we improve our method using some heuristics and conduct experiments to demonstrate the compatibility of the proposed framework for LLM alignment. Both qualitative and quantitative evaluations on multi-objective summarization and safety alignment tasks across multiple LLM families (Qwen 3, Llama 3, Gemma 3) show that our method consistently achieves better Pareto trade-offs compared to existing multi-objective alignment baselines.

### 🤖 AI 总结

**一句话总结**：提出了一种无奖励的对齐框架RACO，旨在解决多目标冲突的对齐问题，提升大语言模型的用户偏好对齐效果。

**研究动机**：现有的对齐方法在处理多重冲突目标时常导致训练不稳定和较差的权衡，亟需新的方法以更好地解决这些问题。

**核心方法**：RACO框架利用成对偏好数据，通过一种新颖的冲突厌恶梯度下降的剪切变体来解决梯度冲突，并提供了收敛性保证。

**主要结论**：实验表明，RACO在多目标总结和安全对齐任务中，相较于现有基线方法，能实现更优的Pareto权衡。

**关键词**：奖励无关对齐, 冲突目标, 大语言模型, 多目标对齐, 梯度冲突, Pareto关键点, Qwen 3, Llama 3, Gemma 3, llm

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02495v1) | [下载PDF](https://arxiv.org/pdf/2602.02495v1.pdf)

---

## [9. Training LLMs for Divide-and-Conquer Reasoning Elevates Test-Time Scalability](https://arxiv.org/abs/2602.02477v1)

**作者**：Xiao Liang, Zhong-Zhi Li, Zhenghao Lin 等 10 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-02

### 📄 论文摘要

Large language models (LLMs) have demonstrated strong reasoning capabilities through step-by-step chain-of-thought (CoT) reasoning. Nevertheless, at the limits of model capability, CoT often proves insufficient, and its strictly sequential nature constrains test-time scalability. A potential alternative is divide-and-conquer (DAC) reasoning, which decomposes a complex problem into subproblems to facilitate more effective exploration of the solution. Although promising, our analysis reveals a fundamental misalignment between general-purpose post-training and DAC-style inference, which limits the model's capacity to fully leverage this potential. To bridge this gap and fully unlock LLMs' reasoning capabilities on the most challenging tasks, we propose an end-to-end reinforcement learning (RL) framework to enhance their DAC-style reasoning capacity. At each step, the policy decomposes a problem into a group of subproblems, solves them sequentially, and addresses the original one conditioned on the subproblem solutions, with both decomposition and solution integrated into RL training. Under comparable training, our DAC-style framework endows the model with a higher performance ceiling and stronger test-time scalability, surpassing CoT by 8.6% in Pass@1 and 6.3% in Pass@32 on competition-level benchmarks.

### 🤖 AI 总结

**一句话总结**：提出了一种基于强化学习的框架，以增强大型语言模型在分治推理中的能力，从而提高测试时的可扩展性。

**研究动机**：尽管大型语言模型在逐步推理方面表现出色，但其顺序特性限制了在复杂任务中的有效性和可扩展性。

**核心方法**：通过一种端到端的强化学习框架，将复杂问题分解为子问题，并在解决过程中整合分解与解决步骤，来提升模型的分治推理能力。

**主要结论**：该框架在竞争性基准测试中显著提升了模型性能，相比传统链式推理在多个指标上均有显著提高。

**关键词**：大语言模型, LLM, 推理能力, 分而治之, 强化学习, 测试时间可扩展性, 解决方案, 子问题, 训练框架, 递归推理

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02477v1) | [下载PDF](https://arxiv.org/pdf/2602.02477v1.pdf)

---

## [10. Indications of Belief-Guided Agency and Meta-Cognitive Monitoring in Large Language Models](https://arxiv.org/abs/2602.02467v1)

**作者**：Noam Steinmetz Yalon, Ariel Goldstein, Liad Mudrik 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-02

### 📄 论文摘要

Rapid advancements in large language models (LLMs) have sparked the question whether these models possess some form of consciousness. To tackle this challenge, Butlin et al. (2023) introduced a list of indicators for consciousness in artificial systems based on neuroscientific theories. In this work, we evaluate a key indicator from this list, called HOT-3, which tests for agency guided by a general belief-formation and action selection system that updates beliefs based on meta-cognitive monitoring. We view beliefs as representations in the model's latent space that emerge in response to a given input, and introduce a metric to quantify their dominance during generation. Analyzing the dynamics between competing beliefs across models and tasks reveals three key findings: (1) external manipulations systematically modulate internal belief formation, (2) belief formation causally drives the model's action selection, and (3) models can monitor and report their own belief states. Together, these results provide empirical support for the existence of belief-guided agency and meta-cognitive monitoring in LLMs. More broadly, our work lays methodological groundwork for investigating the emergence of agency, beliefs, and meta-cognition in LLMs.

### 🤖 AI 总结

**一句话总结**：本研究评估了大型语言模型中的信念引导行为和元认知监控，支持其具备某种形式的意识。

**研究动机**：随着大型语言模型的快速发展，研究其是否具备意识的能力变得重要，因此需要建立验证意识的指标。

**核心方法**：评估名为HOT-3的指标，通过分析模型在生成过程中信念的动态变化，量化信念在行动选择中的主导性。

**主要结论**：研究结果表明，大型语言模型具备信念引导的行为和元认知监控，为进一步研究意识的出现奠定了方法论基础。

**关键词**：大语言模型, belief-guided agency, meta-cognitive monitoring, HOT-3, 行为选择, 认知监控, 代理, 信念形成, 潜在空间, llm

**评分**：75

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02467v1) | [下载PDF](https://arxiv.org/pdf/2602.02467v1.pdf)

---

## [11. From Directions to Regions: Decomposing Activations in Language Models via Local Geometry](https://arxiv.org/abs/2602.02464v1)

**作者**：Or Shafran, Shaked Ronen, Omri Fahn 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-02

### 📄 论文摘要

Activation decomposition methods in language models are tightly coupled to geometric assumptions on how concepts are realized in activation space. Existing approaches search for individual global directions, implicitly assuming linear separability, which overlooks concepts with nonlinear or multi-dimensional structure. In this work, we leverage Mixture of Factor Analyzers (MFA) as a scalable, unsupervised alternative that models the activation space as a collection of Gaussian regions with their local covariance structure. MFA decomposes activations into two compositional geometric objects: the region's centroid in activation space, and the local variation from the centroid. We train large-scale MFAs for Llama-3.1-8B and Gemma-2-2B, and show they capture complex, nonlinear structures in activation space. Moreover, evaluations on localization and steering benchmarks show that MFA outperforms unsupervised baselines, is competitive with supervised localization methods, and often achieves stronger steering performance than sparse autoencoders. Together, our findings position local geometry, expressed through subspaces, as a promising unit of analysis for scalable concept discovery and model control, accounting for complex structures that isolated directions fail to capture.

### 🤖 AI 总结

**一句话总结**：本研究提出了一种基于局部几何的激活分解方法，通过混合因子分析器（MFA）建模语言模型中的激活空间，以捕捉复杂的非线性结构。

**研究动机**：现有的激活分解方法假设概念在激活空间中是线性可分的，但许多概念具有非线性或多维结构，因此需要新的方法来更有效地表示这些结构。

**核心方法**：本研究利用混合因子分析器（MFA）将激活空间视为一组高斯区域，通过区域的质心和局部变异来分解激活，适用于大规模模型。

**主要结论**：MFA在定性和定量评估中表现优于无监督基线，并在控制模型方面显示出更强的性能，强调了局部几何在概念发现和模型控制中的潜力。

**关键词**：激活分解, 语言模型, 几何假设, 非线性结构, Mixture of Factor Analyzers, Gaussian区域, Llama-3.1-8B, Gemma-2-2B, 模型控制, 概念发现, rag

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02464v1) | [下载PDF](https://arxiv.org/pdf/2602.02464v1.pdf)

---

## [12. Abstract Activation Spaces for Content-Invariant Reasoning in Large Language Models](https://arxiv.org/abs/2602.02462v1)

**作者**：Gabriele Maraia, Marco Valentino, Fabio Massimo Zanzotto 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-02

### 📄 论文摘要

Large Language Models (LLMs) often struggle with deductive judgment in syllogistic reasoning, systematically conflating semantic plausibility with formal validity a phenomenon known as content effect. This bias persists even when models generate step-wise explanations, indicating that intermediate rationales may inherit the same semantic shortcuts that affect answers. Recent approaches propose mitigating this issue by increasing inference-time structural constraints, either by encouraging abstract intermediate representations or by intervening directly in the model's internal computations; however, reliably suppressing semantic interference remains an open challenge. To make formal deduction less sensitive to semantic content, we introduce a framework for abstraction-guided reasoning that explicitly separates structural inference from lexical semantics. We construct paired content-laden and abstract syllogisms and use the model's activations on abstract inputs to define an abstract reasoning space. We then learn lightweight Abstractors that, from content-conditioned residual-stream states, predict representations aligned with this space and integrate these predictions via multi-layer interventions during the forward pass. Using cross-lingual transfer as a test bed, we show that abstraction-aligned steering reduces content-driven errors and improves validity-sensitive performance. Our results position activation-level abstraction as a scalable mechanism for enhancing the robustness of formal reasoning in LLMs against semantic interference.

### 🤖 AI 总结

**一句话总结**：本文提出了一种框架，通过抽象引导推理来减少大型语言模型在形式推理中的语义干扰。

**研究动机**：大型语言模型在三段论推理中存在内容效应，导致语义合理性与形式有效性混淆，影响推理准确性。

**核心方法**：构建配对的内容丰富和抽象的三段论，利用模型在抽象输入上的激活定义抽象推理空间，并通过轻量级抽象器在推理过程中整合预测。

**主要结论**：通过跨语言迁移实验，证明抽象对齐的引导可以减少内容驱动的错误，并提高模型在形式推理中的鲁棒性。

**关键词**：关键词: 大语言模型, 语义推理, 抽象推理, 结构推理, 中间表示, 激活空间, 轻量级抽象器, 交叉语言迁移, 形式推理, llm

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02462v1) | [下载PDF](https://arxiv.org/pdf/2602.02462v1.pdf)

---

## [13. Large Language Models for Mental Health: A Multilingual Evaluation](https://arxiv.org/abs/2602.02440v1)

**作者**：Nishat Raihan, Sadiya Sayara Chowdhury Puspo, Ana-Maria Bucur 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-02

### 📄 论文摘要

Large Language Models (LLMs) have remarkable capabilities across NLP tasks. However, their performance in multilingual contexts, especially within the mental health domain, has not been thoroughly explored. In this paper, we evaluate proprietary and open-source LLMs on eight mental health datasets in various languages, as well as their machine-translated (MT) counterparts. We compare LLM performance in zero-shot, few-shot, and fine-tuned settings against conventional NLP baselines that do not employ LLMs. In addition, we assess translation quality across language families and typologies to understand its influence on LLM performance. Proprietary LLMs and fine-tuned open-source LLMs achieve competitive F1 scores on several datasets, often surpassing state-of-the-art results. However, performance on MT data is generally lower, and the extent of this decline varies by language and typology. This variation highlights both the strengths of LLMs in handling mental health tasks in languages other than English and their limitations when translation quality introduces structural or lexical mismatches.

### 🤖 AI 总结

**一句话总结**：本文评估了多种语言的大型语言模型在心理健康领域的表现，发现其在多个数据集上具有竞争力，但机器翻译数据的表现较差。

**研究动机**：尽管大型语言模型在自然语言处理任务中表现出色，但其在心理健康领域的多语言能力尚未得到充分研究。

**核心方法**：对八个不同语言的心理健康数据集进行评估，比较大型语言模型与传统自然语言处理基准在零-shot、few-shot和微调设置下的表现。

**主要结论**：专有和微调的开源大型语言模型在多个数据集上取得了竞争力的F1得分，但在机器翻译数据上的表现较低，反映了翻译质量对模型表现的影响。

**关键词**：大语言模型, LLM, 心理健康, 多语言评估, 自然语言处理, 零样本学习, 微调, 机器翻译, F1分数

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02440v1) | [下载PDF](https://arxiv.org/pdf/2602.02440v1.pdf)

---

## [14. Misconception Diagnosis From Student-Tutor Dialogue: Generate, Retrieve, Rerank](https://arxiv.org/abs/2602.02414v1)

**作者**：Joshua Mitton, Prarthana Bhattacharyya, Digory Smith 等 6 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-02-02

### 📄 论文摘要

Timely and accurate identification of student misconceptions is key to improving learning outcomes and pre-empting the compounding of student errors. However, this task is highly dependent on the effort and intuition of the teacher. In this work, we present a novel approach for detecting misconceptions from student-tutor dialogues using large language models (LLMs). First, we use a fine-tuned LLM to generate plausible misconceptions, and then retrieve the most promising candidates among these using embedding similarity with the input dialogue. These candidates are then assessed and re-ranked by another fine-tuned LLM to improve misconception relevance. Empirically, we evaluate our system on real dialogues from an educational tutoring platform. We consider multiple base LLM models including LLaMA, Qwen and Claude on zero-shot and fine-tuned settings. We find that our approach improves predictive performance over baseline models and that fine-tuning improves both generated misconception quality and can outperform larger closed-source models. Finally, we conduct ablation studies to both validate the importance of our generation and reranking steps on misconception generation quality.

### 🤖 AI 总结

**一句话总结**：本文提出了一种利用大语言模型从学生与辅导员的对话中识别误解的新方法。

**研究动机**：及时准确地识别学生误解对改善学习成果至关重要，但这一过程通常依赖于教师的努力与直觉。

**核心方法**：通过细化的大语言模型生成潜在误解，然后利用嵌入相似性检索候选项，并通过另一个细化的模型进行评估和重新排序。

**主要结论**：该方法在真实对话数据中表现出比基线模型更好的预测性能，细化训练提升了生成误解的质量，并超越了更大规模的闭源模型。

**关键词**：误解诊断, 学生-导师对话, 大语言模型, LLM, 生成与检索, 嵌入相似度, 重新排序, 教育辅导平台, 零样本学习, 微调模型

**评分**：75

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02414v1) | [下载PDF](https://arxiv.org/pdf/2602.02414v1.pdf)

---

## cs.CV

## [15. PixelGen: Pixel Diffusion Beats Latent Diffusion with Perceptual Loss](https://arxiv.org/abs/2602.02493v1)

**作者**：Zehong Ma, Ruihan Xu, Shiliang Zhang  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-02-02

### 📄 论文摘要

Pixel diffusion generates images directly in pixel space in an end-to-end manner, avoiding the artifacts and bottlenecks introduced by VAEs in two-stage latent diffusion. However, it is challenging to optimize high-dimensional pixel manifolds that contain many perceptually irrelevant signals, leaving existing pixel diffusion methods lagging behind latent diffusion models. We propose PixelGen, a simple pixel diffusion framework with perceptual supervision. Instead of modeling the full image manifold, PixelGen introduces two complementary perceptual losses to guide diffusion model towards learning a more meaningful perceptual manifold. An LPIPS loss facilitates learning better local patterns, while a DINO-based perceptual loss strengthens global semantics. With perceptual supervision, PixelGen surpasses strong latent diffusion baselines. It achieves an FID of 5.11 on ImageNet-256 without classifier-free guidance using only 80 training epochs, and demonstrates favorable scaling performance on large-scale text-to-image generation with a GenEval score of 0.79. PixelGen requires no VAEs, no latent representations, and no auxiliary stages, providing a simpler yet more powerful generative paradigm. Codes are publicly available at https://github.com/Zehong-Ma/PixelGen.

### 🤖 AI 总结

**一句话总结**：PixelGen是一种基于像素扩散的图像生成框架，通过感知损失超越了传统的潜在扩散模型。

**研究动机**：现有的像素扩散方法在优化高维像素流形时面临挑战，导致其性能落后于潜在扩散模型。

**核心方法**：PixelGen引入了局部模式和全局语义的两个互补感知损失，以引导扩散模型学习更有意义的感知流形。

**主要结论**：PixelGen在ImageNet-256上实现了5.11的FID，并在大规模文本到图像生成中表现出良好的扩展性能，证明了其有效性和简洁性。

**关键词**：像素扩散, PixelGen, 生成模型, 感知损失, 图像生成, 深度学习, 嵌入, 语义搜索, 代理工作流, generative

**评分**：76

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02493v1) | [下载PDF](https://arxiv.org/pdf/2602.02493v1.pdf)

---

## [16. Multi-head automated segmentation by incorporating detection head into the contextual layer neural network](https://arxiv.org/abs/2602.02471v1)

**作者**：Edwin Kys, Febian Febian  
**分类**：cs.CV, cs.AI, physics.med-ph  
**发布时间**：2026-02-02

### 📄 论文摘要

Deep learning based auto segmentation is increasingly used in radiotherapy, but conventional models often produce anatomically implausible false positives, or hallucinations, in slices lacking target structures. We propose a gated multi-head Transformer architecture based on Swin U-Net, augmented with inter-slice context integration and a parallel detection head, which jointly performs slice-level structure detection via a multi-layer perceptron and pixel-level segmentation through a context-enhanced stream. Detection outputs gate the segmentation predictions to suppress false positives in anatomically invalid slices, and training uses slice-wise Tversky loss to address class imbalance. Experiments on the Prostate-Anatomical-Edge-Cases dataset from The Cancer Imaging Archive demonstrate that the gated model substantially outperforms a non-gated segmentation-only baseline, achieving a mean Dice loss of $0.013 \pm 0.036$ versus $0.732 \pm 0.314$, with detection probabilities strongly correlated with anatomical presence, effectively eliminating spurious segmentations. In contrast, the non-gated model exhibited higher variability and persistent false positives across all slices. These results indicate that detection-based gating enhances robustness and anatomical plausibility in automated segmentation applications, reducing hallucinated predictions without compromising segmentation quality in valid slices, and offers a promising approach for improving the reliability of clinical radiotherapy auto-contouring workflows.

### 🤖 AI 总结

**一句话总结**：提出了一种基于Swin U-Net的门控多头Transformer架构，通过结合检测头和上下文集成，显著提高了放射治疗中的自动分割性能。

**研究动机**：传统深度学习自动分割模型在缺乏目标结构的切片中常产生不符合解剖学的假阳性，影响临床应用的可靠性。

**核心方法**：采用了门控多头Transformer架构，结合检测头进行切片级结构检测和像素级分割，利用Tversky损失函数解决类别不平衡问题。

**主要结论**：检测驱动的门控机制提升了自动分割的稳健性和解剖学合理性，有效减少了虚假预测，同时不影响有效切片的分割质量。

**关键词**：深度学习, 自动分割, Transformer, Swin U-Net, 多头模型, 结构检测, 背景增强, Tversky损失, 临床应用

**评分**：75

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02471v1) | [下载PDF](https://arxiv.org/pdf/2602.02471v1.pdf)

---

## [17. UniReason 1.0: A Unified Reasoning Framework for World Knowledge Aligned Image Generation and Editing](https://arxiv.org/abs/2602.02437v1)

**作者**：Dianyi Wang, Chaofan Ma, Feng Han 等 11 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-02-02

### 📄 论文摘要

Unified multimodal models often struggle with complex synthesis tasks that demand deep reasoning, and typically treat text-to-image generation and image editing as isolated capabilities rather than interconnected reasoning steps. To address this, we propose UniReason, a unified framework that harmonizes these two tasks through a dual reasoning paradigm. We formulate generation as world knowledge-enhanced planning to inject implicit constraints, and leverage editing capabilities for fine-grained visual refinement to further correct visual errors via self-reflection. This approach unifies generation and editing within a shared representation, mirroring the human cognitive process of planning followed by refinement. We support this framework by systematically constructing a large-scale reasoning-centric dataset (~300k samples) covering five major knowledge domains (e.g., cultural commonsense, physics, etc.) for planning, alongside an agent-generated corpus for visual self-correction. Extensive experiments demonstrate that UniReason achieves advanced performance on reasoning-intensive benchmarks such as WISE, KrisBench and UniREditBench, while maintaining superior general synthesis capabilities.

### 🤖 AI 总结

**一句话总结**：UniReason是一个统一的推理框架，通过双重推理范式将图像生成与编辑任务结合起来，以提高复杂合成任务的表现。

**研究动机**：当前的多模态模型在复杂合成任务中表现欠佳，通常将文本到图像生成与图像编辑视为孤立的能力，而不是相互关联的推理步骤。

**核心方法**：UniReason框架将生成视为增强世界知识的规划，引入隐性约束，并利用编辑能力进行细致的视觉修正，从而统一生成与编辑。

**主要结论**：实验结果表明，UniReason在推理密集的基准测试上表现优异，同时保持了出色的综合合成能力。

**关键词**：统一推理, 多模态模型, 生成与编辑, 深度推理, 视觉自我修正, agent生成, 知识增强, 共享表示, 复杂合成任务, 计划与细化

**评分**：75

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02437v1) | [下载PDF](https://arxiv.org/pdf/2602.02437v1.pdf)

---

## [18. SelvaMask: Segmenting Trees in Tropical Forests and Beyond](https://arxiv.org/abs/2602.02426v1)

**作者**：Simon-Olivier Duguay, Hugo Baudchon, Etienne Laliberté 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-02

### 📄 论文摘要

Tropical forests harbor most of the planet's tree biodiversity and are critical to global ecological balance. Canopy trees in particular play a disproportionate role in carbon storage and functioning of these ecosystems. Studying canopy trees at scale requires accurate delineation of individual tree crowns, typically performed using high-resolution aerial imagery. Despite advances in transformer-based models for individual tree crown segmentation, performance remains low in most forests, especially tropical ones. To this end, we introduce SelvaMask, a new tropical dataset containing over 8,800 manually delineated tree crowns across three Neotropical forest sites in Panama, Brazil, and Ecuador. SelvaMask features comprehensive annotations, including an inter-annotator agreement evaluation, capturing the dense structure of tropical forests and highlighting the difficulty of the task. Leveraging this benchmark, we propose a modular detection-segmentation pipeline that adapts vision foundation models (VFMs), using domain-specific detection-prompter. Our approach reaches state-of-the-art performance, outperforming both zero-shot generalist models and fully supervised end-to-end methods in dense tropical forests. We validate these gains on external tropical and temperate datasets, demonstrating that SelvaMask serves as both a challenging benchmark and a key enabler for generalized forest monitoring. Our code and dataset will be released publicly.

### 🤖 AI 总结

**一句话总结**：SelvaMask是一个新数据集和方法，旨在提高热带森林中树冠分割的准确性，尤其是在稠密森林环境中。

**研究动机**：热带森林是地球树木生物多样性的主要栖息地，准确识别树冠对于研究其生态功能和碳储存至关重要。

**核心方法**：研究者提出了一个模块化的检测-分割管道，结合了视觉基础模型和特定领域的检测提示，以实现更高效的树冠分割。

**主要结论**：SelvaMask在热带森林的树冠分割中达到了最先进的性能，验证了其在外部数据集上的有效性，并将公开发布代码和数据集以促进森林监测研究。

**关键词**：树木分割, 热带森林, 语义分割, 深度学习, 视觉基础模型, 森林监测, 模块化检测-分割管道, 数据集, 高分辨率图像, transformer

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02426v1) | [下载PDF](https://arxiv.org/pdf/2602.02426v1.pdf)

---

## [19. Catalyst: Out-of-Distribution Detection via Elastic Scaling](https://arxiv.org/abs/2602.02409v1)

**作者**：Abid Hassan, Tuan Ngo, Saad Shafiq 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-02

### 📄 论文摘要

Out-of-distribution (OOD) detection is critical for the safe deployment of deep neural networks. State-of-the-art post-hoc methods typically derive OOD scores from the output logits or penultimate feature vector obtained via global average pooling (GAP). We contend that this exclusive reliance on the logit or feature vector discards a rich, complementary signal: the raw channel-wise statistics of the pre-pooling feature map lost in GAP. In this paper, we introduce Catalyst, a post-hoc framework that exploits these under-explored signals. Catalyst computes an input-dependent scaling factor ($γ$) on-the-fly from these raw statistics (e.g., mean, standard deviation, and maximum activation). This $γ$ is then fused with the existing baseline score, multiplicatively modulating it -- an ``elastic scaling'' -- to push the ID and OOD distributions further apart. We demonstrate Catalyst is a generalizable framework: it seamlessly integrates with logit-based methods (e.g., Energy, ReAct, SCALE) and also provides a significant boost to distance-based detectors like KNN. As a result, Catalyst achieves substantial and consistent performance gains, reducing the average False Positive Rate by 32.87 on CIFAR-10 (ResNet-18), 27.94% on CIFAR-100 (ResNet-18), and 22.25% on ImageNet (ResNet-50). Our results highlight the untapped potential of pre-pooling statistics and demonstrate that Catalyst is complementary to existing OOD detection approaches.

### 🤖 AI 总结

**一句话总结**：Catalyst是一种通过弹性缩放利用预池化特征图的原始通道统计量来改进异常检测的方法。

**研究动机**：现有的后处理方法过于依赖于输出logits或特征向量，而忽视了预池化特征图中的丰富信号，导致潜在性能损失。

**核心方法**：Catalyst计算输入依赖的缩放因子，并通过弹性缩放将其与现有基线分数相结合，从而进一步优化OOD检测效果。

**主要结论**：Catalyst在多个数据集上显著提高了异常检测性能，并证明了预池化统计量的潜在价值，具有良好的通用性和兼容性。

**关键词**：深度学习, 神经网络, OOD检测, Catalyst, 弹性缩放, 特征图, 统计信息, 误报率, KNN, 机器学习, ml

**评分**：71

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02409v1) | [下载PDF](https://arxiv.org/pdf/2602.02409v1.pdf)

---

## [20. ReasonEdit: Editing Vision-Language Models using Human Reasoning](https://arxiv.org/abs/2602.02408v1)

**作者**：Jiaxing Qiu, Kaihua Hou, Roxana Daneshjou 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-02-02

### 📄 论文摘要

Model editing aims to correct errors in large, pretrained models without altering unrelated behaviors. While some recent works have edited vision-language models (VLMs), no existing editors tackle reasoning-heavy tasks, which typically require humans and models to reason about images.We therefore propose ReasonEdit, the first VLM editor to let users explain their reasoning during editing, introducing a new, practical model editing setup. ReasonEdit continuously stores human reasoning in a codebook, and retrieves only relevant facts during inference using a novel topology-balanced multimodal embedding method inspired by network science. Across four VLMs on multiple rationale-based visual question answering datasets, ReasonEdit achieves state-of-the-art editing performance, ultimately showing that using human reasoning during editing greatly improves edit generalization.

### 🤖 AI 总结

**一句话总结**：ReasonEdit是一种新颖的视觉语言模型编辑工具，允许用户在编辑过程中利用人类推理，从而提升编辑效果。

**研究动机**：现有的视觉语言模型编辑工具未能有效处理需要推理的任务，因此需要一种新的方法来整合人类推理。

**核心方法**：ReasonEdit通过持续存储人类推理到代码本，并使用一种新颖的拓扑平衡多模态嵌入方法来检索相关事实，从而实现模型编辑。

**主要结论**：ReasonEdit在多个基于推理的视觉问答数据集上实现了最先进的编辑性能，证明了在编辑过程中利用人类推理显著提高了编辑的通用性。

**关键词**：模型编辑, 视觉语言模型, 人类推理, 多模态嵌入, 代码本, 视觉问答, 状态最优, ReasonEdit, 推理重用, 编辑性能, embedding

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02408v1) | [下载PDF](https://arxiv.org/pdf/2602.02408v1.pdf)

---

## cs.LG

## [21. RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System](https://arxiv.org/abs/2602.02488v1)

**作者**：Yinjie Wang, Tianbao Xie, Ke Shen 等 5 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-02-02

### 📄 论文摘要

We propose RLAnything, a reinforcement learning framework that dynamically forges environment, policy, and reward models through closed-loop optimization, amplifying learning signals and strengthening the overall RL system for any LLM or agentic scenarios. Specifically, the policy is trained with integrated feedback from step-wise and outcome signals, while the reward model is jointly optimized via consistency feedback, which in turn further improves policy training. Moreover, our theory-motivated automatic environment adaptation improves training for both the reward and policy models by leveraging critic feedback from each, enabling learning from experience. Empirically, each added component consistently improves the overall system, and RLAnything yields substantial gains across various representative LLM and agentic tasks, boosting Qwen3-VL-8B-Thinking by 9.1% on OSWorld and Qwen2.5-7B-Instruct by 18.7% and 11.9% on AlfWorld and LiveBench, respectively. We also that optimized reward-model signals outperform outcomes that rely on human labels. Code: https://github.com/Gen-Verse/Open-AgentRL

### 🤖 AI 总结

**一句话总结**：RLAnything是一个通过闭环优化动态锻造环境、策略和奖励模型的强化学习框架，显著提升了学习信号和系统性能。

**研究动机**：本研究旨在提高强化学习系统的整体性能，特别是在大规模语言模型和自主代理场景中，通过动态适应环境和优化策略及奖励模型来增强学习效果。

**核心方法**：RLAnything结合了逐步和结果信号的集成反馈进行策略训练，并通过一致性反馈共同优化奖励模型，从而提升训练效果，同时利用批评者反馈实现环境的自动适应。

**主要结论**：实验表明，各个组成部分的添加均能一致性地改善整体系统性能，RLAnything在多项代表性任务中取得了显著提升，优化的奖励模型信号超越了依赖人类标签的结果。

**关键词**：强化学习, 动态环境, 策略优化, 奖励模型, LLM, agentic场景, 反馈机制, 经验学习, 自动化适应

**评分**：76

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02488v1) | [下载PDF](https://arxiv.org/pdf/2602.02488v1.pdf)

---

## [22. Expanding the Capabilities of Reinforcement Learning via Text Feedback](https://arxiv.org/abs/2602.02482v1)

**作者**：Yuda Song, Lili Chen, Fahim Tajwar 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-02

### 📄 论文摘要

The success of RL for LLM post-training stems from an unreasonably uninformative source: a single bit of information per rollout as binary reward or preference label. At the other extreme, distillation offers dense supervision but requires demonstrations, which are costly and difficult to scale. We study text feedback as an intermediate signal: richer than scalar rewards, yet cheaper than complete demonstrations. Textual feedback is a natural mode of human interaction and is already abundant in many real-world settings, where users, annotators, and automated judges routinely critique LLM outputs. Towards leveraging text feedback at scale, we formalize a multi-turn RL setup, RL from Text Feedback (RLTF), where text feedback is available during training but not at inference. Therefore, models must learn to internalize the feedback in order to improve their test-time single-turn performance. To do this, we propose two methods: Self Distillation (RLTF-SD), which trains the single-turn policy to match its own feedback-conditioned second-turn generations; and Feedback Modeling (RLTF-FM), which predicts the feedback as an auxiliary objective. We provide theoretical analysis on both methods, and empirically evaluate on reasoning puzzles, competition math, and creative writing tasks. Our results show that both methods consistently outperform strong baselines across benchmarks, highlighting the potential of RL with an additional source of rich supervision at scale.

### 🤖 AI 总结

**一句话总结**：通过使用文本反馈，研究如何扩展强化学习在大型语言模型后训练中的能力。

**研究动机**：现有的强化学习方法依赖于单一的、信息量有限的奖励信号，而文本反馈提供了一种更丰富但成本更低的监督方式。

**核心方法**：提出了两种方法：自我蒸馏（RLTF-SD），通过匹配自身反馈生成的内容来训练单轮策略；反馈建模（RLTF-FM），将预测反馈作为辅助目标。

**主要结论**：实验结果表明，这两种方法在多个基准测试中均优于强基线，展示了在大规模应用中结合文本反馈的潜力。

**关键词**：强化学习, 文本反馈, 机器学习, 深度学习, 自我蒸馏, 反馈建模, LLM, 多轮RL, 监督学习, 训练优化

**评分**：76

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02482v1) | [下载PDF](https://arxiv.org/pdf/2602.02482v1.pdf)

---

## [23. SPARKLING: Balancing Signal Preservation and Symmetry Breaking for Width-Progressive Learning](https://arxiv.org/abs/2602.02472v1)

**作者**：Qifan Yu, Xinyu Ma, Zhijian Zhuo 等 10 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-02-02

### 📄 论文摘要

Progressive Learning (PL) reduces pre-training computational overhead by gradually increasing model scale. While prior work has extensively explored depth expansion, width expansion remains significantly understudied, with the few existing methods limited to the early stages of training. However, expanding width during the mid-stage is essential for maximizing computational savings, yet it remains a formidable challenge due to severe training instabilities. Empirically, we show that naive initialization at this stage disrupts activation statistics, triggering loss spikes, while copy-based initialization introduces gradient symmetry that hinders feature diversity. To address these issues, we propose SPARKLING (balancing {S}ignal {P}reservation {A}nd symmet{R}y brea{K}ing for width-progressive {L}earn{ING}), a novel framework for mid-stage width expansion. Our method achieves signal preservation via RMS-scale consistency, stabilizing activation statistics during expansion. Symmetry breaking is ensured through asymmetric optimizer state resetting and learning rate re-warmup. Extensive experiments on Mixture-of-Experts (MoE) models demonstrate that, across multiple width axes and optimizer families, SPARKLING consistently outperforms training from scratch and reduces training cost by up to 35% under $2\times$ width expansion.

### 🤖 AI 总结

**一句话总结**：SPARKLING是一种新框架，通过信号保护和打破对称性，实现宽度渐进学习中的中期扩展，显著降低训练成本。

**研究动机**：尽管已有研究探索深度扩展，但宽度扩展在训练中期的重要性尚未得到充分重视，特别是为了最大化计算节省。

**核心方法**：SPARKLING通过RMS规模一致性实现信号保护，并通过不对称优化器状态重置和学习率重新升温来打破对称性，从而稳定扩展过程。

**主要结论**：在多个宽度轴和优化器系列上，SPARKLING在训练效率上优于从头开始训练，训练成本降低高达35%。

**关键词**：信号保留, 对称打破, 宽度扩展, 逐步学习, 训练稳定性, Mixture-of-Experts, RMS-scale一致性, 优化器状态重置, 学习率重热, 计算节省, agent

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02472v1) | [下载PDF](https://arxiv.org/pdf/2602.02472v1.pdf)

---

## [24. Conflict-Aware Client Selection for Multi-Server Federated Learning](https://arxiv.org/abs/2602.02458v1)

**作者**：Mingwei Hong, Zheng Lin, Zehang Lin 等 10 位作者  
**分类**：cs.LG, cs.NI  
**发布时间**：2026-02-02

### 📄 论文摘要

Federated learning (FL) has emerged as a promising distributed machine learning (ML) that enables collaborative model training across clients without exposing raw data, thereby preserving user privacy and reducing communication costs. Despite these benefits, traditional single-server FL suffers from high communication latency due to the aggregation of models from a large number of clients. While multi-server FL distributes workloads across edge servers, overlapping client coverage and uncoordinated selection often lead to resource contention, causing bandwidth conflicts and training failures. To address these limitations, we propose a decentralized reinforcement learning with conflict risk prediction, named RL CRP, to optimize client selection in multi-server FL systems. Specifically, each server estimates the likelihood of client selection conflicts using a categorical hidden Markov model based on its sparse historical client selection sequence. Then, a fairness-aware reward mechanism is incorporated to promote long-term client participation for minimizing training latency and resource contention. Extensive experiments demonstrate that the proposed RL-CRP framework effectively reduces inter-server conflicts and significantly improves training efficiency in terms of convergence speed and communication cost.

### 🤖 AI 总结

**一句话总结**：本文提出了一种基于冲突风险预测的去中心化强化学习方法，以优化多服务器联邦学习中的客户端选择。

**研究动机**：传统的单服务器联邦学习存在高通信延迟和资源冲突问题，而多服务器联邦学习却因客户端覆盖重叠和选择不协调导致训练失败。

**核心方法**：作者提出了一种名为RL CRP的框架，通过基于稀疏历史客户端选择序列的分类隐马尔可夫模型来预测冲突，并引入公平奖励机制以促进长期参与。

**主要结论**：实验结果表明，RL-CRP框架有效减少了服务器间的冲突，显著提高了训练效率，包括收敛速度和通信成本。

**关键词**：联邦学习, 分布式机器学习, 客户端选择, 强化学习, 资源竞争, 带宽冲突, 模型聚合, 多服务器, 训练效率, 用户隐私, machine learning

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02458v1) | [下载PDF](https://arxiv.org/pdf/2602.02458v1.pdf)

---

## [25. Active Causal Experimentalist (ACE): Learning Intervention Strategies via Direct Preference Optimization](https://arxiv.org/abs/2602.02451v1)

**作者**：Patrick Cooper, Alvaro Velasquez  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-02

### 📄 论文摘要

Discovering causal relationships requires controlled experiments, but experimentalists face a sequential decision problem: each intervention reveals information that should inform what to try next. Traditional approaches such as random sampling, greedy information maximization, and round-robin coverage treat each decision in isolation, unable to learn adaptive strategies from experience. We propose Active Causal Experimentalist (ACE), which learns experimental design as a sequential policy. Our key insight is that while absolute information gains diminish as knowledge accumulates (making value-based RL unstable), relative comparisons between candidate interventions remain meaningful throughout. ACE exploits this via Direct Preference Optimization, learning from pairwise intervention comparisons rather than non-stationary reward magnitudes. Across synthetic benchmarks, physics simulations, and economic data, ACE achieves 70-71% improvement over baselines at equal intervention budgets (p < 0.001, Cohen's d ~ 2). Notably, the learned policy autonomously discovers that collider mechanisms require concentrated interventions on parent variables, a theoretically-grounded strategy that emerges purely from experience. This suggests preference-based learning can recover principled experimental strategies, complementing theory with learned domain adaptation.

### 🤖 AI 总结

**一句话总结**：本论文提出了一种新的实验设计方法ACE，通过直接偏好优化学习干预策略，以提高因果关系发现的效率和效果。

**研究动机**：传统的实验设计方法无法有效利用经验进行适应性决策，因此需要一种新方法来解决实验中的顺序决策问题。

**核心方法**：ACE通过将实验设计视为一个顺序策略，利用直接偏好优化从成对的干预比较中学习，而非依赖于不稳定的绝对奖励。

**主要结论**：ACE在多个基准实验中表现出显著优越性，表明偏好学习能够有效恢复有原则的实验策略，并从经验中提取理论支持。

**关键词**：因果关系, 实验设计, 优化策略, 深度学习, 机器学习, 代理, 适应性策略, 在线学习, 偏好优化, 经验学习, autonomous

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02451v1) | [下载PDF](https://arxiv.org/pdf/2602.02451v1.pdf)

---

## [26. Finite-Sample Wasserstein Error Bounds and Concentration Inequalities for Nonlinear Stochastic Approximation](https://arxiv.org/abs/2602.02445v1)

**作者**：Seo Taek Kong, R. Srikant  
**分类**：cs.LG, math.ST  
**发布时间**：2026-02-02

### 📄 论文摘要

This paper derives non-asymptotic error bounds for nonlinear stochastic approximation algorithms in the Wasserstein-$p$ distance. To obtain explicit finite-sample guarantees for the last iterate, we develop a coupling argument that compares the discrete-time process to a limiting Ornstein-Uhlenbeck process. Our analysis applies to algorithms driven by general noise conditions, including martingale differences and functions of ergodic Markov chains. Complementing this result, we handle the convergence rate of the Polyak-Ruppert average through a direct analysis that applies under the same general setting.   Assuming the driving noise satisfies a non-asymptotic central limit theorem, we show that the normalized last iterates converge to a Gaussian distribution in the $p$-Wasserstein distance at a rate of order $γ_n^{1/6}$, where $γ_n$ is the step size. Similarly, the Polyak-Ruppert average is shown to converge in the Wasserstein distance at a rate of order $n^{-1/6}$. These distributional guarantees imply high-probability concentration inequalities that improve upon those derived from moment bounds and Markov's inequality. We demonstrate the utility of this approach by considering two applications: (1) linear stochastic approximation, where we explicitly quantify the transition from heavy-tailed to Gaussian behavior of the iterates, thereby bridging the gap between recent finite-sample analyses and asymptotic theory and (2) stochastic gradient descent, where we establish rate of convergence to the central limit theorem.

### 🤖 AI 总结

**一句话总结**：本文推导了非线性随机逼近算法在Wasserstein-$p$距离下的有限样本误差界限，展示了其收敛性和浓度不等式。

**研究动机**：研究非线性随机逼近算法的有限样本表现，以填补有限样本分析与渐进理论之间的空白。

**核心方法**：通过比较离散时间过程与极限Ornstein-Uhlenbeck过程，发展了一种耦合论证，适用于一般噪声条件下的算法。

**主要结论**：算法的最后迭代以速率$γ_n^{1/6}$收敛到高斯分布，同时Polyak-Ruppert平均以速率$n^{-1/6}$收敛，且给出了改进的高概率浓度不等式。

**关键词**：非线性随机逼近, Wasserstein距离, 误差界限, 收敛速率, 高概率浓度不等式, 迭代算法, 马尔可夫链, 随机梯度下降, 机器学习, 深度学习, rag

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02445v1) | [下载PDF](https://arxiv.org/pdf/2602.02445v1.pdf)

---

## [27. Maximizing Reliability with Bayesian Optimization](https://arxiv.org/abs/2602.02432v1)

**作者**：Jack M. Buckingham, Ivo Couckuyt, Juergen Branke  
**分类**：cs.LG, math.OC, stat.ML  
**发布时间**：2026-02-02

### 📄 论文摘要

Bayesian optimization (BO) is a popular, sample-efficient technique for expensive, black-box optimization. One such problem arising in manufacturing is that of maximizing the reliability, or equivalently minimizing the probability of a failure, of a design which is subject to random perturbations - a problem that can involve extremely rare failures ($P_\mathrm{fail} = 10^{-6}-10^{-8}$). In this work, we propose two BO methods based on Thompson sampling and knowledge gradient, the latter approximating the one-step Bayes-optimal policy for minimizing the logarithm of the failure probability. Both methods incorporate importance sampling to target extremely small failure probabilities. Empirical results show the proposed methods outperform existing methods in both extreme and non-extreme regimes.

### 🤖 AI 总结

**一句话总结**：本文提出了两种基于贝叶斯优化的方法，以提高设计的可靠性，特别是在极小失效概率的情况下。

**研究动机**：制造过程中存在需要最大化设计可靠性的问题，该问题涉及到极少发生的失效事件。

**核心方法**：提出的两种贝叶斯优化方法分别基于汤普森采样和知识梯度，并通过重要性采样来处理极小的失效概率。

**主要结论**：实验结果表明，所提出的方法在极端和非极端情况下均优于现有方法。

**关键词**：贝叶斯优化, 可靠性, 黑箱优化, 重要性采样, 采样效率, 设计优化, 失败概率, 机器学习, 深度学习, agent

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02432v1) | [下载PDF](https://arxiv.org/pdf/2602.02432v1.pdf)

---

## [28. Repurposing Protein Language Models for Latent Flow-Based Fitness Optimization](https://arxiv.org/abs/2602.02425v1)

**作者**：Amaru Caceres Arroyo, Lea Bogensperger, Ahmed Allam 等 6 位作者  
**分类**：cs.LG, q-bio.QM  
**发布时间**：2026-02-02

### 📄 论文摘要

Protein fitness optimization is challenged by a vast combinatorial landscape where high-fitness variants are extremely sparse. Many current methods either underperform or require computationally expensive gradient-based sampling. We present CHASE, a framework that repurposes the evolutionary knowledge of pretrained protein language models by compressing their embeddings into a compact latent space. By training a conditional flow-matching model with classifier-free guidance, we enable the direct generation of high-fitness variants without predictor-based guidance during the ODE sampling steps. CHASE achieves state-of-the-art performance on AAV and GFP protein design benchmarks. Finally, we show that bootstrapping with synthetic data can further enhance performance in data-constrained settings.

### 🤖 AI 总结

**一句话总结**：CHASE框架通过重用预训练的蛋白质语言模型，实现了高效的蛋白质适应性优化。

**研究动机**：蛋白质适应性优化面临着组合空间巨大和高适应性变体稀缺的挑战，现有方法表现不佳或计算成本高。

**核心方法**：通过将预训练蛋白质语言模型的嵌入压缩到紧凑的潜在空间，并训练无分类器引导的条件流匹配模型，CHASE能够在ODE采样步骤中直接生成高适应性变体。

**主要结论**：CHASE在AAV和GFP蛋白设计基准上表现出色，并且通过合成数据的引导可以进一步提升在数据受限环境下的性能。

**关键词**：蛋白质优化, 语言模型, 潜在流, 高适应性变体, 生成模型, CHASE, 预训练, 嵌入压缩, 条件流匹配, 无分类器引导, embedding

**评分**：75

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02425v1) | [下载PDF](https://arxiv.org/pdf/2602.02425v1.pdf)

---

## [29. Trust Region Continual Learning as an Implicit Meta-Learner](https://arxiv.org/abs/2602.02417v1)

**作者**：Zekun Wang, Anant Gupta, Christopher J. MacLellan  
**分类**：cs.LG  
**发布时间**：2026-02-02

### 📄 论文摘要

Continual learning aims to acquire tasks sequentially without catastrophic forgetting, yet standard strategies face a core tradeoff: regularization-based methods (e.g., EWC) can overconstrain updates when task optima are weakly overlapping, while replay-based methods can retain performance but drift due to imperfect replay. We study a hybrid perspective: \emph{trust region continual learning} that combines generative replay with a Fisher-metric trust region constraint. We show that, under local approximations, the resulting update admits a MAML-style interpretation with a single implicit inner step: replay supplies an old-task gradient signal (query-like), while the Fisher-weighted penalty provides an efficient offline curvature shaping (support-like). This yields an emergent meta-learning property in continual learning: the model becomes an initialization that rapidly \emph{re-converges} to prior task optima after each task transition, without explicitly optimizing a bilevel objective. Empirically, on task-incremental diffusion image generation and continual diffusion-policy control, trust region continual learning achieves the best final performance and retention, and consistently recovers early-task performance faster than EWC, replay, and continual meta-learning baselines.

### 🤖 AI 总结

**一句话总结**：本文提出了一种信任区域持续学习方法，结合生成重放和Fisher度量约束，显著提高了模型在连续学习中的性能和任务保留能力。

**研究动机**：持续学习旨在顺序获取任务而不发生灾难性遗忘，但现有方法在任务重叠较弱时面临正则化过度约束和重放漂移的权衡。

**核心方法**：提出的信任区域持续学习方法通过生成重放与Fisher度量信任区域约束相结合，形成了一种隐式元学习的更新机制。

**主要结论**：实验结果表明，该方法在图像生成和政策控制任务中表现优异，能够比传统方法更快地恢复早期任务的性能。

**关键词**：信任区域持续学习, 元学习, 生成回放, 任务增量, 深度学习, 机器学习, 神经网络, 任务优化, 性能保留, ml

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02417v1) | [下载PDF](https://arxiv.org/pdf/2602.02417v1.pdf)

---

## [30. Active Transfer Bagging: A New Approach for Accelerated Active Learning Acquisition of Data by Combined Transfer Learning and Bagging Based Models](https://arxiv.org/abs/2602.02415v1)

**作者**：Vivienne Pelletier, Daniel J. Rivera, Obinna Nwokonkwo 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-02

### 📄 论文摘要

Modern machine learning has achieved remarkable success on many problems, but this success often depends on the existence of large, labeled datasets. While active learning can dramatically reduce labeling cost when annotations are expensive, early performance is frequently dominated by the initial seed set, typically chosen at random. In many applications, however, related or approximate datasets are readily available and can be leveraged to construct a better seed set. We introduce a new method for selecting the seed data set for active learning, Active-Transfer Bagging (ATBagging). ATBagging estimates the informativeness of candidate data point from a Bayesian interpretation of bagged ensemble models by comparing in-bag and out-of-bag predictive distributions from the labeled dataset, yielding an information-gain proxy. To avoid redundant selections, we impose feature-space diversity by sampling a determinantal point process (DPP) whose kernel uses Random Fourier Features and a quality-diversity factorization that incorporates the informativeness scores. This same blended method is used for selection of new data points to collect during the active learning phase. We evaluate ATBagging on four real-world datasets covering both target-transfer and feature-shift scenarios (QM9, ERA5, Forbes 2000, and Beijing PM2.5). Across seed sizes nseed = 10-100, ATBagging improves or ties early active learning and increases area under the learning-curve relative to alternative seed subset selection methodologies in almost all cases, with strongest benefits in low-data regimes. Thus, ATBagging provides a low-cost, high reward means to initiating active learning-based data collection.

### 🤖 AI 总结

**一句话总结**：提出了一种新的主动学习种子数据选择方法ATBagging，结合了迁移学习和袋装模型，以提高数据获取效率。

**研究动机**：现代机器学习依赖于大量标注数据，而主动学习可以降低标注成本，但初始种子集的选择通常影响早期表现。

**核心方法**：ATBagging通过比较袋内和袋外预测分布来估计候选数据点的信息量，采用确定性点过程采样以避免冗余选择，并在主动学习阶段选择新数据点。

**主要结论**：ATBagging在多个真实数据集上表现优异，特别是在低数据情况下，显著提高了主动学习的早期效果和学习曲线下面积。

**关键词**：主动学习, 迁移学习, 数据集, 信息增益, 特征选择, Active-Transfer Bagging, 低数据场景, 预测分布, 多样性采样, machine learning

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2602.02415v1) | [下载PDF](https://arxiv.org/pdf/2602.02415v1.pdf)

---

