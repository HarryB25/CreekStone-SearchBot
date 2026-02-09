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

**一句话总结**：Can AI agents predict whether they will succeed at a task? We study agentic uncertainty by eliciting success probability estimates before, during, and after task execution. All results exhibit agentic...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Agentic Uncertainty Reveals Agentic Overconfidence, Can AI agents predict whether they will succeed at a task? We study agentic uncertainty by eliciting success probability estimates before, and after task execution. All results exhibit agentic overconfidence: some agents that succeed only 22% of the time predict 77% success. Counterintuitively

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06948v1) | [下载PDF](https://arxiv.org/pdf/2602.06948v1.pdf)

---

## [2. AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents](https://arxiv.org/abs/2602.06855v1)

**作者**：Alisia Lupidi, Bhavul Gauri, Thomas Simon Foster 等 37 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-06

### 📄 论文摘要

LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce AIRS-Bench (the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. These tasks span diverse domains, including language modeling, mathematics, bioinformatics, and time series forecasting. AIRS-Bench tasks assess agentic capabilities over the full research lifecycle -- including idea generation, experiment analysis and iterative refinement -- without providing baseline code. The AIRS-Bench task format is versatile, enabling easy integration of new tasks and rigorous comparison across different agentic frameworks. We establish baselines using frontier models paired with both sequential and parallel scaffolds. Our results show that agents exceed human SOTA in four tasks but fail to match it in sixteen others. Even when agents surpass human benchmarks, they do not reach the theoretical performance ceiling for the underlying tasks. These findings indicate that AIRS-Bench is far from saturated and offers substantial room for improvement. We open-source the AIRS-Bench task definitions and evaluation code to catalyze further development in autonomous scientific research.

### 🤖 AI 总结

**一句话总结**：LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce AIRS-Bench (the AI Research Science Benchmark), a suite of 20 tasks sourced from state-...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：AIRS, Bench: a Suite of Tasks for Frontier AI Research Science Agents, LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce AIRS, Bench (the AI Research Science Benchmark), art machine learning papers. These tasks span diverse domains, and time series forecasting. AIRS, Bench tasks assess agentic capabilities over the full research lifecycle, without providing baseline code. The AIRS, enabling easy integration of new tasks and rigorous comparison across different agentic frameworks. We establish baselines using frontier models paired with both sequential and parallel scaffolds. Our results show that agents exceed human SOTA in four tasks but fail to match it in sixteen others. Even when agents surpass human benchmarks, they do not reach the theoretical performance ceiling for the underlying tasks. These findings indicate that AIRS, source the AIRS, Bench task definitions and evaluation code to catalyze further development in autonomous scientific research.

**评分**：0

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

**一句话总结**：Hallucinations in large language models remain a persistent challenge, particularly in multilingual and generative settings where factual consistency is difficult to maintain. While recent models show...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：M^3: A multitask multilingual benchmark for hallucination in LLMs, Hallucinations in large language models remain a persistent challenge, particularly in multilingual and generative settings where factual consistency is difficult to maintain. While recent models show strong performance on English, grained hallucination detection. Our results show that question answering is consistently easier than dialogue summarization, level hallucinations remain challenging even for the strongest models. Performance is highest in English and degrades in lower

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06920v1) | [下载PDF](https://arxiv.org/pdf/2602.06920v1.pdf)

---

## [4. Uncovering Cross-Objective Interference in Multi-Objective Alignment](https://arxiv.org/abs/2602.06869v1)

**作者**：Yining Lu, Meng Jiang  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

We study a persistent failure mode in multi-objective alignment for large language models (LLMs): training improves performance on only a subset of objectives while causing others to degrade. We formalize this phenomenon as cross-objective interference and conduct the first systematic study across classic scalarization algorithms, showing that interference is pervasive and exhibits strong model dependence.   To explain this phenomenon, we derive a local covariance law showing that an objective improves at first order when its reward exhibits positive covariance with the scalarized score. We extend this analysis to clipped surrogate objectives used in modern alignment, demonstrating that the covariance law remains valid under mild conditions despite clipping. Building on this analysis, we propose Covariance Targeted Weight Adaptation (CTWA), a plug-and-play method that maintains positive covariance between objective rewards and the training signal to effectively mitigate cross-objective interference. Finally, we complement these local improvement conditions with a global convergence analysis under the Polyak--Łojasiewicz condition, establishing when non-convex scalarized optimization achieves global convergence and how cross-objective interference depends on specific model geometric properties.

### 🤖 AI 总结

**一句话总结**：We study a persistent failure mode in multi-objective alignment for large language models (LLMs): training improves performance on only a subset of objectives while causing others to degrade. We forma...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：We study a persistent failure mode in multi, objective alignment for large language models (LLMs): training improves performance on only a subset of objectives while causing others to degrade. We formalize this phenomenon as cross, showing that interference is pervasive and exhibits strong model dependence.   To explain this phenomenon, demonstrating that the covariance law remains valid under mild conditions despite clipping. Building on this analysis, play method that maintains positive covariance between objective rewards and the training signal to effectively mitigate cross

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06869v1) | [下载PDF](https://arxiv.org/pdf/2602.06869v1.pdf)

---

## [5. SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks](https://arxiv.org/abs/2602.06854v1)

**作者**：Mingqian Feng, Xiaodong Liu, Weiwei Yang 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-06

### 📄 论文摘要

Multi-turn jailbreaks capture the real threat model for safety-aligned chatbots, where single-turn attacks are merely a special case. Yet existing approaches break under exploration complexity and intent drift. We propose SEMA, a simple yet effective framework that trains a multi-turn attacker without relying on any existing strategies or external data. SEMA comprises two stages. Prefilling self-tuning enables usable rollouts by fine-tuning on non-refusal, well-structured, multi-turn adversarial prompts that are self-generated with a minimal prefix, thereby stabilizing subsequent learning. Reinforcement learning with intent-drift-aware reward trains the attacker to elicit valid multi-turn adversarial prompts while maintaining the same harmful objective. We anchor harmful intent in multi-turn jailbreaks via an intent-drift-aware reward that combines intent alignment, compliance risk, and level of detail. Our open-loop attack regime avoids dependence on victim feedback, unifies single- and multi-turn settings, and reduces exploration complexity. Across multiple datasets, victim models, and jailbreak judges, our method achieves state-of-the-art (SOTA) attack success rates (ASR), outperforming all single-turn baselines, manually scripted and template-driven multi-turn baselines, as well as our SFT (Supervised Fine-Tuning) and DPO (Direct Preference Optimization) variants. For instance, SEMA performs an average $80.1\%$ ASR@1 across three closed-source and open-source victim models on AdvBench, 33.9% over SOTA. The approach is compact, reproducible, and transfers across targets, providing a stronger and more realistic stress test for large language model (LLM) safety and enabling automatic redteaming to expose and localize failure modes. Our code is available at: https://github.com/fmmarkmq/SEMA.

### 🤖 AI 总结

**一句话总结**：Multi-turn jailbreaks capture the real threat model for safety-aligned chatbots, where single-turn attacks are merely a special case. Yet existing approaches break under exploration complexity and int...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Turn Jailbreak Attacks, turn jailbreaks capture the real threat model for safety, aligned chatbots, a simple yet effective framework that trains a multi, aware reward trains the attacker to elicit valid multi, turn adversarial prompts while maintaining the same harmful objective. We anchor harmful intent in multi, turn jailbreaks via an intent, and level of detail. Our open, and jailbreak judges, as well as our SFT (Supervised Fine, Tuning) and DPO (Direct Preference Optimization) variants. For instance, SEMA performs an average $80.1\%$ ASR@1 across three closed, providing a stronger and more realistic stress test for large language model (LLM) safety and enabling automatic redteaming to expose and localize failure modes. Our code is available at: https://github.com/fmmarkmq/SEMA.

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06854v1) | [下载PDF](https://arxiv.org/pdf/2602.06854v1.pdf)

---

## [6. The Representational Geometry of Number](https://arxiv.org/abs/2602.06843v1)

**作者**：Zhimin Hu, Lanhao Niu, Sashank Varma  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-06

### 📄 论文摘要

A central question in cognitive science is whether conceptual representations converge onto a shared manifold to support generalization, or diverge into orthogonal subspaces to minimize task interference. While prior work has discovered evidence for both, a mechanistic account of how these properties coexist and transform across tasks remains elusive. We propose that representational sharing lies not in the concepts themselves, but in the geometric relations between them. Using number concepts as a testbed and language models as high-dimensional computational substrates, we show that number representations preserve a stable relational structure across tasks. Task-specific representations are embedded in distinct subspaces, with low-level features like magnitude and parity encoded along separable linear directions. Crucially, we find that these subspaces are largely transformable into one another via linear mappings, indicating that representations share relational structure despite being located in distinct subspaces. Together, these results provide a mechanistic lens of how language models balance the shared structure of number representation with functional flexibility. It suggests that understanding arises when task-specific transformations are applied to a shared underlying relational structure of conceptual representations.

### 🤖 AI 总结

**一句话总结**：A central question in cognitive science is whether conceptual representations converge onto a shared manifold to support generalization, or diverge into orthogonal subspaces to minimize task interfere...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：a mechanistic account of how these properties coexist and transform across tasks remains elusive. We propose that representational sharing lies not in the concepts themselves

**评分**：0

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

**一句话总结**：Multimodal large language models (MLLMs) have rapidly advanced, yet their adoption in medicine remains limited by gaps in domain coverage, modality alignment, and grounded reasoning. In this work, we ...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Multimodal large language models (MLLMs) have rapidly advanced, yet their adoption in medicine remains limited by gaps in domain coverage, a medical foundation model built upon a generalized MLLM architecture and trained exclusively on large, domain, stage training recipe: (i) cross, modal pretraining to align heterogeneous visual encoders with a medical language backbone; (ii) instruction tuning on multi, retrieval, source medical MLLMs across multiple modalities and tasks. On VQA benchmarks, MedMO achieves an average accuracy improvement of +13.7% over the baseline and performs within 1.9% of the SOTA Fleming, it attains +6.9% over the baseline and +14.5% over Fleming, MedMO delivers significant gains in both semantic and clinical accuracy. Moreover, modality generalization. We release two versions of MedMO: 4B and 8B. Project is available at https://genmilab.github.io/MedMO

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06965v1) | [下载PDF](https://arxiv.org/pdf/2602.06965v1.pdf)

---

## [8. CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation](https://arxiv.org/abs/2602.06959v1)

**作者**：Kaiyi Huang, Yukun Huang, Yu Li 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-06

### 📄 论文摘要

Cinematic video production requires control over scene-subject composition and camera movement, but live-action shooting remains costly due to the need for constructing physical sets. To address this, we introduce the task of cinematic video generation with decoupled scene context: given multiple images of a static environment, the goal is to synthesize high-quality videos featuring dynamic subject while preserving the underlying scene consistency and following a user-specified camera trajectory. We present CineScene, a framework that leverages implicit 3D-aware scene representation for cinematic video generation. Our key innovation is a novel context conditioning mechanism that injects 3D-aware features in an implicit way: By encoding scene images into visual representations through VGGT, CineScene injects spatial priors into a pretrained text-to-video generation model by additional context concatenation, enabling camera-controlled video synthesis with consistent scenes and dynamic subjects. To further enhance the model's robustness, we introduce a simple yet effective random-shuffling strategy for the input scene images during training. To address the lack of training data, we construct a scene-decoupled dataset with Unreal Engine 5, containing paired videos of scenes with and without dynamic subjects, panoramic images representing the underlying static scene, along with their camera trajectories. Experiments show that CineScene achieves state-of-the-art performance in scene-consistent cinematic video generation, handling large camera movements and demonstrating generalization across diverse environments.

### 🤖 AI 总结

**一句话总结**：Cinematic video production requires control over scene-subject composition and camera movement, but live-action shooting remains costly due to the need for constructing physical sets. To address this,...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：action shooting remains costly due to the need for constructing physical sets. To address this, we introduce the task of cinematic video generation with decoupled scene context: given multiple images of a static environment, a framework that leverages implicit 3D, aware scene representation for cinematic video generation. Our key innovation is a novel context conditioning mechanism that injects 3D, CineScene injects spatial priors into a pretrained text, video generation model by additional context concatenation, shuffling strategy for the input scene images during training. To address the lack of training data, containing paired videos of scenes with and without dynamic subjects

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06959v1) | [下载PDF](https://arxiv.org/pdf/2602.06959v1.pdf)

---

## [9. Reliable Mislabel Detection for Video Capsule Endoscopy Data](https://arxiv.org/abs/2602.06938v1)

**作者**：Julia Werner, Julius Oexle, Oliver Bause 等 8 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

The classification performance of deep neural networks relies strongly on access to large, accurately annotated datasets. In medical imaging, however, obtaining such datasets is particularly challenging since annotations must be provided by specialized physicians, which severely limits the pool of annotators. Furthermore, class boundaries can often be ambiguous or difficult to define which further complicates machine learning-based classification. In this paper, we want to address this problem and introduce a framework for mislabel detection in medical datasets. This is validated on the two largest, publicly available datasets for Video Capsule Endoscopy, an important imaging procedure for examining the gastrointestinal tract based on a video stream of lowresolution images. In addition, potentially mislabeled samples identified by our pipeline were reviewed and re-annotated by three experienced gastroenterologists. Our results show that the proposed framework successfully detects incorrectly labeled data and results in an improved anomaly detection performance after cleaning the datasets compared to current baselines.

### 🤖 AI 总结

**一句话总结**：The classification performance of deep neural networks relies strongly on access to large, accurately annotated datasets. In medical imaging, however, obtaining such datasets is particularly challengi...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：The classification performance of deep neural networks relies strongly on access to large, obtaining such datasets is particularly challenging since annotations must be provided by specialized physicians, class boundaries can often be ambiguous or difficult to define which further complicates machine learning, publicly available datasets for Video Capsule Endoscopy

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06938v1) | [下载PDF](https://arxiv.org/pdf/2602.06938v1.pdf)

---

## [10. RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing](https://arxiv.org/abs/2602.06871v1)

**作者**：Mohammadreza Salehi, Mehdi Noroozi, Luca Morreale 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-06

### 📄 论文摘要

Instructional video editing applies edits to an input video using only text prompts, enabling intuitive natural-language control. Despite rapid progress, most methods still require fixed-length inputs and substantial compute. Meanwhile, autoregressive video generation enables efficient variable-length synthesis, yet remains under-explored for video editing. We introduce a causal, efficient video editing model that edits variable-length videos frame by frame. For efficiency, we start from a 2D image-to-image (I2I) diffusion model and adapt it to video-to-video (V2V) editing by conditioning the edit at time step t on the model's prediction at t-1. To leverage videos' temporal redundancy, we propose a new I2I diffusion forward process formulation that encourages the model to predict the residual between the target output and the previous prediction. We call this Residual Flow Diffusion Model (RFDM), which focuses the denoising process on changes between consecutive frames. Moreover, we propose a new benchmark that better ranks state-of-the-art methods for editing tasks. Trained on paired video data for global/local style transfer and object removal, RFDM surpasses I2I-based methods and competes with fully spatiotemporal (3D) V2V models, while matching the compute of image models and scaling independently of input video length. More content can be found in: https://smsd75.github.io/RFDM_page/

### 🤖 AI 总结

**一句话总结**：Instructional video editing applies edits to an input video using only text prompts, enabling intuitive natural-language control. Despite rapid progress, most methods still require fixed-length inputs...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing, yet remains under, image (I2I) diffusion model and adapt it to video, 1. To leverage videos' temporal redundancy, we propose a new I2I diffusion forward process formulation that encourages the model to predict the residual between the target output and the previous prediction. We call this Residual Flow Diffusion Model (RFDM), art methods for editing tasks. Trained on paired video data for global/local style transfer and object removal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06871v1) | [下载PDF](https://arxiv.org/pdf/2602.06871v1.pdf)

---

## [11. Parameters as Experts: Adapting Vision Models with Dynamic Parameter Routing](https://arxiv.org/abs/2602.06862v1)

**作者**：Meng Lou, Stanley Yu, Yizhou Yu  
**分类**：cs.CV  
**发布时间**：2026-02-06

### 📄 论文摘要

Adapting pre-trained vision models using parameter-efficient fine-tuning (PEFT) remains challenging, as it aims to achieve performance comparable to full fine-tuning using a minimal number of trainable parameters. When applied to complex dense prediction tasks, existing methods exhibit limitations, including input-agnostic modeling and redundant cross-layer representations. To this end, we propose AdaRoute, a new adapter-style method featuring a simple mixture-of-experts (MoE) architecture. Specifically, we introduce shared expert centers, where each expert is a trainable parameter matrix. During a feedforward pass, each AdaRoute module in the network dynamically generates weight matrices tailored for the current module via a simple dynamic parameter routing mechanism, which selectively aggregates parameter matrices in the corresponding expert center. Dynamic weight matrices in AdaRoute modules facilitate low-rank adaptation in an input-dependent manner, thus generating more customized and powerful feature representations. Moreover, since AdaRoute modules across multiple network layers share the same expert center, they improve feature diversity by promoting implicit cross-layer feature interaction. Extensive experiments demonstrate the superiority of AdaRoute on diverse vision tasks, including semantic segmentation, object detection and instance segmentation, and panoptic segmentation. Code will be available at: https://bit.ly/3NZcr0H.

### 🤖 AI 总结

**一句话总结**：Adapting pre-trained vision models using parameter-efficient fine-tuning (PEFT) remains challenging, as it aims to achieve performance comparable to full fine-tuning using a minimal number of trainabl...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：trained vision models using parameter, tuning (PEFT) remains challenging, as it aims to achieve performance comparable to full fine, tuning using a minimal number of trainable parameters. When applied to complex dense prediction tasks, where each expert is a trainable parameter matrix. During a feedforward pass, each AdaRoute module in the network dynamically generates weight matrices tailored for the current module via a simple dynamic parameter routing mechanism, and panoptic segmentation. Code will be available at: https://bit.ly/3NZcr0H.

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06862v1) | [下载PDF](https://arxiv.org/pdf/2602.06862v1.pdf)

---

## [12. Rethinking Multi-Condition DiTs: Eliminating Redundant Attention via Position-Alignment and Keyword-Scoping](https://arxiv.org/abs/2602.06850v1)

**作者**：Chao Zhou, Tianyi Wei, Yiling Chen 等 5 位作者  
**分类**：cs.CV, cs.AI, cs.MM  
**发布时间**：2026-02-06

### 📄 论文摘要

While modern text-to-image models excel at prompt-based generation, they often lack the fine-grained control necessary for specific user requirements like spatial layouts or subject appearances. Multi-condition control addresses this, yet its integration into Diffusion Transformers (DiTs) is bottlenecked by the conventional ``concatenate-and-attend'' strategy, which suffers from quadratic computational and memory overhead as the number of conditions scales. Our analysis reveals that much of this cross-modal interaction is spatially or semantically redundant. To this end, we propose Position-aligned and Keyword-scoped Attention (PKA), a highly efficient framework designed to eliminate these redundancies. Specifically, Position-Aligned Attention (PAA) linearizes spatial control by enforcing localized patch alignment, while Keyword-Scoped Attention (KSA) prunes irrelevant subject-driven interactions via semantic-aware masking. To facilitate efficient learning, we further introduce a Conditional Sensitivity-Aware Sampling (CSAS) strategy that reweights the training objective towards critical denoising phases, drastically accelerating convergence and enhancing conditional fidelity. Empirically, PKA delivers a 10.0$\times$ inference speedup and a 5.1$\times$ VRAM saving, providing a scalable and resource-friendly solution for high-fidelity multi-conditioned generation.

### 🤖 AI 总结

**一句话总结**：While modern text-to-image models excel at prompt-based generation, they often lack the fine-grained control necessary for specific user requirements like spatial layouts or subject appearances. Multi...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：grained control necessary for specific user requirements like spatial layouts or subject appearances. Multi, yet its integration into Diffusion Transformers (DiTs) is bottlenecked by the conventional ``concatenate, Aware Sampling (CSAS) strategy that reweights the training objective towards critical denoising phases

**评分**：0

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

**一句话总结**：Existing approaches for analyzing neural network activations, such as PCA and sparse autoencoders, rely on strong structural assumptions. Generative models offer an alternative: they can uncover struc...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Learning a Generative Meta, Model of LLM Activations, Existing approaches for analyzing neural network activations, rely on strong structural assumptions. Generative models offer an alternative: they can uncover structure without such assumptions and act as priors that improve intervention fidelity. We explore this direction by training diffusion models on one billion residual stream activations, models" that learn the distribution of a network's internal states. We find that diffusion loss decreases smoothly with compute and reliably predicts downstream utility. In particular, with larger gains as loss decreases. Moreover, with sparse probing scores that scale as loss decreases. These results suggest generative meta, models offer a scalable path toward interpretability without restrictive structural assumptions. Project page: https://generative

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06964v1) | [下载PDF](https://arxiv.org/pdf/2602.06964v1.pdf)

---

## [14. Improving Credit Card Fraud Detection with an Optimized Explainable Boosting Machine](https://arxiv.org/abs/2602.06955v1)

**作者**：Reza E. Fazel, Arash Bakhtiary, Siavash A. Bigdeli  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Addressing class imbalance is a central challenge in credit card fraud detection, as it directly impacts predictive reliability in real-world financial systems. To overcome this, the study proposes an enhanced workflow based on the Explainable Boosting Machine (EBM)-a transparent, state-of-the-art implementation of the GA2M algorithm-optimized through systematic hyperparameter tuning, feature selection, and preprocessing refinement. Rather than relying on conventional sampling techniques that may introduce bias or cause information loss, the optimized EBM achieves an effective balance between accuracy and interpretability, enabling precise detection of fraudulent transactions while providing actionable insights into feature importance and interaction effects. Furthermore, the Taguchi method is employed to optimize both the sequence of data scalers and model hyperparameters, ensuring robust, reproducible, and systematically validated performance improvements. Experimental evaluation on benchmark credit card data yields an ROC-AUC of 0.983, surpassing prior EBM baselines (0.975) and outperforming Logistic Regression, Random Forest, XGBoost, and Decision Tree models. These results highlight the potential of interpretable machine learning and data-driven optimization for advancing trustworthy fraud analytics in financial systems.

### 🤖 AI 总结

**一句话总结**：Addressing class imbalance is a central challenge in credit card fraud detection, as it directly impacts predictive reliability in real-world financial systems. To overcome this, the study proposes an...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Improving Credit Card Fraud Detection with an Optimized Explainable Boosting Machine, the study proposes an enhanced workflow based on the Explainable Boosting Machine (EBM), and Decision Tree models. These results highlight the potential of interpretable machine learning and data

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06955v1) | [下载PDF](https://arxiv.org/pdf/2602.06955v1.pdf)

---

## [15. Endogenous Resistance to Activation Steering in Language Models](https://arxiv.org/abs/2602.06941v1)

**作者**：Alex McKenzie, Keenan Pepper, Stijn Servaes 等 9 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-02-06

### 📄 论文摘要

Large language models can resist task-misaligned activation steering during inference, sometimes recovering mid-generation to produce improved responses even when steering remains active. We term this Endogenous Steering Resistance (ESR). Using sparse autoencoder (SAE) latents to steer model activations, we find that Llama-3.3-70B shows substantial ESR, while smaller models from the Llama-3 and Gemma-2 families exhibit the phenomenon less frequently. We identify 26 SAE latents that activate differentially during off-topic content and are causally linked to ESR in Llama-3.3-70B. Zero-ablating these latents reduces the multi-attempt rate by 25%, providing causal evidence for dedicated internal consistency-checking circuits. We demonstrate that ESR can be deliberately enhanced through both prompting and training: meta-prompts instructing the model to self-monitor increase the multi-attempt rate by 4x for Llama-3.3-70B, and fine-tuning on self-correction examples successfully induces ESR-like behavior in smaller models. These findings have dual implications: ESR could protect against adversarial manipulation but might also interfere with beneficial safety interventions that rely on activation steering. Understanding and controlling these resistance mechanisms is important for developing transparent and controllable AI systems. Code is available at github.com/agencyenterprise/endogenous-steering-resistance.

### 🤖 AI 总结

**一句话总结**：Large language models can resist task-misaligned activation steering during inference, sometimes recovering mid-generation to produce improved responses even when steering remains active. We term this...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：generation to produce improved responses even when steering remains active. We term this Endogenous Steering Resistance (ESR). Using sparse autoencoder (SAE) latents to steer model activations, checking circuits. We demonstrate that ESR can be deliberately enhanced through both prompting and training: meta, like behavior in smaller models. These findings have dual implications: ESR could protect against adversarial manipulation but might also interfere with beneficial safety interventions that rely on activation steering. Understanding and controlling these resistance mechanisms is important for developing transparent and controllable AI systems. Code is available at github.com/agencyenterprise/endogenous

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06941v1) | [下载PDF](https://arxiv.org/pdf/2602.06941v1.pdf)

---

## [16. From Core to Detail: Unsupervised Disentanglement with Entropy-Ordered Flows](https://arxiv.org/abs/2602.06940v1)

**作者**：Daniel Galperin, Ullrich Köthe  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Learning unsupervised representations that are both semantically meaningful and stable across runs remains a central challenge in modern representation learning. We introduce entropy-ordered flows (EOFlows), a normalizing-flow framework that orders latent dimensions by their explained entropy, analogously to PCA's explained variance. This ordering enables adaptive injective flows: after training, one may retain only the top C latent variables to form a compact core representation while the remaining variables capture fine-grained detail and noise, with C chosen flexibly at inference time rather than fixed during training. EOFlows build on insights from Independent Mechanism Analysis, Principal Component Flows and Manifold Entropic Metrics. We combine likelihood-based training with local Jacobian regularization and noise augmentation into a method that scales well to high-dimensional data such as images. Experiments on the CelebA dataset show that our method uncovers a rich set of semantically interpretable features, allowing for high compression and strong denoising.

### 🤖 AI 总结

**一句话总结**：Learning unsupervised representations that are both semantically meaningful and stable across runs remains a central challenge in modern representation learning. We introduce entropy-ordered flows (EO...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：From Core to Detail: Unsupervised Disentanglement with Entropy, Learning unsupervised representations that are both semantically meaningful and stable across runs remains a central challenge in modern representation learning. We introduce entropy, flow framework that orders latent dimensions by their explained entropy, analogously to PCA's explained variance. This ordering enables adaptive injective flows: after training, one may retain only the top C latent variables to form a compact core representation while the remaining variables capture fine, grained detail and noise, with C chosen flexibly at inference time rather than fixed during training. EOFlows build on insights from Independent Mechanism Analysis, based training with local Jacobian regularization and noise augmentation into a method that scales well to high

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06940v1) | [下载PDF](https://arxiv.org/pdf/2602.06940v1.pdf)

---

## [17. Cochain Perspectives on Temporal-Difference Signals for Learning Beyond Markov Dynamics](https://arxiv.org/abs/2602.06939v1)

**作者**：Zuyuan Zhang, Sizhe Tang, Tian Lan  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-06

### 📄 论文摘要

Non-Markovian dynamics are commonly found in real-world environments due to long-range dependencies, partial observability, and memory effects. The Bellman equation that is the central pillar of Reinforcement learning (RL) becomes only approximately valid under Non-Markovian. Existing work often focus on practical algorithm designs and offer limited theoretical treatment to address key questions, such as what dynamics are indeed capturable by the Bellman framework and how to inspire new algorithm classes with optimal approximations. In this paper, we present a novel topological viewpoint on temporal-difference (TD) based RL. We show that TD errors can be viewed as 1-cochain in the topological space of state transitions, while Markov dynamics are then interpreted as topological integrability. This novel view enables us to obtain a Hodge-type decomposition of TD errors into an integrable component and a topological residual, through a Bellman-de Rham projection. We further propose HodgeFlow Policy Search (HFPS) by fitting a potential network to minimize the non-integrable projection residual in RL, achieving stability/sensitivity guarantees. In numerical evaluations, HFPS is shown to significantly improve RL performance under non-Markovian.

### 🤖 AI 总结

**一句话总结**：Non-Markovian dynamics are commonly found in real-world environments due to long-range dependencies, partial observability, and memory effects. The Bellman equation that is the central pillar of Reinf...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Cochain Perspectives on Temporal, and memory effects. The Bellman equation that is the central pillar of Reinforcement learning (RL) becomes only approximately valid under Non, such as what dynamics are indeed capturable by the Bellman framework and how to inspire new algorithm classes with optimal approximations. In this paper, cochain in the topological space of state transitions, while Markov dynamics are then interpreted as topological integrability. This novel view enables us to obtain a Hodge, through a Bellman

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06939v1) | [下载PDF](https://arxiv.org/pdf/2602.06939v1.pdf)

---

## [18. Robustness Beyond Known Groups with Low-rank Adaptation](https://arxiv.org/abs/2602.06924v1)

**作者**：Abinitha Gourabathina, Hyewon Jeong, Teya Bergamaschi 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Deep learning models trained to optimize average accuracy often exhibit systematic failures on particular subpopulations. In real world settings, the subpopulations most affected by such disparities are frequently unlabeled or unknown, thereby motivating the development of methods that are performant on sensitive subgroups without being pre-specified. However, existing group-robust methods typically assume prior knowledge of relevant subgroups, using group annotations for training or model selection. We propose Low-rank Error Informed Adaptation (LEIA), a simple two-stage method that improves group robustness by identifying a low-dimensional subspace in the representation space where model errors concentrate. LEIA restricts adaptation to this error-informed subspace via a low-rank adjustment to the classifier logits, directly targeting latent failure modes without modifying the backbone or requiring group labels. Using five real-world datasets, we analyze group robustness under three settings: (1) truly no knowledge of subgroup relevance, (2) partial knowledge of subgroup relevance, and (3) full knowledge of subgroup relevance. Across all settings, LEIA consistently improves worst-group performance while remaining fast, parameter-efficient, and robust to hyperparameter choice.

### 🤖 AI 总结

**一句话总结**：Deep learning models trained to optimize average accuracy often exhibit systematic failures on particular subpopulations. In real world settings, the subpopulations most affected by such disparities a...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Deep learning models trained to optimize average accuracy often exhibit systematic failures on particular subpopulations. In real world settings, using group annotations for training or model selection. We propose Low, directly targeting latent failure modes without modifying the backbone or requiring group labels. Using five real, group performance while remaining fast

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06924v1) | [下载PDF](https://arxiv.org/pdf/2602.06924v1.pdf)

---

## [19. From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers](https://arxiv.org/abs/2602.06923v1)

**作者**：Ziming Liu, Sophia Sanborn, Surya Ganguli 等 4 位作者  
**分类**：cs.LG, cs.AI, physics.class-ph  
**发布时间**：2026-02-06

### 📄 论文摘要

Can general-purpose AI architectures go beyond prediction to discover the physical laws governing the universe? True intelligence relies on "world models" -- causal abstractions that allow an agent to not only predict future states but understand the underlying governing dynamics. While previous "AI Physicist" approaches have successfully recovered such laws, they typically rely on strong, domain-specific priors that effectively "bake in" the physics. Conversely, Vafa et al. recently showed that generic Transformers fail to acquire these world models, achieving high predictive accuracy without capturing the underlying physical laws. We bridge this gap by systematically introducing three minimal inductive biases. We show that ensuring spatial smoothness (by formulating prediction as continuous regression) and stability (by training with noisy contexts to mitigate error accumulation) enables generic Transformers to surpass prior failures and learn a coherent Keplerian world model, successfully fitting ellipses to planetary trajectories. However, true physical insight requires a third bias: temporal locality. By restricting the attention window to the immediate past -- imposing the simple assumption that future states depend only on the local state rather than a complex history -- we force the model to abandon curve-fitting and discover Newtonian force representations. Our results demonstrate that simple architectural choices determine whether an AI becomes a curve-fitter or a physicist, marking a critical step toward automated scientific discovery.

### 🤖 AI 总结

**一句话总结**：Can general-purpose AI architectures go beyond prediction to discover the physical laws governing the universe? True intelligence relies on "world models" -- causal abstractions that allow an agent to...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers, purpose AI architectures go beyond prediction to discover the physical laws governing the universe? True intelligence relies on "world models", causal abstractions that allow an agent to not only predict future states but understand the underlying governing dynamics. While previous "AI Physicist" approaches have successfully recovered such laws, domain, Vafa et al. recently showed that generic Transformers fail to acquire these world models, achieving high predictive accuracy without capturing the underlying physical laws. We bridge this gap by systematically introducing three minimal inductive biases. We show that ensuring spatial smoothness (by formulating prediction as continuous regression) and stability (by training with noisy contexts to mitigate error accumulation) enables generic Transformers to surpass prior failures and learn a coherent Keplerian world model, fitting and discover Newtonian force representations. Our results demonstrate that simple architectural choices determine whether an AI becomes a curve

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06923v1) | [下载PDF](https://arxiv.org/pdf/2602.06923v1.pdf)

---

## [20. Revisiting the Generic Transformer: Deconstructing a Strong Baseline for Time Series Foundation Models](https://arxiv.org/abs/2602.06909v1)

**作者**：Yunshi Wen, Wesley M. Gifford, Chandra Reddy 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

The recent surge in Time Series Foundation Models has rapidly advanced the field, yet the heterogeneous training setups across studies make it difficult to attribute improvements to architectural innovations versus data engineering. In this work, we investigate the potential of a standard patch Transformer, demonstrating that this generic architecture achieves state-of-the-art zero-shot forecasting performance using a straightforward training protocol. We conduct a comprehensive ablation study that covers model scaling, data composition, and training techniques to isolate the essential ingredients for high performance. Our findings identify the key drivers of performance, while confirming that the generic architecture itself demonstrates excellent scalability. By strictly controlling these variables, we provide comprehensive empirical results on model scaling across multiple dimensions. We release our open-source model and detailed findings to establish a transparent, reproducible baseline for future research.

### 🤖 AI 总结

**一句话总结**：The recent surge in Time Series Foundation Models has rapidly advanced the field, yet the heterogeneous training setups across studies make it difficult to attribute improvements to architectural inno...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Revisiting the Generic Transformer: Deconstructing a Strong Baseline for Time Series Foundation Models, yet the heterogeneous training setups across studies make it difficult to attribute improvements to architectural innovations versus data engineering. In this work, we investigate the potential of a standard patch Transformer, shot forecasting performance using a straightforward training protocol. We conduct a comprehensive ablation study that covers model scaling, and training techniques to isolate the essential ingredients for high performance. Our findings identify the key drivers of performance, source model and detailed findings to establish a transparent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06909v1) | [下载PDF](https://arxiv.org/pdf/2602.06909v1.pdf)

---

## [21. A first realization of reinforcement learning-based closed-loop EEG-TMS](https://arxiv.org/abs/2602.06907v1)

**作者**：Dania Humaidan, Jiahua Xu, Jing Chen 等 11 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Background: Transcranial magnetic stimulation (TMS) is a powerful tool to investigate neurophysiology of the human brain and treat brain disorders. Traditionally, therapeutic TMS has been applied in a one-size-fits-all approach, disregarding inter- and intra-individual differences. Brain state-dependent EEG-TMS, such as coupling TMS with a pre-specified phase of the sensorimotor mu-rhythm, enables the induction of differential neuroplastic effects depending on the targeted phase. But this approach is still user-dependent as it requires defining an a-priori target phase. Objectives: To present a first realization of a machine-learning-based, closed-loop real-time EEG-TMS setup to identify user-independently the individual mu-rhythm phase associated with high- vs. low-corticospinal excitability states. Methods: We applied EEG-TMS to 25 participants targeting the supplementary motor area-primary motor cortex network and used a reinforcement learning algorithm to identify the mu-rhythm phase associated with high- vs. low corticospinal excitability. We employed linear mixed effects models and Bayesian analysis to determine effects of reinforced learning on corticospinal excitability indexed by motor evoked potential amplitude, and functional connectivity indexed by the imaginary part of resting-state EEG coherence. Results: Reinforcement learning effectively identified the mu-rhythm phase associated with high- vs. low-excitability states, and their repetitive stimulation resulted in long-term increases vs. decreases in functional connectivity in the stimulated sensorimotor network. Conclusions: We demonstrated for the first time the feasibility of closed-loop EEG-TMS in humans, a critical step towards individualized treatment of brain disorders.

### 🤖 AI 总结

**一句话总结**：Background: Transcranial magnetic stimulation (TMS) is a powerful tool to investigate neurophysiology of the human brain and treat brain disorders. Traditionally, therapeutic TMS has been applied in a...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Background: Transcranial magnetic stimulation (TMS) is a powerful tool to investigate neurophysiology of the human brain and treat brain disorders. Traditionally, individual differences. Brain state, a critical step towards individualized treatment of brain disorders.

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06907v1) | [下载PDF](https://arxiv.org/pdf/2602.06907v1.pdf)

---

## [22. Parameter-free Dynamic Regret: Time-varying Movement Costs, Delayed Feedback, and Memory](https://arxiv.org/abs/2602.06902v1)

**作者**：Emmanuel Esposito, Andrew Jacobsen, Hao Qiu 等 4 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-02-06

### 📄 论文摘要

In this paper, we study dynamic regret in unconstrained online convex optimization (OCO) with movement costs. Specifically, we generalize the standard setting by allowing the movement cost coefficients $λ_t$ to vary arbitrarily over time. Our main contribution is a novel algorithm that establishes the first comparator-adaptive dynamic regret bound for this setting, guaranteeing $\widetilde{\mathcal{O}}(\sqrt{(1+P_T)(T+\sum_t λ_t)})$ regret, where $P_T$ is the path length of the comparator sequence over $T$ rounds. This recovers the optimal guarantees for both static and dynamic regret in standard OCO as a special case where $λ_t=0$ for all rounds. To demonstrate the versatility of our results, we consider two applications: OCO with delayed feedback and OCO with time-varying memory. We show that both problems can be translated into time-varying movement costs, establishing a novel reduction specifically for the delayed feedback setting that is of independent interest. A crucial observation is that the first-order dependence on movement costs in our regret bound plays a key role in enabling optimal comparator-adaptive dynamic regret guarantees in both settings.

### 🤖 AI 总结

**一句话总结**：In this paper, we study dynamic regret in unconstrained online convex optimization (OCO) with movement costs. Specifically, we generalize the standard setting by allowing the movement cost coefficient...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：we study dynamic regret in unconstrained online convex optimization (OCO) with movement costs. Specifically, we generalize the standard setting by allowing the movement cost coefficients $λ_t$ to vary arbitrarily over time. Our main contribution is a novel algorithm that establishes the first comparator

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06902v1) | [下载PDF](https://arxiv.org/pdf/2602.06902v1.pdf)

---

## [23. Supercharging Simulation-Based Inference for Bayesian Optimal Experimental Design](https://arxiv.org/abs/2602.06900v1)

**作者**：Samuel Klein, Willie Neiswanger, Daniel Ratner 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.IT, cs.NE, stat.ML  
**发布时间**：2026-02-06

### 📄 论文摘要

Bayesian optimal experimental design (BOED) seeks to maximize the expected information gain (EIG) of experiments. This requires a likelihood estimate, which in many settings is intractable. Simulation-based inference (SBI) provides powerful tools for this regime. However, existing work explicitly connecting SBI and BOED is restricted to a single contrastive EIG bound. We show that the EIG admits multiple formulations which can directly leverage modern SBI density estimators, encompassing neural posterior, likelihood, and ratio estimation. Building on this perspective, we define a novel EIG estimator using neural likelihood estimation. Further, we identify optimization as a key bottleneck of gradient based EIG maximization and show that a simple multi-start parallel gradient ascent procedure can substantially improve reliability and performance. With these innovations, our SBI-based BOED methods are able to match or outperform by up to $22\%$ existing state-of-the-art approaches across standard BOED benchmarks.

### 🤖 AI 总结

**一句话总结**：Bayesian optimal experimental design (BOED) seeks to maximize the expected information gain (EIG) of experiments. This requires a likelihood estimate, which in many settings is intractable. Simulation...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Bayesian optimal experimental design (BOED) seeks to maximize the expected information gain (EIG) of experiments. This requires a likelihood estimate, existing work explicitly connecting SBI and BOED is restricted to a single contrastive EIG bound. We show that the EIG admits multiple formulations which can directly leverage modern SBI density estimators

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06900v1) | [下载PDF](https://arxiv.org/pdf/2602.06900v1.pdf)

---

## [24. Sample Complexity of Causal Identification with Temporal Heterogeneity](https://arxiv.org/abs/2602.06899v1)

**作者**：Ameya Rathod, Sujay Belsare, Salvik Krishna Nautiyal 等 5 位作者  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-02-06

### 📄 论文摘要

Recovering a unique causal graph from observational data is an ill-posed problem because multiple generating mechanisms can lead to the same observational distribution. This problem becomes solvable only by exploiting specific structural or distributional assumptions. While recent work has separately utilized time-series dynamics or multi-environment heterogeneity to constrain this problem, we integrate both as complementary sources of heterogeneity. This integration yields unified necessary identifiability conditions and enables a rigorous analysis of the statistical limits of recovery under thin versus heavy-tailed noise. In particular, temporal structure is shown to effectively substitute for missing environmental diversity, possibly achieving identifiability even under insufficient heterogeneity. Extending this analysis to heavy-tailed (Student's t) distributions, we demonstrate that while geometric identifiability conditions remain invariant, the sample complexity diverges significantly from the Gaussian baseline. Explicit information-theoretic bounds quantify this cost of robustness, establishing the fundamental limits of covariance-based causal graph recovery methods in realistic non-stationary systems. This work shifts the focus from whether causal structure is identifiable to whether it is statistically recoverable in practice.

### 🤖 AI 总结

**一句话总结**：Recovering a unique causal graph from observational data is an ill-posed problem because multiple generating mechanisms can lead to the same observational distribution. This problem becomes solvable o...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：environment heterogeneity to constrain this problem, tailed noise. In particular, tailed (Student's t) distributions, we demonstrate that while geometric identifiability conditions remain invariant

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06899v1) | [下载PDF](https://arxiv.org/pdf/2602.06899v1.pdf)

---

## [25. A Cycle-Consistent Graph Surrogate for Full-Cycle Left Ventricular Myocardial Biomechanics](https://arxiv.org/abs/2602.06884v1)

**作者**：Siyu Mu, Wei Xuan Chan, Choon Hwai Yap  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Image-based patient-specific simulation of left ventricular (LV) mechanics is valuable for understanding cardiac function and supporting clinical intervention planning, but conventional finite-element analysis (FEA) is computationally intensive. Current graph-based surrogates do not have full-cycle prediction capabilities, and physics-informed neural networks often struggle to converge on complex cardiac geometries. We present CardioGraphFENet (CGFENet), a unified graph-based surrogate for rapid full-cycle estimation of LV myocardial biomechanics, supervised by a large FEA simulation dataset. The proposed model integrates (i) a global--local graph encoder to capture mesh features with weak-form-inspired global coupling, (ii) a gated recurrent unit-based temporal encoder conditioned on the target volume-time signal to model cycle-coherent dynamics, and (iii) a cycle-consistent bidirectional formulation for both loading and inverse unloading within a single framework. These strategies enable high fidelity with respect to traditional FEA ground truths and produce physiologically plausible pressure-volume loops that match FEA results when coupled with a lumped-parameter model. In particular, the cycle-consistency strategy enables a significant reduction in FEA supervision with only minimal loss in accuracy.

### 🤖 AI 总结

**一句话总结**：Image-based patient-specific simulation of left ventricular (LV) mechanics is valuable for understanding cardiac function and supporting clinical intervention planning, but conventional finite-element...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：informed neural networks often struggle to converge on complex cardiac geometries. We present CardioGraphFENet (CGFENet)

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06884v1) | [下载PDF](https://arxiv.org/pdf/2602.06884v1.pdf)

---

## [26. Vision Transformer Finetuning Benefits from Non-Smooth Components](https://arxiv.org/abs/2602.06883v1)

**作者**：Ambroise Odonnat, Laetitia Chapel, Romain Tavenard 等 4 位作者  
**分类**：cs.LG, cs.CV, stat.ML  
**发布时间**：2026-02-06

### 📄 论文摘要

The smoothness of the transformer architecture has been extensively studied in the context of generalization, training stability, and adversarial robustness. However, its role in transfer learning remains poorly understood. In this paper, we analyze the ability of vision transformer components to adapt their outputs to changes in inputs, or, in other words, their plasticity. Defined as an average rate of change, it captures the sensitivity to input perturbation; in particular, a high plasticity implies low smoothness. We demonstrate through theoretical analysis and comprehensive experiments that this perspective provides principled guidance in choosing the components to prioritize during adaptation. A key takeaway for practitioners is that the high plasticity of the attention modules and feedforward layers consistently leads to better finetuning performance. Our findings depart from the prevailing assumption that smoothness is desirable, offering a novel perspective on the functional properties of transformers. The code is available at https://github.com/ambroiseodt/vit-plasticity.

### 🤖 AI 总结

**一句话总结**：The smoothness of the transformer architecture has been extensively studied in the context of generalization, training stability, and adversarial robustness. However, its role in transfer learning rem...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Vision Transformer Finetuning Benefits from Non, The smoothness of the transformer architecture has been extensively studied in the context of generalization, training stability, its role in transfer learning remains poorly understood. In this paper, we analyze the ability of vision transformer components to adapt their outputs to changes in inputs, their plasticity. Defined as an average rate of change, a high plasticity implies low smoothness. We demonstrate through theoretical analysis and comprehensive experiments that this perspective provides principled guidance in choosing the components to prioritize during adaptation. A key takeaway for practitioners is that the high plasticity of the attention modules and feedforward layers consistently leads to better finetuning performance. Our findings depart from the prevailing assumption that smoothness is desirable, offering a novel perspective on the functional properties of transformers. The code is available at https://github.com/ambroiseodt/vit

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06883v1) | [下载PDF](https://arxiv.org/pdf/2602.06883v1.pdf)

---

## [27. T-STAR: A Context-Aware Transformer Framework for Short-Term Probabilistic Demand Forecasting in Dock-Based Shared Micro-Mobility](https://arxiv.org/abs/2602.06866v1)

**作者**：Jingyi Cheng, Gonçalo Homem de Almeida Correia, Oded Cats 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Reliable short-term demand forecasting is essential for managing shared micro-mobility services and ensuring responsive, user-centered operations. This study introduces T-STAR (Two-stage Spatial and Temporal Adaptive contextual Representation), a novel transformer-based probabilistic framework designed to forecast station-level bike-sharing demand at a 15-minute resolution. T-STAR addresses key challenges in high-resolution forecasting by disentangling consistent demand patterns from short-term fluctuations through a hierarchical two-stage structure. The first stage captures coarse-grained hourly demand patterns, while the second stage improves prediction accuracy by incorporating high-frequency, localized inputs, including recent fluctuations and real-time demand variations in connected metro services, to account for temporal shifts in short-term demand. Time series transformer models are employed in both stages to generate probabilistic predictions. Extensive experiments using Washington D.C.'s Capital Bikeshare data demonstrate that T-STAR outperforms existing methods in both deterministic and probabilistic accuracy. The model exhibits strong spatial and temporal robustness across stations and time periods. A zero-shot forecasting experiment further highlights T-STAR's ability to transfer to previously unseen service areas without retraining. These results underscore the framework's potential to deliver granular, reliable, and uncertainty-aware short-term demand forecasts, which enable seamless integration to support multimodal trip planning for travelers and enhance real-time operations in shared micro-mobility services.

### 🤖 AI 总结

**一句话总结**：Reliable short-term demand forecasting is essential for managing shared micro-mobility services and ensuring responsive, user-centered operations. This study introduces T-STAR (Two-stage Spatial and T...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：STAR: A Context, Aware Transformer Framework for Short, stage Spatial and Temporal Adaptive contextual Representation), a novel transformer, grained hourly demand patterns, term demand. Time series transformer models are employed in both stages to generate probabilistic predictions. Extensive experiments using Washington D.C.'s Capital Bikeshare data demonstrate that T, STAR's ability to transfer to previously unseen service areas without retraining. These results underscore the framework's potential to deliver granular, and uncertainty, which enable seamless integration to support multimodal trip planning for travelers and enhance real

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06866v1) | [下载PDF](https://arxiv.org/pdf/2602.06866v1.pdf)

---

## [28. Zero-shot Generalizable Graph Anomaly Detection with Mixture of Riemannian Experts](https://arxiv.org/abs/2602.06859v1)

**作者**：Xinyu Zhao, Qingyun Sun, Jiayi Luo 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-06

### 📄 论文摘要

Graph Anomaly Detection (GAD) aims to identify irregular patterns in graph data, and recent works have explored zero-shot generalist GAD to enable generalization to unseen graph datasets. However, existing zero-shot GAD methods largely ignore intrinsic geometric differences across diverse anomaly patterns, substantially limiting their cross-domain generalization. In this work, we reveal that anomaly detectability is highly dependent on the underlying geometric properties and that embedding graphs from different domains into a single static curvature space can distort the structural signatures of anomalies. To address the challenge that a single curvature space cannot capture geometry-dependent graph anomaly patterns, we propose GAD-MoRE, a novel framework for zero-shot Generalizable Graph Anomaly Detection with a Mixture of Riemannian Experts architecture. Specifically, to ensure that each anomaly pattern is modeled in the Riemannian space where it is most detectable, GAD-MoRE employs a set of specialized Riemannian expert networks, each operating in a distinct curvature space. To align raw node features with curvature-specific anomaly characteristics, we introduce an anomaly-aware multi-curvature feature alignment module that projects inputs into parallel Riemannian spaces, enabling the capture of diverse geometric characteristics. Finally, to facilitate better generalization beyond seen patterns, we design a memory-based dynamic router that adaptively assigns each input to the most compatible expert based on historical reconstruction performance on similar anomalies. Extensive experiments in the zero-shot setting demonstrate that GAD-MoRE significantly outperforms state-of-the-art generalist GAD baselines, and even surpasses strong competitors that are few-shot fine-tuned with labeled data from the target domain.

### 🤖 AI 总结

**一句话总结**：Graph Anomaly Detection (GAD) aims to identify irregular patterns in graph data, and recent works have explored zero-shot generalist GAD to enable generalization to unseen graph datasets. However, exi...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Graph Anomaly Detection (GAD) aims to identify irregular patterns in graph data, domain generalization. In this work, we reveal that anomaly detectability is highly dependent on the underlying geometric properties and that embedding graphs from different domains into a single static curvature space can distort the structural signatures of anomalies. To address the challenge that a single curvature space cannot capture geometry, tuned with labeled data from the target domain.

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06859v1) | [下载PDF](https://arxiv.org/pdf/2602.06859v1.pdf)

---

## [29. Designing a Robust, Bounded, and Smooth Loss Function for Improved Supervised Learning](https://arxiv.org/abs/2602.06858v1)

**作者**：Soumi Mahato, Lineesh M. C  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

The loss function is crucial to machine learning, especially in supervised learning frameworks. It is a fundamental component that controls the behavior and general efficacy of learning algorithms. However, despite their widespread use, traditional loss functions have significant drawbacks when dealing with high-dimensional and outlier-sensitive datasets, which frequently results in reduced performance and slower convergence during training. In this work, we develop a robust, bounded, and smooth (RoBoS-NN) loss function to resolve the aforementioned hindrances. The generalization ability of the loss function has also been theoretically analyzed to rigorously justify its robustness. Moreover, we implement RoboS-NN loss in the framework of a neural network (NN) to forecast time series and present a new robust algorithm named $\mathcal{L}_{\text{RoBoS}}$-NN. To assess the potential of $\mathcal{L}_{\text{RoBoS}}$-NN, we conduct experiments on multiple real-world datasets. In addition, we infuse outliers into data sets to evaluate the performance of $\mathcal{L}_{\text{RoBoS}}$-NN in more challenging scenarios. Numerical results show that $\mathcal{L}_{\text{RoBoS}}$-NN outperforms the other benchmark models in terms of accuracy measures.

### 🤖 AI 总结

**一句话总结**：The loss function is crucial to machine learning, especially in supervised learning frameworks. It is a fundamental component that controls the behavior and general efficacy of learning algorithms. Ho...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：The loss function is crucial to machine learning, which frequently results in reduced performance and slower convergence during training. In this work, NN loss in the framework of a neural network (NN) to forecast time series and present a new robust algorithm named $\mathcal{L}_{\text{RoBoS}}$

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06858v1) | [下载PDF](https://arxiv.org/pdf/2602.06858v1.pdf)

---

## [30. Improved Sampling Schedules for Discrete Diffusion Models](https://arxiv.org/abs/2602.06849v1)

**作者**：Alberto Foresti, Mustapha Bounoua, Giulio Franzese 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-06

### 📄 论文摘要

Discrete diffusion models have emerged as a powerful paradigm for generative modeling on sequence data; however, the information-theoretic principles governing their reverse processes remain significantly less understood than those of their continuous counterparts. In this work, we bridge this gap by analyzing the reverse process dynamics through the lens of thermodynamic entropy production. We propose the entropy production rate as a rigorous proxy for quantifying information generation, deriving as a byproduct a bound on the Wasserstein distance between intermediate states and the data distribution. Leveraging these insights, we introduce two novel sampling schedules that are uniformly spaced with respect to their corresponding physics-inspired metrics: the Entropic Discrete Schedule (EDS), which is defined by maintaining a constant rate of information gain, and the Wasserstein Discrete Schedule (WDS), which is defined by taking equal steps in terms of the Wasserstein distance. We empirically demonstrate that our proposed schedules significantly outperform state-of-the-art strategies across diverse application domains, including synthetic data, music notation, vision and language modeling, consistently achieving superior performance at a lower computational budget.

### 🤖 AI 总结

**一句话总结**：Discrete diffusion models have emerged as a powerful paradigm for generative modeling on sequence data; however, the information-theoretic principles governing their reverse processes remain significa...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Improved Sampling Schedules for Discrete Diffusion Models, Discrete diffusion models have emerged as a powerful paradigm for generative modeling on sequence data; however, theoretic principles governing their reverse processes remain significantly less understood than those of their continuous counterparts. In this work, deriving as a byproduct a bound on the Wasserstein distance between intermediate states and the data distribution. Leveraging these insights, we introduce two novel sampling schedules that are uniformly spaced with respect to their corresponding physics, which is defined by maintaining a constant rate of information gain, art strategies across diverse application domains

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.06849v1) | [下载PDF](https://arxiv.org/pdf/2602.06849v1.pdf)

---

