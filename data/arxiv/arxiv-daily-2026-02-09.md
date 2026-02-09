# arXiv AI 论文日报 | 2026-02-09

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

**一句话总结**：研究表明AI代理在任务成功预测中表现出过度自信，且预执行评估的有效性高于后执行评估。

**研究动机**：旨在探讨AI代理在任务执行前后对成功概率的自我评估，以理解其不确定性和自信程度。

**核心方法**：通过在任务执行的不同阶段收集成功概率估计，分析代理的自信水平和信息使用情况。

**主要结论**：发现代理在成功率仅为22%的情况下仍预测77%的成功，且在特定条件下，预执行评估比后执行回顾更具区分力。

**关键词**：代理不确定性, 代理过度自信, 任务执行, 成功概率估计, 对抗性提示, 预执行评估, 机器学习, 深度学习, 神经网络, 生成模型, agent

**评分**：61

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06948v1) | [下载PDF](https://arxiv.org/pdf/2602.06948v1.pdf)

---

## [2. AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents](https://arxiv.org/abs/2602.06855v1)

**作者**：Alisia Lupidi, Bhavul Gauri, Thomas Simon Foster 等 37 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-06

### 📄 论文摘要

LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce AIRS-Bench (the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. These tasks span diverse domains, including language modeling, mathematics, bioinformatics, and time series forecasting. AIRS-Bench tasks assess agentic capabilities over the full research lifecycle -- including idea generation, experiment analysis and iterative refinement -- without providing baseline code. The AIRS-Bench task format is versatile, enabling easy integration of new tasks and rigorous comparison across different agentic frameworks. We establish baselines using frontier models paired with both sequential and parallel scaffolds. Our results show that agents exceed human SOTA in four tasks but fail to match it in sixteen others. Even when agents surpass human benchmarks, they do not reach the theoretical performance ceiling for the underlying tasks. These findings indicate that AIRS-Bench is far from saturated and offers substantial room for improvement. We open-source the AIRS-Bench task definitions and evaluation code to catalyze further development in autonomous scientific research.

### 🤖 AI 总结

**一句话总结**：AIRS-Bench是一个包含20个科学研究任务的基准，旨在评估大型语言模型代理在科学研究中的表现。

**研究动机**：随着大型语言模型（LLM）在科学研究中的潜力逐渐凸显，急需一个标准化的基准来推动这一领域的进展。

**核心方法**：AIRS-Bench定义了20个来自前沿机器学习论文的任务，涵盖多个领域，并不提供基准代码，支持新任务的集成和不同框架的比较。

**主要结论**：虽然代理在四个任务上超过了人类最优表现，但在其他十六个任务上仍未达到，表明AIRS-Bench还有很大的改进空间。

**关键词**：生成关键词如下：

LLM, 机器学习, 深度学习, 神经网络, 代理, 自主代理, 任务基准, 科学研究, 实验分析, 迭代优化

**评分**：72

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

**一句话总结**：Halluverse-M^3是一个多任务多语言基准数据集，用于系统分析大语言模型中的幻觉问题。

**研究动机**：当前大语言模型在多语言和生成任务中面临幻觉问题，尤其是在事实一致性方面，亟需更好的评估工具。

**核心方法**：Halluverse-M^3数据集涵盖英语、阿拉伯语、印地语和土耳其语，支持问答和对话摘要生成任务，并通过控制编辑过程构建幻觉输出。

**主要结论**：研究表明，问答任务的幻觉检测相对简单，而句子级幻觉检测对模型仍然具有挑战性，尤其在低资源语言中表现较差。

**关键词**：多任务, 多语言, 生成任务, 大语言模型, 幻觉检测, Halluverse-M^3, 问答, 对话摘要, 实体级幻觉, 关系级幻觉, 句子级幻觉, llm

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06920v1) | [下载PDF](https://arxiv.org/pdf/2602.06920v1.pdf)

---

## [4. Uncovering Cross-Objective Interference in Multi-Objective Alignment](https://arxiv.org/abs/2602.06869v1)

**作者**：Yining Lu, Meng Jiang  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

We study a persistent failure mode in multi-objective alignment for large language models (LLMs): training improves performance on only a subset of objectives while causing others to degrade. We formalize this phenomenon as cross-objective interference and conduct the first systematic study across classic scalarization algorithms, showing that interference is pervasive and exhibits strong model dependence.   To explain this phenomenon, we derive a local covariance law showing that an objective improves at first order when its reward exhibits positive covariance with the scalarized score. We extend this analysis to clipped surrogate objectives used in modern alignment, demonstrating that the covariance law remains valid under mild conditions despite clipping. Building on this analysis, we propose Covariance Targeted Weight Adaptation (CTWA), a plug-and-play method that maintains positive covariance between objective rewards and the training signal to effectively mitigate cross-objective interference. Finally, we complement these local improvement conditions with a global convergence analysis under the Polyak--Łojasiewicz condition, establishing when non-convex scalarized optimization achieves global convergence and how cross-objective interference depends on specific model geometric properties.

### 🤖 AI 总结

**一句话总结**：本研究揭示了大型语言模型在多目标对齐中存在的交叉目标干扰现象，并提出了一种新的方法来缓解这一问题。

**研究动机**：多目标对齐在大型语言模型训练中常导致部分目标性能提升而其他目标性能下降，因此需要深入研究这一现象的机制。

**核心方法**：提出了一种协方差针对权重适配方法（CTWA），通过维持目标奖励与训练信号之间的正协方差来缓解交叉目标干扰，并进行了局部和全局收敛分析。

**主要结论**：交叉目标干扰是普遍存在的，并且与特定模型的几何性质相关，通过CTWA方法可以有效改善多目标对齐的效果。

**关键词**：多目标对齐, 大语言模型, 交叉目标干扰, 奖励模型, 协方差目标权重适应, Covariance Targeted Weight Adaptation, 训练信号, 全局收敛分析, 非凸标量优化, llm

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06869v1) | [下载PDF](https://arxiv.org/pdf/2602.06869v1.pdf)

---

## [5. SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks](https://arxiv.org/abs/2602.06854v1)

**作者**：Mingqian Feng, Xiaodong Liu, Weiwei Yang 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-06

### 📄 论文摘要

Multi-turn jailbreaks capture the real threat model for safety-aligned chatbots, where single-turn attacks are merely a special case. Yet existing approaches break under exploration complexity and intent drift. We propose SEMA, a simple yet effective framework that trains a multi-turn attacker without relying on any existing strategies or external data. SEMA comprises two stages. Prefilling self-tuning enables usable rollouts by fine-tuning on non-refusal, well-structured, multi-turn adversarial prompts that are self-generated with a minimal prefix, thereby stabilizing subsequent learning. Reinforcement learning with intent-drift-aware reward trains the attacker to elicit valid multi-turn adversarial prompts while maintaining the same harmful objective. We anchor harmful intent in multi-turn jailbreaks via an intent-drift-aware reward that combines intent alignment, compliance risk, and level of detail. Our open-loop attack regime avoids dependence on victim feedback, unifies single- and multi-turn settings, and reduces exploration complexity. Across multiple datasets, victim models, and jailbreak judges, our method achieves state-of-the-art (SOTA) attack success rates (ASR), outperforming all single-turn baselines, manually scripted and template-driven multi-turn baselines, as well as our SFT (Supervised Fine-Tuning) and DPO (Direct Preference Optimization) variants. For instance, SEMA performs an average $80.1\%$ ASR@1 across three closed-source and open-source victim models on AdvBench, 33.9% over SOTA. The approach is compact, reproducible, and transfers across targets, providing a stronger and more realistic stress test for large language model (LLM) safety and enabling automatic redteaming to expose and localize failure modes. Our code is available at: https://github.com/fmmarkmq/SEMA.

### 🤖 AI 总结

**一句话总结**：SEMA是一个简单有效的多轮越狱攻击框架，通过自我调节和意图漂移感知奖励实现高成功率。

**研究动机**：现有单轮攻击方法在多轮越狱攻击中表现不佳，因此需要一个新的框架来应对复杂的探索和意图漂移问题。

**核心方法**：SEMA包括两个阶段：自我调节的预填充和意图漂移感知奖励的强化学习，旨在生成有效的多轮对抗性提示。

**主要结论**：SEMA在多个数据集和受害模型上实现了最先进的攻击成功率，提供了更强的安全性测试和自动化红队能力。

**关键词**：多轮攻击, SEMA, 强化学习, 对抗性提示, 模型安全, 自适应训练, intent-drift, 多智能体, llm

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

**一句话总结**：本文探讨了数字概念的表征几何结构，揭示了它们在不同任务中如何保持关系结构的稳定性。

**研究动机**：认知科学中的一个核心问题是概念表征是如何在支持泛化与最小化任务干扰之间平衡的。

**核心方法**：通过使用数字概念作为实验对象，并将语言模型作为高维计算基础，研究了数字表征在不同任务中的几何关系。

**主要结论**：研究结果表明，尽管任务特定的表征嵌入于不同的子空间，但它们之间可以通过线性映射相互转化，从而共享关系结构。

**关键词**：表示几何, 概念表示, 认知科学, 任务干扰, 语言模型, 关系结构, 嵌入, 任务特定, 线性映射, 数字概念, agent

**评分**：52

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

**一句话总结**：MedMO是一种医学基础模型，采用多阶段训练策略，显著提升了医学图像处理的准确性和推理能力。

**研究动机**：尽管多模态大语言模型在发展迅速，但在医学领域的应用受到领域覆盖、模态对齐和基础推理等问题的限制，因此需要一个专门的医学模型。

**核心方法**：MedMO的训练分为三个阶段：跨模态预训练、基于多任务监督的指令调优，以及结合事实检查和空间定位的强化学习，以提高模型的推理和定位能力。

**主要结论**：MedMO在多个医学任务中表现优异，尤其是在视觉问答和医学报告生成方面，显示出强大的空间推理和定位性能，并且在放射学、眼科学和病理显微镜等领域具有广泛的跨模态泛化能力。

**关键词**：多模态, 大语言模型, 医疗图像, 跨模态预训练, 强化学习, 医学基础模型, 语义理解, 空间推理, 医学报告生成, 任务监督, ml

**评分**：75

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06965v1) | [下载PDF](https://arxiv.org/pdf/2602.06965v1.pdf)

---

## [8. CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation](https://arxiv.org/abs/2602.06959v1)

**作者**：Kaiyi Huang, Yukun Huang, Yu Li 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-06

### 📄 论文摘要

Cinematic video production requires control over scene-subject composition and camera movement, but live-action shooting remains costly due to the need for constructing physical sets. To address this, we introduce the task of cinematic video generation with decoupled scene context: given multiple images of a static environment, the goal is to synthesize high-quality videos featuring dynamic subject while preserving the underlying scene consistency and following a user-specified camera trajectory. We present CineScene, a framework that leverages implicit 3D-aware scene representation for cinematic video generation. Our key innovation is a novel context conditioning mechanism that injects 3D-aware features in an implicit way: By encoding scene images into visual representations through VGGT, CineScene injects spatial priors into a pretrained text-to-video generation model by additional context concatenation, enabling camera-controlled video synthesis with consistent scenes and dynamic subjects. To further enhance the model's robustness, we introduce a simple yet effective random-shuffling strategy for the input scene images during training. To address the lack of training data, we construct a scene-decoupled dataset with Unreal Engine 5, containing paired videos of scenes with and without dynamic subjects, panoramic images representing the underlying static scene, along with their camera trajectories. Experiments show that CineScene achieves state-of-the-art performance in scene-consistent cinematic video generation, handling large camera movements and demonstrating generalization across diverse environments.

### 🤖 AI 总结

**一句话总结**：CineScene是一个利用隐式3D场景表示进行电影视频生成的框架，能够在保持场景一致性的同时合成动态主体的高质量视频。

**研究动机**：电影视频制作需要对场景和主体的组合以及相机运动进行控制，但传统的实景拍摄成本高昂，因此亟需一种新的视频生成方法。

**核心方法**：CineScene通过将场景图像编码为视觉表示并注入3D感知特征，结合随机打乱策略和场景解耦数据集，提升了视频合成的鲁棒性和一致性。

**主要结论**：实验表明，CineScene在场景一致的电影视频生成方面达到了最先进的性能，能够处理大幅度相机移动，并展示出在多样环境中的泛化能力。

**关键词**：关键词：深度学习, 生成, 3D, 视频生成, 语义搜索, 场景一致性, 相机轨迹, 显示动态主体, 数据集, rag

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06959v1) | [下载PDF](https://arxiv.org/pdf/2602.06959v1.pdf)

---

## [9. Reliable Mislabel Detection for Video Capsule Endoscopy Data](https://arxiv.org/abs/2602.06938v1)

**作者**：Julia Werner, Julius Oexle, Oliver Bause 等 8 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

The classification performance of deep neural networks relies strongly on access to large, accurately annotated datasets. In medical imaging, however, obtaining such datasets is particularly challenging since annotations must be provided by specialized physicians, which severely limits the pool of annotators. Furthermore, class boundaries can often be ambiguous or difficult to define which further complicates machine learning-based classification. In this paper, we want to address this problem and introduce a framework for mislabel detection in medical datasets. This is validated on the two largest, publicly available datasets for Video Capsule Endoscopy, an important imaging procedure for examining the gastrointestinal tract based on a video stream of lowresolution images. In addition, potentially mislabeled samples identified by our pipeline were reviewed and re-annotated by three experienced gastroenterologists. Our results show that the proposed framework successfully detects incorrectly labeled data and results in an improved anomaly detection performance after cleaning the datasets compared to current baselines.

### 🤖 AI 总结

**一句话总结**：本研究提出了一种框架，用于检测视频胶囊内窥镜数据中的错误标签，提高医疗数据集的准确性。

**研究动机**：医疗影像领域对准确标注数据集的依赖性强，但专业医生的标注资源有限且界限模糊，导致分类性能受损。

**核心方法**：本文提出了一种错误标签检测框架，针对视频胶囊内窥镜的两个大型公开数据集进行验证，并由经验丰富的胃肠病医生重新标注潜在错误样本。

**主要结论**：实验结果表明，所提出的框架有效检测了错误标记的数据，并在清理数据集后，异常检测性能显著提升，优于当前基线方法。

**关键词**：深度学习, 神经网络, 医学影像, 视频胶囊内窥镜, 异常检测, 标注检测, 数据清洗, 机器学习, 分类性能, machine learning

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06938v1) | [下载PDF](https://arxiv.org/pdf/2602.06938v1.pdf)

---

## [10. RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing](https://arxiv.org/abs/2602.06871v1)

**作者**：Mohammadreza Salehi, Mehdi Noroozi, Luca Morreale 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-06

### 📄 论文摘要

Instructional video editing applies edits to an input video using only text prompts, enabling intuitive natural-language control. Despite rapid progress, most methods still require fixed-length inputs and substantial compute. Meanwhile, autoregressive video generation enables efficient variable-length synthesis, yet remains under-explored for video editing. We introduce a causal, efficient video editing model that edits variable-length videos frame by frame. For efficiency, we start from a 2D image-to-image (I2I) diffusion model and adapt it to video-to-video (V2V) editing by conditioning the edit at time step t on the model's prediction at t-1. To leverage videos' temporal redundancy, we propose a new I2I diffusion forward process formulation that encourages the model to predict the residual between the target output and the previous prediction. We call this Residual Flow Diffusion Model (RFDM), which focuses the denoising process on changes between consecutive frames. Moreover, we propose a new benchmark that better ranks state-of-the-art methods for editing tasks. Trained on paired video data for global/local style transfer and object removal, RFDM surpasses I2I-based methods and competes with fully spatiotemporal (3D) V2V models, while matching the compute of image models and scaling independently of input video length. More content can be found in: https://smsd75.github.io/RFDM_page/

### 🤖 AI 总结

**一句话总结**：RFDM是一种高效的因果视频编辑模型，通过预测连续帧之间的残差实现可变长度视频的编辑。

**研究动机**：现有的视频编辑方法通常需要固定长度输入且计算量大，因而需要寻找更高效的编辑方式。

**核心方法**：RFDM模型基于2D图像扩散模型，采用残差流扩散方法，通过对连续帧之间的变化进行去噪，提升视频编辑效率。

**主要结论**：RFDM在全局/局部风格转移和物体移除任务上超越传统方法，并在计算效率上与图像模型相匹配，同时具备独立于输入视频长度的可扩展性。

**关键词**：残差流扩散模型, 视频编辑, 自然语言控制, 变量长度合成, 计算效率, 生成模型, 预测残差, 任务基准, 逐帧编辑, diffusion

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06871v1) | [下载PDF](https://arxiv.org/pdf/2602.06871v1.pdf)

---

## [11. Parameters as Experts: Adapting Vision Models with Dynamic Parameter Routing](https://arxiv.org/abs/2602.06862v1)

**作者**：Meng Lou, Stanley Yu, Yizhou Yu  
**分类**：cs.CV  
**发布时间**：2026-02-06

### 📄 论文摘要

Adapting pre-trained vision models using parameter-efficient fine-tuning (PEFT) remains challenging, as it aims to achieve performance comparable to full fine-tuning using a minimal number of trainable parameters. When applied to complex dense prediction tasks, existing methods exhibit limitations, including input-agnostic modeling and redundant cross-layer representations. To this end, we propose AdaRoute, a new adapter-style method featuring a simple mixture-of-experts (MoE) architecture. Specifically, we introduce shared expert centers, where each expert is a trainable parameter matrix. During a feedforward pass, each AdaRoute module in the network dynamically generates weight matrices tailored for the current module via a simple dynamic parameter routing mechanism, which selectively aggregates parameter matrices in the corresponding expert center. Dynamic weight matrices in AdaRoute modules facilitate low-rank adaptation in an input-dependent manner, thus generating more customized and powerful feature representations. Moreover, since AdaRoute modules across multiple network layers share the same expert center, they improve feature diversity by promoting implicit cross-layer feature interaction. Extensive experiments demonstrate the superiority of AdaRoute on diverse vision tasks, including semantic segmentation, object detection and instance segmentation, and panoptic segmentation. Code will be available at: https://bit.ly/3NZcr0H.

### 🤖 AI 总结

**一句话总结**：提出了一种新的适应性视觉模型方法AdaRoute，通过动态参数路由实现高效的特征表示。

**研究动机**：在复杂的密集预测任务中，现有的参数高效微调方法存在输入无关建模和冗余跨层表示的局限性。

**核心方法**：AdaRoute采用混合专家架构，通过动态生成权重矩阵和共享专家中心，实现输入依赖的低秩适应。

**主要结论**：实验结果表明，AdaRoute在语义分割、目标检测和实例分割等多种视觉任务中表现优越。

**关键词**：视觉模型, 参数高效微调, 动态参数路由, 混合专家, 特征表示, 语义分割, 目标检测, 实例分割, AdaRoute, agent

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06862v1) | [下载PDF](https://arxiv.org/pdf/2602.06862v1.pdf)

---

## [12. Rethinking Multi-Condition DiTs: Eliminating Redundant Attention via Position-Alignment and Keyword-Scoping](https://arxiv.org/abs/2602.06850v1)

**作者**：Chao Zhou, Tianyi Wei, Yiling Chen 等 5 位作者  
**分类**：cs.CV, cs.AI, cs.MM  
**发布时间**：2026-02-06

### 📄 论文摘要

While modern text-to-image models excel at prompt-based generation, they often lack the fine-grained control necessary for specific user requirements like spatial layouts or subject appearances. Multi-condition control addresses this, yet its integration into Diffusion Transformers (DiTs) is bottlenecked by the conventional ``concatenate-and-attend'' strategy, which suffers from quadratic computational and memory overhead as the number of conditions scales. Our analysis reveals that much of this cross-modal interaction is spatially or semantically redundant. To this end, we propose Position-aligned and Keyword-scoped Attention (PKA), a highly efficient framework designed to eliminate these redundancies. Specifically, Position-Aligned Attention (PAA) linearizes spatial control by enforcing localized patch alignment, while Keyword-Scoped Attention (KSA) prunes irrelevant subject-driven interactions via semantic-aware masking. To facilitate efficient learning, we further introduce a Conditional Sensitivity-Aware Sampling (CSAS) strategy that reweights the training objective towards critical denoising phases, drastically accelerating convergence and enhancing conditional fidelity. Empirically, PKA delivers a 10.0$\times$ inference speedup and a 5.1$\times$ VRAM saving, providing a scalable and resource-friendly solution for high-fidelity multi-conditioned generation.

### 🤖 AI 总结

**一句话总结**：本文提出了一种新颖的多条件Diffusion Transformers模型，通过消除冗余注意力机制实现高效的文本到图像生成。

**研究动机**：当前的文本到图像模型虽然在提示生成方面表现良好，但在特定用户需求如空间布局和主题外观的控制上存在不足，尤其是在多条件控制的整合上面临计算和内存瓶颈。

**核心方法**：提出了位置对齐和关键词范围注意力（PKA）框架，通过位置对齐注意力（PAA）和关键词范围注意力（KSA）消除跨模态交互中的冗余，并引入条件敏感采样（CSAS）加速学习过程。

**主要结论**：PKA显著提高了推理速度（10.0倍加速）和显存节省（5.1倍），为高保真多条件生成提供了可扩展和资源友好的解决方案。

**关键词**：多条件控制, 文本生成, 扩散变换器, 位置对齐, 关键词范围注意力, 语义感知, 高效学习, 条件敏感采样, 计算效率, diffusion

**评分**：70

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

**一句话总结**：本文探讨了通过训练扩散模型来学习神经网络内部状态分布的生成元模型，从而提高干预的流畅性和可解释性。

**研究动机**：现有的神经网络激活分析方法依赖于严格的结构假设，而生成模型可以在没有这些假设的情况下揭示结构并提高干预的效果。

**核心方法**：研究通过对十亿个残差流激活进行训练，构建生成元模型，利用扩散模型捕捉网络内部状态的分布。

**主要结论**：结果表明，生成元模型提供了一种可扩展的可解释性途径，且在降低损失时，干预的流畅性和概念的孤立性均有提升。

**关键词**：生成模型, 深度学习, 神经网络, 激活分析, 介入干预, 扩散模型, 可解释性, 结构假设, 元模型, 训练方法, neural network

**评分**：65

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06964v1) | [下载PDF](https://arxiv.org/pdf/2602.06964v1.pdf)

---

## [14. Improving Credit Card Fraud Detection with an Optimized Explainable Boosting Machine](https://arxiv.org/abs/2602.06955v1)

**作者**：Reza E. Fazel, Arash Bakhtiary, Siavash A. Bigdeli  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Addressing class imbalance is a central challenge in credit card fraud detection, as it directly impacts predictive reliability in real-world financial systems. To overcome this, the study proposes an enhanced workflow based on the Explainable Boosting Machine (EBM)-a transparent, state-of-the-art implementation of the GA2M algorithm-optimized through systematic hyperparameter tuning, feature selection, and preprocessing refinement. Rather than relying on conventional sampling techniques that may introduce bias or cause information loss, the optimized EBM achieves an effective balance between accuracy and interpretability, enabling precise detection of fraudulent transactions while providing actionable insights into feature importance and interaction effects. Furthermore, the Taguchi method is employed to optimize both the sequence of data scalers and model hyperparameters, ensuring robust, reproducible, and systematically validated performance improvements. Experimental evaluation on benchmark credit card data yields an ROC-AUC of 0.983, surpassing prior EBM baselines (0.975) and outperforming Logistic Regression, Random Forest, XGBoost, and Decision Tree models. These results highlight the potential of interpretable machine learning and data-driven optimization for advancing trustworthy fraud analytics in financial systems.

### 🤖 AI 总结

**一句话总结**：通过优化的可解释提升机，研究有效解决信用卡欺诈检测中的类别不平衡问题，显著提升了检测准确性和可解释性。

**研究动机**：信用卡欺诈检测面临类别不平衡的挑战，这直接影响金融系统的预测可靠性。

**核心方法**：本研究提出基于可解释提升机的增强工作流程，通过超参数调优、特征选择和预处理优化，提升模型性能。

**主要结论**：实验结果显示，优化后的模型在ROC-AUC上达到0.983，超越了传统模型，展示了可解释机器学习在金融欺诈分析中的潜力。

**关键词**：信用卡欺诈检测, 机器学习, 可解释性, 优化, 数据预处理, EBM, 特征选择, ROC-AUC, 金融系统, 预测模型, machine learning

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

**一句话总结**：大型语言模型在推理过程中能够抵抗任务不一致的激活引导，表现出内生抵抗能力（ESR）。

**研究动机**：研究旨在探讨大型语言模型在面临激活引导时的自我恢复能力及其对生成响应的影响。

**核心方法**：通过使用稀疏自编码器（SAE）潜变量来引导模型激活，分析不同模型在ESR现象中的表现，并通过实验验证其因果关系。

**主要结论**：ESR不仅可能保护模型免受对抗性操控，还可能干扰依赖激活引导的安全干预措施，因此理解和控制这种机制对于开发透明可控的AI系统至关重要。

**关键词**：内生抵抗, 激活引导, 语言模型, 深度学习, 自我监控, 自我纠正, Llama-3.3-70B, 稀疏自编码器, 透明可控系统, agent

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06941v1) | [下载PDF](https://arxiv.org/pdf/2602.06941v1.pdf)

---

## [16. From Core to Detail: Unsupervised Disentanglement with Entropy-Ordered Flows](https://arxiv.org/abs/2602.06940v1)

**作者**：Daniel Galperin, Ullrich Köthe  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Learning unsupervised representations that are both semantically meaningful and stable across runs remains a central challenge in modern representation learning. We introduce entropy-ordered flows (EOFlows), a normalizing-flow framework that orders latent dimensions by their explained entropy, analogously to PCA's explained variance. This ordering enables adaptive injective flows: after training, one may retain only the top C latent variables to form a compact core representation while the remaining variables capture fine-grained detail and noise, with C chosen flexibly at inference time rather than fixed during training. EOFlows build on insights from Independent Mechanism Analysis, Principal Component Flows and Manifold Entropic Metrics. We combine likelihood-based training with local Jacobian regularization and noise augmentation into a method that scales well to high-dimensional data such as images. Experiments on the CelebA dataset show that our method uncovers a rich set of semantically interpretable features, allowing for high compression and strong denoising.

### 🤖 AI 总结

**一句话总结**：该论文提出了一种新的无监督表示学习框架——熵有序流（EOFlows），通过对潜在维度进行熵排序以实现高效的表示压缩和去噪。

**研究动机**：在现代表示学习中，如何学习既具有语义意义又在多次运行中稳定的无监督表示仍然是一个主要挑战。

**核心方法**：EOFlows框架通过熵排序潜在维度，结合基于似然的训练、局部雅可比正则化和噪声增强，适应性地保留最重要的潜在变量。

**主要结论**：实验结果表明，EOFlows能有效提取出丰富的语义特征，实现高压缩率和强去噪能力。

**关键词**：无监督表示, 表示学习, 潜在变量, 自适应注入流, 高维数据, EOFlows, 噪声增强, Jacobian正则化, 语义可解释特征, agent

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06940v1) | [下载PDF](https://arxiv.org/pdf/2602.06940v1.pdf)

---

## [17. Cochain Perspectives on Temporal-Difference Signals for Learning Beyond Markov Dynamics](https://arxiv.org/abs/2602.06939v1)

**作者**：Zuyuan Zhang, Sizhe Tang, Tian Lan  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-06

### 📄 论文摘要

Non-Markovian dynamics are commonly found in real-world environments due to long-range dependencies, partial observability, and memory effects. The Bellman equation that is the central pillar of Reinforcement learning (RL) becomes only approximately valid under Non-Markovian. Existing work often focus on practical algorithm designs and offer limited theoretical treatment to address key questions, such as what dynamics are indeed capturable by the Bellman framework and how to inspire new algorithm classes with optimal approximations. In this paper, we present a novel topological viewpoint on temporal-difference (TD) based RL. We show that TD errors can be viewed as 1-cochain in the topological space of state transitions, while Markov dynamics are then interpreted as topological integrability. This novel view enables us to obtain a Hodge-type decomposition of TD errors into an integrable component and a topological residual, through a Bellman-de Rham projection. We further propose HodgeFlow Policy Search (HFPS) by fitting a potential network to minimize the non-integrable projection residual in RL, achieving stability/sensitivity guarantees. In numerical evaluations, HFPS is shown to significantly improve RL performance under non-Markovian.

### 🤖 AI 总结

**一句话总结**：本研究提出了一种新的拓扑视角，通过将时间差误差视为状态转移的1-共链，改进了非马尔可夫动态下的强化学习算法。

**研究动机**：非马尔可夫动态在现实环境中普遍存在，现有强化学习算法在理论上对其处理有限，亟需新的方法来捕捉这些动态。

**核心方法**：提出了HodgeFlow策略搜索（HFPS），通过拟合潜在网络来最小化非可积投影残差，从而优化强化学习过程。

**主要结论**：HFPS在数值评估中显示出在非马尔可夫情境下显著提升了强化学习性能。

**关键词**：强化学习, 非马尔可夫, 时序差分, HodgeFlow, 深度学习, 神经网络, 代理, 多智能体, 在线学习, 奖励模型, llm

**评分**：65

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06939v1) | [下载PDF](https://arxiv.org/pdf/2602.06939v1.pdf)

---

## [18. Robustness Beyond Known Groups with Low-rank Adaptation](https://arxiv.org/abs/2602.06924v1)

**作者**：Abinitha Gourabathina, Hyewon Jeong, Teya Bergamaschi 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Deep learning models trained to optimize average accuracy often exhibit systematic failures on particular subpopulations. In real world settings, the subpopulations most affected by such disparities are frequently unlabeled or unknown, thereby motivating the development of methods that are performant on sensitive subgroups without being pre-specified. However, existing group-robust methods typically assume prior knowledge of relevant subgroups, using group annotations for training or model selection. We propose Low-rank Error Informed Adaptation (LEIA), a simple two-stage method that improves group robustness by identifying a low-dimensional subspace in the representation space where model errors concentrate. LEIA restricts adaptation to this error-informed subspace via a low-rank adjustment to the classifier logits, directly targeting latent failure modes without modifying the backbone or requiring group labels. Using five real-world datasets, we analyze group robustness under three settings: (1) truly no knowledge of subgroup relevance, (2) partial knowledge of subgroup relevance, and (3) full knowledge of subgroup relevance. Across all settings, LEIA consistently improves worst-group performance while remaining fast, parameter-efficient, and robust to hyperparameter choice.

### 🤖 AI 总结

**一句话总结**：提出了一种低秩误差信息适应方法（LEIA），旨在提高深度学习模型在未知子群体上的鲁棒性。

**研究动机**：现有的群体鲁棒性方法依赖于已知的子群体标签，而现实中许多受影响的子群体往往是未知的，因此需要开发新的方法。

**核心方法**：LEIA通过识别表示空间中的低维子空间，利用低秩调整分类器的逻辑值，直接针对潜在的失败模式进行适应，而不需要修改主干网络或依赖群组标签。

**主要结论**：在多种设置下，LEIA在改善最差群体性能的同时，保持了快速、参数高效和对超参数选择的鲁棒性。

**关键词**：低秩适应, 深度学习, 模型鲁棒性, 群体敏感性, 低秩错误信息适应, group robustness, subpopulation, representation space, deep learning

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06924v1) | [下载PDF](https://arxiv.org/pdf/2602.06924v1.pdf)

---

## [19. From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers](https://arxiv.org/abs/2602.06923v1)

**作者**：Ziming Liu, Sophia Sanborn, Surya Ganguli 等 4 位作者  
**分类**：cs.LG, cs.AI, physics.class-ph  
**发布时间**：2026-02-06

### 📄 论文摘要

Can general-purpose AI architectures go beyond prediction to discover the physical laws governing the universe? True intelligence relies on "world models" -- causal abstractions that allow an agent to not only predict future states but understand the underlying governing dynamics. While previous "AI Physicist" approaches have successfully recovered such laws, they typically rely on strong, domain-specific priors that effectively "bake in" the physics. Conversely, Vafa et al. recently showed that generic Transformers fail to acquire these world models, achieving high predictive accuracy without capturing the underlying physical laws. We bridge this gap by systematically introducing three minimal inductive biases. We show that ensuring spatial smoothness (by formulating prediction as continuous regression) and stability (by training with noisy contexts to mitigate error accumulation) enables generic Transformers to surpass prior failures and learn a coherent Keplerian world model, successfully fitting ellipses to planetary trajectories. However, true physical insight requires a third bias: temporal locality. By restricting the attention window to the immediate past -- imposing the simple assumption that future states depend only on the local state rather than a complex history -- we force the model to abandon curve-fitting and discover Newtonian force representations. Our results demonstrate that simple architectural choices determine whether an AI becomes a curve-fitter or a physicist, marking a critical step toward automated scientific discovery.

### 🤖 AI 总结

**一句话总结**：通过引入三种最小的归纳偏置，研究表明通用Transformer可以学习物理世界模型，从而超越简单的预测。

**研究动机**：研究旨在探讨通用AI架构是否能够超越预测，发现宇宙的物理法则，尤其关注如何构建有效的世界模型。

**核心方法**：通过确保空间平滑性、稳定性和时间局部性，引导Transformer学习有效的物理模型，特别是基于开普勒和牛顿的力学表现。

**主要结论**：简单的架构选择可以决定AI是否成为曲线拟合器或物理学家，标志着向自动科学发现的重要一步。

**关键词**：深度学习, 变换器, 世界模型, 物理法则, 代理, 预测, 空间平滑性, 时间局部性, 自动化科学发现, agent

**评分**：64

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06923v1) | [下载PDF](https://arxiv.org/pdf/2602.06923v1.pdf)

---

## [20. Revisiting the Generic Transformer: Deconstructing a Strong Baseline for Time Series Foundation Models](https://arxiv.org/abs/2602.06909v1)

**作者**：Yunshi Wen, Wesley M. Gifford, Chandra Reddy 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

The recent surge in Time Series Foundation Models has rapidly advanced the field, yet the heterogeneous training setups across studies make it difficult to attribute improvements to architectural innovations versus data engineering. In this work, we investigate the potential of a standard patch Transformer, demonstrating that this generic architecture achieves state-of-the-art zero-shot forecasting performance using a straightforward training protocol. We conduct a comprehensive ablation study that covers model scaling, data composition, and training techniques to isolate the essential ingredients for high performance. Our findings identify the key drivers of performance, while confirming that the generic architecture itself demonstrates excellent scalability. By strictly controlling these variables, we provide comprehensive empirical results on model scaling across multiple dimensions. We release our open-source model and detailed findings to establish a transparent, reproducible baseline for future research.

### 🤖 AI 总结

**一句话总结**：本文探讨了一种标准的补丁Transformer在时间序列预测中的表现，展示了其在零样本预测中的优秀性能。

**研究动机**：随着时间序列基础模型的发展，研究间的训练设置差异使得难以明确归因于架构创新或数据工程的改进。

**核心方法**：通过综合的消融研究，分析模型扩展、数据组成和训练技术，以识别高性能的关键要素。

**主要结论**：研究表明通用架构具有优异的可扩展性，并提供了透明、可重复的基准，以促进未来研究。

**关键词**：时间序列, Transformer, 预测, 深度学习, 模型扩展, 数据组成, 训练技术, 开源模型, 性能驱动因素, 零-shot 预测

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06909v1) | [下载PDF](https://arxiv.org/pdf/2602.06909v1.pdf)

---

## [21. A first realization of reinforcement learning-based closed-loop EEG-TMS](https://arxiv.org/abs/2602.06907v1)

**作者**：Dania Humaidan, Jiahua Xu, Jing Chen 等 11 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Background: Transcranial magnetic stimulation (TMS) is a powerful tool to investigate neurophysiology of the human brain and treat brain disorders. Traditionally, therapeutic TMS has been applied in a one-size-fits-all approach, disregarding inter- and intra-individual differences. Brain state-dependent EEG-TMS, such as coupling TMS with a pre-specified phase of the sensorimotor mu-rhythm, enables the induction of differential neuroplastic effects depending on the targeted phase. But this approach is still user-dependent as it requires defining an a-priori target phase. Objectives: To present a first realization of a machine-learning-based, closed-loop real-time EEG-TMS setup to identify user-independently the individual mu-rhythm phase associated with high- vs. low-corticospinal excitability states. Methods: We applied EEG-TMS to 25 participants targeting the supplementary motor area-primary motor cortex network and used a reinforcement learning algorithm to identify the mu-rhythm phase associated with high- vs. low corticospinal excitability. We employed linear mixed effects models and Bayesian analysis to determine effects of reinforced learning on corticospinal excitability indexed by motor evoked potential amplitude, and functional connectivity indexed by the imaginary part of resting-state EEG coherence. Results: Reinforcement learning effectively identified the mu-rhythm phase associated with high- vs. low-excitability states, and their repetitive stimulation resulted in long-term increases vs. decreases in functional connectivity in the stimulated sensorimotor network. Conclusions: We demonstrated for the first time the feasibility of closed-loop EEG-TMS in humans, a critical step towards individualized treatment of brain disorders.

### 🤖 AI 总结

**一句话总结**：本研究首次实现了基于强化学习的闭环EEG-TMS系统，能够用户独立地识别与高低皮层脊髓兴奋性状态相关的个体mu节律相位。

**研究动机**：传统的TMS治疗方法未能考虑个体差异，而脑状态依赖的EEG-TMS方法仍需用户定义目标相位，因此需要一种更为个性化的解决方案。

**核心方法**：研究中对25名参与者应用EEG-TMS，利用强化学习算法识别与高低脊髓兴奋性相关的mu节律相位，并采用线性混合效应模型和贝叶斯分析评估其对兴奋性的影响。

**主要结论**：研究首次展示了人类中闭环EEG-TMS的可行性，为个性化脑部疾病治疗迈出了重要一步。

**关键词**：机器学习, 深度学习, 神经网络, 强化学习, 反馈机制, EEG-TMS, 功能连接性, 脑电图, 个性化治疗, agent

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06907v1) | [下载PDF](https://arxiv.org/pdf/2602.06907v1.pdf)

---

## [22. Parameter-free Dynamic Regret: Time-varying Movement Costs, Delayed Feedback, and Memory](https://arxiv.org/abs/2602.06902v1)

**作者**：Emmanuel Esposito, Andrew Jacobsen, Hao Qiu 等 4 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-02-06

### 📄 论文摘要

In this paper, we study dynamic regret in unconstrained online convex optimization (OCO) with movement costs. Specifically, we generalize the standard setting by allowing the movement cost coefficients $λ_t$ to vary arbitrarily over time. Our main contribution is a novel algorithm that establishes the first comparator-adaptive dynamic regret bound for this setting, guaranteeing $\widetilde{\mathcal{O}}(\sqrt{(1+P_T)(T+\sum_t λ_t)})$ regret, where $P_T$ is the path length of the comparator sequence over $T$ rounds. This recovers the optimal guarantees for both static and dynamic regret in standard OCO as a special case where $λ_t=0$ for all rounds. To demonstrate the versatility of our results, we consider two applications: OCO with delayed feedback and OCO with time-varying memory. We show that both problems can be translated into time-varying movement costs, establishing a novel reduction specifically for the delayed feedback setting that is of independent interest. A crucial observation is that the first-order dependence on movement costs in our regret bound plays a key role in enabling optimal comparator-adaptive dynamic regret guarantees in both settings.

### 🤖 AI 总结

**一句话总结**：本论文提出了一种新算法，可在动态在线凸优化中实现适应比较器的动态遗憾界限，并适用于变动成本和延迟反馈问题。

**研究动机**：研究动态遗憾在不受约束的在线凸优化中的表现，尤其是在移动成本随时间变化的情况下。

**核心方法**：提出了一种新算法，建立了动态遗憾界限，确保遗憾值与路径长度和时间变化的移动成本成正比。

**主要结论**：算法在静态和动态遗憾的最优保证下表现良好，并能应用于延迟反馈和时间变化的记忆问题。

**关键词**：动态悔恨, 在线凸优化, 算法, 反馈延迟, 时间变化, 记忆, 运动成本, 自适应, 约束, 最优保证, agent

**评分**：50

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06902v1) | [下载PDF](https://arxiv.org/pdf/2602.06902v1.pdf)

---

## [23. Supercharging Simulation-Based Inference for Bayesian Optimal Experimental Design](https://arxiv.org/abs/2602.06900v1)

**作者**：Samuel Klein, Willie Neiswanger, Daniel Ratner 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.IT, cs.NE, stat.ML  
**发布时间**：2026-02-06

### 📄 论文摘要

Bayesian optimal experimental design (BOED) seeks to maximize the expected information gain (EIG) of experiments. This requires a likelihood estimate, which in many settings is intractable. Simulation-based inference (SBI) provides powerful tools for this regime. However, existing work explicitly connecting SBI and BOED is restricted to a single contrastive EIG bound. We show that the EIG admits multiple formulations which can directly leverage modern SBI density estimators, encompassing neural posterior, likelihood, and ratio estimation. Building on this perspective, we define a novel EIG estimator using neural likelihood estimation. Further, we identify optimization as a key bottleneck of gradient based EIG maximization and show that a simple multi-start parallel gradient ascent procedure can substantially improve reliability and performance. With these innovations, our SBI-based BOED methods are able to match or outperform by up to $22\%$ existing state-of-the-art approaches across standard BOED benchmarks.

### 🤖 AI 总结

**一句话总结**：该论文提出了一种基于模拟推断的贝叶斯最佳实验设计新方法，显著提升了信息增益的估计和优化性能。

**研究动机**：贝叶斯最佳实验设计旨在最大化实验的信息增益，但在许多情况下，似然估计难以实现，因此需要有效的模拟推断工具。

**核心方法**：论文通过定义新的信息增益估计器，利用神经似然估计，并提出了一种多起始并行梯度上升程序来优化信息增益最大化。

**主要结论**：通过这些创新，提出的方法在标准实验设计基准上能够与现有的最先进方法相匹配或提高多达22%的性能。

**关键词**：贝叶斯最优实验设计, 模拟推断, 信息增益, 神经网络, 梯度上升, 多启动并行优化, 实验设计, 机器学习, 深度学习, 期望信息增益, rag

**评分**：64

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06900v1) | [下载PDF](https://arxiv.org/pdf/2602.06900v1.pdf)

---

## [24. Sample Complexity of Causal Identification with Temporal Heterogeneity](https://arxiv.org/abs/2602.06899v1)

**作者**：Ameya Rathod, Sujay Belsare, Salvik Krishna Nautiyal 等 5 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-02-06

### 📄 论文摘要

Recovering a unique causal graph from observational data is an ill-posed problem because multiple generating mechanisms can lead to the same observational distribution. This problem becomes solvable only by exploiting specific structural or distributional assumptions. While recent work has separately utilized time-series dynamics or multi-environment heterogeneity to constrain this problem, we integrate both as complementary sources of heterogeneity. This integration yields unified necessary identifiability conditions and enables a rigorous analysis of the statistical limits of recovery under thin versus heavy-tailed noise. In particular, temporal structure is shown to effectively substitute for missing environmental diversity, possibly achieving identifiability even under insufficient heterogeneity. Extending this analysis to heavy-tailed (Student's t) distributions, we demonstrate that while geometric identifiability conditions remain invariant, the sample complexity diverges significantly from the Gaussian baseline. Explicit information-theoretic bounds quantify this cost of robustness, establishing the fundamental limits of covariance-based causal graph recovery methods in realistic non-stationary systems. This work shifts the focus from whether causal structure is identifiable to whether it is statistically recoverable in practice.

### 🤖 AI 总结

**一句话总结**：该论文探讨了如何通过时间序列动态和多环境异质性来识别因果图的样本复杂性。

**研究动机**：由于多个生成机制可能导致相同的观察分布，唯一因果图的恢复成为一个不适定的问题，因此需要特定的结构或分布假设来解决。

**核心方法**：论文将时间序列动态与多环境异质性结合，提出统一的必要可识别性条件，并分析在薄尾与重尾噪声下的统计极限。

**主要结论**：研究表明，时间结构可以有效替代缺失的环境多样性，并且在重尾分布下样本复杂性显著不同于高斯分布，建立了基于协方差的因果图恢复方法的基本极限。

**关键词**：因果识别, 统计极限, 样本复杂度, 时间序列, 结构假设, 非平稳系统, causal graph, identifiability conditions, agent

**评分**：58

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06899v1) | [下载PDF](https://arxiv.org/pdf/2602.06899v1.pdf)

---

## [25. A Cycle-Consistent Graph Surrogate for Full-Cycle Left Ventricular Myocardial Biomechanics](https://arxiv.org/abs/2602.06884v1)

**作者**：Siyu Mu, Wei Xuan Chan, Choon Hwai Yap  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Image-based patient-specific simulation of left ventricular (LV) mechanics is valuable for understanding cardiac function and supporting clinical intervention planning, but conventional finite-element analysis (FEA) is computationally intensive. Current graph-based surrogates do not have full-cycle prediction capabilities, and physics-informed neural networks often struggle to converge on complex cardiac geometries. We present CardioGraphFENet (CGFENet), a unified graph-based surrogate for rapid full-cycle estimation of LV myocardial biomechanics, supervised by a large FEA simulation dataset. The proposed model integrates (i) a global--local graph encoder to capture mesh features with weak-form-inspired global coupling, (ii) a gated recurrent unit-based temporal encoder conditioned on the target volume-time signal to model cycle-coherent dynamics, and (iii) a cycle-consistent bidirectional formulation for both loading and inverse unloading within a single framework. These strategies enable high fidelity with respect to traditional FEA ground truths and produce physiologically plausible pressure-volume loops that match FEA results when coupled with a lumped-parameter model. In particular, the cycle-consistency strategy enables a significant reduction in FEA supervision with only minimal loss in accuracy.

### 🤖 AI 总结

**一句话总结**：本研究提出了一种名为CardioGraphFENet的图形代理模型，以快速估计左心室肌肉力学，克服传统有限元分析的计算复杂性。

**研究动机**：图像基础的患者特定左心室力学模拟对理解心脏功能和支持临床干预规划至关重要，但传统的有限元分析计算量大且耗时。

**核心方法**：CGFENet结合了全球-局部图编码器、基于门控递归单元的时间编码器和循环一致的双向公式，能够在单一框架内高效捕捉心脏循环动力学。

**主要结论**：该模型在准确性上仅有轻微损失的情况下，显著减少了对有限元分析的监督，并生成与传统有限元结果相匹配的生理合理的压力-体积循环。

**关键词**：图神经网络, 机器学习, 深度学习, 生物力学, 循环一致性, 模型预测, CardioGraphFENet, 全周期估计, 物理信息神经网络, neural network

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

**一句话总结**：本研究表明，视觉变换器的高可塑性在微调过程中优于平滑性，有助于提高性能。

**研究动机**：虽然变换器架构的平滑性在多个领域得到研究，但其在迁移学习中的作用仍不明确，因此需要探讨可塑性对适应性的影响。

**核心方法**：通过理论分析和实验，评估视觉变换器组件的输出对输入变化的适应能力，特别关注注意力模块和前馈层的可塑性。

**主要结论**：高可塑性的注意力模块和前馈层在微调表现上优于传统认为的平滑性，这为变换器的功能特性提供了新的视角。

**关键词**：视觉变换器, finetuning, 平滑性, 适应性, 注意力模块, 迁移学习, 深度学习, transformer, 组件选择

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

**一句话总结**：T-STAR是一个基于Transformer的框架，用于短期概率需求预测，特别适用于共享微出行服务。

**研究动机**：短期需求预测对于管理共享微出行服务至关重要，以确保响应迅速和以用户为中心的运营。

**核心方法**：T-STAR采用两阶段结构，第一阶段捕捉粗略的小时需求模式，第二阶段通过高频本地输入提高预测准确性。

**主要结论**：实验表明，T-STAR在确定性和概率准确性方面优于现有方法，并能在未见服务区域中进行零-shot预测，展示了其强大的适应性和可靠性。

**关键词**：短期需求预测, 共享微出行, T-STAR, transformer, 概率预测, 时序模型, 高分辨率预测, 实时需求, 多模态出行规划, 用户中心化

**评分**：63

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06866v1) | [下载PDF](https://arxiv.org/pdf/2602.06866v1.pdf)

---

## [28. Zero-shot Generalizable Graph Anomaly Detection with Mixture of Riemannian Experts](https://arxiv.org/abs/2602.06859v1)

**作者**：Xinyu Zhao, Qingyun Sun, Jiayi Luo 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-06

### 📄 论文摘要

Graph Anomaly Detection (GAD) aims to identify irregular patterns in graph data, and recent works have explored zero-shot generalist GAD to enable generalization to unseen graph datasets. However, existing zero-shot GAD methods largely ignore intrinsic geometric differences across diverse anomaly patterns, substantially limiting their cross-domain generalization. In this work, we reveal that anomaly detectability is highly dependent on the underlying geometric properties and that embedding graphs from different domains into a single static curvature space can distort the structural signatures of anomalies. To address the challenge that a single curvature space cannot capture geometry-dependent graph anomaly patterns, we propose GAD-MoRE, a novel framework for zero-shot Generalizable Graph Anomaly Detection with a Mixture of Riemannian Experts architecture. Specifically, to ensure that each anomaly pattern is modeled in the Riemannian space where it is most detectable, GAD-MoRE employs a set of specialized Riemannian expert networks, each operating in a distinct curvature space. To align raw node features with curvature-specific anomaly characteristics, we introduce an anomaly-aware multi-curvature feature alignment module that projects inputs into parallel Riemannian spaces, enabling the capture of diverse geometric characteristics. Finally, to facilitate better generalization beyond seen patterns, we design a memory-based dynamic router that adaptively assigns each input to the most compatible expert based on historical reconstruction performance on similar anomalies. Extensive experiments in the zero-shot setting demonstrate that GAD-MoRE significantly outperforms state-of-the-art generalist GAD baselines, and even surpasses strong competitors that are few-shot fine-tuned with labeled data from the target domain.

### 🤖 AI 总结

**一句话总结**：GAD-MoRE是一种新的零-shot图异常检测框架，通过混合Riemannian专家网络改进了跨域泛化能力。

**研究动机**：现有的零-shot图异常检测方法未能充分考虑不同异常模式的几何特性，限制了其跨域泛化能力。

**核心方法**：GAD-MoRE采用多个专门的Riemannian专家网络，每个网络在不同的曲率空间中操作，并引入多曲率特征对齐模块和基于记忆的动态路由器来优化异常检测。

**主要结论**：实验结果表明，GAD-MoRE在零-shot设置下显著超越了现有的图异常检测基线，并优于在目标领域经过少量标记数据微调的竞争对手。

**关键词**：图异常检测, 零-shot, Riemannian专家, 几何特性, 特征对齐, 动态路由, 多曲率, 通用化, 机器学习, 深度学习, embedding

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06859v1) | [下载PDF](https://arxiv.org/pdf/2602.06859v1.pdf)

---

## [29. Designing a Robust, Bounded, and Smooth Loss Function for Improved Supervised Learning](https://arxiv.org/abs/2602.06858v1)

**作者**：Soumi Mahato, Lineesh M. C  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

The loss function is crucial to machine learning, especially in supervised learning frameworks. It is a fundamental component that controls the behavior and general efficacy of learning algorithms. However, despite their widespread use, traditional loss functions have significant drawbacks when dealing with high-dimensional and outlier-sensitive datasets, which frequently results in reduced performance and slower convergence during training. In this work, we develop a robust, bounded, and smooth (RoBoS-NN) loss function to resolve the aforementioned hindrances. The generalization ability of the loss function has also been theoretically analyzed to rigorously justify its robustness. Moreover, we implement RoboS-NN loss in the framework of a neural network (NN) to forecast time series and present a new robust algorithm named $\mathcal{L}_{\text{RoBoS}}$-NN. To assess the potential of $\mathcal{L}_{\text{RoBoS}}$-NN, we conduct experiments on multiple real-world datasets. In addition, we infuse outliers into data sets to evaluate the performance of $\mathcal{L}_{\text{RoBoS}}$-NN in more challenging scenarios. Numerical results show that $\mathcal{L}_{\text{RoBoS}}$-NN outperforms the other benchmark models in terms of accuracy measures.

### 🤖 AI 总结

**一句话总结**：本文提出了一种新的鲁棒、有界且平滑的损失函数（RoBoS-NN），以提高监督学习的性能，尤其是在处理高维和异常值敏感数据集时。

**研究动机**：传统损失函数在高维和异常值敏感数据集上表现不佳，导致学习算法的性能下降和收敛速度变慢，因此需要开发更有效的损失函数。

**核心方法**：本文提出了RoBoS-NN损失函数，并在神经网络框架中实现，进行了时间序列预测，并开发了新的鲁棒算法$	ext{L}_{	ext{RoBoS}}$-NN。

**主要结论**：实验结果表明，$	ext{L}_{	ext{RoBoS}}$-NN在准确性指标上优于其他基准模型，证明了其在处理复杂数据集时的有效性。

**关键词**：机器学习, 深度学习, 神经网络, RoBoS-NN, 监督学习, 算法优化, 时间序列预测, 鲁棒性, 性能评估, machine learning

**评分**：50

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06858v1) | [下载PDF](https://arxiv.org/pdf/2602.06858v1.pdf)

---

## [30. Improved Sampling Schedules for Discrete Diffusion Models](https://arxiv.org/abs/2602.06849v1)

**作者**：Alberto Foresti, Mustapha Bounoua, Giulio Franzese 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Discrete diffusion models have emerged as a powerful paradigm for generative modeling on sequence data; however, the information-theoretic principles governing their reverse processes remain significantly less understood than those of their continuous counterparts. In this work, we bridge this gap by analyzing the reverse process dynamics through the lens of thermodynamic entropy production. We propose the entropy production rate as a rigorous proxy for quantifying information generation, deriving as a byproduct a bound on the Wasserstein distance between intermediate states and the data distribution. Leveraging these insights, we introduce two novel sampling schedules that are uniformly spaced with respect to their corresponding physics-inspired metrics: the Entropic Discrete Schedule (EDS), which is defined by maintaining a constant rate of information gain, and the Wasserstein Discrete Schedule (WDS), which is defined by taking equal steps in terms of the Wasserstein distance. We empirically demonstrate that our proposed schedules significantly outperform state-of-the-art strategies across diverse application domains, including synthetic data, music notation, vision and language modeling, consistently achieving superior performance at a lower computational budget.

### 🤖 AI 总结

**一句话总结**：本文提出了改进的离散扩散模型采样调度，通过热力学熵产生分析其逆过程，并提出了两种新的采样策略。

**研究动机**：离散扩散模型在序列数据生成建模中表现出色，但其逆过程的信息理论原理尚不明确，因此需要进一步研究。

**核心方法**：本文分析了逆过程动态，并提出了熵产生率作为信息生成的量化代理，进而提出了基于这一理论的两种新的均匀采样调度：熵离散调度和Wasserstein离散调度。

**主要结论**：实验结果表明，所提采样调度在多种应用领域中显著优于现有策略，且在计算预算上表现更为高效。

**关键词**：离散扩散模型, 生成建模, 信息生成, 熵产生率, Wasserstein距离, Entropic Discrete Schedule, Wasserstein Discrete Schedule, 机器学习, 深度学习, 神经网络, ml

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06849v1) | [下载PDF](https://arxiv.org/pdf/2602.06849v1.pdf)

---

