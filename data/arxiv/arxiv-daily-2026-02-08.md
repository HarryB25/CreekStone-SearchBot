# arXiv AI 论文日报 | 2026-02-08

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (6 篇)
- [cs.LG](#csLG) (18 篇)
- [cs.AI](#csAI) (2 篇)
- [cs.CL](#csCL) (4 篇)

---

## cs.AI

## [1. Agentic Uncertainty Reveals Agentic Overconfidence](https://arxiv.org/abs/2602.06948v1)

**作者**：Jean Kaddour, Srijan Patel, Gbètondji Dovonon 等 6 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Can AI agents predict whether they will succeed at a task? We study agentic uncertainty by eliciting success probability estimates before, during, and after task execution. All results exhibit agentic overconfidence: some agents that succeed only 22% of the time predict 77% success. Counterintuitively, pre-execution assessment with strictly less information tends to yield better discrimination than standard post-execution review, though differences are not always significant. Adversarial prompting reframing assessment as bug-finding achieves the best calibration.

### 🤖 AI 总结

**一句话总结**：研究表明AI代理在任务成功预测上存在过度自信现象，且预执行评估多信息情况下的表现优于标准后评估。

**研究动机**：本研究旨在探讨AI代理在任务执行前、中、后对成功概率的评估及其准确性。

**核心方法**：通过在任务执行前后收集AI代理的成功概率估计，分析其与实际成功率的差异。

**主要结论**：研究发现，AI代理在任务成功率预测中普遍存在过度自信现象，且在某些情况下，预执行评估的准确性优于后执行评估。

**关键词**：代理不确定性, 代理过度自信, 任务执行, 成功概率预测, 评估方法, adversarial prompting, 机器学习, 深度学习, 神经网络, agent

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06948v1) | [下载PDF](https://arxiv.org/pdf/2602.06948v1.pdf)

---

## [2. AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents](https://arxiv.org/abs/2602.06855v1)

**作者**：Alisia Lupidi, Bhavul Gauri, Thomas Simon Foster 等 37 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-06

### 📄 论文摘要

LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce AIRS-Bench (the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. These tasks span diverse domains, including language modeling, mathematics, bioinformatics, and time series forecasting. AIRS-Bench tasks assess agentic capabilities over the full research lifecycle -- including idea generation, experiment analysis and iterative refinement -- without providing baseline code. The AIRS-Bench task format is versatile, enabling easy integration of new tasks and rigorous comparison across different agentic frameworks. We establish baselines using frontier models paired with both sequential and parallel scaffolds. Our results show that agents exceed human SOTA in four tasks but fail to match it in sixteen others. Even when agents surpass human benchmarks, they do not reach the theoretical performance ceiling for the underlying tasks. These findings indicate that AIRS-Bench is far from saturated and offers substantial room for improvement. We open-source the AIRS-Bench task definitions and evaluation code to catalyze further development in autonomous scientific research.

### 🤖 AI 总结

**一句话总结**：AIRS-Bench是一个包含20个科学研究任务的基准套件，旨在评估大型语言模型代理在科学研究中的能力。

**研究动机**：随着大型语言模型代理在科学研究中的潜力不断显现，急需一个标准化的基准来推动这一领域的进展。

**核心方法**：AIRS-Bench任务涵盖多个领域，评估代理在研究生命周期各阶段的能力，并建立了基于前沿模型的基准。

**主要结论**：虽然代理在四个任务上超过了人类的最佳表现，但在其他十六个任务中仍未达到人类水平，表明该基准仍有很大的改进空间。

**关键词**：LLM, 机器学习, 深度学习, 神经网络, 生成模型, 任务基准, 实验分析, 迭代优化, 代理能力, 科学研究

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06855v1) | [下载PDF](https://arxiv.org/pdf/2602.06855v1.pdf)

---

## cs.CL

## [3. Halluverse-M^3: A multitask multilingual benchmark for hallucination in LLMs](https://arxiv.org/abs/2602.06920v1)

**作者**：Samir Abdaljalil, Parichit Sharma, Erchin Serpedin 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-06

### 📄 论文摘要

Hallucinations in large language models remain a persistent challenge, particularly in multilingual and generative settings where factual consistency is difficult to maintain. While recent models show strong performance on English-centric benchmarks, their behavior across languages, tasks, and hallucination types is not yet well understood. In this work, we introduce Halluverse-M^3, a dataset designed to enable systematic analysis of hallucinations across multiple languages, multiple generation tasks, and multiple hallucination categories. Halluverse-M^3 covers four languages, English, Arabic, Hindi, and Turkish, and supports two generation tasks: question answering and dialogue summarization. The dataset explicitly distinguishes between entity-level, relation-level, and sentence-level hallucinations. Hallucinated outputs are constructed through a controlled editing process and validated by human annotators, ensuring clear alignment between original content and hallucinated generations. Using this dataset, we evaluate a diverse set of contemporary open-source and proprietary language models on fine-grained hallucination detection. Our results show that question answering is consistently easier than dialogue summarization, while sentence-level hallucinations remain challenging even for the strongest models. Performance is highest in English and degrades in lower-resource languages, with Hindi exhibiting the lowest detection accuracy. Overall, Halluverse-M^3 provides a realistic and challenging benchmark for studying hallucinations in multilingual, multi-task settings. We release the dataset to support future research on hallucination detection and mitigation\footnote{https://huggingface.co/datasets/sabdalja/HalluVerse-M3}.

### 🤖 AI 总结

**一句话总结**：Halluverse-M^3是一个多任务多语言基准数据集，用于系统分析大语言模型中的幻觉现象。

**研究动机**：大语言模型在多语言和生成环境中存在幻觉问题，尤其是在事实一致性难以维持的情况下，现有研究对多语言表现仍不够充分了解。

**核心方法**：通过控制编辑过程构建幻觉输出，并由人类标注者验证，Halluverse-M^3涵盖四种语言和两种生成任务，并区分不同层次的幻觉。

**主要结论**：结果表明，问答任务比对话总结更容易处理幻觉，而句子级幻觉对模型仍具挑战性，模型在低资源语言上的表现下降最为明显。

**关键词**：多任务, 多语言, 语言模型, 生成任务, 幻觉检测, Halluverse-M^3, 语义一致性, 人工标注, 生成对话, 问答系统, llm

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06920v1) | [下载PDF](https://arxiv.org/pdf/2602.06920v1.pdf)

---

## [4. Uncovering Cross-Objective Interference in Multi-Objective Alignment](https://arxiv.org/abs/2602.06869v1)

**作者**：Yining Lu, Meng Jiang  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

We study a persistent failure mode in multi-objective alignment for large language models (LLMs): training improves performance on only a subset of objectives while causing others to degrade. We formalize this phenomenon as cross-objective interference and conduct the first systematic study across classic scalarization algorithms, showing that interference is pervasive and exhibits strong model dependence.   To explain this phenomenon, we derive a local covariance law showing that an objective improves at first order when its reward exhibits positive covariance with the scalarized score. We extend this analysis to clipped surrogate objectives used in modern alignment, demonstrating that the covariance law remains valid under mild conditions despite clipping. Building on this analysis, we propose Covariance Targeted Weight Adaptation (CTWA), a plug-and-play method that maintains positive covariance between objective rewards and the training signal to effectively mitigate cross-objective interference. Finally, we complement these local improvement conditions with a global convergence analysis under the Polyak--Łojasiewicz condition, establishing when non-convex scalarized optimization achieves global convergence and how cross-objective interference depends on specific model geometric properties.

### 🤖 AI 总结

**一句话总结**：本文研究了多目标对齐中的交叉目标干扰现象，并提出了一种新的方法来缓解这种干扰。

**研究动机**：在大语言模型的多目标对齐中，训练通常只改善部分目标的性能，而导致其他目标性能下降，理解这一现象的原因具有重要意义。

**核心方法**：提出了协方差目标权重适应（CTWA）方法，以保持目标奖励与训练信号之间的正协方差，从而有效减轻交叉目标干扰。

**主要结论**：通过局部改进条件和全球收敛分析，研究表明非凸标量优化在特定模型几何属性下可以实现全球收敛，并揭示了交叉目标干扰的普遍性和模型依赖性。

**关键词**：多目标对齐, 大语言模型, 交叉目标干扰, Covariance Targeted Weight Adaptation, 训练信号, 优化算法, 模型几何属性, 局部改进条件, 全局收敛分析, llm

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06869v1) | [下载PDF](https://arxiv.org/pdf/2602.06869v1.pdf)

---

## [5. SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks](https://arxiv.org/abs/2602.06854v1)

**作者**：Mingqian Feng, Xiaodong Liu, Weiwei Yang 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-06

### 📄 论文摘要

Multi-turn jailbreaks capture the real threat model for safety-aligned chatbots, where single-turn attacks are merely a special case. Yet existing approaches break under exploration complexity and intent drift. We propose SEMA, a simple yet effective framework that trains a multi-turn attacker without relying on any existing strategies or external data. SEMA comprises two stages. Prefilling self-tuning enables usable rollouts by fine-tuning on non-refusal, well-structured, multi-turn adversarial prompts that are self-generated with a minimal prefix, thereby stabilizing subsequent learning. Reinforcement learning with intent-drift-aware reward trains the attacker to elicit valid multi-turn adversarial prompts while maintaining the same harmful objective. We anchor harmful intent in multi-turn jailbreaks via an intent-drift-aware reward that combines intent alignment, compliance risk, and level of detail. Our open-loop attack regime avoids dependence on victim feedback, unifies single- and multi-turn settings, and reduces exploration complexity. Across multiple datasets, victim models, and jailbreak judges, our method achieves state-of-the-art (SOTA) attack success rates (ASR), outperforming all single-turn baselines, manually scripted and template-driven multi-turn baselines, as well as our SFT (Supervised Fine-Tuning) and DPO (Direct Preference Optimization) variants. For instance, SEMA performs an average $80.1\%$ ASR@1 across three closed-source and open-source victim models on AdvBench, 33.9% over SOTA. The approach is compact, reproducible, and transfers across targets, providing a stronger and more realistic stress test for large language model (LLM) safety and enabling automatic redteaming to expose and localize failure modes. Our code is available at: https://github.com/fmmarkmq/SEMA.

### 🤖 AI 总结

**一句话总结**：SEMA是一种新颖的多轮攻击框架，能够有效地应对安全对齐聊天机器人的多轮越狱攻击。

**研究动机**：现有的单轮攻击方法在探索复杂性和意图漂移方面存在局限，亟需一种更有效的多轮攻击策略。

**核心方法**：SEMA框架由两个阶段组成：自调优的预填充和意图漂移感知奖励的强化学习，前者生成结构良好的多轮对抗提示，后者确保攻击者能够维持有害意图。

**主要结论**：SEMA在多个数据集和模型上实现了最先进的攻击成功率，展示了其在大型语言模型安全性测试中的有效性和可移植性。

**关键词**：多轮攻击, jailbreak, 强化学习, 自我调优, 对抗性提示, 大语言模型, intent-drift, 攻击成功率, 安全性测试

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06854v1) | [下载PDF](https://arxiv.org/pdf/2602.06854v1.pdf)

---

## [6. The Representational Geometry of Number](https://arxiv.org/abs/2602.06843v1)

**作者**：Zhimin Hu, Lanhao Niu, Sashank Varma  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-06

### 📄 论文摘要

A central question in cognitive science is whether conceptual representations converge onto a shared manifold to support generalization, or diverge into orthogonal subspaces to minimize task interference. While prior work has discovered evidence for both, a mechanistic account of how these properties coexist and transform across tasks remains elusive. We propose that representational sharing lies not in the concepts themselves, but in the geometric relations between them. Using number concepts as a testbed and language models as high-dimensional computational substrates, we show that number representations preserve a stable relational structure across tasks. Task-specific representations are embedded in distinct subspaces, with low-level features like magnitude and parity encoded along separable linear directions. Crucially, we find that these subspaces are largely transformable into one another via linear mappings, indicating that representations share relational structure despite being located in distinct subspaces. Together, these results provide a mechanistic lens of how language models balance the shared structure of number representation with functional flexibility. It suggests that understanding arises when task-specific transformations are applied to a shared underlying relational structure of conceptual representations.

### 🤖 AI 总结

**一句话总结**：本研究探讨了数字概念的表征几何特征，展示了任务特定表征之间的关系结构如何在不同任务中保持稳定。

**研究动机**：认知科学中一个核心问题是概念表征是否在共享流形上聚合以支持泛化，或在正交子空间中分散以减少任务干扰。

**核心方法**：使用数字概念作为测试平台，并利用语言模型作为高维计算基础，研究了数字表征在不同任务中的关系结构及其可变性。

**主要结论**：研究结果表明，尽管任务特定表征位于不同子空间中，但它们通过线性映射可以相互转换，从而共享关系结构，这为理解概念表征提供了机制视角。

**关键词**：关键词：数值概念, 表示几何, 语言模型, 任务特定, 关系结构, 机器学习, 深度学习, 嵌入, 语义搜索, agent

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06843v1) | [下载PDF](https://arxiv.org/pdf/2602.06843v1.pdf)

---

## cs.CV

## [7. MedMO: Grounding and Understanding Multimodal Large Language Model for Medical Images](https://arxiv.org/abs/2602.06965v1)

**作者**：Ankan Deria, Komal Kumar, Adinath Madhavrao Dukre 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-06

### 📄 论文摘要

Multimodal large language models (MLLMs) have rapidly advanced, yet their adoption in medicine remains limited by gaps in domain coverage, modality alignment, and grounded reasoning. In this work, we introduce MedMO, a medical foundation model built upon a generalized MLLM architecture and trained exclusively on large-scale, domain-specific data. MedMO follows a multi-stage training recipe: (i) cross-modal pretraining to align heterogeneous visual encoders with a medical language backbone; (ii) instruction tuning on multi-task supervision that spans captioning, VQA, report generation, retrieval, and grounded disease localization with bounding boxes; and (iii) reinforcement learning with verifiable rewards that combine factuality checks with a box-level GIoU reward to strengthen spatial grounding and step-by-step reasoning in complex clinical scenarios. MedMO consistently outperforms strong open-source medical MLLMs across multiple modalities and tasks. On VQA benchmarks, MedMO achieves an average accuracy improvement of +13.7% over the baseline and performs within 1.9% of the SOTA Fleming-VL. For text-based QA, it attains +6.9% over the baseline and +14.5% over Fleming-VL. In medical report generation, MedMO delivers significant gains in both semantic and clinical accuracy. Moreover, it exhibits strong grounding capability, achieving an IoU improvement of +40.4 over the baseline and +37.0% over Fleming-VL, underscoring its robust spatial reasoning and localization performance. Evaluations across radiology, ophthalmology, and pathology-microscopy confirm MedMO's broad cross-modality generalization. We release two versions of MedMO: 4B and 8B. Project is available at https://genmilab.github.io/MedMO-Page

### 🤖 AI 总结

**一句话总结**：MedMO是一种专为医学图像构建的多模态大型语言模型，显著提高了在医学领域的推理和生成能力。

**研究动机**：尽管多模态大型语言模型迅速发展，但在医学领域的应用仍受限于领域覆盖、模态对齐和基础推理能力的不足。

**核心方法**：MedMO采用多阶段训练策略，包括跨模态预训练、指令调优和基于可验证奖励的强化学习，以增强医学图像与语言的结合和推理能力。

**主要结论**：MedMO在多个任务和模态上超越了现有的开源医学多模态大型语言模型，展示了出色的空间推理和定位性能。

**关键词**：多模态, 大语言模型, 医学图像, 强化学习, 语义搜索, 医学基础模型, 视觉编码器, 复杂临床场景, 跨模态预训练, 任务监督, ml

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06965v1) | [下载PDF](https://arxiv.org/pdf/2602.06965v1.pdf)

---

## [8. CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation](https://arxiv.org/abs/2602.06959v1)

**作者**：Kaiyi Huang, Yukun Huang, Yu Li 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-06

### 📄 论文摘要

Cinematic video production requires control over scene-subject composition and camera movement, but live-action shooting remains costly due to the need for constructing physical sets. To address this, we introduce the task of cinematic video generation with decoupled scene context: given multiple images of a static environment, the goal is to synthesize high-quality videos featuring dynamic subject while preserving the underlying scene consistency and following a user-specified camera trajectory. We present CineScene, a framework that leverages implicit 3D-aware scene representation for cinematic video generation. Our key innovation is a novel context conditioning mechanism that injects 3D-aware features in an implicit way: By encoding scene images into visual representations through VGGT, CineScene injects spatial priors into a pretrained text-to-video generation model by additional context concatenation, enabling camera-controlled video synthesis with consistent scenes and dynamic subjects. To further enhance the model's robustness, we introduce a simple yet effective random-shuffling strategy for the input scene images during training. To address the lack of training data, we construct a scene-decoupled dataset with Unreal Engine 5, containing paired videos of scenes with and without dynamic subjects, panoramic images representing the underlying static scene, along with their camera trajectories. Experiments show that CineScene achieves state-of-the-art performance in scene-consistent cinematic video generation, handling large camera movements and demonstrating generalization across diverse environments.

### 🤖 AI 总结

**一句话总结**：CineScene框架通过隐式3D场景表示生成高质量的动态视频，同时保持场景一致性和用户指定的摄像机轨迹。

**研究动机**：电影视频制作需要控制场景与主体的组合及摄像机移动，但传统的实拍成本高昂，因此需要一种新的生成方法来降低成本。

**核心方法**：CineScene利用隐式3D感知场景表示和一种新颖的上下文条件机制，将空间先验信息融入到预训练的文本到视频生成模型中，增强视频合成能力。

**主要结论**：实验表明，CineScene在场景一致的电影视频生成上取得了最先进的性能，能够处理大幅度的摄像机移动并在多样化环境中表现出良好的泛化能力。

**关键词**：关键词：深度学习, 生成, 视觉表示, 视频生成, 3D场景, 语境条件, 相机控制, 一致性, 动态主体, rag

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06959v1) | [下载PDF](https://arxiv.org/pdf/2602.06959v1.pdf)

---

## [9. Reliable Mislabel Detection for Video Capsule Endoscopy Data](https://arxiv.org/abs/2602.06938v1)

**作者**：Julia Werner, Julius Oexle, Oliver Bause 等 8 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

The classification performance of deep neural networks relies strongly on access to large, accurately annotated datasets. In medical imaging, however, obtaining such datasets is particularly challenging since annotations must be provided by specialized physicians, which severely limits the pool of annotators. Furthermore, class boundaries can often be ambiguous or difficult to define which further complicates machine learning-based classification. In this paper, we want to address this problem and introduce a framework for mislabel detection in medical datasets. This is validated on the two largest, publicly available datasets for Video Capsule Endoscopy, an important imaging procedure for examining the gastrointestinal tract based on a video stream of lowresolution images. In addition, potentially mislabeled samples identified by our pipeline were reviewed and re-annotated by three experienced gastroenterologists. Our results show that the proposed framework successfully detects incorrectly labeled data and results in an improved anomaly detection performance after cleaning the datasets compared to current baselines.

### 🤖 AI 总结

**一句话总结**：提出了一种框架用于检测医疗数据中的错误标签，特别是视频胶囊内窥镜数据，能够提高异常检测性能。

**研究动机**：医疗影像数据的准确标注依赖于专业医生，但获取这样的大规模数据集极具挑战性，且标签可能存在模糊性。

**核心方法**：开发了一个用于错误标签检测的框架，并在两个大型公开视频胶囊内窥镜数据集上进行验证，识别出潜在错误标签的样本并由经验丰富的胃肠病专家重新标注。

**主要结论**：该框架成功识别了错误标记的数据，并在清理数据集后，异常检测性能相较于当前基线有所提升。

**关键词**：深度学习, 神经网络, 机器学习, 医学影像, 视频胶囊内镜, 错误标注检测, 数据集清洗, 异常检测, 监督学习, machine learning

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06938v1) | [下载PDF](https://arxiv.org/pdf/2602.06938v1.pdf)

---

## [10. RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing](https://arxiv.org/abs/2602.06871v1)

**作者**：Mohammadreza Salehi, Mehdi Noroozi, Luca Morreale 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-06

### 📄 论文摘要

Instructional video editing applies edits to an input video using only text prompts, enabling intuitive natural-language control. Despite rapid progress, most methods still require fixed-length inputs and substantial compute. Meanwhile, autoregressive video generation enables efficient variable-length synthesis, yet remains under-explored for video editing. We introduce a causal, efficient video editing model that edits variable-length videos frame by frame. For efficiency, we start from a 2D image-to-image (I2I) diffusion model and adapt it to video-to-video (V2V) editing by conditioning the edit at time step t on the model's prediction at t-1. To leverage videos' temporal redundancy, we propose a new I2I diffusion forward process formulation that encourages the model to predict the residual between the target output and the previous prediction. We call this Residual Flow Diffusion Model (RFDM), which focuses the denoising process on changes between consecutive frames. Moreover, we propose a new benchmark that better ranks state-of-the-art methods for editing tasks. Trained on paired video data for global/local style transfer and object removal, RFDM surpasses I2I-based methods and competes with fully spatiotemporal (3D) V2V models, while matching the compute of image models and scaling independently of input video length. More content can be found in: https://smsd75.github.io/RFDM_page/

### 🤖 AI 总结

**一句话总结**：RFDM是一种针对可变长度视频的高效编辑模型，利用残差流扩散方法进行逐帧编辑。

**研究动机**：当前视频编辑方法多需固定长度输入且计算资源消耗大，因此需要更高效的编辑模型。

**核心方法**：RFDM通过将2D图像到图像的扩散模型适配为视频到视频编辑，利用时间冗余预测帧间变化的残差。

**主要结论**：RFDM在风格转移和物体移除任务中超越了传统方法，并在计算效率上与图像模型相匹配，表现出色。

**关键词**：残差流扩散模型, 视频编辑, 自然语言控制, 变量长度合成, 2D图像到图像, I2I扩散模型, V2V编辑, 时序冗余, 计算效率, diffusion

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06871v1) | [下载PDF](https://arxiv.org/pdf/2602.06871v1.pdf)

---

## [11. Parameters as Experts: Adapting Vision Models with Dynamic Parameter Routing](https://arxiv.org/abs/2602.06862v1)

**作者**：Meng Lou, Stanley Yu, Yizhou Yu  
**分类**：cs.CV  
**发布时间**：2026-02-06

### 📄 论文摘要

Adapting pre-trained vision models using parameter-efficient fine-tuning (PEFT) remains challenging, as it aims to achieve performance comparable to full fine-tuning using a minimal number of trainable parameters. When applied to complex dense prediction tasks, existing methods exhibit limitations, including input-agnostic modeling and redundant cross-layer representations. To this end, we propose AdaRoute, a new adapter-style method featuring a simple mixture-of-experts (MoE) architecture. Specifically, we introduce shared expert centers, where each expert is a trainable parameter matrix. During a feedforward pass, each AdaRoute module in the network dynamically generates weight matrices tailored for the current module via a simple dynamic parameter routing mechanism, which selectively aggregates parameter matrices in the corresponding expert center. Dynamic weight matrices in AdaRoute modules facilitate low-rank adaptation in an input-dependent manner, thus generating more customized and powerful feature representations. Moreover, since AdaRoute modules across multiple network layers share the same expert center, they improve feature diversity by promoting implicit cross-layer feature interaction. Extensive experiments demonstrate the superiority of AdaRoute on diverse vision tasks, including semantic segmentation, object detection and instance segmentation, and panoptic segmentation. Code will be available at: https://bit.ly/3NZcr0H.

### 🤖 AI 总结

**一句话总结**：本文提出AdaRoute，一种基于混合专家架构的适应性方法，通过动态参数路由实现高效的视觉模型调整。

**研究动机**：现有的参数高效微调方法在复杂的密集预测任务中存在输入无关建模和冗余跨层表示等局限。

**核心方法**：AdaRoute使用共享专家中心和动态生成的权重矩阵，以实现输入依赖的低秩适应，从而增强特征表示能力。

**主要结论**：实验结果表明，AdaRoute在语义分割、目标检测等多种视觉任务上均表现优越。

**关键词**：动态参数路由, 视觉模型, 适应性, 混合专家, 参数高效微调, 特征表示, 深度学习, 任务适应, agent

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06862v1) | [下载PDF](https://arxiv.org/pdf/2602.06862v1.pdf)

---

## [12. Rethinking Multi-Condition DiTs: Eliminating Redundant Attention via Position-Alignment and Keyword-Scoping](https://arxiv.org/abs/2602.06850v1)

**作者**：Chao Zhou, Tianyi Wei, Yiling Chen 等 5 位作者  
**分类**：cs.CV, cs.AI, cs.MM  
**发布时间**：2026-02-06

### 📄 论文摘要

While modern text-to-image models excel at prompt-based generation, they often lack the fine-grained control necessary for specific user requirements like spatial layouts or subject appearances. Multi-condition control addresses this, yet its integration into Diffusion Transformers (DiTs) is bottlenecked by the conventional ``concatenate-and-attend'' strategy, which suffers from quadratic computational and memory overhead as the number of conditions scales. Our analysis reveals that much of this cross-modal interaction is spatially or semantically redundant. To this end, we propose Position-aligned and Keyword-scoped Attention (PKA), a highly efficient framework designed to eliminate these redundancies. Specifically, Position-Aligned Attention (PAA) linearizes spatial control by enforcing localized patch alignment, while Keyword-Scoped Attention (KSA) prunes irrelevant subject-driven interactions via semantic-aware masking. To facilitate efficient learning, we further introduce a Conditional Sensitivity-Aware Sampling (CSAS) strategy that reweights the training objective towards critical denoising phases, drastically accelerating convergence and enhancing conditional fidelity. Empirically, PKA delivers a 10.0$\times$ inference speedup and a 5.1$\times$ VRAM saving, providing a scalable and resource-friendly solution for high-fidelity multi-conditioned generation.

### 🤖 AI 总结

**一句话总结**：本文提出了一种高效的注意力机制，通过位置对齐和关键词范围控制来消除多条件生成中的冗余，从而提高生成效率。

**研究动机**：现代文本到图像模型在基于提示的生成方面表现出色，但缺乏对特定用户需求的精细控制，尤其是在多条件控制的应用中存在计算和内存开销问题。

**核心方法**：提出了位置对齐注意力（PAA）和关键词范围注意力（KSA）来优化多条件交互，同时引入条件敏感性采样（CSAS）策略加速学习过程。

**主要结论**：实验结果表明，PKA在推理速度上提升了10倍，并节省了5.1倍的显存，为高保真多条件生成提供了可扩展的解决方案。

**关键词**：多条件控制, 文本生成, 扩散变换器, 位置对齐, 关键词范围, 语义遮罩, 高效学习, 训练目标, 生成模型, 深度学习, diffusion

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06850v1) | [下载PDF](https://arxiv.org/pdf/2602.06850v1.pdf)

---

## cs.LG

## [13. Learning a Generative Meta-Model of LLM Activations](https://arxiv.org/abs/2602.06964v1)

**作者**：Grace Luo, Jiahai Feng, Trevor Darrell 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-02-06

### 📄 论文摘要

Existing approaches for analyzing neural network activations, such as PCA and sparse autoencoders, rely on strong structural assumptions. Generative models offer an alternative: they can uncover structure without such assumptions and act as priors that improve intervention fidelity. We explore this direction by training diffusion models on one billion residual stream activations, creating "meta-models" that learn the distribution of a network's internal states. We find that diffusion loss decreases smoothly with compute and reliably predicts downstream utility. In particular, applying the meta-model's learned prior to steering interventions improves fluency, with larger gains as loss decreases. Moreover, the meta-model's neurons increasingly isolate concepts into individual units, with sparse probing scores that scale as loss decreases. These results suggest generative meta-models offer a scalable path toward interpretability without restrictive structural assumptions. Project page: https://generative-latent-prior.github.io.

### 🤖 AI 总结

**一句话总结**：本文提出了一种生成性元模型，通过训练扩散模型分析神经网络激活，提供了无结构假设的可解释性路径。

**研究动机**：传统的神经网络激活分析方法依赖于强结构假设，限制了其灵活性和有效性，因此需要探索新的方法来揭示网络的内部状态。

**核心方法**：研究通过对十亿个残差流激活进行扩散模型训练，创建了学习网络内部状态分布的“元模型”。

**主要结论**：生成性元模型在提高干预的流畅性和可解释性方面表现出色，并且在损失减小时，神经元能够更好地隔离概念。

**关键词**：生成模型, 神经网络, 深度学习, 激活分析, 介入干预, 结构假设, 扩散模型, 语义搜索, 多任务学习, 生成元模型, neural network

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06964v1) | [下载PDF](https://arxiv.org/pdf/2602.06964v1.pdf)

---

## [14. Improving Credit Card Fraud Detection with an Optimized Explainable Boosting Machine](https://arxiv.org/abs/2602.06955v1)

**作者**：Reza E. Fazel, Arash Bakhtiary, Siavash A. Bigdeli  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Addressing class imbalance is a central challenge in credit card fraud detection, as it directly impacts predictive reliability in real-world financial systems. To overcome this, the study proposes an enhanced workflow based on the Explainable Boosting Machine (EBM)-a transparent, state-of-the-art implementation of the GA2M algorithm-optimized through systematic hyperparameter tuning, feature selection, and preprocessing refinement. Rather than relying on conventional sampling techniques that may introduce bias or cause information loss, the optimized EBM achieves an effective balance between accuracy and interpretability, enabling precise detection of fraudulent transactions while providing actionable insights into feature importance and interaction effects. Furthermore, the Taguchi method is employed to optimize both the sequence of data scalers and model hyperparameters, ensuring robust, reproducible, and systematically validated performance improvements. Experimental evaluation on benchmark credit card data yields an ROC-AUC of 0.983, surpassing prior EBM baselines (0.975) and outperforming Logistic Regression, Random Forest, XGBoost, and Decision Tree models. These results highlight the potential of interpretable machine learning and data-driven optimization for advancing trustworthy fraud analytics in financial systems.

### 🤖 AI 总结

**一句话总结**：研究通过优化的可解释增强机（EBM）提升信用卡欺诈检测的准确性和可解释性，解决类不平衡问题。

**研究动机**：信用卡欺诈检测中的类不平衡问题直接影响预测可靠性，因此需要改进检测方法以提高准确性和解释能力。

**核心方法**：采用优化的可解释增强机（EBM），通过超参数调优、特征选择和预处理改进，实现高效的准确性与可解释性的平衡，并使用田口法优化数据缩放器和模型超参数。

**主要结论**：实验表明，优化后的EBM在信用卡数据集上的ROC-AUC达到0.983，超越了以往的EBM基准和其他主流模型，展示了可解释机器学习在金融欺诈分析中的潜力。

**关键词**：信用卡欺诈检测, 解释性增强机器, 机器学习, 深度学习, 特征选择, 数据预处理, 预测可靠性, 透明性, ROC-AUC, machine learning

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06955v1) | [下载PDF](https://arxiv.org/pdf/2602.06955v1.pdf)

---

## [15. Endogenous Resistance to Activation Steering in Language Models](https://arxiv.org/abs/2602.06941v1)

**作者**：Alex McKenzie, Keenan Pepper, Stijn Servaes 等 9 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-02-06

### 📄 论文摘要

Large language models can resist task-misaligned activation steering during inference, sometimes recovering mid-generation to produce improved responses even when steering remains active. We term this Endogenous Steering Resistance (ESR). Using sparse autoencoder (SAE) latents to steer model activations, we find that Llama-3.3-70B shows substantial ESR, while smaller models from the Llama-3 and Gemma-2 families exhibit the phenomenon less frequently. We identify 26 SAE latents that activate differentially during off-topic content and are causally linked to ESR in Llama-3.3-70B. Zero-ablating these latents reduces the multi-attempt rate by 25%, providing causal evidence for dedicated internal consistency-checking circuits. We demonstrate that ESR can be deliberately enhanced through both prompting and training: meta-prompts instructing the model to self-monitor increase the multi-attempt rate by 4x for Llama-3.3-70B, and fine-tuning on self-correction examples successfully induces ESR-like behavior in smaller models. These findings have dual implications: ESR could protect against adversarial manipulation but might also interfere with beneficial safety interventions that rely on activation steering. Understanding and controlling these resistance mechanisms is important for developing transparent and controllable AI systems. Code is available at github.com/agencyenterprise/endogenous-steering-resistance.

### 🤖 AI 总结

**一句话总结**：大型语言模型具有自我监控的能力，能够抵抗任务不对齐的激活引导，表现出内生性抵抗现象。

**研究动机**：研究旨在探讨语言模型在推理过程中如何抵抗不当的激活引导，进而改善生成结果。

**核心方法**：通过稀疏自编码器潜变量（SAE）对模型激活进行引导，分析不同模型的内生性抵抗现象及其因果关系。

**主要结论**：内生性抵抗可能保护模型免受攻击，但也可能干扰依赖激活引导的安全干预，因此理解和控制这些机制对发展透明可控的AI系统至关重要。

**关键词**：语言模型, 深度学习, 神经网络, 自然语言处理, 自我监控, 激活引导, 透明可控AI, Llama-3.3-70B, 稀疏自编码器

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06941v1) | [下载PDF](https://arxiv.org/pdf/2602.06941v1.pdf)

---

## [16. From Core to Detail: Unsupervised Disentanglement with Entropy-Ordered Flows](https://arxiv.org/abs/2602.06940v1)

**作者**：Daniel Galperin, Ullrich Köthe  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Learning unsupervised representations that are both semantically meaningful and stable across runs remains a central challenge in modern representation learning. We introduce entropy-ordered flows (EOFlows), a normalizing-flow framework that orders latent dimensions by their explained entropy, analogously to PCA's explained variance. This ordering enables adaptive injective flows: after training, one may retain only the top C latent variables to form a compact core representation while the remaining variables capture fine-grained detail and noise, with C chosen flexibly at inference time rather than fixed during training. EOFlows build on insights from Independent Mechanism Analysis, Principal Component Flows and Manifold Entropic Metrics. We combine likelihood-based training with local Jacobian regularization and noise augmentation into a method that scales well to high-dimensional data such as images. Experiments on the CelebA dataset show that our method uncovers a rich set of semantically interpretable features, allowing for high compression and strong denoising.

### 🤖 AI 总结

**一句话总结**：提出了一种新的无监督表示学习方法EOFlows，通过熵排序流框架实现语义明确且稳定的特征提取。

**研究动机**：在现代表示学习中，如何学习到语义明确且在多次实验中稳定的表示依然是一个重要挑战。

**核心方法**：EOFlows通过按解释熵对潜在维度进行排序，结合基于似然的训练和局部雅可比正则化，能够在高维数据上有效工作。

**主要结论**：在CelebA数据集上的实验表明，EOFlows能够发现丰富的语义可解释特征，实现高压缩和强去噪。

**关键词**：无监督表示学习, 表示学习, 归一化流, 潜在变量, 语义特征, 高维数据, 噪声增强, EOFlows, 图像处理, agent

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06940v1) | [下载PDF](https://arxiv.org/pdf/2602.06940v1.pdf)

---

## [17. Cochain Perspectives on Temporal-Difference Signals for Learning Beyond Markov Dynamics](https://arxiv.org/abs/2602.06939v1)

**作者**：Zuyuan Zhang, Sizhe Tang, Tian Lan  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-06

### 📄 论文摘要

Non-Markovian dynamics are commonly found in real-world environments due to long-range dependencies, partial observability, and memory effects. The Bellman equation that is the central pillar of Reinforcement learning (RL) becomes only approximately valid under Non-Markovian. Existing work often focus on practical algorithm designs and offer limited theoretical treatment to address key questions, such as what dynamics are indeed capturable by the Bellman framework and how to inspire new algorithm classes with optimal approximations. In this paper, we present a novel topological viewpoint on temporal-difference (TD) based RL. We show that TD errors can be viewed as 1-cochain in the topological space of state transitions, while Markov dynamics are then interpreted as topological integrability. This novel view enables us to obtain a Hodge-type decomposition of TD errors into an integrable component and a topological residual, through a Bellman-de Rham projection. We further propose HodgeFlow Policy Search (HFPS) by fitting a potential network to minimize the non-integrable projection residual in RL, achieving stability/sensitivity guarantees. In numerical evaluations, HFPS is shown to significantly improve RL performance under non-Markovian.

### 🤖 AI 总结

**一句话总结**：本文提出了一种新颖的拓扑视角来处理非马尔可夫动态下的时序差分信号，以改进强化学习性能。

**研究动机**：非马尔可夫动态在真实环境中普遍存在，现有的强化学习理论和算法在处理这些动态时存在局限性。

**核心方法**：作者将时序差分误差视为状态转移的1-链，通过贝尔曼-德拉姆投影实现误差的霍奇型分解，并提出霍奇流策略搜索方法以最小化非可积投影残差。

**主要结论**：霍奇流策略搜索方法在数值评估中显著提高了非马尔可夫环境下的强化学习性能，展示了新方法的有效性。

**关键词**：强化学习, 非马尔可夫, 时间差分, HodgeFlow策略搜索, 状态转移, 潜在网络, llm

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06939v1) | [下载PDF](https://arxiv.org/pdf/2602.06939v1.pdf)

---

## [18. Robustness Beyond Known Groups with Low-rank Adaptation](https://arxiv.org/abs/2602.06924v1)

**作者**：Abinitha Gourabathina, Hyewon Jeong, Teya Bergamaschi 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Deep learning models trained to optimize average accuracy often exhibit systematic failures on particular subpopulations. In real world settings, the subpopulations most affected by such disparities are frequently unlabeled or unknown, thereby motivating the development of methods that are performant on sensitive subgroups without being pre-specified. However, existing group-robust methods typically assume prior knowledge of relevant subgroups, using group annotations for training or model selection. We propose Low-rank Error Informed Adaptation (LEIA), a simple two-stage method that improves group robustness by identifying a low-dimensional subspace in the representation space where model errors concentrate. LEIA restricts adaptation to this error-informed subspace via a low-rank adjustment to the classifier logits, directly targeting latent failure modes without modifying the backbone or requiring group labels. Using five real-world datasets, we analyze group robustness under three settings: (1) truly no knowledge of subgroup relevance, (2) partial knowledge of subgroup relevance, and (3) full knowledge of subgroup relevance. Across all settings, LEIA consistently improves worst-group performance while remaining fast, parameter-efficient, and robust to hyperparameter choice.

### 🤖 AI 总结

**一句话总结**：提出了一种名为LEIA的方法，通过低秩调整提高深度学习模型对未知子群体的鲁棒性。

**研究动机**：深度学习模型在特定子群体上的系统性失效激励了对无标签或未知子群体的鲁棒性方法的需求。

**核心方法**：LEIA通过识别表示空间中的低维子空间来集中模型错误，并通过低秩调整分类器的logits进行适应。

**主要结论**：LEIA在不同的子群体知识设置下均能提高模型在最差子群体上的表现，同时保持快速和参数高效。

**关键词**：深度学习, 机器学习, 低秩适应, 模型鲁棒性, 子群体, 表示空间, 错误调整, 适应性算法, group robustness, error-informed adaptation, deep learning

**评分**：69

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06924v1) | [下载PDF](https://arxiv.org/pdf/2602.06924v1.pdf)

---

## [19. From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers](https://arxiv.org/abs/2602.06923v1)

**作者**：Ziming Liu, Sophia Sanborn, Surya Ganguli 等 4 位作者  
**分类**：cs.LG, cs.AI, physics.class-ph  
**发布时间**：2026-02-06

### 📄 论文摘要

Can general-purpose AI architectures go beyond prediction to discover the physical laws governing the universe? True intelligence relies on "world models" -- causal abstractions that allow an agent to not only predict future states but understand the underlying governing dynamics. While previous "AI Physicist" approaches have successfully recovered such laws, they typically rely on strong, domain-specific priors that effectively "bake in" the physics. Conversely, Vafa et al. recently showed that generic Transformers fail to acquire these world models, achieving high predictive accuracy without capturing the underlying physical laws. We bridge this gap by systematically introducing three minimal inductive biases. We show that ensuring spatial smoothness (by formulating prediction as continuous regression) and stability (by training with noisy contexts to mitigate error accumulation) enables generic Transformers to surpass prior failures and learn a coherent Keplerian world model, successfully fitting ellipses to planetary trajectories. However, true physical insight requires a third bias: temporal locality. By restricting the attention window to the immediate past -- imposing the simple assumption that future states depend only on the local state rather than a complex history -- we force the model to abandon curve-fitting and discover Newtonian force representations. Our results demonstrate that simple architectural choices determine whether an AI becomes a curve-fitter or a physicist, marking a critical step toward automated scientific discovery.

### 🤖 AI 总结

**一句话总结**：通过引入简单的归纳偏置，研究表明通用变压器可以学习物理世界模型，从而实现自动化科学发现。

**研究动机**：研究旨在探索通用AI架构能否超越预测，实现对宇宙物理法则的发现，强调世界模型在智能中的重要性。

**核心方法**：通过引入空间平滑性、稳定性和时间局部性这三种归纳偏置，改善了通用变压器的学习效果，使其能够学习到凯普勒和牛顿的物理模型。

**主要结论**：简单的架构选择决定了AI是成为曲线拟合器还是物理学家，标志着自动化科学发现的重要进展。

**关键词**：深度学习, 变换器, 世界模型, 代理, 归纳偏置, 空间平滑性, 时序局部性, 预测模型, 物理法则, causal abstraction, agent

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06923v1) | [下载PDF](https://arxiv.org/pdf/2602.06923v1.pdf)

---

## [20. Revisiting the Generic Transformer: Deconstructing a Strong Baseline for Time Series Foundation Models](https://arxiv.org/abs/2602.06909v1)

**作者**：Yunshi Wen, Wesley M. Gifford, Chandra Reddy 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

The recent surge in Time Series Foundation Models has rapidly advanced the field, yet the heterogeneous training setups across studies make it difficult to attribute improvements to architectural innovations versus data engineering. In this work, we investigate the potential of a standard patch Transformer, demonstrating that this generic architecture achieves state-of-the-art zero-shot forecasting performance using a straightforward training protocol. We conduct a comprehensive ablation study that covers model scaling, data composition, and training techniques to isolate the essential ingredients for high performance. Our findings identify the key drivers of performance, while confirming that the generic architecture itself demonstrates excellent scalability. By strictly controlling these variables, we provide comprehensive empirical results on model scaling across multiple dimensions. We release our open-source model and detailed findings to establish a transparent, reproducible baseline for future research.

### 🤖 AI 总结

**一句话总结**：本研究探讨了标准补丁Transformer在时间序列预测中的优势，证明其在简单训练协议下可实现最佳零-shot预测性能。

**研究动机**：随着时间序列基础模型的快速发展，研究中训练设置的异质性使得难以明确性能提升来自架构创新还是数据工程。

**核心方法**：通过全面的消融研究，分析模型扩展、数据组成和训练技术，隔离出高性能的关键因素。

**主要结论**：发现通用架构表现出优越的可扩展性，并提供了透明、可重复的基线以支持未来研究。

**关键词**：时间序列, Transformer, 预测模型, 深度学习, 模型缩放, 数据组合, 训练技术, 生成模型, 语义搜索

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06909v1) | [下载PDF](https://arxiv.org/pdf/2602.06909v1.pdf)

---

## [21. A first realization of reinforcement learning-based closed-loop EEG-TMS](https://arxiv.org/abs/2602.06907v1)

**作者**：Dania Humaidan, Jiahua Xu, Jing Chen 等 11 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Background: Transcranial magnetic stimulation (TMS) is a powerful tool to investigate neurophysiology of the human brain and treat brain disorders. Traditionally, therapeutic TMS has been applied in a one-size-fits-all approach, disregarding inter- and intra-individual differences. Brain state-dependent EEG-TMS, such as coupling TMS with a pre-specified phase of the sensorimotor mu-rhythm, enables the induction of differential neuroplastic effects depending on the targeted phase. But this approach is still user-dependent as it requires defining an a-priori target phase. Objectives: To present a first realization of a machine-learning-based, closed-loop real-time EEG-TMS setup to identify user-independently the individual mu-rhythm phase associated with high- vs. low-corticospinal excitability states. Methods: We applied EEG-TMS to 25 participants targeting the supplementary motor area-primary motor cortex network and used a reinforcement learning algorithm to identify the mu-rhythm phase associated with high- vs. low corticospinal excitability. We employed linear mixed effects models and Bayesian analysis to determine effects of reinforced learning on corticospinal excitability indexed by motor evoked potential amplitude, and functional connectivity indexed by the imaginary part of resting-state EEG coherence. Results: Reinforcement learning effectively identified the mu-rhythm phase associated with high- vs. low-excitability states, and their repetitive stimulation resulted in long-term increases vs. decreases in functional connectivity in the stimulated sensorimotor network. Conclusions: We demonstrated for the first time the feasibility of closed-loop EEG-TMS in humans, a critical step towards individualized treatment of brain disorders.

### 🤖 AI 总结

**一句话总结**：该研究首次实现了基于强化学习的闭环EEG-TMS系统，能够用户独立地识别与高低皮质脊髓兴奋性状态相关的mu节律相位。

**研究动机**：传统的TMS治疗方法未考虑个体差异，因此研究者希望通过EEG-TMS结合机器学习实现个性化治疗。

**核心方法**：研究团队对25名参与者应用EEG-TMS，利用强化学习算法识别与皮质脊髓兴奋性状态相关的mu节律相位，并通过混合效应模型和贝叶斯分析评估其效果。

**主要结论**：研究成果表明，闭环EEG-TMS在人体中的可行性，为个性化脑部疾病治疗迈出了重要一步。

**关键词**：强化学习, 机器学习, 脑电图, 运动皮层, 神经可塑性, 实时系统, 用户独立, 功能连接性, 反馈学习, agent

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06907v1) | [下载PDF](https://arxiv.org/pdf/2602.06907v1.pdf)

---

## [22. Parameter-free Dynamic Regret: Time-varying Movement Costs, Delayed Feedback, and Memory](https://arxiv.org/abs/2602.06902v1)

**作者**：Emmanuel Esposito, Andrew Jacobsen, Hao Qiu 等 4 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-02-06

### 📄 论文摘要

In this paper, we study dynamic regret in unconstrained online convex optimization (OCO) with movement costs. Specifically, we generalize the standard setting by allowing the movement cost coefficients $λ_t$ to vary arbitrarily over time. Our main contribution is a novel algorithm that establishes the first comparator-adaptive dynamic regret bound for this setting, guaranteeing $\widetilde{\mathcal{O}}(\sqrt{(1+P_T)(T+\sum_t λ_t)})$ regret, where $P_T$ is the path length of the comparator sequence over $T$ rounds. This recovers the optimal guarantees for both static and dynamic regret in standard OCO as a special case where $λ_t=0$ for all rounds. To demonstrate the versatility of our results, we consider two applications: OCO with delayed feedback and OCO with time-varying memory. We show that both problems can be translated into time-varying movement costs, establishing a novel reduction specifically for the delayed feedback setting that is of independent interest. A crucial observation is that the first-order dependence on movement costs in our regret bound plays a key role in enabling optimal comparator-adaptive dynamic regret guarantees in both settings.

### 🤖 AI 总结

**一句话总结**：本文提出了一种新的算法，针对动态在线凸优化中的运动成本，建立了首个比较器自适应的动态遗憾界限。

**研究动机**：研究动态遗憾在不受约束的在线凸优化中的表现，特别是在运动成本随时间变化的情况下。

**核心方法**：通过引入时间变化的运动成本系数，提出了一种新算法并证明其动态遗憾界限的有效性。

**主要结论**：该算法在处理延迟反馈和时间变化记忆等问题时，实现了最佳的比较器自适应动态遗憾界限。

**关键词**：动态遗憾, 在线凸优化, 算法, 反馈延迟, 记忆, 自适应, 最优保证, 运动成本, 时间变化, agent

**评分**：55

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06902v1) | [下载PDF](https://arxiv.org/pdf/2602.06902v1.pdf)

---

## [23. Supercharging Simulation-Based Inference for Bayesian Optimal Experimental Design](https://arxiv.org/abs/2602.06900v1)

**作者**：Samuel Klein, Willie Neiswanger, Daniel Ratner 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.IT, cs.NE, stat.ML  
**发布时间**：2026-02-06

### 📄 论文摘要

Bayesian optimal experimental design (BOED) seeks to maximize the expected information gain (EIG) of experiments. This requires a likelihood estimate, which in many settings is intractable. Simulation-based inference (SBI) provides powerful tools for this regime. However, existing work explicitly connecting SBI and BOED is restricted to a single contrastive EIG bound. We show that the EIG admits multiple formulations which can directly leverage modern SBI density estimators, encompassing neural posterior, likelihood, and ratio estimation. Building on this perspective, we define a novel EIG estimator using neural likelihood estimation. Further, we identify optimization as a key bottleneck of gradient based EIG maximization and show that a simple multi-start parallel gradient ascent procedure can substantially improve reliability and performance. With these innovations, our SBI-based BOED methods are able to match or outperform by up to $22\%$ existing state-of-the-art approaches across standard BOED benchmarks.

### 🤖 AI 总结

**一句话总结**：本文提出了一种改进的贝叶斯最优实验设计方法，通过模拟推断提高信息增益的估计精度。

**研究动机**：贝叶斯最优实验设计旨在最大化实验的信息增益，但在许多情况下似乎难以获得有效的似然估计，而模拟推断提供了强有力的解决方案。

**核心方法**：本文定义了一种新颖的信息增益估计器，利用神经似然估计，并提出了一种多起始并行梯度上升程序来优化信息增益的最大化过程。

**主要结论**：通过这些创新，基于模拟推断的贝叶斯最优实验设计方法在标准基准测试中能够达到或超过现有最先进的方法，性能提高了最多22%。

**关键词**：贝叶斯, 最优实验设计, 期望信息增益, 模拟推断, 神经网络, 生成模型, 多启动并行梯度上升, 优化瓶颈, 可靠性提升, rag

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06900v1) | [下载PDF](https://arxiv.org/pdf/2602.06900v1.pdf)

---

## [24. Sample Complexity of Causal Identification with Temporal Heterogeneity](https://arxiv.org/abs/2602.06899v1)

**作者**：Ameya Rathod, Sujay Belsare, Salvik Krishna Nautiyal 等 5 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-02-06

### 📄 论文摘要

Recovering a unique causal graph from observational data is an ill-posed problem because multiple generating mechanisms can lead to the same observational distribution. This problem becomes solvable only by exploiting specific structural or distributional assumptions. While recent work has separately utilized time-series dynamics or multi-environment heterogeneity to constrain this problem, we integrate both as complementary sources of heterogeneity. This integration yields unified necessary identifiability conditions and enables a rigorous analysis of the statistical limits of recovery under thin versus heavy-tailed noise. In particular, temporal structure is shown to effectively substitute for missing environmental diversity, possibly achieving identifiability even under insufficient heterogeneity. Extending this analysis to heavy-tailed (Student's t) distributions, we demonstrate that while geometric identifiability conditions remain invariant, the sample complexity diverges significantly from the Gaussian baseline. Explicit information-theoretic bounds quantify this cost of robustness, establishing the fundamental limits of covariance-based causal graph recovery methods in realistic non-stationary systems. This work shifts the focus from whether causal structure is identifiable to whether it is statistically recoverable in practice.

### 🤖 AI 总结

**一句话总结**：本研究通过整合时间序列动态和多环境异质性，为因果图的唯一恢复提供了统一的可识别性条件。

**研究动机**：因果图的恢复是一个不适定的问题，传统方法难以解决，因此需要利用特定的结构或分布假设来约束这一问题。

**核心方法**：将时间序列动态与多环境异质性相结合，提出了统一的识别条件，并分析了在不同噪声条件下的统计极限。

**主要结论**：研究表明，时间结构可以有效替代缺失的环境多样性，且在重尾分布下，样本复杂度与高斯基线显著不同，确立了因果图恢复方法的基本极限。

**关键词**：因果识别, 观察数据, 统计极限, 时间序列, 多环境异质性, 采样复杂度, 结构假设, 统计恢复, 非平稳系统, 信息论界限, agent

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06899v1) | [下载PDF](https://arxiv.org/pdf/2602.06899v1.pdf)

---

## [25. A Cycle-Consistent Graph Surrogate for Full-Cycle Left Ventricular Myocardial Biomechanics](https://arxiv.org/abs/2602.06884v1)

**作者**：Siyu Mu, Wei Xuan Chan, Choon Hwai Yap  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Image-based patient-specific simulation of left ventricular (LV) mechanics is valuable for understanding cardiac function and supporting clinical intervention planning, but conventional finite-element analysis (FEA) is computationally intensive. Current graph-based surrogates do not have full-cycle prediction capabilities, and physics-informed neural networks often struggle to converge on complex cardiac geometries. We present CardioGraphFENet (CGFENet), a unified graph-based surrogate for rapid full-cycle estimation of LV myocardial biomechanics, supervised by a large FEA simulation dataset. The proposed model integrates (i) a global--local graph encoder to capture mesh features with weak-form-inspired global coupling, (ii) a gated recurrent unit-based temporal encoder conditioned on the target volume-time signal to model cycle-coherent dynamics, and (iii) a cycle-consistent bidirectional formulation for both loading and inverse unloading within a single framework. These strategies enable high fidelity with respect to traditional FEA ground truths and produce physiologically plausible pressure-volume loops that match FEA results when coupled with a lumped-parameter model. In particular, the cycle-consistency strategy enables a significant reduction in FEA supervision with only minimal loss in accuracy.

### 🤖 AI 总结

**一句话总结**：提出了一种名为CardioGraphFENet的图形代理模型，能够快速估算左心室心肌生物力学，并具备完整的周期预测能力。

**研究动机**：传统的有限元分析计算量大且效率低下，现有的图形代理模型缺乏完整周期预测能力，因此需要一种新的方法来提高心脏功能模拟的效率。

**核心方法**：CGFENet结合了全球-局部图编码器、基于门控循环单元的时间编码器以及循环一致的双向公式，能够在一个框架内进行负载和逆卸载的建模。

**主要结论**：该模型在保证与传统有限元分析结果一致性的同时，显著减少了对有限元监督的需求，且只造成了微小的准确度损失。

**关键词**：图神经网络, 深度学习, 机器学习, 图像处理, CardioGraphFENet, 循环一致性, 生物力学, 模型融合, 预测模型, neural network

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06884v1) | [下载PDF](https://arxiv.org/pdf/2602.06884v1.pdf)

---

## [26. Vision Transformer Finetuning Benefits from Non-Smooth Components](https://arxiv.org/abs/2602.06883v1)

**作者**：Ambroise Odonnat, Laetitia Chapel, Romain Tavenard 等 4 位作者  
**分类**：cs.LG, cs.CV, stat.ML  
**发布时间**：2026-02-06

### 📄 论文摘要

The smoothness of the transformer architecture has been extensively studied in the context of generalization, training stability, and adversarial robustness. However, its role in transfer learning remains poorly understood. In this paper, we analyze the ability of vision transformer components to adapt their outputs to changes in inputs, or, in other words, their plasticity. Defined as an average rate of change, it captures the sensitivity to input perturbation; in particular, a high plasticity implies low smoothness. We demonstrate through theoretical analysis and comprehensive experiments that this perspective provides principled guidance in choosing the components to prioritize during adaptation. A key takeaway for practitioners is that the high plasticity of the attention modules and feedforward layers consistently leads to better finetuning performance. Our findings depart from the prevailing assumption that smoothness is desirable, offering a novel perspective on the functional properties of transformers. The code is available at https://github.com/ambroiseodt/vit-plasticity.

### 🤖 AI 总结

**一句话总结**：研究表明视觉变换器的非平滑特性有助于提高微调性能，尤其是在注意力模块和前馈层中表现突出。

**研究动机**：传统上，变换器的平滑性被认为对泛化和稳定性有利，但在迁移学习中的作用尚不明确。

**核心方法**：通过理论分析和全面实验，研究了视觉变换器组件对输入变化的适应能力，定义为塑性，强调高塑性与低平滑性之间的关系。

**主要结论**：高塑性的关注模块和前馈层在微调中表现更佳，挑战了平滑性为优的传统假设，为变换器的功能特性提供了新视角。

**关键词**：视觉变换器, finetuning, transformer, 适应性, 迁移学习, 注意力模块, 反馈层, 高塑性, 训练稳定性

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06883v1) | [下载PDF](https://arxiv.org/pdf/2602.06883v1.pdf)

---

## [27. T-STAR: A Context-Aware Transformer Framework for Short-Term Probabilistic Demand Forecasting in Dock-Based Shared Micro-Mobility](https://arxiv.org/abs/2602.06866v1)

**作者**：Jingyi Cheng, Gonçalo Homem de Almeida Correia, Oded Cats 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Reliable short-term demand forecasting is essential for managing shared micro-mobility services and ensuring responsive, user-centered operations. This study introduces T-STAR (Two-stage Spatial and Temporal Adaptive contextual Representation), a novel transformer-based probabilistic framework designed to forecast station-level bike-sharing demand at a 15-minute resolution. T-STAR addresses key challenges in high-resolution forecasting by disentangling consistent demand patterns from short-term fluctuations through a hierarchical two-stage structure. The first stage captures coarse-grained hourly demand patterns, while the second stage improves prediction accuracy by incorporating high-frequency, localized inputs, including recent fluctuations and real-time demand variations in connected metro services, to account for temporal shifts in short-term demand. Time series transformer models are employed in both stages to generate probabilistic predictions. Extensive experiments using Washington D.C.'s Capital Bikeshare data demonstrate that T-STAR outperforms existing methods in both deterministic and probabilistic accuracy. The model exhibits strong spatial and temporal robustness across stations and time periods. A zero-shot forecasting experiment further highlights T-STAR's ability to transfer to previously unseen service areas without retraining. These results underscore the framework's potential to deliver granular, reliable, and uncertainty-aware short-term demand forecasts, which enable seamless integration to support multimodal trip planning for travelers and enhance real-time operations in shared micro-mobility services.

### 🤖 AI 总结

**一句话总结**：T-STAR是一种基于变换器的框架，用于在15分钟分辨率下进行高精度的共享单车需求预测。

**研究动机**：可靠的短期需求预测对于管理共享微出行服务至关重要，以确保用户中心的响应性操作。

**核心方法**：T-STAR采用两阶段的空间和时间自适应上下文表示，分别捕捉粗粒度的小时需求模式和高频局部输入，使用时间序列变换器模型生成概率预测。

**主要结论**：T-STAR在不同站点和时间段中展现出强大的空间和时间鲁棒性，并能在未见服务区域进行零样本预测，显示出其在短期需求预测中的潜力。

**关键词**：短期需求预测, 共享微出行, 变换器模型, 概率预测, 时序分析, 机器学习, T-STAR, 高分辨率预测, 实时需求变化, ml

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06866v1) | [下载PDF](https://arxiv.org/pdf/2602.06866v1.pdf)

---

## [28. Zero-shot Generalizable Graph Anomaly Detection with Mixture of Riemannian Experts](https://arxiv.org/abs/2602.06859v1)

**作者**：Xinyu Zhao, Qingyun Sun, Jiayi Luo 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-06

### 📄 论文摘要

Graph Anomaly Detection (GAD) aims to identify irregular patterns in graph data, and recent works have explored zero-shot generalist GAD to enable generalization to unseen graph datasets. However, existing zero-shot GAD methods largely ignore intrinsic geometric differences across diverse anomaly patterns, substantially limiting their cross-domain generalization. In this work, we reveal that anomaly detectability is highly dependent on the underlying geometric properties and that embedding graphs from different domains into a single static curvature space can distort the structural signatures of anomalies. To address the challenge that a single curvature space cannot capture geometry-dependent graph anomaly patterns, we propose GAD-MoRE, a novel framework for zero-shot Generalizable Graph Anomaly Detection with a Mixture of Riemannian Experts architecture. Specifically, to ensure that each anomaly pattern is modeled in the Riemannian space where it is most detectable, GAD-MoRE employs a set of specialized Riemannian expert networks, each operating in a distinct curvature space. To align raw node features with curvature-specific anomaly characteristics, we introduce an anomaly-aware multi-curvature feature alignment module that projects inputs into parallel Riemannian spaces, enabling the capture of diverse geometric characteristics. Finally, to facilitate better generalization beyond seen patterns, we design a memory-based dynamic router that adaptively assigns each input to the most compatible expert based on historical reconstruction performance on similar anomalies. Extensive experiments in the zero-shot setting demonstrate that GAD-MoRE significantly outperforms state-of-the-art generalist GAD baselines, and even surpasses strong competitors that are few-shot fine-tuned with labeled data from the target domain.

### 🤖 AI 总结

**一句话总结**：提出了一种名为GAD-MoRE的框架，通过混合黎曼专家实现零-shot图异常检测，显著提升跨域泛化能力。

**研究动机**：现有零-shot图异常检测方法未能充分考虑不同异常模式的几何差异，限制了其跨域泛化能力。

**核心方法**：GAD-MoRE利用多个专门的黎曼专家网络在不同曲率空间中建模异常模式，并引入异常感知的多曲率特征对齐模块和基于记忆的动态路由器以优化输入分配。

**主要结论**：GAD-MoRE在零-shot设置下显著超越了现有的通用图异常检测基线，甚至超过了在目标领域用标签数据进行少量微调的竞争对手。

**关键词**：图神经网络, 异常检测, 零-shot学习, 里曼专家, 多曲率特征对齐, 结构签名, 跨域泛化, 动态路由, 机器学习, 深度学习, embedding

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06859v1) | [下载PDF](https://arxiv.org/pdf/2602.06859v1.pdf)

---

## [29. Designing a Robust, Bounded, and Smooth Loss Function for Improved Supervised Learning](https://arxiv.org/abs/2602.06858v1)

**作者**：Soumi Mahato, Lineesh M. C  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

The loss function is crucial to machine learning, especially in supervised learning frameworks. It is a fundamental component that controls the behavior and general efficacy of learning algorithms. However, despite their widespread use, traditional loss functions have significant drawbacks when dealing with high-dimensional and outlier-sensitive datasets, which frequently results in reduced performance and slower convergence during training. In this work, we develop a robust, bounded, and smooth (RoBoS-NN) loss function to resolve the aforementioned hindrances. The generalization ability of the loss function has also been theoretically analyzed to rigorously justify its robustness. Moreover, we implement RoboS-NN loss in the framework of a neural network (NN) to forecast time series and present a new robust algorithm named $\mathcal{L}_{\text{RoBoS}}$-NN. To assess the potential of $\mathcal{L}_{\text{RoBoS}}$-NN, we conduct experiments on multiple real-world datasets. In addition, we infuse outliers into data sets to evaluate the performance of $\mathcal{L}_{\text{RoBoS}}$-NN in more challenging scenarios. Numerical results show that $\mathcal{L}_{\text{RoBoS}}$-NN outperforms the other benchmark models in terms of accuracy measures.

### 🤖 AI 总结

**一句话总结**：本文提出了一种新的鲁棒、有界和平滑的损失函数RoBoS-NN，以改善监督学习中的性能和收敛速度。

**研究动机**：传统损失函数在处理高维和对异常值敏感的数据集时存在显著不足，影响了学习算法的表现和收敛速度。

**核心方法**：本研究开发了RoBoS-NN损失函数，并将其应用于神经网络框架中，以预测时间序列并评估其在包含异常值的数据集上的表现。

**主要结论**：实验结果表明，$	ext{L}_{	ext{RoBoS}}$-NN在准确性指标上优于其他基准模型，证明了其有效性。

**关键词**：机器学习, 深度学习, 神经网络, 鲁棒损失函数, 监督学习, 时间序列预测, RoBoS-NN, 算法性能, 数据集评估, machine learning

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06858v1) | [下载PDF](https://arxiv.org/pdf/2602.06858v1.pdf)

---

## [30. Improved Sampling Schedules for Discrete Diffusion Models](https://arxiv.org/abs/2602.06849v1)

**作者**：Alberto Foresti, Mustapha Bounoua, Giulio Franzese 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Discrete diffusion models have emerged as a powerful paradigm for generative modeling on sequence data; however, the information-theoretic principles governing their reverse processes remain significantly less understood than those of their continuous counterparts. In this work, we bridge this gap by analyzing the reverse process dynamics through the lens of thermodynamic entropy production. We propose the entropy production rate as a rigorous proxy for quantifying information generation, deriving as a byproduct a bound on the Wasserstein distance between intermediate states and the data distribution. Leveraging these insights, we introduce two novel sampling schedules that are uniformly spaced with respect to their corresponding physics-inspired metrics: the Entropic Discrete Schedule (EDS), which is defined by maintaining a constant rate of information gain, and the Wasserstein Discrete Schedule (WDS), which is defined by taking equal steps in terms of the Wasserstein distance. We empirically demonstrate that our proposed schedules significantly outperform state-of-the-art strategies across diverse application domains, including synthetic data, music notation, vision and language modeling, consistently achieving superior performance at a lower computational budget.

### 🤖 AI 总结

**一句话总结**：提出了基于热力学熵产生的新采样调度方法，显著提升离散扩散模型在生成建模中的性能。

**研究动机**：离散扩散模型在序列数据生成建模中表现出色，但其反向过程的信息理论原理尚不清晰，因此需要进一步研究。

**核心方法**：通过热力学熵产生分析反向过程，并提出两种新颖的采样调度：熵离散调度（EDS）和瓦瑟斯坦离散调度（WDS），以提高信息生成效率。

**主要结论**：实验结果表明，所提出的采样调度在多个应用领域上显著超越了现有最先进策略，且在计算预算上更具优势。

**关键词**：离散扩散模型, 生成建模, 信息论, 熵产生, 采样调度, Entropic Discrete Schedule, Wasserstein Discrete Schedule, 计算效率, 视觉与语言建模, ml

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06849v1) | [下载PDF](https://arxiv.org/pdf/2602.06849v1.pdf)

---

