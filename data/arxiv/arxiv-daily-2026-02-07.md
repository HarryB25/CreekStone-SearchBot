# arXiv AI 论文日报 | 2026-02-07

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

**一句话总结**：研究发现AI代理在任务成功预测上表现出过度自信，预执行评估的效果优于后执行回顾。

**研究动机**：探讨AI代理在执行任务时是否能够准确预测成功概率，以理解其决策过程中的不确定性。

**核心方法**：通过在任务执行前、中、后收集成功概率估计，评估代理的自信程度。

**主要结论**：尽管一些代理的成功率仅为22%，但他们预测的成功率高达77%；而且，前期评估在信息较少的情况下通常能更好地区分成功与否。

**关键词**：智能代理, 代理不确定性, 任务执行, 成功概率, 预执行评估, 对抗提示, 评估校准, agentic overconfidence, human-in-the-loop

**评分**：65

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06948v1) | [下载PDF](https://arxiv.org/pdf/2602.06948v1.pdf)

---

## [2. AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents](https://arxiv.org/abs/2602.06855v1)

**作者**：Alisia Lupidi, Bhavul Gauri, Thomas Simon Foster 等 37 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-06

### 📄 论文摘要

LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce AIRS-Bench (the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. These tasks span diverse domains, including language modeling, mathematics, bioinformatics, and time series forecasting. AIRS-Bench tasks assess agentic capabilities over the full research lifecycle -- including idea generation, experiment analysis and iterative refinement -- without providing baseline code. The AIRS-Bench task format is versatile, enabling easy integration of new tasks and rigorous comparison across different agentic frameworks. We establish baselines using frontier models paired with both sequential and parallel scaffolds. Our results show that agents exceed human SOTA in four tasks but fail to match it in sixteen others. Even when agents surpass human benchmarks, they do not reach the theoretical performance ceiling for the underlying tasks. These findings indicate that AIRS-Bench is far from saturated and offers substantial room for improvement. We open-source the AIRS-Bench task definitions and evaluation code to catalyze further development in autonomous scientific research.

### 🤖 AI 总结

**一句话总结**：AIRS-Bench是一个针对前沿AI研究科学代理的任务套件，包含20个来自领先机器学习论文的任务，旨在评估智能体在科学研究生命周期中的能力。

**研究动机**：随着大规模语言模型代理在科学研究中的潜力逐步显现，急需一个标准化的基准来加速这一领域的发展。

**核心方法**：AIRS-Bench提供多样化的任务格式，涵盖语言建模、数学、生物信息学等领域，支持新任务的轻松集成和不同智能体框架的比较。

**主要结论**：尽管在四项任务中智能体超越了人类的最好表现，但在其他十六项任务中仍未达到人类水平，表明AIRS-Bench仍有很大的改进空间。

**关键词**：LLM, agent, machine learning, 深度学习, 自主代理, 任务评估, 实验分析, 迭代优化, 科学研究

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

**一句话总结**：Halluverse-M^3是一个多任务多语言的数据集，旨在系统分析大型语言模型中的幻觉现象。

**研究动机**：大型语言模型在多语言和生成任务中的幻觉问题依然严重，尤其是在确保事实一致性方面需要更多研究。

**核心方法**：该数据集覆盖英语、阿拉伯语、印地语和土耳其语，支持问答和对话摘要两种生成任务，并通过控制编辑和人类注释验证幻觉输出。

**主要结论**：研究表明，问答任务的幻觉检测相对容易，而句子级幻觉检测依然具有挑战性，且在低资源语言中表现较差，印地语的检测准确率最低。

**关键词**：多任务, 多语言, LLM, 生成, 幻觉检测, 数据集, 对话摘要, 问答, 语言模型, 评估

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06920v1) | [下载PDF](https://arxiv.org/pdf/2602.06920v1.pdf)

---

## [4. Uncovering Cross-Objective Interference in Multi-Objective Alignment](https://arxiv.org/abs/2602.06869v1)

**作者**：Yining Lu, Meng Jiang  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

We study a persistent failure mode in multi-objective alignment for large language models (LLMs): training improves performance on only a subset of objectives while causing others to degrade. We formalize this phenomenon as cross-objective interference and conduct the first systematic study across classic scalarization algorithms, showing that interference is pervasive and exhibits strong model dependence.   To explain this phenomenon, we derive a local covariance law showing that an objective improves at first order when its reward exhibits positive covariance with the scalarized score. We extend this analysis to clipped surrogate objectives used in modern alignment, demonstrating that the covariance law remains valid under mild conditions despite clipping. Building on this analysis, we propose Covariance Targeted Weight Adaptation (CTWA), a plug-and-play method that maintains positive covariance between objective rewards and the training signal to effectively mitigate cross-objective interference. Finally, we complement these local improvement conditions with a global convergence analysis under the Polyak--Łojasiewicz condition, establishing when non-convex scalarized optimization achieves global convergence and how cross-objective interference depends on specific model geometric properties.

### 🤖 AI 总结

**一句话总结**：本文研究了多目标对齐中存在的交叉目标干扰现象，并提出了一种新方法以减少这种干扰。

**研究动机**：随着大语言模型的发展，多目标对齐中的性能提升往往只在部分目标上有效，而导致其他目标性能下降，因此需要深入理解和解决这一问题。

**核心方法**：我们提出了协方差目标加权适应（CTWA）方法，通过保持目标奖励与训练信号之间的正协方差来减轻交叉目标干扰，同时进行了局部和全局收敛分析。

**主要结论**：研究表明，交叉目标干扰普遍存在且依赖于模型几何特性，通过CTWA方法可以有效改善多目标对齐的整体性能。

**关键词**：多目标对齐, 大语言模型, 交叉目标干扰, 奖励模型, 协方差法则, Covariance Targeted Weight Adaptation, 训练信号, 非凸优化, 模型几何特性, llm

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06869v1) | [下载PDF](https://arxiv.org/pdf/2602.06869v1.pdf)

---

## [5. SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks](https://arxiv.org/abs/2602.06854v1)

**作者**：Mingqian Feng, Xiaodong Liu, Weiwei Yang 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-06

### 📄 论文摘要

Multi-turn jailbreaks capture the real threat model for safety-aligned chatbots, where single-turn attacks are merely a special case. Yet existing approaches break under exploration complexity and intent drift. We propose SEMA, a simple yet effective framework that trains a multi-turn attacker without relying on any existing strategies or external data. SEMA comprises two stages. Prefilling self-tuning enables usable rollouts by fine-tuning on non-refusal, well-structured, multi-turn adversarial prompts that are self-generated with a minimal prefix, thereby stabilizing subsequent learning. Reinforcement learning with intent-drift-aware reward trains the attacker to elicit valid multi-turn adversarial prompts while maintaining the same harmful objective. We anchor harmful intent in multi-turn jailbreaks via an intent-drift-aware reward that combines intent alignment, compliance risk, and level of detail. Our open-loop attack regime avoids dependence on victim feedback, unifies single- and multi-turn settings, and reduces exploration complexity. Across multiple datasets, victim models, and jailbreak judges, our method achieves state-of-the-art (SOTA) attack success rates (ASR), outperforming all single-turn baselines, manually scripted and template-driven multi-turn baselines, as well as our SFT (Supervised Fine-Tuning) and DPO (Direct Preference Optimization) variants. For instance, SEMA performs an average $80.1\%$ ASR@1 across three closed-source and open-source victim models on AdvBench, 33.9% over SOTA. The approach is compact, reproducible, and transfers across targets, providing a stronger and more realistic stress test for large language model (LLM) safety and enabling automatic redteaming to expose and localize failure modes. Our code is available at: https://github.com/fmmarkmq/SEMA.

### 🤖 AI 总结

**一句话总结**：SEMA是一个简单高效的框架，专注于多轮越狱攻击，超越了现有方法的局限性。

**研究动机**：多轮越狱攻击反映了安全对齐聊天机器人的真实威胁模型，但现有方法在探索复杂性和意图漂移方面面临挑战。

**核心方法**：SEMA包含两个阶段：自我调节的预填充和基于意图漂移的强化学习，旨在生成有效的多轮对抗提示。

**主要结论**：SEMA在多个数据集和模型上实现了最先进的攻击成功率，提供了对大型语言模型安全性的强有力测试，并支持自动化的红队操作。

**关键词**：多轮攻击, 生成对抗, 强化学习, 多智能体, 意图预测, 自适应学习, 语义搜索, 模型安全, SEMA, llm

**评分**：65

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06854v1) | [下载PDF](https://arxiv.org/pdf/2602.06854v1.pdf)

---

## [6. The Representational Geometry of Number](https://arxiv.org/abs/2602.06843v1)

**作者**：Zhimin Hu, Lanhao Niu, Sashank Varma  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-06

### 📄 论文摘要

A central question in cognitive science is whether conceptual representations converge onto a shared manifold to support generalization, or diverge into orthogonal subspaces to minimize task interference. While prior work has discovered evidence for both, a mechanistic account of how these properties coexist and transform across tasks remains elusive. We propose that representational sharing lies not in the concepts themselves, but in the geometric relations between them. Using number concepts as a testbed and language models as high-dimensional computational substrates, we show that number representations preserve a stable relational structure across tasks. Task-specific representations are embedded in distinct subspaces, with low-level features like magnitude and parity encoded along separable linear directions. Crucially, we find that these subspaces are largely transformable into one another via linear mappings, indicating that representations share relational structure despite being located in distinct subspaces. Together, these results provide a mechanistic lens of how language models balance the shared structure of number representation with functional flexibility. It suggests that understanding arises when task-specific transformations are applied to a shared underlying relational structure of conceptual representations.

### 🤖 AI 总结

**一句话总结**：该研究探讨了数字概念的表征几何结构，揭示了任务特定表征如何在几何关系中共享结构。

**研究动机**：研究认知科学中概念表征在任务间的共享与干扰问题，寻求理解其机制。

**核心方法**：利用数字概念和语言模型，分析其在不同任务中的表征稳定性及几何关系。

**主要结论**：任务特定表征在不同子空间中具有可变换性，表明尽管位于不同子空间，它们之间依然共享关系结构。

**关键词**：表示几何, 概念表示, 共享流形, 任务干扰, 语言模型, 数字概念, 关系结构, 任务特定表示, 嵌入空间, 线性映射, agent

**评分**：55

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

**一句话总结**：MedMO是一个专注于医学图像的多模态大语言模型，针对医学领域的特定需求进行优化和训练。

**研究动机**：尽管多模态大语言模型的技术迅速发展，但在医学领域的应用仍然受到领域覆盖、模态对齐和基础推理等问题的限制。

**核心方法**：MedMO采用多阶段训练方案，包括跨模态预训练、基于多任务的指令调优和结合事实检查的强化学习，以增强模型的空间对齐和推理能力。

**主要结论**：MedMO在多个医学任务和模态上表现优异，显著提高了准确性和空间推理能力，并在放射学、眼科学和病理显微镜等领域展现了广泛的跨模态泛化能力。

**关键词**：多模态, 大语言模型, 医学图像, 强化学习, 语义理解, MedMO, 医学基础模型, 任务监督, 空间推理, 跨模态对齐, ml

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06965v1) | [下载PDF](https://arxiv.org/pdf/2602.06965v1.pdf)

---

## [8. CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation](https://arxiv.org/abs/2602.06959v1)

**作者**：Kaiyi Huang, Yukun Huang, Yu Li 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-06

### 📄 论文摘要

Cinematic video production requires control over scene-subject composition and camera movement, but live-action shooting remains costly due to the need for constructing physical sets. To address this, we introduce the task of cinematic video generation with decoupled scene context: given multiple images of a static environment, the goal is to synthesize high-quality videos featuring dynamic subject while preserving the underlying scene consistency and following a user-specified camera trajectory. We present CineScene, a framework that leverages implicit 3D-aware scene representation for cinematic video generation. Our key innovation is a novel context conditioning mechanism that injects 3D-aware features in an implicit way: By encoding scene images into visual representations through VGGT, CineScene injects spatial priors into a pretrained text-to-video generation model by additional context concatenation, enabling camera-controlled video synthesis with consistent scenes and dynamic subjects. To further enhance the model's robustness, we introduce a simple yet effective random-shuffling strategy for the input scene images during training. To address the lack of training data, we construct a scene-decoupled dataset with Unreal Engine 5, containing paired videos of scenes with and without dynamic subjects, panoramic images representing the underlying static scene, along with their camera trajectories. Experiments show that CineScene achieves state-of-the-art performance in scene-consistent cinematic video generation, handling large camera movements and demonstrating generalization across diverse environments.

### 🤖 AI 总结

**一句话总结**：CineScene提出了一种基于隐式3D场景表示的框架，用于合成动态主题的高质量电影视频，保持场景一致性并支持用户指定的摄像机轨迹。

**研究动机**：电影视频制作需要控制场景和摄像机运动，但传统的实拍成本高，亟需一种新的生成方法。

**核心方法**：CineScene通过将场景图像编码为视觉表示，结合上下文条件机制，实现了对预训练文本到视频生成模型的隐式3D特征注入。

**主要结论**：实验结果表明，CineScene在场景一致的电影视频生成中表现优越，能够有效处理大范围摄像机运动，并具备跨环境的泛化能力。

**关键词**：关键词：深度学习, 生成, 3D场景, 视频生成, 语义搜索, 视觉表示, 预训练模型, 场景一致性, 动态主体, rag

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

**一句话总结**：本文提出了一种框架用于检测视频胶囊内窥镜数据中的错误标签，并在清洗数据后提高了异常检测性能。

**研究动机**：医学影像中的标注数据获取困难，且标注常常存在模糊性，影响深度学习模型的分类表现。

**核心方法**：论文中引入了一种误标检测框架，并在两个大型公开数据集上进行了验证，通过三位经验丰富的胃肠病专家对潜在误标样本进行复审和重新标注。

**主要结论**：实验结果表明，该框架有效检测不正确标记的数据，并在清洗数据后显著提高了异常检测的性能。

**关键词**：深度学习, 神经网络, 医学影像, 视频胶囊内窥镜, 异常检测, 数据清洗, 机器学习, 分类性能, 医疗数据, machine learning

**评分**：65

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06938v1) | [下载PDF](https://arxiv.org/pdf/2602.06938v1.pdf)

---

## [10. RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing](https://arxiv.org/abs/2602.06871v1)

**作者**：Mohammadreza Salehi, Mehdi Noroozi, Luca Morreale 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-06

### 📄 论文摘要

Instructional video editing applies edits to an input video using only text prompts, enabling intuitive natural-language control. Despite rapid progress, most methods still require fixed-length inputs and substantial compute. Meanwhile, autoregressive video generation enables efficient variable-length synthesis, yet remains under-explored for video editing. We introduce a causal, efficient video editing model that edits variable-length videos frame by frame. For efficiency, we start from a 2D image-to-image (I2I) diffusion model and adapt it to video-to-video (V2V) editing by conditioning the edit at time step t on the model's prediction at t-1. To leverage videos' temporal redundancy, we propose a new I2I diffusion forward process formulation that encourages the model to predict the residual between the target output and the previous prediction. We call this Residual Flow Diffusion Model (RFDM), which focuses the denoising process on changes between consecutive frames. Moreover, we propose a new benchmark that better ranks state-of-the-art methods for editing tasks. Trained on paired video data for global/local style transfer and object removal, RFDM surpasses I2I-based methods and competes with fully spatiotemporal (3D) V2V models, while matching the compute of image models and scaling independently of input video length. More content can be found in: https://smsd75.github.io/RFDM_page/

### 🤖 AI 总结

**一句话总结**：RFDM是一种高效的因果视频编辑模型，通过残差流扩散方法实现对可变长度视频的逐帧编辑。

**研究动机**：传统视频编辑方法依赖固定长度输入且计算量大，而自回归视频生成尚未充分探索用于视频编辑。

**核心方法**：RFDM从2D图像扩散模型出发，通过预测目标输出与前一预测之间的残差进行视频到视频的编辑。

**主要结论**：RFDM在全局/局部风格转移和物体去除任务上超越了基于图像的方法，并与全时空V2V模型相竞争，同时计算量与图像模型相当。

**关键词**：残差流扩散模型, 视频编辑, 自然语言控制, 变量长度, 时序冗余, 生成模型, 深度学习, 预测模型, 编辑任务, 计算效率, diffusion

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06871v1) | [下载PDF](https://arxiv.org/pdf/2602.06871v1.pdf)

---

## [11. Parameters as Experts: Adapting Vision Models with Dynamic Parameter Routing](https://arxiv.org/abs/2602.06862v1)

**作者**：Meng Lou, Stanley Yu, Yizhou Yu  
**分类**：cs.CV  
**发布时间**：2026-02-06

### 📄 论文摘要

Adapting pre-trained vision models using parameter-efficient fine-tuning (PEFT) remains challenging, as it aims to achieve performance comparable to full fine-tuning using a minimal number of trainable parameters. When applied to complex dense prediction tasks, existing methods exhibit limitations, including input-agnostic modeling and redundant cross-layer representations. To this end, we propose AdaRoute, a new adapter-style method featuring a simple mixture-of-experts (MoE) architecture. Specifically, we introduce shared expert centers, where each expert is a trainable parameter matrix. During a feedforward pass, each AdaRoute module in the network dynamically generates weight matrices tailored for the current module via a simple dynamic parameter routing mechanism, which selectively aggregates parameter matrices in the corresponding expert center. Dynamic weight matrices in AdaRoute modules facilitate low-rank adaptation in an input-dependent manner, thus generating more customized and powerful feature representations. Moreover, since AdaRoute modules across multiple network layers share the same expert center, they improve feature diversity by promoting implicit cross-layer feature interaction. Extensive experiments demonstrate the superiority of AdaRoute on diverse vision tasks, including semantic segmentation, object detection and instance segmentation, and panoptic segmentation. Code will be available at: https://bit.ly/3NZcr0H.

### 🤖 AI 总结

**一句话总结**：本文提出了一种新的适应性方法AdaRoute，通过动态参数路由改进视觉模型的参数效率，显著提升了多种视觉任务的表现。

**研究动机**：在复杂的密集预测任务中，现有的参数高效微调方法存在输入无关建模和冗余跨层表示的局限性，因此需要一种新的解决方案来提高性能。

**核心方法**：AdaRoute采用混合专家架构，动态生成与当前模块相匹配的权重矩阵，并通过共享专家中心促进跨层特征交互，从而实现输入相关的低秩适应。

**主要结论**：大量实验表明，AdaRoute在语义分割、目标检测等多种视觉任务中表现优越，证明了该方法的有效性和潜力。

**关键词**：深度学习, 视觉模型, 动态参数路由, 适应性, 训练参数, 特征表示, 语义分割, 目标检测, 实例分割, agent

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06862v1) | [下载PDF](https://arxiv.org/pdf/2602.06862v1.pdf)

---

## [12. Rethinking Multi-Condition DiTs: Eliminating Redundant Attention via Position-Alignment and Keyword-Scoping](https://arxiv.org/abs/2602.06850v1)

**作者**：Chao Zhou, Tianyi Wei, Yiling Chen 等 5 位作者  
**分类**：cs.CV, cs.AI, cs.MM  
**发布时间**：2026-02-06

### 📄 论文摘要

While modern text-to-image models excel at prompt-based generation, they often lack the fine-grained control necessary for specific user requirements like spatial layouts or subject appearances. Multi-condition control addresses this, yet its integration into Diffusion Transformers (DiTs) is bottlenecked by the conventional ``concatenate-and-attend'' strategy, which suffers from quadratic computational and memory overhead as the number of conditions scales. Our analysis reveals that much of this cross-modal interaction is spatially or semantically redundant. To this end, we propose Position-aligned and Keyword-scoped Attention (PKA), a highly efficient framework designed to eliminate these redundancies. Specifically, Position-Aligned Attention (PAA) linearizes spatial control by enforcing localized patch alignment, while Keyword-Scoped Attention (KSA) prunes irrelevant subject-driven interactions via semantic-aware masking. To facilitate efficient learning, we further introduce a Conditional Sensitivity-Aware Sampling (CSAS) strategy that reweights the training objective towards critical denoising phases, drastically accelerating convergence and enhancing conditional fidelity. Empirically, PKA delivers a 10.0$\times$ inference speedup and a 5.1$\times$ VRAM saving, providing a scalable and resource-friendly solution for high-fidelity multi-conditioned generation.

### 🤖 AI 总结

**一句话总结**：本论文提出了一种新颖的注意力机制，通过位置对齐和关键词范围控制来提高多条件生成模型的效率，显著降低计算和内存开销。

**研究动机**：现代文本生成模型在满足用户特定需求（如空间布局和主题外观）方面存在不足，而多条件控制的整合受到传统策略的限制，导致计算和内存开销过大。

**核心方法**：提出了位置对齐注意力（PAA）和关键词范围注意力（KSA）两个新机制，以消除冗余的跨模态交互，并通过条件敏感采样（CSAS）策略加速训练过程。

**主要结论**：通过实验，PKA框架实现了10倍的推理速度提升和5.1倍的显存节省，为高保真多条件生成提供了可扩展且资源友好的解决方案。

**关键词**：多条件控制, 文本生成, 扩散变换器, 位置对齐注意力, 关键字范围注意力, 语义掩蔽, 高效学习, 训练目标, 资源友好, diffusion

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

**一句话总结**：本研究提出了一种生成性元模型，通过训练扩散模型分析神经网络激活，提供更好的可解释性和干预效果。

**研究动机**：现有的神经网络激活分析方法依赖于严格的结构假设，限制了其灵活性和有效性，因此需要探索生成模型作为替代方案。

**核心方法**：研究通过在十亿个残差流激活上训练扩散模型，创建学习网络内部状态分布的“元模型”。

**主要结论**：生成性元模型提供了一种可扩展的可解释性路径，无需限制性的结构假设，同时在干预中显著提高流畅度。

**关键词**：生成模型, 神经网络, 深度学习, 激活分析, 元模型, 扩散模型, 结构假设, 介入忠实度, 概念隔离, 稀疏探测评分, neural network

**评分**：60

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06964v1) | [下载PDF](https://arxiv.org/pdf/2602.06964v1.pdf)

---

## [14. Improving Credit Card Fraud Detection with an Optimized Explainable Boosting Machine](https://arxiv.org/abs/2602.06955v1)

**作者**：Reza E. Fazel, Arash Bakhtiary, Siavash A. Bigdeli  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Addressing class imbalance is a central challenge in credit card fraud detection, as it directly impacts predictive reliability in real-world financial systems. To overcome this, the study proposes an enhanced workflow based on the Explainable Boosting Machine (EBM)-a transparent, state-of-the-art implementation of the GA2M algorithm-optimized through systematic hyperparameter tuning, feature selection, and preprocessing refinement. Rather than relying on conventional sampling techniques that may introduce bias or cause information loss, the optimized EBM achieves an effective balance between accuracy and interpretability, enabling precise detection of fraudulent transactions while providing actionable insights into feature importance and interaction effects. Furthermore, the Taguchi method is employed to optimize both the sequence of data scalers and model hyperparameters, ensuring robust, reproducible, and systematically validated performance improvements. Experimental evaluation on benchmark credit card data yields an ROC-AUC of 0.983, surpassing prior EBM baselines (0.975) and outperforming Logistic Regression, Random Forest, XGBoost, and Decision Tree models. These results highlight the potential of interpretable machine learning and data-driven optimization for advancing trustworthy fraud analytics in financial systems.

### 🤖 AI 总结

**一句话总结**：通过优化的可解释增强机器，改进信用卡欺诈检测以应对类别不平衡问题，取得了优异的预测性能。

**研究动机**：信用卡欺诈检测面临类别不平衡的挑战，这影响了预测的可靠性，因此需要改进方法。

**核心方法**：本研究提出了一种基于可解释增强机器的优化工作流程，通过系统的超参数调优、特征选择和预处理改进，来提高模型的准确性和可解释性。

**主要结论**：优化后的EBM在信用卡数据集上实现了0.983的ROC-AUC，超越了之前的基线和其他模型，展示了可解释机器学习在金融欺诈分析中的潜力。

**关键词**：信用卡欺诈检测, 解释性增强机器, 机器学习, 特征选择, 数据预处理, 模型优化, 透明性, 预测可靠性, ROC-AUC, 数据驱动优化, machine learning

**评分**：56

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06955v1) | [下载PDF](https://arxiv.org/pdf/2602.06955v1.pdf)

---

## [15. Endogenous Resistance to Activation Steering in Language Models](https://arxiv.org/abs/2602.06941v1)

**作者**：Alex McKenzie, Keenan Pepper, Stijn Servaes 等 9 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-02-06

### 📄 论文摘要

Large language models can resist task-misaligned activation steering during inference, sometimes recovering mid-generation to produce improved responses even when steering remains active. We term this Endogenous Steering Resistance (ESR). Using sparse autoencoder (SAE) latents to steer model activations, we find that Llama-3.3-70B shows substantial ESR, while smaller models from the Llama-3 and Gemma-2 families exhibit the phenomenon less frequently. We identify 26 SAE latents that activate differentially during off-topic content and are causally linked to ESR in Llama-3.3-70B. Zero-ablating these latents reduces the multi-attempt rate by 25%, providing causal evidence for dedicated internal consistency-checking circuits. We demonstrate that ESR can be deliberately enhanced through both prompting and training: meta-prompts instructing the model to self-monitor increase the multi-attempt rate by 4x for Llama-3.3-70B, and fine-tuning on self-correction examples successfully induces ESR-like behavior in smaller models. These findings have dual implications: ESR could protect against adversarial manipulation but might also interfere with beneficial safety interventions that rely on activation steering. Understanding and controlling these resistance mechanisms is important for developing transparent and controllable AI systems. Code is available at github.com/agencyenterprise/endogenous-steering-resistance.

### 🤖 AI 总结

**一句话总结**：大型语言模型在推理过程中表现出内生抗干扰能力，即使在干扰持续存在时也能自我修正以提升响应质量。

**研究动机**：研究语言模型在任务不一致的情况下如何抵抗激活引导，以理解其内生抗干扰机制的重要性。

**核心方法**：通过使用稀疏自编码器潜变量来引导模型激活，分析不同模型在面对离题内容时的激活差异。

**主要结论**：发现内生抗干扰能力不仅可能防止恶意操控，还可能干扰依赖激活引导的安全干预措施，强调理解和控制这些机制的重要性。

**关键词**：内生抗激活引导, 语言模型, 大型语言模型, 自监控, 稀疏自编码器, 自我修正, 激活引导, 内部一致性检查, 多次尝试, 透明可控AI

**评分**：60

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06941v1) | [下载PDF](https://arxiv.org/pdf/2602.06941v1.pdf)

---

## [16. From Core to Detail: Unsupervised Disentanglement with Entropy-Ordered Flows](https://arxiv.org/abs/2602.06940v1)

**作者**：Daniel Galperin, Ullrich Köthe  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Learning unsupervised representations that are both semantically meaningful and stable across runs remains a central challenge in modern representation learning. We introduce entropy-ordered flows (EOFlows), a normalizing-flow framework that orders latent dimensions by their explained entropy, analogously to PCA's explained variance. This ordering enables adaptive injective flows: after training, one may retain only the top C latent variables to form a compact core representation while the remaining variables capture fine-grained detail and noise, with C chosen flexibly at inference time rather than fixed during training. EOFlows build on insights from Independent Mechanism Analysis, Principal Component Flows and Manifold Entropic Metrics. We combine likelihood-based training with local Jacobian regularization and noise augmentation into a method that scales well to high-dimensional data such as images. Experiments on the CelebA dataset show that our method uncovers a rich set of semantically interpretable features, allowing for high compression and strong denoising.

### 🤖 AI 总结

**一句话总结**：提出了一种新的无监督表示学习方法EOFlows，通过熵排序的流模型有效提取语义特征和细节信息。

**研究动机**：在无监督表示学习中，获取语义明确且稳定的表示是一个重要挑战。

**核心方法**：EOFlows通过熵排序的正则化流框架，对潜在维度进行排序，以实现自适应的注入流，并结合局部雅可比正则化和噪声增强，适用于高维数据。

**主要结论**：实验结果表明，EOFlows能够发现丰富的语义特征，实现高压缩率和强去噪能力。

**关键词**：无监督表示学习, 概率流, 潜在变量, 特征提取, 高维数据, 噪声增强, EOFlows, Jacobian正则化, agent

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

**一句话总结**：本文提出了一种新的拓扑视角来理解非马尔可夫动态下的时序差分信号，并提出了HodgeFlow政策搜索算法以改善强化学习性能。

**研究动机**：研究者希望解决非马尔可夫动态下强化学习的理论和算法局限性，探索Bellman框架的适用性和新算法的灵感。

**核心方法**：通过将时序差分误差视为状态转换的1-共链，利用Bellman-de Rham投影进行Hodge类型分解，提出了一种最小化非可积投影残差的HodgeFlow政策搜索算法。

**主要结论**：HFPS在数值评估中显示出在非马尔可夫环境下显著提高了强化学习的性能，并提供了稳定性和敏感性保证。

**关键词**：强化学习, 非马尔可夫动态, 时序差分, Bellman方程, HodgeFlow策略搜索, 状态转移, 顶点空间, 潜在网络, 稳定性保障

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

**一句话总结**：提出了一种低秩误差信息适应方法（LEIA），以提高模型在未知子群体上的鲁棒性。

**研究动机**：现有的群体鲁棒性方法通常需要先验知识，而许多在现实世界中受影响的子群体往往是未知或未标记的，因此需要开发不依赖于群体标签的方法。

**核心方法**：LEIA通过识别表示空间中模型错误集中的低维子空间，采用低秩调整分类器的logits来实现自适应。

**主要结论**：在三种不同的知识设置下，LEIA在改善最差群体表现的同时，保持了快速、参数高效和对超参数选择的鲁棒性。

**关键词**：深度学习, 低秩适应, 模型鲁棒性, 群体敏感性, 表示空间, 错误信息适应, subgroup relevance, 性能优化, 适应性调整, deep learning

**评分**：63

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06924v1) | [下载PDF](https://arxiv.org/pdf/2602.06924v1.pdf)

---

## [19. From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers](https://arxiv.org/abs/2602.06923v1)

**作者**：Ziming Liu, Sophia Sanborn, Surya Ganguli 等 4 位作者  
**分类**：cs.LG, cs.AI, physics.class-ph  
**发布时间**：2026-02-06

### 📄 论文摘要

Can general-purpose AI architectures go beyond prediction to discover the physical laws governing the universe? True intelligence relies on "world models" -- causal abstractions that allow an agent to not only predict future states but understand the underlying governing dynamics. While previous "AI Physicist" approaches have successfully recovered such laws, they typically rely on strong, domain-specific priors that effectively "bake in" the physics. Conversely, Vafa et al. recently showed that generic Transformers fail to acquire these world models, achieving high predictive accuracy without capturing the underlying physical laws. We bridge this gap by systematically introducing three minimal inductive biases. We show that ensuring spatial smoothness (by formulating prediction as continuous regression) and stability (by training with noisy contexts to mitigate error accumulation) enables generic Transformers to surpass prior failures and learn a coherent Keplerian world model, successfully fitting ellipses to planetary trajectories. However, true physical insight requires a third bias: temporal locality. By restricting the attention window to the immediate past -- imposing the simple assumption that future states depend only on the local state rather than a complex history -- we force the model to abandon curve-fitting and discover Newtonian force representations. Our results demonstrate that simple architectural choices determine whether an AI becomes a curve-fitter or a physicist, marking a critical step toward automated scientific discovery.

### 🤖 AI 总结

**一句话总结**：通过引入简单的归纳偏差，研究表明通用Transformer可以学习物理规律，超越传统的预测能力。

**研究动机**：研究旨在探索通用AI架构是否能够超越简单预测，发现宇宙的物理法则。

**核心方法**：通过引入空间平滑性、稳定性和时间局部性三个归纳偏差，改善Transformer在学习世界模型时的表现。

**主要结论**：简单的架构选择决定了AI是成为曲线拟合者还是物理学家，为自动化科学发现铺平了道路。

**关键词**：深度学习, 变换器, 世界模型, 物理法则, 代理, 自主智能, 空间平滑性, 时域局部性, 预测模型, 训练优化, agent

**评分**：56

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06923v1) | [下载PDF](https://arxiv.org/pdf/2602.06923v1.pdf)

---

## [20. Revisiting the Generic Transformer: Deconstructing a Strong Baseline for Time Series Foundation Models](https://arxiv.org/abs/2602.06909v1)

**作者**：Yunshi Wen, Wesley M. Gifford, Chandra Reddy 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

The recent surge in Time Series Foundation Models has rapidly advanced the field, yet the heterogeneous training setups across studies make it difficult to attribute improvements to architectural innovations versus data engineering. In this work, we investigate the potential of a standard patch Transformer, demonstrating that this generic architecture achieves state-of-the-art zero-shot forecasting performance using a straightforward training protocol. We conduct a comprehensive ablation study that covers model scaling, data composition, and training techniques to isolate the essential ingredients for high performance. Our findings identify the key drivers of performance, while confirming that the generic architecture itself demonstrates excellent scalability. By strictly controlling these variables, we provide comprehensive empirical results on model scaling across multiple dimensions. We release our open-source model and detailed findings to establish a transparent, reproducible baseline for future research.

### 🤖 AI 总结

**一句话总结**：本文探讨了一种标准补丁Transformer在时间序列预测中的优越表现，提供了高效的训练协议和全面的消融研究。

**研究动机**：随着时间序列基础模型的快速发展，研究中异构的训练设置使得很难区分架构创新与数据工程的贡献。

**核心方法**：研究采用标准补丁Transformer，进行全面的消融研究，涵盖模型扩展、数据组成和训练技术，以识别高性能的关键因素。

**主要结论**：研究结果表明，通用架构在性能上具有优越的可扩展性，并通过严格控制变量提供了各维度模型扩展的实证结果，发布了开源模型和详细发现以支持未来研究。

**关键词**：时间序列, Transformer, 基线模型, 预测性能, 模型缩放, 数据组合, 训练技术, 深度学习, 生成模型

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

**一句话总结**：本研究首次实现了基于强化学习的闭环EEG-TMS系统，为个性化脑部疾病治疗提供了新思路。

**研究动机**：传统的TMS治疗方法忽视了个体差异，研究旨在通过EEG-TMS技术提升治疗的个性化和有效性。

**核心方法**：研究对25名参与者应用EEG-TMS，使用强化学习算法识别与高低皮层脊髓兴奋性状态相关的mu节律相位。

**主要结论**：研究表明，强化学习能够有效识别mu节律相位，并通过重复刺激改善功能连接性，为个性化脑部疾病治疗奠定了基础。

**关键词**：机器学习, 强化学习, EEG-TMS, 神经网络, 闭环系统, 实时监测, 个性化治疗, 功能连接性, mu-rhythm, agent

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

**一句话总结**：提出了一种新算法，为动态在线凸优化中的时间变化移动成本提供了参数自适应动态遗憾界限。

**研究动机**：研究动态遗憾在不受限的在线凸优化中的应用，以更好地处理时间变化的移动成本和延迟反馈问题。

**核心方法**：通过引入可变的移动成本系数，设计了一种新算法，建立了第一个适应比较器的动态遗憾界限。

**主要结论**：该算法能够在多种应用中（如延迟反馈和时间变化记忆）实现最优的动态遗憾保证，并且在静态和动态遗憾的特殊情况下也恢复了最佳保证。

**关键词**：动态后悔, 在线凸优化, 运动成本, 延迟反馈, 记忆, 算法, 自适应, 运动成本系数, 无约束优化, 深度学习, agent

**评分**：58

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06902v1) | [下载PDF](https://arxiv.org/pdf/2602.06902v1.pdf)

---

## [23. Supercharging Simulation-Based Inference for Bayesian Optimal Experimental Design](https://arxiv.org/abs/2602.06900v1)

**作者**：Samuel Klein, Willie Neiswanger, Daniel Ratner 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.IT, cs.NE, stat.ML  
**发布时间**：2026-02-06

### 📄 论文摘要

Bayesian optimal experimental design (BOED) seeks to maximize the expected information gain (EIG) of experiments. This requires a likelihood estimate, which in many settings is intractable. Simulation-based inference (SBI) provides powerful tools for this regime. However, existing work explicitly connecting SBI and BOED is restricted to a single contrastive EIG bound. We show that the EIG admits multiple formulations which can directly leverage modern SBI density estimators, encompassing neural posterior, likelihood, and ratio estimation. Building on this perspective, we define a novel EIG estimator using neural likelihood estimation. Further, we identify optimization as a key bottleneck of gradient based EIG maximization and show that a simple multi-start parallel gradient ascent procedure can substantially improve reliability and performance. With these innovations, our SBI-based BOED methods are able to match or outperform by up to $22\%$ existing state-of-the-art approaches across standard BOED benchmarks.

### 🤖 AI 总结

**一句话总结**：本文提出了一种基于模拟推断的贝叶斯最优实验设计的新方法，能够显著提高实验信息增益的估计和优化性能。

**研究动机**：贝叶斯最优实验设计旨在最大化实验的预期信息增益，但现有方法在处理复杂的似然估计时面临挑战，因此需要新的方法来提高效率和可靠性。

**核心方法**：通过定义新的信息增益估计器，并采用多起始并行梯度上升方法，本文有效地连接了模拟推断与贝叶斯最优实验设计，利用现代密度估计工具来优化实验设计。

**主要结论**：通过这些创新，本文提出的方法在标准的贝叶斯最优实验设计基准测试中能够与现有的最先进方法相匹配或超越，提升了性能达22%。

**关键词**：贝叶斯最优实验设计, 期望信息增益, 模拟推断, 神经网络, 梯度优化, 多起始并行梯度上升, 性能提升, 可靠性, EIG最大化, rag

**评分**：65

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06900v1) | [下载PDF](https://arxiv.org/pdf/2602.06900v1.pdf)

---

## [24. Sample Complexity of Causal Identification with Temporal Heterogeneity](https://arxiv.org/abs/2602.06899v1)

**作者**：Ameya Rathod, Sujay Belsare, Salvik Krishna Nautiyal 等 5 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-02-06

### 📄 论文摘要

Recovering a unique causal graph from observational data is an ill-posed problem because multiple generating mechanisms can lead to the same observational distribution. This problem becomes solvable only by exploiting specific structural or distributional assumptions. While recent work has separately utilized time-series dynamics or multi-environment heterogeneity to constrain this problem, we integrate both as complementary sources of heterogeneity. This integration yields unified necessary identifiability conditions and enables a rigorous analysis of the statistical limits of recovery under thin versus heavy-tailed noise. In particular, temporal structure is shown to effectively substitute for missing environmental diversity, possibly achieving identifiability even under insufficient heterogeneity. Extending this analysis to heavy-tailed (Student's t) distributions, we demonstrate that while geometric identifiability conditions remain invariant, the sample complexity diverges significantly from the Gaussian baseline. Explicit information-theoretic bounds quantify this cost of robustness, establishing the fundamental limits of covariance-based causal graph recovery methods in realistic non-stationary systems. This work shifts the focus from whether causal structure is identifiable to whether it is statistically recoverable in practice.

### 🤖 AI 总结

**一句话总结**：本研究通过整合时间序列动态与多环境异质性，提出了统一的因果识别必要条件，分析了不同噪声下的样本复杂性。

**研究动机**：恢复唯一的因果图是一个不适定的问题，传统方法无法有效解决，而特定的结构或分布假设能够帮助识别因果关系。

**核心方法**：本研究整合了时间序列动态与环境异质性，提出了统一的识别条件，并通过信息论界限量化了在不同噪声条件下的样本复杂性。

**主要结论**：研究表明，时间结构可以有效弥补环境多样性的缺失，即使在异质性不足的情况下也能实现可识别性，同时揭示了在重尾分布下样本复杂性与高斯基准的显著差异。

**关键词**：因果识别, 观察数据, 统计极限, 时序动态, 多环境异质性, 采样复杂度, 非平稳系统, 识别条件, 结构假设, 统计恢复, agent

**评分**：54

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06899v1) | [下载PDF](https://arxiv.org/pdf/2602.06899v1.pdf)

---

## [25. A Cycle-Consistent Graph Surrogate for Full-Cycle Left Ventricular Myocardial Biomechanics](https://arxiv.org/abs/2602.06884v1)

**作者**：Siyu Mu, Wei Xuan Chan, Choon Hwai Yap  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Image-based patient-specific simulation of left ventricular (LV) mechanics is valuable for understanding cardiac function and supporting clinical intervention planning, but conventional finite-element analysis (FEA) is computationally intensive. Current graph-based surrogates do not have full-cycle prediction capabilities, and physics-informed neural networks often struggle to converge on complex cardiac geometries. We present CardioGraphFENet (CGFENet), a unified graph-based surrogate for rapid full-cycle estimation of LV myocardial biomechanics, supervised by a large FEA simulation dataset. The proposed model integrates (i) a global--local graph encoder to capture mesh features with weak-form-inspired global coupling, (ii) a gated recurrent unit-based temporal encoder conditioned on the target volume-time signal to model cycle-coherent dynamics, and (iii) a cycle-consistent bidirectional formulation for both loading and inverse unloading within a single framework. These strategies enable high fidelity with respect to traditional FEA ground truths and produce physiologically plausible pressure-volume loops that match FEA results when coupled with a lumped-parameter model. In particular, the cycle-consistency strategy enables a significant reduction in FEA supervision with only minimal loss in accuracy.

### 🤖 AI 总结

**一句话总结**：提出了一种快速全周期左心室心肌生物力学估计的图形代理模型CardioGraphFENet，克服了传统有限元分析的计算负担。

**研究动机**：传统的有限元分析在进行左心室力学模拟时计算量大，而现有的图形代理模型缺乏全周期预测能力，因此需要一种新的方法来提高计算效率和准确性。

**核心方法**：CardioGraphFENet结合了全球-局部图编码器、基于门控递归单元的时间编码器，以及一个循环一致的双向公式，以实现对左心室生物力学的快速预测。

**主要结论**：该模型在减少有限元分析监督的同时，仍能保持高精度，并生成与有限元结果相匹配的生理上合理的压力-体积循环。

**关键词**：图神经网络, 机器学习, 深度学习, 循环一致性, 生物力学模拟, CardioGraphFENet, 全周期预测, 物理信息神经网络, 高保真度, neural network

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06884v1) | [下载PDF](https://arxiv.org/pdf/2602.06884v1.pdf)

---

## [26. Vision Transformer Finetuning Benefits from Non-Smooth Components](https://arxiv.org/abs/2602.06883v1)

**作者**：Ambroise Odonnat, Laetitia Chapel, Romain Tavenard 等 4 位作者  
**分类**：cs.LG, cs.CV, stat.ML  
**发布时间**：2026-02-06

### 📄 论文摘要

The smoothness of the transformer architecture has been extensively studied in the context of generalization, training stability, and adversarial robustness. However, its role in transfer learning remains poorly understood. In this paper, we analyze the ability of vision transformer components to adapt their outputs to changes in inputs, or, in other words, their plasticity. Defined as an average rate of change, it captures the sensitivity to input perturbation; in particular, a high plasticity implies low smoothness. We demonstrate through theoretical analysis and comprehensive experiments that this perspective provides principled guidance in choosing the components to prioritize during adaptation. A key takeaway for practitioners is that the high plasticity of the attention modules and feedforward layers consistently leads to better finetuning performance. Our findings depart from the prevailing assumption that smoothness is desirable, offering a novel perspective on the functional properties of transformers. The code is available at https://github.com/ambroiseodt/vit-plasticity.

### 🤖 AI 总结

**一句话总结**：论文探讨了视觉变换器组件在迁移学习中的非平滑性如何影响其适应性和微调性能。

**研究动机**：尽管变换器架构的平滑性在泛化和稳定性方面得到了广泛研究，但其在迁移学习中的作用尚不清楚。

**核心方法**：通过理论分析和实验，研究了视觉变换器组件在输入变化下的输出适应能力，即其塑性，并分析了不同组件的优先级。

**主要结论**：研究发现，注意力模块和前馈层的高塑性一致地导致更好的微调性能，挑战了平滑性被视为优越性的传统观点。

**关键词**：视觉变换器, finetuning, 适应性, 组件选择, 训练稳定性, 迁移学习, transformer, plasticity, 注意力模块, feedforward层

**评分**：60

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06883v1) | [下载PDF](https://arxiv.org/pdf/2602.06883v1.pdf)

---

## [27. T-STAR: A Context-Aware Transformer Framework for Short-Term Probabilistic Demand Forecasting in Dock-Based Shared Micro-Mobility](https://arxiv.org/abs/2602.06866v1)

**作者**：Jingyi Cheng, Gonçalo Homem de Almeida Correia, Oded Cats 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Reliable short-term demand forecasting is essential for managing shared micro-mobility services and ensuring responsive, user-centered operations. This study introduces T-STAR (Two-stage Spatial and Temporal Adaptive contextual Representation), a novel transformer-based probabilistic framework designed to forecast station-level bike-sharing demand at a 15-minute resolution. T-STAR addresses key challenges in high-resolution forecasting by disentangling consistent demand patterns from short-term fluctuations through a hierarchical two-stage structure. The first stage captures coarse-grained hourly demand patterns, while the second stage improves prediction accuracy by incorporating high-frequency, localized inputs, including recent fluctuations and real-time demand variations in connected metro services, to account for temporal shifts in short-term demand. Time series transformer models are employed in both stages to generate probabilistic predictions. Extensive experiments using Washington D.C.'s Capital Bikeshare data demonstrate that T-STAR outperforms existing methods in both deterministic and probabilistic accuracy. The model exhibits strong spatial and temporal robustness across stations and time periods. A zero-shot forecasting experiment further highlights T-STAR's ability to transfer to previously unseen service areas without retraining. These results underscore the framework's potential to deliver granular, reliable, and uncertainty-aware short-term demand forecasts, which enable seamless integration to support multimodal trip planning for travelers and enhance real-time operations in shared micro-mobility services.

### 🤖 AI 总结

**一句话总结**：T-STAR是一种基于变压器的框架，针对短期共享微出行需求预测，能够提供高精度的概率预测。

**研究动机**：有效的短期需求预测对于管理共享微出行服务至关重要，以确保用户中心的响应操作。

**核心方法**：T-STAR采用两阶段层次结构，第一阶段捕获粗粒度的小时需求模式，第二阶段结合高频本地输入以提高预测准确性，使用时间序列变压器模型生成概率预测。

**主要结论**：T-STAR在确定性和概率准确性方面均优于现有方法，且能够在未见服务区域进行零-shot预测，展示了其在短期需求预测中的潜力。

**关键词**：短期需求预测, 共享微出行, transformer, 概率模型, 时序模型, 高分辨率预测, T-STAR, 实时需求变化, 空间时间鲁棒性

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06866v1) | [下载PDF](https://arxiv.org/pdf/2602.06866v1.pdf)

---

## [28. Zero-shot Generalizable Graph Anomaly Detection with Mixture of Riemannian Experts](https://arxiv.org/abs/2602.06859v1)

**作者**：Xinyu Zhao, Qingyun Sun, Jiayi Luo 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-06

### 📄 论文摘要

Graph Anomaly Detection (GAD) aims to identify irregular patterns in graph data, and recent works have explored zero-shot generalist GAD to enable generalization to unseen graph datasets. However, existing zero-shot GAD methods largely ignore intrinsic geometric differences across diverse anomaly patterns, substantially limiting their cross-domain generalization. In this work, we reveal that anomaly detectability is highly dependent on the underlying geometric properties and that embedding graphs from different domains into a single static curvature space can distort the structural signatures of anomalies. To address the challenge that a single curvature space cannot capture geometry-dependent graph anomaly patterns, we propose GAD-MoRE, a novel framework for zero-shot Generalizable Graph Anomaly Detection with a Mixture of Riemannian Experts architecture. Specifically, to ensure that each anomaly pattern is modeled in the Riemannian space where it is most detectable, GAD-MoRE employs a set of specialized Riemannian expert networks, each operating in a distinct curvature space. To align raw node features with curvature-specific anomaly characteristics, we introduce an anomaly-aware multi-curvature feature alignment module that projects inputs into parallel Riemannian spaces, enabling the capture of diverse geometric characteristics. Finally, to facilitate better generalization beyond seen patterns, we design a memory-based dynamic router that adaptively assigns each input to the most compatible expert based on historical reconstruction performance on similar anomalies. Extensive experiments in the zero-shot setting demonstrate that GAD-MoRE significantly outperforms state-of-the-art generalist GAD baselines, and even surpasses strong competitors that are few-shot fine-tuned with labeled data from the target domain.

### 🤖 AI 总结

**一句话总结**：GAD-MoRE是一种新框架，通过混合黎曼专家在不同曲率空间中建模异常模式，以实现零-shot可泛化的图异常检测。

**研究动机**：现有的零-shot图异常检测方法忽视了异常模式之间的几何差异，限制了其跨域泛化能力。

**核心方法**：GAD-MoRE使用多个专门的黎曼专家网络，在各自的曲率空间中处理输入，并引入一个多曲率特征对齐模块以捕捉多样的几何特征，同时通过记忆驱动的动态路由器优化输入分配。

**主要结论**：大量实验表明，GAD-MoRE在零-shot设置下显著超过了现有的通用图异常检测基线，甚至超越了在目标领域进行少量样本微调的强竞争者。

**关键词**：图神经网络, 零-shot, 异常检测, 几何特性, 多曲率, 生成模型, 特征对齐, 动态路由, 跨域泛化, GAD-MoRE, embedding

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

**一句话总结**：本文提出了一种新的鲁棒、有限和平滑的损失函数RoBoS-NN，以改善监督学习在高维和异常值敏感数据集上的表现。

**研究动机**：传统损失函数在处理高维和异常值敏感数据时存在显著缺陷，影响了学习算法的性能和收敛速度。

**核心方法**：开发RoBoS-NN损失函数，并在神经网络框架中实现，提出新的算法$	ext{L}_{	ext{RoBoS}}$-NN，进行时间序列预测。

**主要结论**：实验结果表明，$	ext{L}_{	ext{RoBoS}}$-NN在准确性上超越了其他基准模型，证明了其在挑战性场景中的优越性。

**关键词**：机器学习, 深度学习, 神经网络, 有界平滑损失函数, 监督学习, 时间序列预测, 鲁棒算法, 实验评估, 数据集, machine learning

**评分**：58

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06858v1) | [下载PDF](https://arxiv.org/pdf/2602.06858v1.pdf)

---

## [30. Improved Sampling Schedules for Discrete Diffusion Models](https://arxiv.org/abs/2602.06849v1)

**作者**：Alberto Foresti, Mustapha Bounoua, Giulio Franzese 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Discrete diffusion models have emerged as a powerful paradigm for generative modeling on sequence data; however, the information-theoretic principles governing their reverse processes remain significantly less understood than those of their continuous counterparts. In this work, we bridge this gap by analyzing the reverse process dynamics through the lens of thermodynamic entropy production. We propose the entropy production rate as a rigorous proxy for quantifying information generation, deriving as a byproduct a bound on the Wasserstein distance between intermediate states and the data distribution. Leveraging these insights, we introduce two novel sampling schedules that are uniformly spaced with respect to their corresponding physics-inspired metrics: the Entropic Discrete Schedule (EDS), which is defined by maintaining a constant rate of information gain, and the Wasserstein Discrete Schedule (WDS), which is defined by taking equal steps in terms of the Wasserstein distance. We empirically demonstrate that our proposed schedules significantly outperform state-of-the-art strategies across diverse application domains, including synthetic data, music notation, vision and language modeling, consistently achieving superior performance at a lower computational budget.

### 🤖 AI 总结

**一句话总结**：本文提出了两种新颖的离散扩散模型采样策略，以提高生成模型在序列数据上的性能。

**研究动机**：离散扩散模型在生成建模中表现出色，但其反向过程的信息理论原理尚不完善，亟需深入研究。

**核心方法**：通过热力学熵产生的视角，本文提出了保持恒定信息增益的熵离散调度（EDS）和在Wasserstein距离上等步长的Wasserstein离散调度（WDS）。

**主要结论**：实验结果表明，所提采样策略在多种应用领域的表现显著优于现有最先进方法，以更低的计算预算实现了更好的性能。

**关键词**：离散扩散模型, 生成建模, 信息生成, 熵产生率, Wasserstein距离, Entropic Discrete Schedule, Wasserstein Discrete Schedule, 计算效率, 视觉与语言建模, 音乐符号, ml

**评分**：60

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06849v1) | [下载PDF](https://arxiv.org/pdf/2602.06849v1.pdf)

---

