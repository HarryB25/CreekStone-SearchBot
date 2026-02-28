# arXiv AI 论文日报 | 2026-02-28

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (10 篇)
- [cs.LG](#csLG) (11 篇)
- [cs.AI](#csAI) (7 篇)
- [cs.CL](#csCL) (2 篇)

---

## cs.AI

## [1. Toward Expert Investment Teams:A Multi-Agent LLM System with Fine-Grained Trading Tasks](https://arxiv.org/abs/2602.23330v1)

**作者**：Kunihiro Miyazaki, Takanobu Kawahara, Stephen Roberts 等 4 位作者  
**分类**：cs.AI, q-fin.TR  
**发布时间**：2026-02-26

### 📄 论文摘要

The advancement of large language models (LLMs) has accelerated the development of autonomous financial trading systems. While mainstream approaches deploy multi-agent systems mimicking analyst and manager roles, they often rely on abstract instructions that overlook the intricacies of real-world workflows, which can lead to degraded inference performance and less transparent decision-making. Therefore, we propose a multi-agent LLM trading framework that explicitly decomposes investment analysis into fine-grained tasks, rather than providing coarse-grained instructions. We evaluate the proposed framework using Japanese stock data, including prices, financial statements, news, and macro information, under a leakage-controlled backtesting setting. Experimental results show that fine-grained task decomposition significantly improves risk-adjusted returns compared to conventional coarse-grained designs. Crucially, further analysis of intermediate agent outputs suggests that alignment between analytical outputs and downstream decision preferences is a critical driver of system performance. Moreover, we conduct standard portfolio optimization, exploiting low correlation with the stock index and the variance of each system's output. This approach achieves superior performance. These findings contribute to the design of agent structure and task configuration when applying LLM agents to trading systems in practical settings.

### 🤖 AI 总结

**一句话总结**：提出一种将投资分析拆解为细粒度交易任务的多智能体LLM框架，在日本股票数据的防泄漏回测中显著提升风险调整后收益，并可通过组合优化进一步增益。

**研究动机**：现有多智能体交易系统多用“分析师/经理”式的粗粒度指令，忽略真实投研流程细节，导致推理性能下降且决策过程不透明。作者希望通过更贴近工作流的任务拆解，提高可控性与收益表现。

**核心方法**：构建多智能体LLM系统，将投研过程显式分解为更细的子任务并串联产出中间结果，在价格、财报、新闻与宏观等日本市场数据上进行防信息泄漏的回测评估。进一步分析各代理中间输出与下游决策偏好的对齐程度，并结合传统投资组合优化利用与指数的低相关性及各系统输出方差来提升表现。

**主要结论**：细粒度任务分解相比粗粒度设计能显著改善风险调整后收益；系统性能的关键驱动之一是“中间分析输出”与“下游决策偏好”的对齐。结合标准组合优化可进一步获得更优的整体表现，提示在实盘应用中代理结构与任务配置至关重要。

**关键词**：多智能体LLM交易, 投资分析任务分解, 细粒度交易任务, 泄漏控制回测, 风险调整收益, 中间输出对齐, 决策偏好对齐, 投资组合优化, 低相关性策略, 日本股票数据

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23330v1) | [下载PDF](https://arxiv.org/pdf/2602.23330v1.pdf)

---

## [2. LLM Novice Uplift on Dual-Use, In Silico Biology Tasks](https://arxiv.org/abs/2602.23329v1)

**作者**：Chen Bo Calvin Zhang, Christina Q. Knight, Nicholas Kruus 等 19 位作者  
**分类**：cs.AI, cs.CL, cs.CR, cs.CY, cs.HC  
**发布时间**：2026-02-26

### 📄 论文摘要

Large language models (LLMs) perform increasingly well on biology benchmarks, but it remains unclear whether they uplift novice users -- i.e., enable humans to perform better than with internet-only resources. This uncertainty is central to understanding both scientific acceleration and dual-use risk. We conducted a multi-model, multi-benchmark human uplift study comparing novices with LLM access versus internet-only access across eight biosecurity-relevant task sets. Participants worked on complex problems with ample time (up to 13 hours for the most involved tasks). We found that LLM access provided substantial uplift: novices with LLMs were 4.16 times more accurate than controls (95% CI [2.63, 6.87]). On four benchmarks with available expert baselines (internet-only), novices with LLMs outperformed experts on three of them. Perhaps surprisingly, standalone LLMs often exceeded LLM-assisted novices, indicating that users were not eliciting the strongest available contributions from the LLMs. Most participants (89.6%) reported little difficulty obtaining dual-use-relevant information despite safeguards. Overall, LLMs substantially uplift novices on biological tasks previously reserved for trained practitioners, underscoring the need for sustained, interactive uplift evaluations alongside traditional benchmarks.

### 🤖 AI 总结

**一句话总结**：研究发现：在多项具生物安全双重用途风险的生物任务上，给予LLM访问会显著提升新手表现，甚至在部分基准上超过仅用互联网的专家，同时暴露出防护措施易被绕过的问题。

**研究动机**：尽管LLM在生物基准测试上表现提升，但尚不清楚它们是否真正“扶起新手”并带来科学加速与双重用途风险上升。为评估现实影响，需要比较“LLM辅助的人”与“仅互联网的人”的任务完成效果。

**核心方法**：作者进行多模型、多基准的人类提升（uplift）实验：让新手在8套生物安全相关任务上完成复杂问题，对照组仅可用互联网，实验组可用LLM且给予充足时间（最复杂任务最高13小时），并在部分任务上与仅互联网的专家基线对比。

**主要结论**：LLM显著提升新手准确率（约4.16倍），且在有专家基线的4个基准中，新手+LLM在其中3个超过专家；同时单独LLM常优于“LLM辅助新手”，显示用户未充分发挥模型能力，且多数参与者能较轻松获取双重用途相关信息，提示需要持续的交互式提升评估与更强的安全治理。

**关键词**：新手能力提升评测, 人类-LLM协作, 生物安全任务, 生物学基准测试, 多模型对比评测, 人类参与实验, 专家-新手对照, 交互式评测框架, 安全护栏有效性, 信息获取可得性

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23329v1) | [下载PDF](https://arxiv.org/pdf/2602.23329v1.pdf)

---

## [3. Invariant Transformation and Resampling based Epistemic-Uncertainty Reduction](https://arxiv.org/abs/2602.23315v1)

**作者**：Sha Hu  
**分类**：cs.AI  
**发布时间**：2026-02-26

### 📄 论文摘要

An artificial intelligence (AI) model can be viewed as a function that maps inputs to outputs in high-dimensional spaces. Once designed and well trained, the AI model is applied for inference. However, even optimized AI models can produce inference errors due to aleatoric and epistemic uncertainties. Interestingly, we observed that when inferring multiple samples based on invariant transformations of an input, inference errors can show partial independences due to epistemic uncertainty. Leveraging this insight, we propose a "resampling" based inferencing that applies to a trained AI model with multiple transformed versions of an input, and aggregates inference outputs to a more accurate result. This approach has the potential to improve inference accuracy and offers a strategy for balancing model size and performance.

### 🤖 AI 总结

**一句话总结**：通过对同一输入施加多种不变变换并进行“重采样式”多次推理与聚合，可利用部分独立的认知不确定性误差来提升最终推理准确率。

**研究动机**：即使训练良好的模型也会因偶然不确定性与认知不确定性产生推理错误；作者观察到对输入做不变变换后，多次推理的误差在认知不确定性层面可能呈部分独立，从而存在可被集成消除的空间。

**核心方法**：对单个输入生成多个满足任务不变性的变换版本（如旋转/缩放/扰动等），在同一已训练模型上分别推理得到多组输出；再通过聚合（如投票/平均/置信度融合等）形成更稳健、更准确的最终预测，以“推理阶段重采样”方式降低认知不确定性影响。

**主要结论**：多变换重采样与输出聚合能在不改动或增大模型的情况下减少由认知不确定性导致的推理错误、提升准确率，并为在模型规模与性能之间进行权衡提供了一种推理期策略。

**关键词**：认知不确定性, 偶然不确定性, 不确定性分解, 测试时增强, 不变性变换, 重采样推理, 多样本推断, 输出聚合, 集成推理, 推理鲁棒性, 误差独立性, 模型规模-性能权衡

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23315v1) | [下载PDF](https://arxiv.org/pdf/2602.23315v1.pdf)

---

## [4. The logic of KM belief update is contained in the logic of AGM belief revision](https://arxiv.org/abs/2602.23302v1)

**作者**：Giacomo Bonanno  
**分类**：cs.AI, cs.LO, math.LO  
**发布时间**：2026-02-26

### 📄 论文摘要

For each axiom of KM belief update we provide a corresponding axiom in a modal logic containing three modal operators: a unimodal belief operator $B$, a bimodal conditional operator $>$ and the unimodal necessity operator $\square$. We then compare the resulting logic to the similar logic obtained from converting the AGM axioms of belief revision into modal axioms and show that the latter contains the former. Denoting the latter by $\mathcal L_{AGM}$ and the former by $\mathcal L_{KM}$ we show that every axiom of $\mathcal L_{KM}$ is a theorem of $\mathcal L_{AGM}$. Thus AGM belief revision can be seen as a special case of KM belief update. For the strong version of KM belief update we show that the difference between $\mathcal L_{KM}$ and $\mathcal L_{AGM}$ can be narrowed down to a single axiom, which deals exclusively with unsurprising information, that is, with formulas that were not initially disbelieved.

### 🤖 AI 总结

**一句话总结**：本文将KM信念更新与AGM信念修正的公理转为同一套模态逻辑框架后证明：由AGM得到的逻辑体系包含KM体系，因此AGM修正可视为KM更新的特例。

**研究动机**：KM更新与AGM修正是两类经典信念变更理论，但它们的形式关系不清晰；作者希望用统一的逻辑语言精确比较两者的表达力与公理强弱。

**核心方法**：把KM与AGM各自的公理逐条翻译为含三个模态算子（信念B、条件算子>、必然性□）的模态逻辑公理体系，分别构造$\mathcal L_{KM}$与$\mathcal L_{AGM}$并进行可导性/包含性证明。

**主要结论**：证明$\mathcal L_{KM}$的每条公理都是$\mathcal L_{AGM}$的定理，即AGM逻辑严格包含KM逻辑，从而AGM修正可被看作KM更新的特殊情形；对“强KM更新”，两者差异可缩减为仅一个关于“非意外信息（最初未被不信）”的公理。

**关键词**：信念更新, 信念修正, KM 信念更新, AGM 信念修正, 模态逻辑公理化, 信念算子, 条件算子, 必然性算子, 逻辑包含关系, 定理可导性

**评分**：6

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23302v1) | [下载PDF](https://arxiv.org/pdf/2602.23302v1.pdf)

---

## [5. ODEBrain: Continuous-Time EEG Graph for Modeling Dynamic Brain Networks](https://arxiv.org/abs/2602.23285v1)

**作者**：Haohui Jia, Zheng Chen, Lingwei Zhu 等 9 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-26

### 📄 论文摘要

Modeling neural population dynamics is crucial for foundational neuroscientific research and various clinical applications. Conventional latent variable methods typically model continuous brain dynamics through discretizing time with recurrent architecture, which necessarily results in compounded cumulative prediction errors and failure of capturing instantaneous, nonlinear characteristics of EEGs. We propose ODEBRAIN, a Neural ODE latent dynamic forecasting framework to overcome these challenges by integrating spatio-temporal-frequency features into spectral graph nodes, followed by a Neural ODE modeling the continuous latent dynamics. Our design ensures that latent representations can capture stochastic variations of complex brain states at any given time point. Extensive experiments verify that ODEBRAIN can improve significantly over existing methods in forecasting EEG dynamics with enhanced robustness and generalization capabilities.

### 🤖 AI 总结

**一句话总结**：ODEBrain通过将EEG构造成谱图节点并用Neural ODE建模连续时间潜在动力学，实现更稳健、更准确的EEG动态预测。

**研究动机**：传统离散时间的循环式潜变量模型需要时间离散化，易产生误差累积且难捕捉EEG瞬时的非线性动态特征。

**核心方法**：先融合时空-频率特征构建谱图节点表示脑网络，再在潜在空间中引入Neural ODE对连续时间动力学进行建模与预测，以在任意时间点刻画复杂脑状态的随机变化。

**主要结论**：实验结果表明，ODEBrain在EEG动态预测上显著优于现有方法，并表现出更强的鲁棒性与泛化能力。

**关键词**：EEG动态预测, 连续时间建模, 潜变量动态模型, 动态图神经网络, 脑网络建模, 谱图节点表示, 时空频特征融合, 非线性脑信号建模, 随机潜在状态表示

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23285v1) | [下载PDF](https://arxiv.org/pdf/2602.23285v1.pdf)

---

## [6. CXReasonAgent: Evidence-Grounded Diagnostic Reasoning Agent for Chest X-rays](https://arxiv.org/abs/2602.23276v1)

**作者**：Hyungyung Lee, Hangyul Yoon, Edward Choi  
**分类**：cs.AI  
**发布时间**：2026-02-26

### 📄 论文摘要

Chest X-ray plays a central role in thoracic diagnosis, and its interpretation inherently requires multi-step, evidence-grounded reasoning. However, large vision-language models (LVLMs) often generate plausible responses that are not faithfully grounded in diagnostic evidence and provide limited visual evidence for verification, while also requiring costly retraining to support new diagnostic tasks, limiting their reliability and adaptability in clinical settings. To address these limitations, we present CXReasonAgent, a diagnostic agent that integrates a large language model (LLM) with clinically grounded diagnostic tools to perform evidence-grounded diagnostic reasoning using image-derived diagnostic and visual evidence. To evaluate these capabilities, we introduce CXReasonDial, a multi-turn dialogue benchmark with 1,946 dialogues across 12 diagnostic tasks, and show that CXReasonAgent produces faithfully grounded responses, enabling more reliable and verifiable diagnostic reasoning than LVLMs. These findings highlight the importance of integrating clinically grounded diagnostic tools, particularly in safety-critical clinical settings.

### 🤖 AI 总结

**一句话总结**：CXReasonAgent 通过将LLM与临床诊断工具结合，在胸片多步推理中生成可由图像证据支撑、可验证的诊断对话结果。

**研究动机**：现有LVLM在胸片解读中容易产出“看似合理但缺乏证据支撑”的回答，且可视化证据不足以核验；同时为新任务适配常需昂贵再训练，影响临床可靠性与可扩展性。

**核心方法**：提出CXReasonAgent：用LLM作为推理与对话中枢，调用基于图像的诊断/视觉证据提取工具来支撑每一步诊断推理；并构建多轮对话评测集CXReasonDial（12项任务、1,946段对话）评估证据扎根与可验证性。

**主要结论**：在CXReasonDial上，CXReasonAgent 相比传统LVLM能生成更忠实于图像证据的回答并提供可核验的视觉依据，表明将临床诊断工具融入LLM代理对安全关键医疗场景尤为重要。

**关键词**：胸部X光, 胸部影像诊断, 多步诊断推理, 证据支撑推理, 视觉证据定位, 幻觉抑制, 多轮医学对话评测, 安全关键医疗AI

**评分**：50

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23276v1) | [下载PDF](https://arxiv.org/pdf/2602.23276v1.pdf)

---

## [7. Evaluating Stochasticity in Deep Research Agents](https://arxiv.org/abs/2602.23271v1)

**作者**：Haotian Zhai, Elias Stengel-Eskin, Pratik Patil 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-26

### 📄 论文摘要

Deep Research Agents (DRAs) are promising agentic systems that gather and synthesize information to support research across domains such as financial decision-making, medical analysis, and scientific discovery. Despite recent improvements in research quality (e.g., outcome accuracy when ground truth is available), DRA system design often overlooks a critical barrier to real-world deployment: stochasticity. Under identical queries, repeated executions of DRAs can exhibit substantial variability in terms of research outcome, findings, and citations. In this paper, we formalize the study of stochasticity in DRAs by modeling them as information acquisition Markov Decision Processes. We introduce an evaluation framework that quantifies variance in the system and identify three sources of it: information acquisition, information compression, and inference. Through controlled experiments, we investigate how stochasticity from these modules across different decision steps influences the variance of DRA outputs. Our results show that reducing stochasticity can improve research output quality, with inference and early-stage stochasticity contributing the most to DRA output variance. Based on these findings, we propose strategies for mitigating stochasticity while maintaining output quality via structured output and ensemble-based query generation. Our experiments on DeepSearchQA show that our proposed mitigation methods reduce average stochasticity by 22% while maintaining high research quality.

### 🤖 AI 总结

**一句话总结**：本文系统性评估深度研究代理（DRA）在同一问题下输出的随机性来源与影响，并提出降低随机性且不损质量的缓解策略。

**研究动机**：尽管DRA的平均研究质量在提升，但在真实部署中同样输入多次运行会产生显著不同的结论、依据与引用，导致结果不稳定、难以信任与复现。

**核心方法**：将DRA建模为信息获取的马尔可夫决策过程，提出量化输出方差的评估框架，并将随机性归因到信息获取、信息压缩与推理三模块，随后通过受控实验分析不同决策步（尤其早期）随机性对最终方差的贡献；最后用结构化输出与基于集成的查询生成来缓解随机性。

**主要结论**：降低随机性通常能提升研究输出质量，其中推理阶段与早期步骤的随机性对方差贡献最大；在DeepSearchQA上，所提方法在保持高质量的同时将平均随机性降低约22%。

**关键词**：深度研究代理, 随机性评估, 输出方差, 评测框架, 信息获取MDP, 马尔可夫决策过程, 信息获取, 信息压缩, 推理随机性, 结构化输出, 集成式查询生成

**评分**：40

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23271v1) | [下载PDF](https://arxiv.org/pdf/2602.23271v1.pdf)

---

## cs.CL

## [8. A Mixture-of-Experts Model for Multimodal Emotion Recognition in Conversations](https://arxiv.org/abs/2602.23300v1)

**作者**：Soumya Dutta, Smruthi Balaji, Sriram Ganapathy  
**分类**：cs.CL, eess.AS  
**发布时间**：2026-02-26

### 📄 论文摘要

Emotion Recognition in Conversations (ERC) presents unique challenges, requiring models to capture the temporal flow of multi-turn dialogues and to effectively integrate cues from multiple modalities. We propose Mixture of Speech-Text Experts for Recognition of Emotions (MiSTER-E), a modular Mixture-of-Experts (MoE) framework designed to decouple two core challenges in ERC: modality-specific context modeling and multimodal information fusion. MiSTER-E leverages large language models (LLMs) fine-tuned for both speech and text to provide rich utterance-level embeddings, which are then enhanced through a convolutional-recurrent context modeling layer. The system integrates predictions from three experts-speech-only, text-only, and cross-modal-using a learned gating mechanism that dynamically weighs their outputs. To further encourage consistency and alignment across modalities, we introduce a supervised contrastive loss between paired speech-text representations and a KL-divergence-based regulariza-tion across expert predictions. Importantly, MiSTER-E does not rely on speaker identity at any stage. Experiments on three benchmark datasets-IEMOCAP, MELD, and MOSI-show that our proposal achieves 70.9%, 69.5%, and 87.9% weighted F1-scores respectively, outperforming several baseline speech-text ERC systems. We also provide various ablations to highlight the contributions made in the proposed approach.

### 🤖 AI 总结

**一句话总结**：提出MiSTER-E混合专家框架，将语音/文本各自建模与跨模态融合解耦，用门控动态融合三类专家以提升对话情感识别性能。

**研究动机**：对话情感识别需要同时处理多轮上下文的时序依赖与多模态信息融合，现有方法常将两者耦合导致建模不够灵活且对齐不足。

**核心方法**：用分别针对语音与文本微调的LLM生成话语级表示，经卷积-循环上下文层增强；构建语音专家、文本专家与跨模态专家三路预测，并用学习到的gate加权融合，同时加入语音-文本监督对比损失与跨专家预测的KL正则以促进对齐一致，且不使用说话人身份信息。

**主要结论**：在IEMOCAP/MELD/MOSI上分别达到70.9/69.5/87.9的加权F1并优于多种基线，消融实验表明MoE门控融合与对比/KL正则对性能提升关键。

**关键词**：多模态情感识别, 语音-文本融合, 混合专家模型, 门控机制, 模态特定上下文建模, 卷积-循环上下文编码, 监督对比学习, KL散度正则化, 话语级表示学习, 无说话人身份建模

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23300v1) | [下载PDF](https://arxiv.org/pdf/2602.23300v1.pdf)

---

## [9. SPARTA: Scalable and Principled Benchmark of Tree-Structured Multi-hop QA over Text and Tables](https://arxiv.org/abs/2602.23286v1)

**作者**：Sungho Park, Jueun Kim, Wook-Shin Han  
**分类**：cs.CL, cs.AI, cs.DB, cs.IR  
**发布时间**：2026-02-26

### 📄 论文摘要

Real-world Table-Text question answering (QA) tasks require models that can reason across long text and source tables, traversing multiple hops and executing complex operations such as aggregation. Yet existing benchmarks are small, manually curated - and therefore error-prone - and contain shallow questions that seldom demand more than two hops or invoke aggregations, grouping, or other advanced analytical operations expressible in natural-language queries. We present SPARTA, an end-to-end construction framework that automatically generates large-scale Table-Text QA benchmarks with lightweight human validation, requiring only one quarter of the annotation time of HybridQA. The framework first constructs a reference fact database by enriching each source table with grounding tables whose tuples are atomic facts automatically extracted from the accompanying unstructured passages, then synthesizes nested queries whose number of nested predicates matches the desired hop count. To ensure that every SQL statement is executable and that its verbalization yields a fluent, human-sounding question, we propose two novel techniques: provenance-based refinement, which rewrites any syntactically valid query that returns a non-empty result, and realistic-structure enforcement, which confines generation to post-order traversals of the query graph. The resulting pipeline produces thousands of high-fidelity question-answer pairs covering aggregations, grouping, and deep multi-hop reasoning across text and tables. On SPARTA, state-of-the-art models that reach over 70 F1 on HybridQA or over 50 F1 on OTT-QA drop by more than 30 F1 points, exposing fundamental weaknesses in current cross-modal reasoning. Our benchmark, construction code, and baseline models are available at https://github.com/pshlego/SPARTA/tree/main.

### 🤖 AI 总结

**一句话总结**：提出SPARTA，一个可扩展、原则化的自动化构建框架，用于生成大规模、深层多跳且包含聚合/分组等操作的表格-文本联合问答基准，并揭示现有模型在该任务上的显著能力缺口。

**研究动机**：现有表格-文本QA基准规模小且人工构建易出错，问题多为浅层推理，较少覆盖>2跳与聚合、分组等复杂分析操作，难以真实评测跨文本与表格的多步推理能力。

**核心方法**：先将源表与文本段落对齐，自动从文本抽取原子事实形成“grounding tables”，构建可查询的参考事实库；再按目标hop数合成嵌套SQL/查询图，并用provenance-based refinement保证查询可执行且非空、用realistic-structure enforcement限制为查询图后序遍历以生成更自然流畅的问题，辅以轻量人工验证。

**主要结论**：SPARTA生成了覆盖深多跳与聚合/分组等操作的高保真QA数据集，标注成本约为HybridQA的四分之一；在该基准上SOTA模型相对HybridQA/OTT-QA的表现下降30+ F1，表明当前跨表-文推理模型仍存在根本性不足。

**关键词**：表格-文本问答, 多跳推理, 树结构查询, 问答基准构建, 自动数据生成, 轻量人工验证, 参考事实数据库, 原子事实抽取, SQL可执行性校验, 溯源式查询改写, 查询图后序遍历, 聚合与分组操作

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23286v1) | [下载PDF](https://arxiv.org/pdf/2602.23286v1.pdf)

---

## cs.CV

## [10. MediX-R1: Open Ended Medical Reinforcement Learning](https://arxiv.org/abs/2602.23363v1)

**作者**：Sahal Shaji Mullappilly, Mohammed Irfan Kurpath, Omair Mohamed 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-26

### 📄 论文摘要

We introduce MediX-R1, an open-ended Reinforcement Learning (RL) framework for medical multimodal large language models (MLLMs) that enables clinically grounded, free-form answers beyond multiple-choice formats. MediX-R1 fine-tunes a baseline vision-language backbone with Group Based RL and a composite reward tailored for medical reasoning: an LLM-based accuracy reward that judges semantic correctness with a strict YES/NO decision, a medical embedding-based semantic reward to capture paraphrases and terminology variants, and lightweight format and modality rewards that enforce interpretable reasoning and modality recognition. This multi-signal design provides stable, informative feedback for open-ended outputs where traditional verifiable or MCQ-only rewards fall short. To measure progress, we propose a unified evaluation framework for both text-only and image+text tasks that uses a Reference-based LLM-as-judge in place of brittle string-overlap metrics, capturing semantic correctness, reasoning, and contextual alignment. Despite using only $\sim51$K instruction examples, MediX-R1 achieves excellent results across standard medical LLM (text-only) and VLM (image + text) benchmarks, outperforming strong open-source baselines and delivering particularly large gains on open-ended clinical tasks. Our results demonstrate that open-ended RL with comprehensive reward signals and LLM-based evaluation is a practical path toward reliable medical reasoning in multimodal models. Our trained models, curated datasets and source code are available at https://medix.cvmbzuai.com

### 🤖 AI 总结

**一句话总结**：MediX-R1提出面向医学多模态大模型的开放式强化学习框架，通过多信号奖励与LLM评估，实现比选择题更贴近临床的自由文本回答与推理提升。

**研究动机**：现有医学RL训练与评测常依赖可验证答案或MCQ，难以为开放式临床回答提供稳定、有效的反馈与可靠的语义评估。

**核心方法**：在视觉-语言骨干上进行Group-based RL微调，设计复合奖励：LLM严格YES/NO语义正确性奖励、医学embedding语义奖励（覆盖同义改写/术语变体）、以及格式与模态识别奖励；同时提出统一评测，用reference-based LLM-as-judge替代脆弱的字符串匹配指标。

**主要结论**：仅用约51K指令数据，MediX-R1在文本与图文医学基准上优于强开源基线，尤其在开放式临床任务上提升显著，表明开放式RL+复合奖励+LLM评估是提升多模态医学推理可靠性的可行路径。

**关键词**：开放式强化学习, 医学多模态大模型, 视觉语言模型, 临床推理, 组式强化学习, 复合奖励函数, 奖励建模, 医学语义嵌入, 参考答案评测, 多模态识别奖励, 格式约束奖励

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23363v1) | [下载PDF](https://arxiv.org/pdf/2602.23363v1.pdf)

---

## [11. VGG-T$^3$: Offline Feed-Forward 3D Reconstruction at Scale](https://arxiv.org/abs/2602.23361v1)

**作者**：Sven Elflein, Ruilong Li, Sérgio Agostinho 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-26

### 📄 论文摘要

We present a scalable 3D reconstruction model that addresses a critical limitation in offline feed-forward methods: their computational and memory requirements grow quadratically w.r.t. the number of input images. Our approach is built on the key insight that this bottleneck stems from the varying-length Key-Value (KV) space representation of scene geometry, which we distill into a fixed-size Multi-Layer Perceptron (MLP) via test-time training. VGG-T$^3$ (Visual Geometry Grounded Test Time Training) scales linearly w.r.t. the number of input views, similar to online models, and reconstructs a $1k$ image collection in just $54$ seconds, achieving a $11.6\times$ speed-up over baselines that rely on softmax attention. Since our method retains global scene aggregation capability, our point map reconstruction error outperforming other linear-time methods by large margins. Finally, we demonstrate visual localization capabilities of our model by querying the scene representation with unseen images.

### 🤖 AI 总结

**一句话总结**：VGG-T³通过将可变长度的几何KV表示在测试时蒸馏为固定大小MLP，使离线前馈3D重建在输入视角数上实现线性扩展并显著加速。

**研究动机**：现有离线前馈3D重建方法因基于softmax注意力的全局聚合导致计算与内存随图像数量二次增长，难以扩展到上千张图像的场景。

**核心方法**：洞察瓶颈来自可变长度的Key-Value几何表示，提出Visual Geometry Grounded Test Time Training：在测试阶段训练/蒸馏一个固定容量的MLP来承载全局场景信息，从而在保持全局聚合能力的同时将复杂度降为线性。

**主要结论**：该方法可在54秒内重建1k图像集合，相比注意力基线提速11.6×，并在点图重建误差上显著优于其他线性时间方法，同时支持用未见图像查询场景表示进行视觉定位。

**关键词**：多视图3D重建, 离线前馈重建, 线性时间扩展, 测试时训练（TTT）, KV空间蒸馏, 固定大小场景表示, 多层感知机（MLP）, 全局场景聚合, 软最大注意力替代, 点图（point map）重建

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23361v1) | [下载PDF](https://arxiv.org/pdf/2602.23361v1.pdf)

---

## [12. Sensor Generalization for Adaptive Sensing in Event-based Object Detection via Joint Distribution Training](https://arxiv.org/abs/2602.23357v1)

**作者**：Aheli Saha, René Schuster, Didier Stricker  
**分类**：cs.CV  
**发布时间**：2026-02-26

### 📄 论文摘要

Bio-inspired event cameras have recently attracted significant research due to their asynchronous and low-latency capabilities. These features provide a high dynamic range and significantly reduce motion blur. However, because of the novelty in the nature of their output signals, there is a gap in the variability of available data and a lack of extensive analysis of the parameters characterizing their signals. This paper addresses these issues by providing readers with an in-depth understanding of how intrinsic parameters affect the performance of a model trained on event data, specifically for object detection. We also use our findings to expand the capabilities of the downstream model towards sensor-agnostic robustness.

### 🤖 AI 总结

**一句话总结**：论文研究事件相机的内在传感参数如何影响事件流目标检测，并通过联合分布训练提升模型对不同传感器/参数设置的鲁棒泛化能力。

**研究动机**：事件相机数据形态新颖且可用数据与参数分析不足，导致模型对传感器参数变化敏感、跨设备/配置泛化差；因此需要系统理解参数影响并构建传感器无关的稳健检测器。

**核心方法**：系统考察事件相机信号的关键内参（如触发阈值、噪声/事件率相关设置等）对检测性能的作用规律，并据此在训练时对多种参数分布进行“联合分布训练”，让模型在多配置数据上共同学习以获得适应性与传感器泛化。

**主要结论**：不同内参会显著改变事件分布并影响检测精度与稳定性；采用联合分布训练可提升对参数漂移与跨传感器差异的鲁棒性，使下游目标检测更接近传感器无关的泛化表现。

**关键词**：事件相机, 事件视觉, 事件流目标检测, 自适应感知, 传感器泛化, 传感器无关鲁棒性, 内参敏感性分析, 联合分布训练, 领域泛化, 异步成像

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23357v1) | [下载PDF](https://arxiv.org/pdf/2602.23357v1.pdf)

---

## [13. Retrieve and Segment: Are a Few Examples Enough to Bridge the Supervision Gap in Open-Vocabulary Segmentation?](https://arxiv.org/abs/2602.23339v1)

**作者**：Tilemachos Aravanis, Vladan Stojnić, Bill Psomas 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-26

### 📄 论文摘要

Open-vocabulary segmentation (OVS) extends the zero-shot recognition capabilities of vision-language models (VLMs) to pixel-level prediction, enabling segmentation of arbitrary categories specified by text prompts. Despite recent progress, OVS lags behind fully supervised approaches due to two challenges: the coarse image-level supervision used to train VLMs and the semantic ambiguity of natural language. We address these limitations by introducing a few-shot setting that augments textual prompts with a support set of pixel-annotated images. Building on this, we propose a retrieval-augmented test-time adapter that learns a lightweight, per-image classifier by fusing textual and visual support features. Unlike prior methods relying on late, hand-crafted fusion, our approach performs learned, per-query fusion, achieving stronger synergy between modalities. The method supports continually expanding support sets, and applies to fine-grained tasks such as personalized segmentation. Experiments show that we significantly narrow the gap between zero-shot and supervised segmentation while preserving open-vocabulary ability.

### 🤖 AI 总结

**一句话总结**：提出一种“检索+测试时适配”的少样本开放词汇分割方法，通过融合文本提示与少量像素标注支持样本，显著缩小零样本与全监督分割的性能差距。

**研究动机**：现有开放词汇分割依赖VLM的图像级弱监督且自然语言语义易歧义，导致像素级分割性能落后于全监督；作者希望用少量像素标注示例在不丢失开放词汇能力的前提下补足监督缺口。

**核心方法**：在测试时从可扩展的支持集检索与当前查询相关的像素标注样本，并用轻量级适配器为“每张图”学习一个分类器，将文本特征与支持图像的视觉特征进行可学习的、按查询动态的融合（而非手工晚期融合），再输出分割结果。

**主要结论**：该方法在保持开放词汇泛化的同时显著提升分割精度、缩小与全监督方法的差距；并支持持续扩充支持集，适用于细粒度/个性化分割等场景。

**关键词**：开放词汇分割, 少样本分割, 零样本分割, 视觉语言模型, 检索增强, 测试时适配, 像素级标注, 多模态特征融合, 逐查询融合, 个性化分割

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23339v1) | [下载PDF](https://arxiv.org/pdf/2602.23339v1.pdf)

---

## [14. ThinkOmni: Lifting Textual Reasoning to Omni-modal Scenarios via Guidance Decoding](https://arxiv.org/abs/2602.23306v1)

**作者**：Yiran Guan, Sifan Tu, Dingkang Liang 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-26

### 📄 论文摘要

Omni-modal reasoning is essential for intelligent systems to understand and draw inferences from diverse data sources. While existing omni-modal large language models (OLLM) excel at perceiving diverse modalities, they lack the complex reasoning abilities of recent large reasoning models (LRM). However, enhancing the reasoning ability of OLLMs through additional training presents significant challenges, including the need for high-quality data, task-specific adaptation, and substantial computational costs. To address these limitations, we propose ThinkOmni, a training-free and data-free framework that lifts textual reasoning to omni-modal scenarios. ThinkOmni introduces two key components: 1) LRM-as-a-Guide, which leverages off-the-shelf LRMs to guide the OLLM decoding process; 2) Stepwise Contrastive Scaling, which adaptively balances perception and reasoning signals without manual hyperparameter tuning. Experiments on six multi-modal reasoning benchmarks demonstrate that ThinkOmni consistently delivers performance improvements, with main results achieving 70.2 on MathVista and 75.5 on MMAU. Overall, ThinkOmni offers a flexible and generalizable solution for omni-modal reasoning and provides new insights into the generalization and application of reasoning capabilities.

### 🤖 AI 总结

**一句话总结**：ThinkOmni提出一种无需训练、无需数据的解码框架，用现成大推理模型指导全模态大模型，从而显著提升多模态推理能力。

**研究动机**：现有全模态大模型感知强但推理弱，而通过再训练增强推理需要高质量数据、任务适配与高算力，成本和门槛都很高。

**核心方法**：框架包含两部分：用“LRM-as-a-Guide”在解码时引入现成LRM的推理引导信号；并用“Stepwise Contrastive Scaling”按步骤自适应平衡感知与推理贡献，避免手动调参。

**主要结论**：在六个多模态推理基准上方法稳定提升性能，主结果在MathVista达70.2、MMAU达75.5，证明训练/数据自由的引导式解码可有效将文本推理迁移到全模态场景。

**关键词**：全模态推理, 多模态推理, 全模态大语言模型（OLLM）, 大推理模型（LRM）, LRM 引导解码, 感知-推理权衡, 多模态推理基准, ThinkOmni

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23306v1) | [下载PDF](https://arxiv.org/pdf/2602.23306v1.pdf)

---

## [15. PRIMA: Pre-training with Risk-integrated Image-Metadata Alignment for Medical Diagnosis via LLM](https://arxiv.org/abs/2602.23297v1)

**作者**：Yiqing Wang, Chunming He, Ming-Chen Lu 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-26

### 📄 论文摘要

Medical diagnosis requires the effective synthesis of visual manifestations and clinical metadata. However, existing methods often treat metadata as isolated tags, failing to exploit the rich semantic knowledge embedded in clinical descriptions. We propose PRIMA (Pre-training with Risk-integrated Image-Metadata Alignment), a framework that integrates domain-specific knowledge into multi-modal representation learning. We first curate an expert corpus of risk-disease correlations via Retrieval-Augmented Generation (RAG) to refine Clinical ModernBERT, embedding diagnostic priors into the text encoder. To bridge the modality gap, we introduce a dual-encoder pre-training strategy utilizing DINOv3 and our refined BERT, optimized by a suite of four complementary loss functions. These losses are designed to capture multi-granular semantic alignment and handle the ambiguity of clinical correlations through soft labels. Finally, we leverage Qwen-3 to fuse these aligned features for precise disease classification. Extensive experiments demonstrate that PRIMA effectively harmonizes pixel-level features with abstract clinical expertise, significantly outperforming other state-of-the-art methods. Notably, our framework achieves superior robustness without the need for massive data collection or exhaustive computational resources. Our code will be made public upon acceptance.

### 🤖 AI 总结

**一句话总结**：PRIMA通过将风险-疾病先验知识注入文本编码器并与图像特征进行多粒度对齐预训练，再用LLM融合实现更准确且更鲁棒的医学诊断分类。

**研究动机**：现有多模态诊断方法往往把临床元数据当作离散标签，难以利用临床描述中蕴含的风险与诊断语义先验，导致图文/元数据对齐不足与泛化受限。

**核心方法**：先用RAG构建风险-疾病相关的专家语料以精炼Clinical ModernBERT（注入诊断先验），再以DINOv3+精炼BERT的双编码器进行预训练，并用四种互补损失实现多粒度语义对齐与软标签处理相关性歧义；最后用Qwen-3融合对齐后的特征进行疾病分类。

**主要结论**：实验表明PRIMA在分类性能与鲁棒性上显著优于SOTA，能够把像素级视觉线索与抽象临床知识有效统一，同时不依赖超大规模数据或极高算力。

**关键词**：医学影像诊断, 临床元数据, 图文对齐, 多模态预训练, 双编码器, 检索增强生成（RAG）, 风险-疾病关联, 诊断先验, 软标签, 多粒度语义对齐, 特征融合

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23297v1) | [下载PDF](https://arxiv.org/pdf/2602.23297v1.pdf)

---

## [16. ManifoldGD: Training-Free Hierarchical Manifold Guidance for Diffusion-Based Dataset Distillation](https://arxiv.org/abs/2602.23295v1)

**作者**：Ayush Roy, Wei-Yang Alex Lee, Rudrasis Chakraborty 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-02-26

### 📄 论文摘要

In recent times, large datasets hinder efficient model training while also containing redundant concepts. Dataset distillation aims to synthesize compact datasets that preserve the knowledge of large-scale training sets while drastically reducing storage and computation. Recent advances in diffusion models have enabled training-free distillation by leveraging pre-trained generative priors; however, existing guidance strategies remain limited. Current score-based methods either perform unguided denoising or rely on simple mode-based guidance toward instance prototype centroids (IPC centroids), which often are rudimentary and suboptimal. We propose Manifold-Guided Distillation (ManifoldGD), a training-free diffusion-based framework that integrates manifold consistent guidance at every denoising timestep. Our method employs IPCs computed via a hierarchical, divisive clustering of VAE latent features, yielding a multi-scale coreset of IPCs that captures both coarse semantic modes and fine intra-class variability. Using a local neighborhood of the extracted IPC centroids, we create the latent manifold for each diffusion denoising timestep. At each denoising step, we project the mode-alignment vector onto the local tangent space of the estimated latent manifold, thus constraining the generation trajectory to remain manifold-faithful while preserving semantic consistency. This formulation improves representativeness, diversity, and image fidelity without requiring any model retraining. Empirical results demonstrate consistent gains over existing training-free and training-based baselines in terms of FID, l2 distance among real and synthetic dataset embeddings, and classification accuracy, establishing ManifoldGD as the first geometry-aware training-free data distillation framework.

### 🤖 AI 总结

**一句话总结**：ManifoldGD提出一种无需训练的扩散式数据蒸馏方法，通过在每个去噪步加入“流形一致”的几何约束，引导生成更代表性且更高保真的小型合成数据集。

**研究动机**：现有training-free扩散蒸馏多为无引导去噪或仅向类原型/IPC质心做简单模式对齐，导致引导过于粗糙、难以兼顾语义一致性与类内多样性。作者希望利用预训练生成先验的同时，引入更精细的几何结构约束来提升蒸馏质量而不再训练模型。

**核心方法**：先在VAE潜特征上做层次化（divisive）聚类得到多尺度IPC coresets，覆盖粗粒度语义模态与细粒度类内变化；在扩散每个去噪时刻用IPC局部邻域估计潜空间局部流形，并将“模式对齐向量”投影到该流形的局部切空间上，使采样轨迹沿流形前进、保持语义一致且不偏离数据几何结构。

**主要结论**：在无需任何模型重训练的前提下，ManifoldGD相较现有training-free与training-based蒸馏基线，在FID、真实/合成嵌入的l2距离以及下游分类精度上均取得稳定提升，表明几何感知的流形引导能显著增强蒸馏数据的代表性、多样性与保真度。

**关键词**：数据集蒸馏, 无训练蒸馏, Diffusion, 分数匹配扩散, 流形引导, 潜空间流形, 切空间投影, 实例原型中心（IPC）, 层次聚类, VAE 潜特征, 多尺度核心集（coreset）

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23295v1) | [下载PDF](https://arxiv.org/pdf/2602.23295v1.pdf)

---

## [17. Towards Long-Form Spatio-Temporal Video Grounding](https://arxiv.org/abs/2602.23294v1)

**作者**：Xin Gu, Bing Fan, Jiali Yao 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-26

### 📄 论文摘要

In real scenarios, videos can span several minutes or even hours. However, existing research on spatio-temporal video grounding (STVG), given a textual query, mainly focuses on localizing targets in short videos of tens of seconds, typically less than one minute, which limits real-world applications. In this paper, we explore Long-Form STVG (LF-STVG), which aims to locate targets in long-term videos. Compared with short videos, long-term videos contain much longer temporal spans and more irrelevant information, making it difficult for existing STVG methods that process all frames at once. To address this challenge, we propose an AutoRegressive Transformer architecture for LF-STVG, termed ART-STVG. Unlike conventional STVG methods that require the entire video sequence to make predictions at once, ART-STVG treats the video as streaming input and processes frames sequentially, enabling efficient handling of long videos. To model spatio-temporal context, we design spatial and temporal memory banks and apply them to the decoders. Since memories from different moments are not always relevant to the current frame, we introduce simple yet effective memory selection strategies to provide more relevant information to the decoders, significantly improving performance. Furthermore, instead of parallel spatial and temporal localization, we propose a cascaded spatio-temporal design that connects the spatial decoder to the temporal decoder, allowing fine-grained spatial cues to assist complex temporal localization in long videos. Experiments on newly extended LF-STVG datasets show that ART-STVG significantly outperforms state-of-the-art methods, while achieving competitive performance on conventional short-form STVG.

### 🤖 AI 总结

**一句话总结**：提出面向长视频的自回归Transformer框架ART-STVG，以流式逐帧处理与记忆机制实现长时空视频目标定位，并显著优于现有方法。

**研究动机**：现有STVG方法主要针对短视频并常需一次性处理全帧，难以应对长视频中更长时间跨度与大量无关内容带来的计算与定位困难。

**核心方法**：ART-STVG将视频视为流式输入进行自回归顺序建模，设计空间/时间记忆库为解码器提供跨帧上下文，并通过记忆选择策略过滤不相关历史信息；同时采用级联时空定位结构，用空间解码器的细粒度线索辅助更复杂的时间定位。

**主要结论**：在新扩展的长视频LF-STVG数据集上，ART-STVG相较SOTA取得显著性能提升，并在传统短视频STVG任务上保持有竞争力的表现，验证了流式自回归与记忆选择/级联设计的有效性。

**关键词**：长视频时空视频定位, 时空视频定位, 视频目标定位, 流式视频处理, 记忆库机制, 记忆选择策略, 级联时空解码, 空间解码器, 时间解码器, 长时序建模, 长视频数据集扩展

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23294v1) | [下载PDF](https://arxiv.org/pdf/2602.23294v1.pdf)

---

## [18. PGVMS: A Prompt-Guided Unified Framework for Virtual Multiplex IHC Staining with Pathological Semantic Learning](https://arxiv.org/abs/2602.23292v1)

**作者**：Fuqiang Chen, Ranran Zhang, Wanming Hu 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-26

### 📄 论文摘要

Immunohistochemical (IHC) staining enables precise molecular profiling of protein expression, with over 200 clinically available antibody-based tests in modern pathology. However, comprehensive IHC analysis is frequently limited by insufficient tissue quantities in small biopsies. Therefore, virtual multiplex staining emerges as an innovative solution to digitally transform H&E images into multiple IHC representations, yet current methods still face three critical challenges: (1) inadequate semantic guidance for multi-staining, (2) inconsistent distribution of immunochemistry staining, and (3) spatial misalignment across different stain modalities. To overcome these limitations, we present a prompt-guided framework for virtual multiplex IHC staining using only uniplex training data (PGVMS). Our framework introduces three key innovations corresponding to each challenge: First, an adaptive prompt guidance mechanism employing a pathological visual language model dynamically adjusts staining prompts to resolve semantic guidance limitations (Challenge 1). Second, our protein-aware learning strategy (PALS) maintains precise protein expression patterns by direct quantification and constraint of protein distributions (Challenge 2). Third, the prototype-consistent learning strategy (PCLS) establishes cross-image semantic interaction to correct spatial misalignments (Challenge 3).

### 🤖 AI 总结

**一句话总结**：PGVMS提出一种由病理视觉语言模型提示引导的统一框架，仅用单染（uniplex）训练数据即可从H&E图像生成多种IHC虚拟染色，并提升语义一致性、蛋白分布准确性与跨模态对齐。

**研究动机**：临床IHC检测虽丰富，但小活检组织量不足限制了多重IHC分析；现有虚拟多重染色方法在语义指导不足、染色分布不一致以及不同染色模态空间错位上仍存在关键瓶颈。

**核心方法**：框架以自适应提示机制为核心，借助病理视觉语言模型动态调整染色提示以提供多染语义引导；同时引入PALS直接量化并约束蛋白表达分布以稳定免疫化学染色强度/模式，并用PCLS通过跨图像语义交互与原型一致性学习纠正不同染色模态间的空间不对齐。

**主要结论**：PGVMS在仅使用单染数据训练的条件下，能够更可靠地生成多种IHC虚拟染色结果，并在语义可控性、蛋白表达分布一致性与跨模态空间对齐方面缓解了现有方法的三类核心问题。

**关键词**：虚拟多重IHC染色, 数字病理, 提示引导学习, 病理视觉语言模型, 单重染色训练, 蛋白表达分布约束, 蛋白感知学习, 原型一致性学习, 跨染色模态配准, 多染色语义引导

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23292v1) | [下载PDF](https://arxiv.org/pdf/2602.23292v1.pdf)

---

## [19. LineGraph2Road: Structural Graph Reasoning on Line Graphs for Road Network Extraction](https://arxiv.org/abs/2602.23290v1)

**作者**：Zhengyang Wei, Renzhi Jing, Yiyi He 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-26

### 📄 论文摘要

The accurate and automatic extraction of roads from satellite imagery is critical for applications in navigation and urban planning, significantly reducing the need for manual annotation. Many existing methods decompose this task into keypoint extraction and connectedness prediction, but often struggle to capture long-range dependencies and complex topologies. Here, we propose LineGraph2Road, a framework that improves connectedness prediction by formulating it as binary classification over edges in a constructed global but sparse Euclidean graph, where nodes are keypoints extracted from segmentation masks and edges connect node pairs within a predefined distance threshold, representing potential road segments. To better learn structural link representation, we transform the original graph into its corresponding line graph and apply a Graph Transformer on it for connectedness prediction. This formulation overcomes the limitations of endpoint-embedding fusion on set-isomorphic links, enabling rich link representations and effective relational reasoning over the global structure. Additionally, we introduce an overpass/underpass head to resolve multi-level crossings and a coupled NMS strategy to preserve critical connections. We evaluate LineGraph2Road on three benchmarks: City-scale, SpaceNet, and Global-scale, and show that it achieves state-of-the-art results on two key metrics, TOPO-F1 and APLS. It also captures fine visual details critical for real-world deployment. We will make our code publicly available.

### 🤖 AI 总结

**一句话总结**：LineGraph2Road通过将道路连通性预测转化为线图上的结构化图推理，用Graph Transformer更准确地恢复复杂道路拓扑。

**研究动机**：现有“关键点+连通性”范式往往难以建模长程依赖与复杂拓扑（如多分支、交叉），且对边端点特征融合在同构链接上表达受限，导致连接预测不稳。

**核心方法**：先从分割掩码提取关键点，并在全局但稀疏的欧氏图中连接距离阈值内的点对形成候选道路边，再将该图转换为线图（把“边”变成“点”）并在其上用Graph Transformer进行二分类以判断边是否为真实道路连接；同时加入立交/下穿判别头处理多层交叉，并用耦合NMS保留关键连接。

**主要结论**：在City-scale、SpaceNet与Global-scale三套基准上，该方法在TOPO-F1与APLS等指标上取得（部分）SOTA表现，并能更好保留真实场景中细粒度道路细节与拓扑连通性。

**关键词**：道路网络提取, 卫星影像, 拓扑感知分割, 关键点检测, 连通性预测, 欧氏图, 结构化图推理, 多层交叉（立交）建模, 非极大值抑制（NMS）

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23290v1) | [下载PDF](https://arxiv.org/pdf/2602.23290v1.pdf)

---

## cs.LG

## [20. Model Agreement via Anchoring](https://arxiv.org/abs/2602.23360v1)

**作者**：Eric Eaton, Surbhi Goel, Marcel Hussing 等 7 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-26

### 📄 论文摘要

Numerous lines of aim to control $\textit{model disagreement}$ -- the extent to which two machine learning models disagree in their predictions. We adopt a simple and standard notion of model disagreement in real-valued prediction problems, namely the expected squared difference in predictions between two models trained on independent samples, without any coordination of the training processes. We would like to be able to drive disagreement to zero with some natural parameter(s) of the training procedure using analyses that can be applied to existing training methodologies.   We develop a simple general technique for proving bounds on independent model disagreement based on $\textit{anchoring}$ to the average of two models within the analysis. We then apply this technique to prove disagreement bounds for four commonly used machine learning algorithms: (1) stacked aggregation over an arbitrary model class (where disagreement is driven to 0 with the number of models $k$ being stacked) (2) gradient boosting (where disagreement is driven to 0 with the number of iterations $k$) (3) neural network training with architecture search (where disagreement is driven to 0 with the size $n$ of the architecture being optimized over) and (4) regression tree training over all regression trees of fixed depth (where disagreement is driven to 0 with the depth $d$ of the tree architecture). For clarity, we work out our initial bounds in the setting of one-dimensional regression with squared error loss -- but then show that all of our results generalize to multi-dimensional regression with any strongly convex loss.

### 🤖 AI 总结

**一句话总结**：论文提出一种“锚定(anchoring)”分析技巧来上界独立训练模型之间的预测分歧，并证明在多种常用算法中分歧可随关键训练参数增大而趋近于0。

**研究动机**：在不协调训练过程、仅依赖独立采样训练的前提下，作者希望用可适用于现有训练方法的分析，解释并控制两个模型预测不一致（分歧）的程度，理想情况下可将分歧驱动到0。

**核心方法**：以回归任务中“两个独立训练模型预测之差的期望平方”作为分歧度量，在证明中将两个模型锚定到其平均模型以获得一般性分歧上界；先在一维平方损失下推导，再推广到多维回归与任意强凸损失，并分别实例化到stacking、gradient boosting、带架构搜索的神经网络训练、固定深度回归树训练。

**主要结论**：作者给出四类算法的分歧收敛结论：stacking随集成模型数k增大、boosting随迭代次数k增大、架构搜索随候选架构规模n增大、回归树随深度d增大，模型分歧均可被驱动趋近0；且这些结果不局限于平方损失的一维设定，可推广到更一般的强凸损失多维回归。

**关键词**：模型分歧, 独立训练, 预测差异平方期望, 分歧上界, 神经架构搜索（NAS）, 回归树深度, 强凸损失, 多维回归

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23360v1) | [下载PDF](https://arxiv.org/pdf/2602.23360v1.pdf)

---

## [21. A Dataset is Worth 1 MB](https://arxiv.org/abs/2602.23358v1)

**作者**：Elad Kimchi Shoshani, Leeyam Gabay, Yedid Hoshen  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-02-26

### 📄 论文摘要

A dataset server must often distribute the same large payload to many clients, incurring massive communication costs. Since clients frequently operate on diverse hardware and software frameworks, transmitting a pre-trained model is often infeasible; instead, agents require raw data to train their own task-specific models locally. While dataset distillation attempts to compress training signals, current methods struggle to scale to high-resolution data and rarely achieve sufficiently small files. In this paper, we propose Pseudo-Labels as Data (PLADA), a method that completely eliminates pixel transmission. We assume agents are preloaded with a large, generic, unlabeled reference dataset (e.g., ImageNet-1K, ImageNet-21K) and communicate a new task by transmitting only the class labels for specific images. To address the distribution mismatch between the reference and target datasets, we introduce a pruning mechanism that filters the reference dataset to retain only the labels of the most semantically relevant images for the target task. This selection process simultaneously maximizes training efficiency and minimizes transmission payload. Experiments on 10 diverse datasets demonstrate that our approach can transfer task knowledge with a payload of less than 1 MB while retaining high classification accuracy, offering a promising solution for efficient dataset serving.

### 🤖 AI 总结

**一句话总结**：PLADA 通过只传输参考数据集中特定图片的类别标签（不传像素），在小于 1MB 的通信开销下实现跨任务的高精度分类知识传递。

**研究动机**：数据集服务器向多客户端分发大规模原始数据通信成本极高，而直接下发预训练模型又因客户端软硬件差异常不可行；现有数据蒸馏方法难以扩展到高分辨率且压缩率不足。

**核心方法**：假设客户端已预置一个大型通用无标注参考数据集，服务器用“伪标签即数据”的方式仅发送部分参考图像的类别标签来表达新任务；并用剪枝/筛选机制选出与目标任务语义最相关的参考子集以缓解分布不匹配并进一步降低传输量。

**主要结论**：在 10 个多样化数据集上，PLADA 以低于 1MB 的载荷实现有效任务迁移并保持较高分类准确率，显示出面向高效数据集服务的实用潜力。

**关键词**：数据集分发, 通信开销压缩, 标签传输, 伪标签数据化（PLADA）, 参考数据集预加载, 语义相关样本筛选, 数据集剪枝, 分布偏移适配, 数据集蒸馏, 高分辨率数据压缩, 本地训练

**评分**：38

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23358v1) | [下载PDF](https://arxiv.org/pdf/2602.23358v1.pdf)

---

## [22. SOTAlign: Semi-Supervised Alignment of Unimodal Vision and Language Models via Optimal Transport](https://arxiv.org/abs/2602.23353v1)

**作者**：Simon Roschmann, Paul Krzakala, Sonia Mazelet 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-26

### 📄 论文摘要

The Platonic Representation Hypothesis posits that neural networks trained on different modalities converge toward a shared statistical model of the world. Recent work exploits this convergence by aligning frozen pretrained vision and language models with lightweight alignment layers, but typically relies on contrastive losses and millions of paired samples. In this work, we ask whether meaningful alignment can be achieved with substantially less supervision. We introduce a semi-supervised setting in which pretrained unimodal encoders are aligned using a small number of image-text pairs together with large amounts of unpaired data. To address this challenge, we propose SOTAlign, a two-stage framework that first recovers a coarse shared geometry from limited paired data using a linear teacher, then refines the alignment on unpaired samples via an optimal-transport-based divergence that transfers relational structure without overconstraining the target space. Unlike existing semi-supervised methods, SOTAlign effectively leverages unpaired images and text, learning robust joint embeddings across datasets and encoder pairs, and significantly outperforming supervised and semi-supervised baselines.

### 🤖 AI 总结

**一句话总结**：SOTAlign提出一种半监督对齐框架，用少量图文配对数据结合大量非配对数据，通过最优传输在冻结的视觉/语言编码器间学习稳健的联合嵌入。

**研究动机**：现有对齐方法多依赖对比学习与海量配对图文样本，监督成本高；作者探讨能否在显著更少配对监督下仍获得有意义的跨模态对齐。

**核心方法**：两阶段：先用少量配对数据训练线性“教师”恢复粗共享几何并初始化对齐；再用基于最优传输的散度在非配对图像与文本上进行细化，对齐关系结构而不过度约束目标表示空间。

**主要结论**：SOTAlign能有效利用非配对数据，在不同数据集与不同编码器组合上学习更鲁棒的联合表示，并显著优于纯监督及其他半监督基线方法。

**关键词**：半监督对齐, 视觉-语言模型对齐, 单模态编码器, 冻结预训练模型, 图文对齐, 非配对数据, 少样本监督, 最优传输, 最优传输散度, 教师-学生框架, 联合嵌入空间

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23353v1) | [下载PDF](https://arxiv.org/pdf/2602.23353v1.pdf)

---

## [23. FlashOptim: Optimizers for Memory Efficient Training](https://arxiv.org/abs/2602.23349v1)

**作者**：Jose Javier Gonzalez Ortiz, Abhay Gupta, Chris Renard 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-26

### 📄 论文摘要

Standard mixed-precision training of neural networks requires many bytes of accelerator memory for each model parameter. These bytes reflect not just the parameter itself, but also its gradient and one or more optimizer state variables. With each of these values typically requiring 4 bytes, training even a 7 billion parameter model can be impractical for researchers with less than 100GB of accelerator memory.   We introduce FlashOptim, a suite of optimizations that reduces per-parameter memory by over 50% while preserving model quality and API compatibility. Our approach introduces two key techniques. First, we improve master weight splitting by finding and exploiting a tight bound on its quantization error. Second, we design companding functions that greatly reduce the error in 8-bit optimizer state quantization. Together with 16-bit gradients, these techniques reduce AdamW memory from 16 bytes to 7 bytes per parameter, or 5 bytes with gradient release. They also cut model checkpoint sizes by more than half.   Experiments with FlashOptim applied to SGD, AdamW, and Lion show no measurable quality degradation on any task from a collection of standard vision and language benchmarks, including Llama-3.1-8B finetuning.

### 🤖 AI 总结

**一句话总结**：FlashOptim 通过改进主权重切分与8-bit优化器状态量化，将混合精度训练的每参数内存占用降低50%以上且基本不损失模型效果。

**研究动机**：标准混合精度训练除参数外还需保存梯度与优化器状态，导致每参数内存开销很高，使得中大型模型在<100GB显存下训练/微调困难。

**核心方法**：提出两项关键技术：利用更紧的量化误差上界改进master weight splitting，以及设计companding（压扩）函数以显著降低8-bit优化器状态量化误差；配合16-bit梯度将AdamW从16B/参数降至7B（梯度释放可到5B），并减少checkpoint体积。

**主要结论**：在SGD、AdamW与Lion上，FlashOptim在多种视觉与语言基准（含Llama-3.1-8B微调）中未观察到可测的质量退化，同时显著节省训练与存储内存。

**关键词**：混合精度训练, 训练内存优化, 每参数内存开销, 优化器状态量化, 8-bit 量化, 主权重分裂, 量化误差界, 16-bit 梯度, 梯度释放, 模型检查点压缩

**评分**：37

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23349v1) | [下载PDF](https://arxiv.org/pdf/2602.23349v1.pdf)

---

## [24. Mean Estimation from Coarse Data: Characterizations and Efficient Algorithms](https://arxiv.org/abs/2602.23341v1)

**作者**：Alkis Kalavasis, Anay Mehrotra, Manolis Zampetakis 等 5 位作者  
**分类**：cs.LG, cs.DS, math.ST, stat.ML  
**发布时间**：2026-02-26

### 📄 论文摘要

Coarse data arise when learners observe only partial information about samples; namely, a set containing the sample rather than its exact value. This occurs naturally through measurement rounding, sensor limitations, and lag in economic systems. We study Gaussian mean estimation from coarse data, where each true sample $x$ is drawn from a $d$-dimensional Gaussian distribution with identity covariance, but is revealed only through the set of a partition containing $x$. When the coarse samples, roughly speaking, have ``low'' information, the mean cannot be uniquely recovered from observed samples (i.e., the problem is not identifiable). Recent work by Fotakis, Kalavasis, Kontonis, and Tzamos [FKKT21] established that sample-efficient mean estimation is possible when the unknown mean is identifiable and the partition consists of only convex sets. Moreover, they showed that without convexity, mean estimation becomes NP-hard. However, two fundamental questions remained open: (1) When is the mean identifiable under convex partitions? (2) Is computationally efficient estimation possible under identifiability and convex partitions? This work resolves both questions. [...]

### 🤖 AI 总结

**一句话总结**：本文研究在“只观察到样本落在哪个分区集合中”的粗粒度观测下的高斯均值估计，给出了凸分区下均值可辨识性的刻画，并在可辨识时提供了计算高效的估计算法。

**研究动机**：粗数据在测量取整、传感器限制等场景中常见，会导致均值可能无法从观测中唯一恢复；此前工作虽指出凸分区下可样本高效、非凸时NP难，但尚不清楚“何时可辨识”以及“可辨识时是否能多项式时间估计”。

**核心方法**：作者在凸分区设定中推导均值可辨识的充要条件（从分区几何/信息量角度刻画观测对均值的约束强度），并在满足可辨识条件时设计多项式时间的估计流程（在粗观测诱导的约束下进行可计算的参数恢复/优化）。

**主要结论**：工作完整回答了两大开放问题：在凸分区下给出可辨识性的精确刻画，并证明在可辨识时不仅统计上可估计，而且存在计算高效的算法实现；同时也强化了“缺乏结构（如非凸）会导致计算困难”的边界。

**关键词**：粗粒度数据, 集合值观测, 高斯均值估计, 可识别性, 凸划分, 低信息观测, 样本复杂度, 计算高效算法, NP难度, 部分信息学习, 身份协方差高斯

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23341v1) | [下载PDF](https://arxiv.org/pdf/2602.23341v1.pdf)

---

## [25. Differentiable Zero-One Loss via Hypersimplex Projections](https://arxiv.org/abs/2602.23336v1)

**作者**：Camilo Gomez, Pengyang Wang, Liansheng Tang  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-02-26

### 📄 论文摘要

Recent advances in machine learning have emphasized the integration of structured optimization components into end-to-end differentiable models, enabling richer inductive biases and tighter alignment with task-specific objectives. In this work, we introduce a novel differentiable approximation to the zero-one loss-long considered the gold standard for classification performance, yet incompatible with gradient-based optimization due to its non-differentiability. Our method constructs a smooth, order-preserving projection onto the n,k-dimensional hypersimplex through a constrained optimization framework, leading to a new operator we term Soft-Binary-Argmax. After deriving its mathematical properties, we show how its Jacobian can be efficiently computed and integrated into binary and multiclass learning systems. Empirically, our approach achieves significant improvements in generalization under large-batch training by imposing geometric consistency constraints on the output logits, thereby narrowing the performance gap traditionally observed in large-batch training.

### 🤖 AI 总结

**一句话总结**：提出一种通过对超单纯形（hypersimplex）进行可微投影来近似零一损失的算子 Soft-Binary-Argmax，并在大批量训练下提升分类泛化性能。

**研究动机**：零一损失与分类目标最一致但不可导，难以用于端到端梯度优化；同时大批量训练常带来泛化下降，需要更贴合任务且具结构约束的可微组件。

**核心方法**：将“接近二值/argmax”的输出建模为到 n,k-维 hypersimplex 的平滑、保序（order-preserving）约束投影，构造 Soft-Binary-Argmax 作为零一损失的可微近似；推导其性质并给出高效雅可比计算以便集成到二分类与多分类网络中。

**主要结论**：该方法可在保持可微训练的同时更好对齐零一分类目标，并通过对logits施加几何一致性约束，在大批量训练场景显著改善泛化、缩小大批量训练的性能差距。

**关键词**：可微零一损失, 超单纯形投影, 结构化优化层, 约束优化, 顺序保持投影, 雅可比矩阵计算, 大批量训练泛化, 几何一致性约束, 多分类学习

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23336v1) | [下载PDF](https://arxiv.org/pdf/2602.23336v1.pdf)

---

## [26. ParamMem: Augmenting Language Agents with Parametric Reflective Memory](https://arxiv.org/abs/2602.23320v1)

**作者**：Tianjun Yao, Yongqiang Chen, Yujia Zheng 等 6 位作者  
**分类**：cs.LG, cs.MA  
**发布时间**：2026-02-26

### 📄 论文摘要

Self-reflection enables language agents to iteratively refine solutions, yet often produces repetitive outputs that limit reasoning performance. Recent studies have attempted to address this limitation through various approaches, among which increasing reflective diversity has shown promise. Our empirical analysis reveals a strong positive correlation between reflective diversity and task success, further motivating the need for diverse reflection signals. We introduce ParamMem, a parametric memory module that encodes cross-sample reflection patterns into model parameters, enabling diverse reflection generation through temperature-controlled sampling. Building on this module, we propose ParamAgent, a reflection-based agent framework that integrates parametric memory with episodic and cross-sample memory. Extensive experiments on code generation, mathematical reasoning, and multi-hop question answering demonstrate consistent improvements over state-of-the-art baselines. Further analysis reveals that ParamMem is sample-efficient, enables weak-to-strong transfer across model scales, and supports self-improvement without reliance on stronger external model, highlighting the potential of ParamMem as an effective component for enhancing language agents.

### 🤖 AI 总结

**一句话总结**：ParamMem通过把跨样本的反思模式编码进参数化记忆，并用可控采样提升反思多样性，从而系统性增强语言代理在多类推理任务上的表现。

**研究动机**：现有自反思代理常产生重复反思，限制推理增益；作者实证发现“反思多样性”与任务成功率显著正相关，因此需要更丰富的反思信号来源。

**核心方法**：提出ParamMem参数化记忆模块，将跨样本反思规律学习到模型参数中，并通过温度采样生成多样反思；在此基础上构建ParamAgent，将ParamMem与情景记忆（episodic）及跨样本记忆融合以驱动迭代求解。

**主要结论**：在代码生成、数学推理和多跳问答上相对SOTA基线取得稳定提升；此外ParamMem具备样本效率高、可实现弱到强跨尺度迁移、且无需更强外部模型即可自我改进等特性。

**关键词**：反思多样性, 参数化记忆, 参数记忆模块, 跨样本记忆, 情景记忆, 温度采样, 弱到强迁移, 代码生成, 多跳问答

**评分**：42

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23320v1) | [下载PDF](https://arxiv.org/pdf/2602.23320v1.pdf)

---

## [27. A Proper Scoring Rule for Virtual Staining](https://arxiv.org/abs/2602.23305v1)

**作者**：Samuel Tonks, Steve Hood, Ryan Musso 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-26

### 📄 论文摘要

Generative virtual staining (VS) models for high-throughput screening (HTS) can provide an estimated posterior distribution of possible biological feature values for each input and cell. However, when evaluating a VS model, the true posterior is unavailable. Existing evaluation protocols only check the accuracy of the marginal distribution over the dataset rather than the predicted posteriors. We introduce information gain (IG) as a cell-wise evaluation framework that enables direct assessment of predicted posteriors. IG is a strictly proper scoring rule and comes with a sound theoretical motivation allowing for interpretability, and for comparing results across models and features. We evaluate diffusion- and GAN-based models on an extensive HTS dataset using IG and other metrics and show that IG can reveal substantial performance differences other metrics cannot.

### 🤖 AI 总结

**一句话总结**：提出用信息增益（IG）作为严格适当评分规则，逐细胞评估虚拟染色模型输出的后验分布质量，并揭示现有指标难以发现的性能差异。

**研究动机**：虚拟染色模型可为每个细胞预测生物特征的后验分布，但真实后验不可得，现有评估多只看数据集层面的边缘分布准确性，无法直接衡量“预测后验是否可靠”。

**核心方法**：将信息增益（IG）引入为逐细胞的评价框架，把模型给出的后验预测作为被评分对象；证明IG是严格适当评分规则，具有理论可解释性，并在高通量筛选数据上对扩散与GAN模型与多种指标进行对比评测。

**主要结论**：IG能够更直接、可解释地衡量后验预测质量，并在实际评测中揭示扩散/GAN等模型之间显著差异，而这些差异可能被仅看边缘分布或传统指标所掩盖。

**关键词**：虚拟染色, 高通量筛选, 生成模型评测, 后验分布预测, 信息增益评分, 严格适当评分规则, 细胞级评估, 不确定性评估, Diffusion, 生成对抗网络, 边际分布评估, 可解释性指标

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23305v1) | [下载PDF](https://arxiv.org/pdf/2602.23305v1.pdf)

---

## [28. Inferential Mechanics Part 1: Causal Mechanistic Theories of Machine Learning in Chemical Biology with Implications](https://arxiv.org/abs/2602.23303v1)

**作者**：Ilya Balabin, Thomas M. Kaiser  
**分类**：cs.LG  
**发布时间**：2026-02-26

### 📄 论文摘要

Machine learning techniques are now routinely encountered in research laboratories across the globe. Impressive progress has been made through ML and AI techniques with regards to large data set processing. This progress has increased the ability of the experimenter to digest data and make novel predictions regarding phenomena of interest. However, machine learning predictors generated from data sets taken from the natural sciences are often treated as black boxes which are used broadly and generally without detailed consideration of the causal structure of the data set of interest. Work has been attempted to bring causality into discussions of machine learning models of natural phenomena; however, a firm and unified theoretical treatment is lacking. This series of three papers explores the union of chemical theory, biological theory, probability theory and causality that will correct current causal flaws of machine learning in the natural sciences. This paper, Part 1 of the series, provides the formal framework of the foundational causal structure of phenomena in chemical biology and is extended to machine learning through the novel concept of focus, defined here as the ability of a machine learning algorithm to narrow down to a hidden underpinning mechanism in large data sets. Initial proof of these principles on a family of Akt inhibitors is also provided. The second paper containing Part 2 will provide a formal exploration of chemical similarity, and Part 3 will present extensive experimental evidence of how hidden causal structures weaken all machine learning in chemical biology. This series serves to establish for chemical biology a new kind of mathematical framework for modeling mechanisms in Nature without the need for the tools of reductionism: inferential mechanics.

### 🤖 AI 总结

**一句话总结**：论文提出“推断力学（inferential mechanics）”框架，将化学生物现象的因果机制结构显式引入机器学习，以减少黑箱预测并提升对隐藏机制的聚焦（focus）能力。

**研究动机**：自然科学中的ML模型常被当作黑箱使用，忽略数据背后的因果结构，导致对机制的解释与外推存在根本缺陷。作者认为现有“ML+因果”讨论缺乏统一且贴合化学生物学的形式化理论。

**核心方法**：构建化学生物现象的基础因果结构的形式框架，并提出“focus”概念来刻画算法从大规模数据中收敛到隐藏生成机制的能力；同时在Akt抑制剂家族上给出初步验证。

**主要结论**：作者主张需要用统一的因果-概率-化学/生物理论来纠正化学生物ML中的因果缺陷，并以“focus”作为连接机制建模与ML的关键指标；初步实验表明该框架可用于揭示/逼近潜在机制，后续两篇将进一步展开相似性理论与更广泛实证。

**关键词**：因果结构建模, 机制因果理论, 化学生物学建模, 黑盒预测器局限, 隐藏机制识别, 概率论-因果融合, 化学相似性度量, Akt抑制剂案例, 非还原主义框架

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23303v1) | [下载PDF](https://arxiv.org/pdf/2602.23303v1.pdf)

---

## [29. Conformalized Neural Networks for Federated Uncertainty Quantification under Dual Heterogeneity](https://arxiv.org/abs/2602.23296v1)

**作者**：Quang-Huy Nguyen, Jiaqi Wang, Wei-Shinn Ku  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-26

### 📄 论文摘要

Federated learning (FL) faces challenges in uncertainty quantification (UQ). Without reliable UQ, FL systems risk deploying overconfident models at under-resourced agents, leading to silent local failures despite seemingly satisfactory global performance. Existing federated UQ approaches often address data heterogeneity or model heterogeneity in isolation, overlooking their joint effect on coverage reliability across agents. Conformal prediction is a widely used distribution-free UQ framework, yet its applications in heterogeneous FL settings remains underexplored. We provide FedWQ-CP, a simple yet effective approach that balances empirical coverage performance with efficiency at both global and agent levels under the dual heterogeneity. FedWQ-CP performs agent-server calibration in a single communication round. On each agent, conformity scores are computed on calibration data and a local quantile threshold is derived. Each agent then transmits only its quantile threshold and calibration sample size to the server. The server simply aggregates these thresholds through a weighted average to produce a global threshold. Experimental results on seven public datasets for both classification and regression demonstrate that FedWQ-CP empirically maintains agent-wise and global coverage while producing the smallest prediction sets or intervals.

### 🤖 AI 总结

**一句话总结**：提出FedWQ-CP：在数据与模型双重异质的联邦学习中，用一次通信的共形校准实现可靠的不确定性量化并得到更紧的预测区间/集合。

**研究动机**：现有联邦UQ方法多只处理数据异质或模型异质之一，忽视二者叠加会导致各客户端覆盖率不稳定，进而在资源不足节点出现“过度自信”的静默失败。需要一种分布无关且通信高效的UQ方案，同时兼顾全局与客户端层面的覆盖可靠性。

**核心方法**：每个客户端在本地校准集上计算共形一致性分数并得到本地分位数阈值，只上传“阈值+校准样本量”到服务器；服务器用样本量加权平均聚合阈值生成全局阈值，从而在单轮通信内完成客户端-服务器协同校准并用于分类/回归预测集构造。

**主要结论**：在7个公开数据集的分类与回归实验中，FedWQ-CP在保持客户端级与全局经验覆盖率的同时，产生最小的预测集合或区间，兼具可靠性与效率。

**关键词**：联邦学习, 不确定性量化, 保形预测, 分布无关置信区间, 双重异质性, 覆盖率保证, 代理-服务器校准, 单轮通信, 加权分位数聚合, 预测集合, 预测区间

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23296v1) | [下载PDF](https://arxiv.org/pdf/2602.23296v1.pdf)

---

## [30. Physics Informed Viscous Value Representations](https://arxiv.org/abs/2602.23280v1)

**作者**：Hrishikesh Viswanath, Juanwu Lu, S. Talha Bukhari 等 6 位作者  
**分类**：cs.LG, cs.RO  
**发布时间**：2026-02-26

### 📄 论文摘要

Offline goal-conditioned reinforcement learning (GCRL) learns goal-conditioned policies from static pre-collected datasets. However, accurate value estimation remains a challenge due to the limited coverage of the state-action space. Recent physics-informed approaches have sought to address this by imposing physical and geometric constraints on the value function through regularization defined over first-order partial differential equations (PDEs), such as the Eikonal equation. However, these formulations can often be ill-posed in complex, high-dimensional environments. In this work, we propose a physics-informed regularization derived from the viscosity solution of the Hamilton-Jacobi-Bellman (HJB) equation. By providing a physics-based inductive bias, our approach grounds the learning process in optimal control theory, explicitly regularizing and bounding updates during value iterations. Furthermore, we leverage the Feynman-Kac theorem to recast the PDE solution as an expectation, enabling a tractable Monte Carlo estimation of the objective that avoids numerical instability in higher-order gradients. Experiments demonstrate that our method improves geometric consistency, making it broadly applicable to navigation and high-dimensional, complex manipulation tasks. Open-source codes are available at https://github.com/HrishikeshVish/phys-fk-value-GCRL.

### 🤖 AI 总结

**一句话总结**：提出一种基于HJB方程粘性解的物理信息正则，用Feynman-Kac将PDE解转为可蒙特卡洛估计的期望，从而提升离线目标条件RL中的价值估计与几何一致性。

**研究动机**：离线GCRL由于数据覆盖不足，价值函数在未覆盖状态-动作区域易产生误差；现有基于一阶PDE（如Eikonal）的物理正则在高维复杂环境中常出现不适定与训练不稳定。

**核心方法**：从最优控制理论出发，构造源自Hamilton-Jacobi-Bellman方程粘性解的正则项，在价值迭代中对更新进行显式约束与界定；再用Feynman-Kac定理把PDE求解改写为期望形式，使用蒙特卡洛估计目标以避免高阶梯度带来的数值不稳定。

**主要结论**：实验表明该方法能改善价值表示的几何一致性，并在导航与高维复杂操作任务上带来更好的离线GCRL性能与适用性。

**关键词**：离线目标条件强化学习, 价值函数估计, 物理信息正则化, 黏性解, PDE约束学习, 蒙特卡洛估计, 最优控制理论, 高维机器人导航, 高维机器人操控

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23280v1) | [下载PDF](https://arxiv.org/pdf/2602.23280v1.pdf)

---

