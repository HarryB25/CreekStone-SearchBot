# arXiv AI 论文日报 | 2026-02-27

> 共 15 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (5 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.AI](#csAI) (3 篇)

---

## cs.AI

## [1. Toward Expert Investment Teams:A Multi-Agent LLM System with Fine-Grained Trading Tasks](https://arxiv.org/abs/2602.23330v1)

**作者**：Kunihiro Miyazaki, Takanobu Kawahara, Stephen Roberts 等 4 位作者  
**分类**：cs.AI, q-fin.TR  
**发布时间**：2026-02-26

### 📄 论文摘要

The advancement of large language models (LLMs) has accelerated the development of autonomous financial trading systems. While mainstream approaches deploy multi-agent systems mimicking analyst and manager roles, they often rely on abstract instructions that overlook the intricacies of real-world workflows, which can lead to degraded inference performance and less transparent decision-making. Therefore, we propose a multi-agent LLM trading framework that explicitly decomposes investment analysis into fine-grained tasks, rather than providing coarse-grained instructions. We evaluate the proposed framework using Japanese stock data, including prices, financial statements, news, and macro information, under a leakage-controlled backtesting setting. Experimental results show that fine-grained task decomposition significantly improves risk-adjusted returns compared to conventional coarse-grained designs. Crucially, further analysis of intermediate agent outputs suggests that alignment between analytical outputs and downstream decision preferences is a critical driver of system performance. Moreover, we conduct standard portfolio optimization, exploiting low correlation with the stock index and the variance of each system's output. This approach achieves superior performance. These findings contribute to the design of agent structure and task configuration when applying LLM agents to trading systems in practical settings.

### 🤖 AI 总结

**一句话总结**：提出一种将投资分析拆解为细粒度交易任务的多智能体LLM交易系统，在防泄漏回测的日本股市数据上显著提升风险调整后收益。

**研究动机**：现有多智能体交易系统多用粗粒度角色/指令驱动，忽视真实投研流程细节，导致推理性能下降且决策过程不透明。

**核心方法**：设计多智能体框架，把投研流程显式分解为多个细粒度分析与决策子任务，并在包含价格、财报、新闻与宏观信息的日本股票数据上进行泄漏控制回测；同时分析中间产物与下游偏好的对齐，并结合标准组合优化利用与指数低相关性和输出方差构建投资组合。

**主要结论**：细粒度任务分解相较粗粒度设计能显著改善风险调整后回报；系统表现的关键驱动因素之一是各阶段分析输出与最终决策偏好的对齐，进一步通过组合优化可获得更优整体表现。

**关键词**：多智能体 LLM, 量化交易, 细粒度任务分解, 投资分析工作流, 泄漏控制回测, 日本股市数据, 风险调整收益, 偏好对齐, 中间输出可解释性, 投资组合优化, 低相关性分散

**评分**：37

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23330v1) | [下载PDF](https://arxiv.org/pdf/2602.23330v1.pdf)

---

## [2. LLM Novice Uplift on Dual-Use, In Silico Biology Tasks](https://arxiv.org/abs/2602.23329v1)

**作者**：Chen Bo Calvin Zhang, Christina Q. Knight, Nicholas Kruus 等 19 位作者  
**分类**：cs.AI, cs.CL, cs.CR, cs.CY, cs.HC  
**发布时间**：2026-02-26

### 📄 论文摘要

Large language models (LLMs) perform increasingly well on biology benchmarks, but it remains unclear whether they uplift novice users -- i.e., enable humans to perform better than with internet-only resources. This uncertainty is central to understanding both scientific acceleration and dual-use risk. We conducted a multi-model, multi-benchmark human uplift study comparing novices with LLM access versus internet-only access across eight biosecurity-relevant task sets. Participants worked on complex problems with ample time (up to 13 hours for the most involved tasks). We found that LLM access provided substantial uplift: novices with LLMs were 4.16 times more accurate than controls (95% CI [2.63, 6.87]). On four benchmarks with available expert baselines (internet-only), novices with LLMs outperformed experts on three of them. Perhaps surprisingly, standalone LLMs often exceeded LLM-assisted novices, indicating that users were not eliciting the strongest available contributions from the LLMs. Most participants (89.6%) reported little difficulty obtaining dual-use-relevant information despite safeguards. Overall, LLMs substantially uplift novices on biological tasks previously reserved for trained practitioners, underscoring the need for sustained, interactive uplift evaluations alongside traditional benchmarks.

### 🤖 AI 总结

**一句话总结**：研究发现：在多项与生物安全相关的复杂任务中，给新手提供LLM显著提升其表现（准确率约为仅用互联网的4.16倍），并暴露出潜在双用途风险与评测缺口。

**研究动机**：尽管LLM在生物学基准上表现越来越好，但不清楚它们是否真正“抬升”缺乏训练的用户到超越仅靠互联网的水平；这直接关系到科研加速与生物安全双用途风险评估。

**核心方法**：开展多模型、多基准的人类“uplift”对照实验：比较新手在“可用LLM”与“仅互联网”条件下完成8组生物安全相关任务的表现，并在部分任务上与仅互联网条件下的专家基线对比。

**主要结论**：LLM显著提升新手准确率（4.16倍，且部分任务新手+LLM超过专家基线），但纯LLM往往又优于“人+LLM”，说明用户未能充分发挥模型能力；多数参与者也表示较易获得双用途相关信息，提示需持续、交互式的uplift评估与更强防护。

**关键词**：新手能力提升, 人机协作评测, LLM辅助任务, 生物安全, 计算生物学任务, 基准测试, 专家基线对比, 安全防护绕过, 交互式评估

**评分**：16

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23329v1) | [下载PDF](https://arxiv.org/pdf/2602.23329v1.pdf)

---

## [3. Invariant Transformation and Resampling based Epistemic-Uncertainty Reduction](https://arxiv.org/abs/2602.23315v1)

**作者**：Sha Hu  
**分类**：cs.AI  
**发布时间**：2026-02-26

### 📄 论文摘要

An artificial intelligence (AI) model can be viewed as a function that maps inputs to outputs in high-dimensional spaces. Once designed and well trained, the AI model is applied for inference. However, even optimized AI models can produce inference errors due to aleatoric and epistemic uncertainties. Interestingly, we observed that when inferring multiple samples based on invariant transformations of an input, inference errors can show partial independences due to epistemic uncertainty. Leveraging this insight, we propose a "resampling" based inferencing that applies to a trained AI model with multiple transformed versions of an input, and aggregates inference outputs to a more accurate result. This approach has the potential to improve inference accuracy and offers a strategy for balancing model size and performance.

### 🤖 AI 总结

**一句话总结**：提出利用输入的不变变换生成多样本并对预测结果重采样聚合，以降低认知（epistemic）不确定性并提升推理精度。

**研究动机**：即使训练良好的模型在推理时仍会因偶然（aleatoric）与认知（epistemic）不确定性产生错误，且模型增大并非唯一提精路径。作者观察到对同一输入做不变变换后得到的多次推理误差在认知不确定性上呈部分独立性，可被用来“抵消”错误。

**核心方法**：对单个输入施加多种保持语义/标签不变的变换（如几何、增强等），用同一已训练模型分别推理得到多份输出。再通过“resampling/聚合”策略将这些输出整合为更可靠的最终预测，从而减少由认知不确定性导致的偏差与错误。

**主要结论**：多变换多次推理并聚合可有效降低认知不确定性带来的推理错误、提升准确率。该策略为在不显著增大模型规模的情况下获取更好性能提供了折中方案（以额外推理开销换取精度提升）。

**关键词**：认知不确定性, 偶然不确定性, 不确定性分解, 不变性变换, 测试时增强, 重采样推理, 多视角推理, 预测集成, 输出聚合, 推理误差降低, 模型规模-性能权衡

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23315v1) | [下载PDF](https://arxiv.org/pdf/2602.23315v1.pdf)

---

## cs.CV

## [4. MediX-R1: Open Ended Medical Reinforcement Learning](https://arxiv.org/abs/2602.23363v1)

**作者**：Sahal Shaji Mullappilly, Mohammed Irfan Kurpath, Omair Mohamed 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-26

### 📄 论文摘要

We introduce MediX-R1, an open-ended Reinforcement Learning (RL) framework for medical multimodal large language models (MLLMs) that enables clinically grounded, free-form answers beyond multiple-choice formats. MediX-R1 fine-tunes a baseline vision-language backbone with Group Based RL and a composite reward tailored for medical reasoning: an LLM-based accuracy reward that judges semantic correctness with a strict YES/NO decision, a medical embedding-based semantic reward to capture paraphrases and terminology variants, and lightweight format and modality rewards that enforce interpretable reasoning and modality recognition. This multi-signal design provides stable, informative feedback for open-ended outputs where traditional verifiable or MCQ-only rewards fall short. To measure progress, we propose a unified evaluation framework for both text-only and image+text tasks that uses a Reference-based LLM-as-judge in place of brittle string-overlap metrics, capturing semantic correctness, reasoning, and contextual alignment. Despite using only $\sim51$K instruction examples, MediX-R1 achieves excellent results across standard medical LLM (text-only) and VLM (image + text) benchmarks, outperforming strong open-source baselines and delivering particularly large gains on open-ended clinical tasks. Our results demonstrate that open-ended RL with comprehensive reward signals and LLM-based evaluation is a practical path toward reliable medical reasoning in multimodal models. Our trained models, curated datasets and source code are available at https://medix.cvmbzuai.com

### 🤖 AI 总结

**一句话总结**：MediX-R1 提出面向医疗多模态大模型的开放式强化学习框架，通过多信号复合奖励与基于LLM的评测，实现超越选择题的临床自由文本回答能力并在多项基准上显著提升。

**研究动机**：现有医疗LLM/VLM训练与评测多依赖可验证答案或多选题，难以对开放式临床回答提供稳定、细粒度的反馈与可靠评估。为提升真实场景下的语义正确性与可解释推理，需要面向自由文本的奖励设计与评测体系。

**核心方法**：在视觉-语言骨干模型上进行Group Based RL微调，设计复合奖励：LLM判定的严格语义正确性(YES/NO)奖励、医学嵌入的语义相似奖励，以及格式与模态识别的轻量奖励以约束可解释推理与输入模态理解。评测上提出统一框架，用Reference-based LLM-as-judge替代字符串匹配指标，覆盖文本与图文任务的语义正确性、推理与上下文对齐。

**主要结论**：仅用约51K指令样本，MediX-R1在标准医疗文本LLM与图文VLM基准上超过强开源基线，尤其在开放式临床任务上提升显著。结果表明，结合综合奖励信号与LLM评测的开放式RL是提升医疗多模态模型可靠推理的可行路径。

**关键词**：开放式强化学习, 医疗多模态大语言模型, 语义正确性, 奖励机制, 评估框架, 临床任务, 模型训练, 数据集

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23363v1) | [下载PDF](https://arxiv.org/pdf/2602.23363v1.pdf)

---

## [5. VGG-T$^3$: Offline Feed-Forward 3D Reconstruction at Scale](https://arxiv.org/abs/2602.23361v1)

**作者**：Sven Elflein, Ruilong Li, Sérgio Agostinho 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-26

### 📄 论文摘要

We present a scalable 3D reconstruction model that addresses a critical limitation in offline feed-forward methods: their computational and memory requirements grow quadratically w.r.t. the number of input images. Our approach is built on the key insight that this bottleneck stems from the varying-length Key-Value (KV) space representation of scene geometry, which we distill into a fixed-size Multi-Layer Perceptron (MLP) via test-time training. VGG-T$^3$ (Visual Geometry Grounded Test Time Training) scales linearly w.r.t. the number of input views, similar to online models, and reconstructs a $1k$ image collection in just $54$ seconds, achieving a $11.6\times$ speed-up over baselines that rely on softmax attention. Since our method retains global scene aggregation capability, our point map reconstruction error outperforming other linear-time methods by large margins. Finally, we demonstrate visual localization capabilities of our model by querying the scene representation with unseen images.

### 🤖 AI 总结

**一句话总结**：VGG-T$^3$通过将可变长度的场景KV表示在测试时蒸馏为固定大小的MLP，实现对大规模多视图离线前馈3D重建的线性扩展，并在速度与精度上优于现有线性方法。

**研究动机**：现有离线前馈3D重建方法的计算与显存开销随输入图像数呈二次增长，难以处理上千张图像的集合。瓶颈来源于用softmax注意力聚合时产生的可变长度KV空间表示。

**核心方法**：提出Visual Geometry Grounded Test Time Training：在测试时对场景的KV几何表征进行训练/蒸馏，用固定容量的MLP替代可变长度KV存储，从而保持全局聚合能力并将复杂度降为随视角数线性增长。模型可用未见图像查询该场景表示以支持视觉定位。

**主要结论**：方法在1k图像集合上54秒完成重建，相比依赖softmax注意力的基线加速11.6×；同时在点图重建误差上显著优于其他线性时间方法，并展示了对未见视图的定位/查询能力。

**关键词**：三维重建, 多视图重建, 离线前馈推理, 线性时间扩展, 测试时训练, 全局场景聚合, 软最大注意力, 点图重建误差, 视觉定位

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23361v1) | [下载PDF](https://arxiv.org/pdf/2602.23361v1.pdf)

---

## [6. Sensor Generalization for Adaptive Sensing in Event-based Object Detection via Joint Distribution Training](https://arxiv.org/abs/2602.23357v1)

**作者**：Aheli Saha, René Schuster, Didier Stricker  
**分类**：cs.CV  
**发布时间**：2026-02-26

### 📄 论文摘要

Bio-inspired event cameras have recently attracted significant research due to their asynchronous and low-latency capabilities. These features provide a high dynamic range and significantly reduce motion blur. However, because of the novelty in the nature of their output signals, there is a gap in the variability of available data and a lack of extensive analysis of the parameters characterizing their signals. This paper addresses these issues by providing readers with an in-depth understanding of how intrinsic parameters affect the performance of a model trained on event data, specifically for object detection. We also use our findings to expand the capabilities of the downstream model towards sensor-agnostic robustness.

### 🤖 AI 总结

**一句话总结**：本文研究事件相机的内在参数如何影响事件流目标检测性能，并提出联合分布训练以提升模型对不同传感器设置的鲁棒泛化。

**研究动机**：事件相机数据形态新颖且公开数据与参数覆盖不足，导致模型容易对特定传感器/参数“过拟合”，缺乏跨设备与跨配置的可靠性。作者希望系统分析关键内参对检测效果的作用，并让下游检测模型具备传感器无关的稳健性。

**核心方法**：对事件相机信号的关键内在参数进行细致分析与对比实验，量化其对目标检测模型表现的影响；在此基础上，通过“联合分布训练”（在训练中覆盖并混合多种参数/数据分布）来学习对参数变化不敏感的表征，从而实现自适应感知与传感器泛化。

**主要结论**：事件相机的内参变化会显著影响事件数据分布与检测性能；通过联合分布训练可有效提升目标检测模型对不同传感器配置的泛化能力与鲁棒性，向传感器无关的下游应用迈进。

**关键词**：事件相机, 事件视觉, 事件流目标检测, 自适应感知, 传感器泛化, 传感器无关鲁棒性, 联合分布训练, 内在参数建模, 参数敏感性分析, 域泛化

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23357v1) | [下载PDF](https://arxiv.org/pdf/2602.23357v1.pdf)

---

## [7. Retrieve and Segment: Are a Few Examples Enough to Bridge the Supervision Gap in Open-Vocabulary Segmentation?](https://arxiv.org/abs/2602.23339v1)

**作者**：Tilemachos Aravanis, Vladan Stojnić, Bill Psomas 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-26

### 📄 论文摘要

Open-vocabulary segmentation (OVS) extends the zero-shot recognition capabilities of vision-language models (VLMs) to pixel-level prediction, enabling segmentation of arbitrary categories specified by text prompts. Despite recent progress, OVS lags behind fully supervised approaches due to two challenges: the coarse image-level supervision used to train VLMs and the semantic ambiguity of natural language. We address these limitations by introducing a few-shot setting that augments textual prompts with a support set of pixel-annotated images. Building on this, we propose a retrieval-augmented test-time adapter that learns a lightweight, per-image classifier by fusing textual and visual support features. Unlike prior methods relying on late, hand-crafted fusion, our approach performs learned, per-query fusion, achieving stronger synergy between modalities. The method supports continually expanding support sets, and applies to fine-grained tasks such as personalized segmentation. Experiments show that we significantly narrow the gap between zero-shot and supervised segmentation while preserving open-vocabulary ability.

### 🤖 AI 总结

**一句话总结**：提出一种检索增强的测试时适配方法，在开放词汇分割中用少量像素标注支持样本显著缩小零样本与全监督的性能差距。

**研究动机**：现有开放词汇分割主要依赖VLM的图像级粗监督且受自然语言语义歧义影响，导致像素级预测精度落后于全监督方法。作者希望用少量像素标注样本弥补监督鸿沟，同时保持开放词汇能力。

**核心方法**：在few-shot设定下，引入带像素标注的支持集，并在测试时进行检索增强：为每个查询图像检索相关支持样本，融合文本与支持视觉特征，学习一个轻量的“按图定制”分类器/适配器。与手工晚融合不同，该方法进行可学习的逐查询融合，且支持集可持续扩展并适用于个性化/细粒度分割。

**主要结论**：实验表明该检索+测试时适配策略能显著提升OVS性能、缩小与全监督分割的差距，同时仍保留对任意文本类别的开放词汇泛化能力。

**关键词**：开放词汇分割, 视觉语言模型, 零样本分割, 小样本分割, 检索增强, 测试时自适应, 轻量分类器, 跨模态特征融合, 逐查询融合, 个性化分割

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23339v1) | [下载PDF](https://arxiv.org/pdf/2602.23339v1.pdf)

---

## [8. ThinkOmni: Lifting Textual Reasoning to Omni-modal Scenarios via Guidance Decoding](https://arxiv.org/abs/2602.23306v1)

**作者**：Yiran Guan, Sifan Tu, Dingkang Liang 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-26

### 📄 论文摘要

Omni-modal reasoning is essential for intelligent systems to understand and draw inferences from diverse data sources. While existing omni-modal large language models (OLLM) excel at perceiving diverse modalities, they lack the complex reasoning abilities of recent large reasoning models (LRM). However, enhancing the reasoning ability of OLLMs through additional training presents significant challenges, including the need for high-quality data, task-specific adaptation, and substantial computational costs. To address these limitations, we propose ThinkOmni, a training-free and data-free framework that lifts textual reasoning to omni-modal scenarios. ThinkOmni introduces two key components: 1) LRM-as-a-Guide, which leverages off-the-shelf LRMs to guide the OLLM decoding process; 2) Stepwise Contrastive Scaling, which adaptively balances perception and reasoning signals without manual hyperparameter tuning. Experiments on six multi-modal reasoning benchmarks demonstrate that ThinkOmni consistently delivers performance improvements, with main results achieving 70.2 on MathVista and 75.5 on MMAU. Overall, ThinkOmni offers a flexible and generalizable solution for omni-modal reasoning and provides new insights into the generalization and application of reasoning capabilities.

### 🤖 AI 总结

**一句话总结**：ThinkOmni 通过无需训练的数据无关框架，把现成大推理模型（LRM）的文本推理能力“迁移”到全模态大模型（OLLM）的解码过程中，从而显著提升多模态推理表现。

**研究动机**：现有 OLLM 虽具备多模态感知能力，但推理深度不及近期 LRM；而通过再训练补强推理通常需要高质量数据、任务适配与高算力成本。

**核心方法**：提出 LRM-as-a-Guide：在解码时用现成 LRM 生成/评估推理信号来引导 OLLM 输出；并设计 Stepwise Contrastive Scaling：按推理步骤自适应融合“感知 vs 推理”信号，避免手工调超参。

**主要结论**：在六个多模态推理基准上整体稳定提升（如 MathVista 70.2、MMAU 75.5），表明无需训练也能有效增强 OLLM 的推理能力且具备较强通用性与可迁移性。

**关键词**：全模态推理, 多模态推理, 训练无关框架, 数据无关方法, 引导解码, 推理模型蒸馏式指导, 逐步对比缩放, 感知-推理权衡

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23306v1) | [下载PDF](https://arxiv.org/pdf/2602.23306v1.pdf)

---

## cs.LG

## [9. Model Agreement via Anchoring](https://arxiv.org/abs/2602.23360v1)

**作者**：Eric Eaton, Surbhi Goel, Marcel Hussing 等 7 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-26

### 📄 论文摘要

Numerous lines of aim to control $\textit{model disagreement}$ -- the extent to which two machine learning models disagree in their predictions. We adopt a simple and standard notion of model disagreement in real-valued prediction problems, namely the expected squared difference in predictions between two models trained on independent samples, without any coordination of the training processes. We would like to be able to drive disagreement to zero with some natural parameter(s) of the training procedure using analyses that can be applied to existing training methodologies.   We develop a simple general technique for proving bounds on independent model disagreement based on $\textit{anchoring}$ to the average of two models within the analysis. We then apply this technique to prove disagreement bounds for four commonly used machine learning algorithms: (1) stacked aggregation over an arbitrary model class (where disagreement is driven to 0 with the number of models $k$ being stacked) (2) gradient boosting (where disagreement is driven to 0 with the number of iterations $k$) (3) neural network training with architecture search (where disagreement is driven to 0 with the size $n$ of the architecture being optimized over) and (4) regression tree training over all regression trees of fixed depth (where disagreement is driven to 0 with the depth $d$ of the tree architecture). For clarity, we work out our initial bounds in the setting of one-dimensional regression with squared error loss -- but then show that all of our results generalize to multi-dimensional regression with any strongly convex loss.

### 🤖 AI 总结

**一句话总结**：提出一种“锚定（anchoring）”分析技术，在不协调训练的前提下证明独立训练模型的预测分歧可随训练/模型规模等自然参数趋近于0，并将其应用到多种常见算法。

**研究动机**：独立训练的模型往往存在预测不一致，影响稳定性与可复现性；作者希望用能适配现有训练流程的通用分析框架，刻画并推动这种“模型分歧”降到接近零。

**核心方法**：以回归任务中两模型预测差的期望平方（独立样本训练、无协调）作为分歧度量，在证明中引入“锚定到两模型平均值”的技巧来上界分歧；并将该技巧分别用于堆叠集成、梯度提升、带架构搜索的神经网络训练、固定深度回归树训练，同时从一维平方损失推广到多维与任意强凸损失。

**主要结论**：给出四类算法的分歧上界与收敛趋势：堆叠集成随模型数k增大分歧趋0，梯度提升随迭代k增大趋0，架构搜索随候选架构规模n增大趋0，回归树随深度d增大趋0；结果可推广到更一般的多维回归与强凸损失设置。

**关键词**：模型分歧, 独立训练, 预测差平方期望, 锚定分析, 分歧界, 堆叠集成, 梯度提升, 神经架构搜索, 回归树深度, 强凸损失, 多维回归

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23360v1) | [下载PDF](https://arxiv.org/pdf/2602.23360v1.pdf)

---

## [10. A Dataset is Worth 1 MB](https://arxiv.org/abs/2602.23358v1)

**作者**：Elad Kimchi Shoshani, Leeyam Gabay, Yedid Hoshen  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-02-26

### 📄 论文摘要

A dataset server must often distribute the same large payload to many clients, incurring massive communication costs. Since clients frequently operate on diverse hardware and software frameworks, transmitting a pre-trained model is often infeasible; instead, agents require raw data to train their own task-specific models locally. While dataset distillation attempts to compress training signals, current methods struggle to scale to high-resolution data and rarely achieve sufficiently small files. In this paper, we propose Pseudo-Labels as Data (PLADA), a method that completely eliminates pixel transmission. We assume agents are preloaded with a large, generic, unlabeled reference dataset (e.g., ImageNet-1K, ImageNet-21K) and communicate a new task by transmitting only the class labels for specific images. To address the distribution mismatch between the reference and target datasets, we introduce a pruning mechanism that filters the reference dataset to retain only the labels of the most semantically relevant images for the target task. This selection process simultaneously maximizes training efficiency and minimizes transmission payload. Experiments on 10 diverse datasets demonstrate that our approach can transfer task knowledge with a payload of less than 1 MB while retaining high classification accuracy, offering a promising solution for efficient dataset serving.

### 🤖 AI 总结

**一句话总结**：PLADA通过在客户端预置的大规模无标注参考数据集上只传输少量图像的类别标签（并剪枝挑选最相关样本），实现以<1MB载荷高效传递新分类任务。

**研究动机**：数据集服务器向多客户端分发高分辨率原始数据通信成本极高，而直接下发预训练模型又因硬件/框架差异常不可行；现有数据集蒸馏方法难以在高分辨率场景下做到足够小的文件。

**核心方法**：假设客户端已拥有通用参考数据集（如ImageNet），服务器不发送像素而仅发送“哪些参考图像对应哪些类别”的伪标签集合；为缓解参考集与目标任务分布不匹配，引入剪枝机制筛选语义最相关的参考图像以提升训练效率并进一步压缩传输量。

**主要结论**：在10个多样化数据集上，PLADA能在不传输图像像素的情况下以小于1MB的通信载荷保持较高分类准确率，展示了面向数据集服务的极低成本任务传递潜力。

**关键词**：数据集服务, 伪标签, 数据压缩, 传输效率, 任务知识转移, 图像分类, 数据修剪, 高分辨率数据

**评分**：37

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23358v1) | [下载PDF](https://arxiv.org/pdf/2602.23358v1.pdf)

---

## [11. SOTAlign: Semi-Supervised Alignment of Unimodal Vision and Language Models via Optimal Transport](https://arxiv.org/abs/2602.23353v1)

**作者**：Simon Roschmann, Paul Krzakala, Sonia Mazelet 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-26

### 📄 论文摘要

The Platonic Representation Hypothesis posits that neural networks trained on different modalities converge toward a shared statistical model of the world. Recent work exploits this convergence by aligning frozen pretrained vision and language models with lightweight alignment layers, but typically relies on contrastive losses and millions of paired samples. In this work, we ask whether meaningful alignment can be achieved with substantially less supervision. We introduce a semi-supervised setting in which pretrained unimodal encoders are aligned using a small number of image-text pairs together with large amounts of unpaired data. To address this challenge, we propose SOTAlign, a two-stage framework that first recovers a coarse shared geometry from limited paired data using a linear teacher, then refines the alignment on unpaired samples via an optimal-transport-based divergence that transfers relational structure without overconstraining the target space. Unlike existing semi-supervised methods, SOTAlign effectively leverages unpaired images and text, learning robust joint embeddings across datasets and encoder pairs, and significantly outperforming supervised and semi-supervised baselines.

### 🤖 AI 总结

**一句话总结**：SOTAlign提出一种半监督对齐框架，用少量图文配对与大量非配对数据，通过最优传输在冻结的视觉/语言单模态编码器间学到稳健的联合嵌入。

**研究动机**：现有对齐方法多依赖对比学习与海量配对样本，成本高且难获取；作者希望在配对监督极少的情况下，仍能有效对齐预训练的单模态模型。

**核心方法**：两阶段：先用少量配对数据训练线性“教师”恢复粗略共享几何；再在大量非配对图像/文本上用基于最优传输的散度对齐关系结构，从而细化联合空间且避免对目标空间过度约束。

**主要结论**：SOTAlign能有效利用非配对数据，在不同数据集与不同编码器组合上学习到更鲁棒的跨模态嵌入，并显著优于纯监督与现有半监督对齐基线。

**关键词**：半监督对齐, 视觉-语言对齐, 单模态编码器, 冻结预训练模型, 轻量对齐层, 最优传输, 最优传输散度, 非配对数据, 少量图文配对, 联合嵌入空间, 共享几何结构, 线性教师模型

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23353v1) | [下载PDF](https://arxiv.org/pdf/2602.23353v1.pdf)

---

## [12. FlashOptim: Optimizers for Memory Efficient Training](https://arxiv.org/abs/2602.23349v1)

**作者**：Jose Javier Gonzalez Ortiz, Abhay Gupta, Chris Renard 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-26

### 📄 论文摘要

Standard mixed-precision training of neural networks requires many bytes of accelerator memory for each model parameter. These bytes reflect not just the parameter itself, but also its gradient and one or more optimizer state variables. With each of these values typically requiring 4 bytes, training even a 7 billion parameter model can be impractical for researchers with less than 100GB of accelerator memory.   We introduce FlashOptim, a suite of optimizations that reduces per-parameter memory by over 50% while preserving model quality and API compatibility. Our approach introduces two key techniques. First, we improve master weight splitting by finding and exploiting a tight bound on its quantization error. Second, we design companding functions that greatly reduce the error in 8-bit optimizer state quantization. Together with 16-bit gradients, these techniques reduce AdamW memory from 16 bytes to 7 bytes per parameter, or 5 bytes with gradient release. They also cut model checkpoint sizes by more than half.   Experiments with FlashOptim applied to SGD, AdamW, and Lion show no measurable quality degradation on any task from a collection of standard vision and language benchmarks, including Llama-3.1-8B finetuning.

### 🤖 AI 总结

**一句话总结**：FlashOptim 通过更精确的主权重拆分与更低误差的8-bit优化器状态量化，将混合精度训练的每参数显存占用降低50%以上且不损失效果。

**研究动机**：标准混合精度训练除参数外还需存梯度与优化器状态（常各4字节），导致大模型训练/微调在<100GB显存下难以负担，并且checkpoint体积过大。

**核心方法**：提出两项关键技术：基于量化误差紧界改进master weight splitting以降低主权重拆分误差；设计companding（压扩）函数以显著降低8-bit优化器状态量化误差，并配合16-bit梯度与可选gradient release。

**主要结论**：在SGD/AdamW/Lion上，FlashOptim 将AdamW内存从16B/param降至7B（启用梯度释放可至5B），checkpoint减半以上，并在多项视觉与语言基准（含Llama-3.1-8B微调）上未观察到质量下降。

**关键词**：混合精度训练, 显存优化, 优化器状态量化, 8-bit量化, 主权重拆分, 量化误差界, 压扩函数, 16-bit梯度, 梯度释放, 模型检查点压缩

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23349v1) | [下载PDF](https://arxiv.org/pdf/2602.23349v1.pdf)

---

## [13. Mean Estimation from Coarse Data: Characterizations and Efficient Algorithms](https://arxiv.org/abs/2602.23341v1)

**作者**：Alkis Kalavasis, Anay Mehrotra, Manolis Zampetakis 等 5 位作者  
**分类**：cs.LG, cs.DS, math.ST, stat.ML  
**发布时间**：2026-02-26

### 📄 论文摘要

Coarse data arise when learners observe only partial information about samples; namely, a set containing the sample rather than its exact value. This occurs naturally through measurement rounding, sensor limitations, and lag in economic systems. We study Gaussian mean estimation from coarse data, where each true sample $x$ is drawn from a $d$-dimensional Gaussian distribution with identity covariance, but is revealed only through the set of a partition containing $x$. When the coarse samples, roughly speaking, have ``low'' information, the mean cannot be uniquely recovered from observed samples (i.e., the problem is not identifiable). Recent work by Fotakis, Kalavasis, Kontonis, and Tzamos [FKKT21] established that sample-efficient mean estimation is possible when the unknown mean is identifiable and the partition consists of only convex sets. Moreover, they showed that without convexity, mean estimation becomes NP-hard. However, two fundamental questions remained open: (1) When is the mean identifiable under convex partitions? (2) Is computationally efficient estimation possible under identifiability and convex partitions? This work resolves both questions. [...]

### 🤖 AI 总结

**一句话总结**：本文研究在仅观测到“样本所在分区集合”(coarse data)的情况下进行高斯均值估计，给出了凸分区下均值可识别性的几何刻画，并在可识别时提供多项式时间的高效估计算法。

**研究动机**：在取整测量、传感器分辨率或经济系统滞后等场景中，数据常以集合/区间而非精确值出现，导致均值可能不可唯一恢复；已有工作虽表明凸分区下可在可识别时样本高效，但缺少“何时可识别”以及“能否计算高效”的完整答案。

**核心方法**：作者从凸几何与统计可识别性出发，建立“观测到的分区标签分布”与均值之间的一一对应条件（对凸分区给出必要且充分的结构刻画），并据此构造可在多项式时间内求解的估计流程（利用凸性将估计转化为可计算的优化/推断问题）。

**主要结论**：结果完整回答了两个开放问题：在凸分区下精确刻画了均值可识别当且仅当满足特定几何/信息条件；且一旦满足该条件，就存在计算上高效、并保持良好样本复杂度的均值估计方法，从而将“可识别性”与“可计算性”在该模型中对齐。

**关键词**：粗粒度数据, 集合值观测, 高斯均值估计, 多维高斯分布, 可识别性, 凸划分, 样本复杂度, 信息量条件, 多项式时间算法, NP-困难性

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23341v1) | [下载PDF](https://arxiv.org/pdf/2602.23341v1.pdf)

---

## [14. Differentiable Zero-One Loss via Hypersimplex Projections](https://arxiv.org/abs/2602.23336v1)

**作者**：Camilo Gomez, Pengyang Wang, Liansheng Tang  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-02-26

### 📄 论文摘要

Recent advances in machine learning have emphasized the integration of structured optimization components into end-to-end differentiable models, enabling richer inductive biases and tighter alignment with task-specific objectives. In this work, we introduce a novel differentiable approximation to the zero-one loss-long considered the gold standard for classification performance, yet incompatible with gradient-based optimization due to its non-differentiability. Our method constructs a smooth, order-preserving projection onto the n,k-dimensional hypersimplex through a constrained optimization framework, leading to a new operator we term Soft-Binary-Argmax. After deriving its mathematical properties, we show how its Jacobian can be efficiently computed and integrated into binary and multiclass learning systems. Empirically, our approach achieves significant improvements in generalization under large-batch training by imposing geometric consistency constraints on the output logits, thereby narrowing the performance gap traditionally observed in large-batch training.

### 🤖 AI 总结

**一句话总结**：提出一种基于超单纯形（hypersimplex）平滑投影的可微“0-1损失”近似算子Soft-Binary-Argmax，并在大批量训练下提升分类泛化性能。

**研究动机**：0-1损失与分类目标最一致但不可微，难以用于端到端梯度优化；同时大batch训练常出现泛化下降，需要更贴合任务的结构化约束来缩小性能差距。

**核心方法**：通过受约束优化构造到n,k维超单纯形的平滑、保序投影，定义Soft-Binary-Argmax作为可微近似的二值/argmax选择算子；推导其性质并给出高效Jacobian计算，使其可嵌入二分类与多分类网络进行反向传播。

**主要结论**：该算子在logits上施加几何一致性约束，实验显示能在大批量训练情形显著改善泛化表现，并缩小大batch相较小batch的性能差距。

**关键词**：可微零一损失, 零一损失近似, 超单纯形投影, 结构化优化层, 约束优化, 雅可比矩阵计算, 大批量训练, 泛化提升, 几何一致性约束, 多分类学习

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23336v1) | [下载PDF](https://arxiv.org/pdf/2602.23336v1.pdf)

---

## [15. ParamMem: Augmenting Language Agents with Parametric Reflective Memory](https://arxiv.org/abs/2602.23320v1)

**作者**：Tianjun Yao, Yongqiang Chen, Yujia Zheng 等 6 位作者  
**分类**：cs.LG, cs.MA  
**发布时间**：2026-02-26

### 📄 论文摘要

Self-reflection enables language agents to iteratively refine solutions, yet often produces repetitive outputs that limit reasoning performance. Recent studies have attempted to address this limitation through various approaches, among which increasing reflective diversity has shown promise. Our empirical analysis reveals a strong positive correlation between reflective diversity and task success, further motivating the need for diverse reflection signals. We introduce ParamMem, a parametric memory module that encodes cross-sample reflection patterns into model parameters, enabling diverse reflection generation through temperature-controlled sampling. Building on this module, we propose ParamAgent, a reflection-based agent framework that integrates parametric memory with episodic and cross-sample memory. Extensive experiments on code generation, mathematical reasoning, and multi-hop question answering demonstrate consistent improvements over state-of-the-art baselines. Further analysis reveals that ParamMem is sample-efficient, enables weak-to-strong transfer across model scales, and supports self-improvement without reliance on stronger external model, highlighting the potential of ParamMem as an effective component for enhancing language agents.

### 🤖 AI 总结

**一句话总结**：ParamMem将跨样本的反思模式参数化存入模型，并通过可控采样生成更具多样性的反思，从而提升反思型语言代理在多类推理任务上的成功率。

**研究动机**：现有自我反思常产生重复内容，限制推理增益；作者实证发现“反思多样性”与任务成功率显著正相关，因此需要更丰富的反思信号来源与生成机制。

**核心方法**：提出ParamMem参数化记忆模块，把跨样本反思规律编码进模型参数，并用温度采样控制反思多样性；在此基础上构建ParamAgent，将ParamMem与情景记忆（episodic）及跨样本记忆联合，用于迭代反思与解题。

**主要结论**：在代码生成、数学推理、多跳问答上相对SOTA基线稳定提升；同时ParamMem更样本高效、支持跨模型规模的弱到强迁移，并能在不依赖更强外部模型的情况下实现自我改进。

**关键词**：反思多样性, 参数化记忆, 参数化反思记忆, 跨样本记忆, 情节记忆, 温度采样, 样本效率, 弱到强迁移, 多跳问答

**评分**：49

**论文链接**：[查看原文](https://arxiv.org/abs/2602.23320v1) | [下载PDF](https://arxiv.org/pdf/2602.23320v1.pdf)

---

