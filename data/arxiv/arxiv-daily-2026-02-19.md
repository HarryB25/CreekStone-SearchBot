# arXiv AI 论文日报 | 2026-02-19

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (8 篇)
- [cs.LG](#csLG) (14 篇)
- [cs.CL](#csCL) (5 篇)
- [cs.AI](#csAI) (3 篇)

---

## cs.AI

## [1. Towards a Science of AI Agent Reliability](https://arxiv.org/abs/2602.16666v1)

**作者**：Stephan Rabanser, Sayash Kapoor, Peter Kirgis 等 6 位作者  
**分类**：cs.AI, cs.CY, cs.LG  
**发布时间**：2026-02-18

### 📄 论文摘要

AI agents are increasingly deployed to execute important tasks. While rising accuracy scores on standard benchmarks suggest rapid progress, many agents still continue to fail in practice. This discrepancy highlights a fundamental limitation of current evaluations: compressing agent behavior into a single success metric obscures critical operational flaws. Notably, it ignores whether agents behave consistently across runs, withstand perturbations, fail predictably, or have bounded error severity. Grounded in safety-critical engineering, we provide a holistic performance profile by proposing twelve concrete metrics that decompose agent reliability along four key dimensions: consistency, robustness, predictability, and safety. Evaluating 14 agentic models across two complementary benchmarks, we find that recent capability gains have only yielded small improvements in reliability. By exposing these persistent limitations, our metrics complement traditional evaluations while offering tools for reasoning about how agents perform, degrade, and fail.

### 🤖 AI 总结

**一句话总结**：论文从安全工程视角系统化定义并度量“AI智能体可靠性”，提出12项指标揭示当前高能力模型在可靠性上仍存在显著缺陷。

**研究动机**：现有评估往往用单一成功率概括智能体表现，但在真实应用中，智能体仍频繁出现不稳定、脆弱和不可预测的失败，亟需更细粒度的可靠性评价体系。

**核心方法**：作者从一致性、鲁棒性、可预测性和安全性四个维度构建12个具体可靠性指标，并在两个基准上系统评测14个智能体模型，形成多维“性能画像”。

**主要结论**：结果显示，尽管近年的模型能力显著提升，但在可靠性各维度上的改善有限且不均衡；所提出指标能揭示传统单一成功率无法暴露的失效模式，为分析和改进智能体在真实环境中的表现与失效机理提供了新工具。

**关键词**：AI代理, autonomous agents, 多智能体评估, agent可靠性度量, 鲁棒性测试, 安全关键场景, 行为一致性分析, 故障模式分析, 任务执行稳定性, 模型性能剖面

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16666v1) | [下载PDF](https://arxiv.org/pdf/2602.16666v1.pdf)

---

## [2. Agent Skill Framework: Perspectives on the Potential of Small Language Models in Industrial Environments](https://arxiv.org/abs/2602.16653v1)

**作者**：Yangjie Xu, Lujun Li, Lama Sleem 等 9 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-18

### 📄 论文摘要

Agent Skill framework, now widely and officially supported by major players such as GitHub Copilot, LangChain, and OpenAI, performs especially well with proprietary models by improving context engineering, reducing hallucinations, and boosting task accuracy. Based on these observations, an investigation is conducted to determine whether the Agent Skill paradigm provides similar benefits to small language models (SLMs). This question matters in industrial scenarios where continuous reliance on public APIs is infeasible due to data-security and budget constraints requirements, and where SLMs often show limited generalization in highly customized scenarios. This work introduces a formal mathematical definition of the Agent Skill process, followed by a systematic evaluation of language models of varying sizes across multiple use cases. The evaluation encompasses two open-source tasks and a real-world insurance claims data set. The results show that tiny models struggle with reliable skill selection, while moderately sized SLMs (approximately 12B - 30B) parameters) benefit substantially from the Agent Skill approach. Moreover, code-specialized variants at around 80B parameters achieve performance comparable to closed-source baselines while improving GPU efficiency. Collectively, these findings provide a comprehensive and nuanced characterization of the capabilities and constraints of the framework, while providing actionable insights for the effective deployment of Agent Skills in SLM-centered environments.

### 🤖 AI 总结

**一句话总结**：本文系统评估了在工业场景中，将“Agent Skill”范式应用于小参数量语言模型（SLMs）的效果与局限。

**研究动机**：在对隐私与成本敏感的工业环境中，长期依赖闭源大模型API不可行，而本地小模型又在复杂自定义任务上泛化不足，因此需要验证Agent Skill框架是否能显著提升SLMs的实际可用性。

**核心方法**：本文首先给出Agent Skill过程的数学形式化定义，然后在多个用例上，对不同参数规模（从tiny到约80B）的开源/专用小模型进行系统对比实验，包括两个开源任务与一个真实保险理赔数据集，主要考察技能选择能力、任务准确率与GPU效率。

**主要结论**：实验表明：极小模型在可靠技能选择上表现较差；中等规模SLMs（约12B–30B）通过Agent Skill可获得显著收益；而约80B参数的代码特化模型在保持更高GPU效率的同时，其表现已可比肩闭源基线，为在以SLM为中心的工业部署中有效使用Agent Skills提供了实证指导。

**关键词**：小语言模型, 多智能体agent, AgentSkill框架, 代码大模型, 上下文工程, 工业场景部署, 保险理赔数据集, 参数规模评估, 任务技能选择, GPU效率优化

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16653v1) | [下载PDF](https://arxiv.org/pdf/2602.16653v1.pdf)

---

## [3. Creating a digital poet](https://arxiv.org/abs/2602.16578v1)

**作者**：Vered Tohar, Tsahi Hayat, Amir Leshem  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-02-18

### 📄 论文摘要

Can a machine write good poetry? Any positive answer raises fundamental questions about the nature and value of art. We report a seven-month poetry workshop in which a large language model was shaped into a digital poet through iterative in-context expert feedback, without retraining. Across sessions, the model developed a distinctive style and a coherent corpus, supported by quantitative and qualitative analyses, and it produced a pen name and author image. In a blinded authorship test with 50 humanities students and graduates (three AI poems and three poems by well-known poets each), judgments were at chance: human poems were labeled human 54% of the time and AI poems 52%, with 95% confidence intervals including 50%. After the workshop, a commercial publisher released a poetry collection authored by the model. These results show that workshop-style prompting can support long-horizon creative shaping and renew debates on creativity and authorship.

### 🤖 AI 总结

**一句话总结**：论文通过为期七个月的“诗歌工作坊式提示”实践，展示了大语言模型在不重新训练的前提下也能被塑造成风格稳定、质量接近人类的“数字诗人”。

**研究动机**：作者想探究：机器是否能写出被严肃读者认可的“好诗”，以及如果可以，这对艺术本质、创造力和作者身份的传统观念意味着什么。

**核心方法**：在七个月中，研究者以工作坊形式对大模型进行多轮上下文内、专家级细致反馈和迭代提示，不做参数更新，逐步塑造其诗歌风格与作品整体性，并通过盲测评估人类与AI诗作的可区分度。

**主要结论**：通过迭代式工作坊提示，模型形成了统一风格、连贯诗集和“笔名+作者形象”，在人文专业读者的盲测中其诗歌与名家诗歌难以区分，并最终由商业出版社出版诗集，表明长周期提示塑形可以支持高水平创作并重新激活关于创作主体与作者权利的讨论。

**关键词**：大语言模型, 生成式, 人机协作创作, 上下文迭代反馈, 诗歌生成, 风格塑造, 作者身份构建, 盲评实验, context

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16578v1) | [下载PDF](https://arxiv.org/pdf/2602.16578v1.pdf)

---

## cs.CL

## [4. Calibrate-Then-Act: Cost-Aware Exploration in LLM Agents](https://arxiv.org/abs/2602.16699v1)

**作者**：Wenxuan Ding, Nicholas Tomlin, Greg Durrett  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-18

### 📄 论文摘要

LLMs are increasingly being used for complex problems which are not necessarily resolved in a single response, but require interacting with an environment to acquire information. In these scenarios, LLMs must reason about inherent cost-uncertainty tradeoffs in when to stop exploring and commit to an answer. For instance, on a programming task, an LLM should test a generated code snippet if it is uncertain about the correctness of that code; the cost of writing a test is nonzero, but typically lower than the cost of making a mistake. In this work, we show that we can induce LLMs to explicitly reason about balancing these cost-uncertainty tradeoffs, then perform more optimal environment exploration. We formalize multiple tasks, including information retrieval and coding, as sequential decision-making problems under uncertainty. Each problem has latent environment state that can be reasoned about via a prior which is passed to the LLM agent. We introduce a framework called Calibrate-Then-Act (CTA), where we feed the LLM this additional context to enable it to act more optimally. This improvement is preserved even under RL training of both the baseline and CTA. Our results on information-seeking QA and on a simplified coding task show that making cost-benefit tradeoffs explicit with CTA can help agents discover more optimal decision-making strategies.

### 🤖 AI 总结

**一句话总结**：论文提出 Calibrate-Then-Act (CTA) 框架，让LLM显式权衡探索成本与不确定性，从而在信息检索与编码等交互式任务中做出更优探索决策。

**研究动机**：现实中的LLM代理在搜索信息、写代码等任务时，需要多轮与环境交互，既要减少试探成本又要避免错误，但现有方法缺乏对“何时继续探索、何时下结论”的显式成本-不确定性权衡。

**核心方法**：作者将信息检索和简化编码任务形式化为带潜在状态的不确定序贯决策问题，为LLM提供关于环境先验与成本结构的额外上下文，设计CTA框架引导模型先校准（估计不确定性与成本收益）再行动，并在有/无强化学习训练下与基线进行对比。

**主要结论**：实验表明，在信息检索问答和简化编程任务中，显式注入成本收益与不确定性结构的CTA代理能学到更优探索策略，在相似或更低交互成本下获得更高任务表现，该优势在RL训练后依然存在。

**关键词**：大语言模型, LLM代理, agent, 人机协作, 信息检索, 顺序决策, 成本敏感探索, 不确定性建模, 代码生成与测试

**评分**：48

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16699v1) | [下载PDF](https://arxiv.org/pdf/2602.16699v1.pdf)

---

## [5. Align Once, Benefit Multilingually: Enforcing Multilingual Consistency for LLM Safety Alignment](https://arxiv.org/abs/2602.16660v1)

**作者**：Yuyan Bu, Xiaohao Liu, ZhaoXing Ren 等 5 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-02-18

### 📄 论文摘要

The widespread deployment of large language models (LLMs) across linguistic communities necessitates reliable multilingual safety alignment. However, recent efforts to extend alignment to other languages often require substantial resources, either through large-scale, high-quality supervision in the target language or through pairwise alignment with high-resource languages, which limits scalability. In this work, we propose a resource-efficient method for improving multilingual safety alignment. We introduce a plug-and-play Multi-Lingual Consistency (MLC) loss that can be integrated into existing monolingual alignment pipelines. By improving collinearity between multilingual representation vectors, our method encourages directional consistency at the multilingual semantic level in a single update. This allows simultaneous alignment across multiple languages using only multilingual prompt variants without requiring additional response-level supervision in low-resource languages. We validate the proposed method across different model architectures and alignment paradigms, and demonstrate its effectiveness in enhancing multilingual safety with limited impact on general model utility. Further evaluation across languages and tasks indicates improved cross-lingual generalization, suggesting the proposed approach as a practical solution for multilingual consistency alignment under limited supervision.

### 🤖 AI 总结

**一句话总结**：本文提出一种可插拔的多语一致性损失MLC，在仅进行一次对齐更新的前提下显著提升LLM的多语言安全对齐能力。

**研究动机**：现有多语言安全对齐往往依赖大量目标语言标注或逐语言对齐，成本高且难以扩展，需要一种在资源有限条件下即可泛化到多语言的安全对齐方法。

**核心方法**：在现有单语对齐流程中加入多语一致性（MLC）损失，通过提升不同语言表示向量的共线性，使模型在语义层面跨语言保持方向一致，从而利用多语言提示变体实现一次性多语言对齐，无需低资源语言的额外响应级监督。

**主要结论**：实验表明MLC在多种模型架构和对齐范式下都能显著提升多语言安全性且对通用能力影响有限，并在多语言任务中展现更好的跨语种泛化，为低监督条件下的多语言一致性对齐提供了实用方案。

**关键词**：大语言模型, 安全对齐, 多语言一致性, 多语种表示学习, 语义向量对齐, 对齐损失函数, 跨语言泛化, 低资源语言场景, 安全评估基准, ml

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16660v1) | [下载PDF](https://arxiv.org/pdf/2602.16660v1.pdf)

---

## [6. Who can we trust? LLM-as-a-jury for Comparative Assessment](https://arxiv.org/abs/2602.16610v1)

**作者**：Mengjie Qian, Guangzhi Sun, Mark J. F. Gales 等 4 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-02-18

### 📄 论文摘要

Large language models (LLMs) are increasingly applied as automatic evaluators for natural language generation assessment often using pairwise comparative judgements. Existing approaches typically rely on single judges or aggregate multiple judges assuming equal reliability. In practice, LLM judges vary substantially in performance across tasks and aspects, and their judgment probabilities may be biased and inconsistent. Furthermore, human-labelled supervision for judge calibration may be unavailable. We first empirically demonstrate that inconsistencies in LLM comparison probabilities exist and show that it limits the effectiveness of direct probability-based ranking. To address this, we study the LLM-as-a-jury setting and propose BT-sigma, a judge-aware extension of the Bradley-Terry model that introduces a discriminator parameter for each judge to jointly infer item rankings and judge reliability from pairwise comparisons alone. Experiments on benchmark NLG evaluation datasets show that BT-sigma consistently outperforms averaging-based aggregation methods, and that the learned discriminator strongly correlates with independent measures of the cycle consistency of LLM judgments. Further analysis reveals that BT-sigma can be interpreted as an unsupervised calibration mechanism that improves aggregation by modelling judge reliability.

### 🤖 AI 总结

**一句话总结**：本文提出BT-sigma模型，在“多LLM评委”场景下从成对比较中同时推断被评对象排名和各评委可信度，从而更可靠地用LLM做自动评测。

**研究动机**：现有用LLM做NLG自动评估时通常简单平均多个LLM评委或只用单一评委，忽略了不同LLM在任务、维度上的可靠性差异及判断概率的不一致和偏差，且往往缺乏人工标注来校准评委。

**核心方法**：在Bradley-Terry成对比较模型基础上，引入对每个LLM评委的判别参数（discriminator），构成BT-sigma：通过仅依赖LLM产生的成对比较数据，联合估计候选文本的质量得分与各评委的可靠性，并利用该模型对比较结果进行聚合和排名。

**主要结论**：在多个NLG评测基准上，BT-sigma相比简单平均等方法显著提高了排名效果，其学到的评委判别参数与LLM判断的循环一致性高度相关，可被视为一种无需人工标注的“无监督校准”机制，用于更好地聚合多LLM评委的意见。

**关键词**：大语言模型, LLM评估, 比较评估, Bradley-Terry模型, 判决可靠性建模, 无监督校准, 自然语言生成评价, 多裁判聚合, 模型排序推断

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16610v1) | [下载PDF](https://arxiv.org/pdf/2602.16610v1.pdf)

---

## [7. ColBERT-Zero: To Pre-train Or Not To Pre-train ColBERT models](https://arxiv.org/abs/2602.16609v1)

**作者**：Antoine Chaffin, Luca Arnaboldi, Amélie Chatelain 等 4 位作者  
**分类**：cs.CL, cs.IR  
**发布时间**：2026-02-18

### 📄 论文摘要

Current state-of-the-art multi-vector models are obtained through a small Knowledge Distillation (KD) training step on top of strong single-vector models, leveraging the large-scale pre-training of these models. In this paper, we study the pre-training of multi-vector models and show that large-scale multi-vector pre-training yields much stronger multi-vector models. Notably, a fully ColBERT-pre-trained model, ColBERT-Zero, trained only on public data, outperforms GTE-ModernColBERT as well as its base model, GTE-ModernBERT, which leverages closed and much stronger data, setting new state-of-the-art for model this size. We also find that, although performing only a small KD step is not enough to achieve results close to full pre-training, adding a supervised step beforehand allows to achieve much closer performance while skipping the most costly unsupervised phase. Finally, we find that aligning the fine-tuning and pre-training setups is crucial when repurposing existing models. To enable exploration of our results, we release various checkpoints as well as code used to train them.

### 🤖 AI 总结

**一句话总结**：本文表明：针对多向量检索模型（ColBERT）进行大规模专门预训练，比只在强单向量模型上做小步蒸馏能得到显著更强的多向量模型。

**研究动机**：现有多向量检索模型大多只是依赖已预训练好的单向量模型做一小步知识蒸馏，尚不清楚直接对多向量架构做大规模预训练是否更优，以及如何高效复用已有模型。

**核心方法**：作者在公开数据上从头大规模预训练ColBERT架构得到ColBERT-Zero，并系统对比：仅小步KD、加入监督微调+KD、以及在不同预训练/微调配置下的性能差异，同时发布多个中间checkpoint用于实验。

**主要结论**：全程基于ColBERT架构进行大规模预训练的ColBERT-Zero在同等规模下超越基于更强闭源数据的GTE-ModernColBERT及其底座GTE-ModernBERT，说明多向量模型本身值得独立预训练；仅做小步KD不足，但若先加一段监督训练再KD，可在跳过最昂贵的无监督阶段的同时接近完全预训练效果，且微调与预训练设置的一致性对迁移性能至关重要。

**关键词**：深度学习, 神经网络, 多向量检索, ColBERT, 知识蒸馏, 语义搜索, 表示学习, 对比学习, 预训练策略, rag

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16609v1) | [下载PDF](https://arxiv.org/pdf/2602.16609v1.pdf)

---

## [8. CitiLink-Summ: Summarization of Discussion Subjects in European Portuguese Municipal Meeting Minutes](https://arxiv.org/abs/2602.16607v1)

**作者**：Miguel Marques, Ana Luísa Fernandes, Ana Filipa Pacheco 等 13 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-18

### 📄 论文摘要

Municipal meeting minutes are formal records documenting the discussions and decisions of local government, yet their content is often lengthy, dense, and difficult for citizens to navigate. Automatic summarization can help address this challenge by producing concise summaries for each discussion subject. Despite its potential, research on summarizing discussion subjects in municipal meeting minutes remains largely unexplored, especially in low-resource languages, where the inherent complexity of these documents adds further challenges. A major bottleneck is the scarcity of datasets containing high-quality, manually crafted summaries, which limits the development and evaluation of effective summarization models for this domain. In this paper, we present CitiLink-Summ, a new corpus of European Portuguese municipal meeting minutes, comprising 100 documents and 2,322 manually hand-written summaries, each corresponding to a distinct discussion subject. Leveraging this dataset, we establish baseline results for automatic summarization in this domain, employing state-of-the-art generative models (e.g., BART, PRIMERA) as well as large language models (LLMs), evaluated with both lexical and semantic metrics such as ROUGE, BLEU, METEOR, and BERTScore. CitiLink-Summ provides the first benchmark for municipal-domain summarization in European Portuguese, offering a valuable resource for advancing NLP research on complex administrative texts.

### 🤖 AI 总结

**一句话总结**：论文构建了一个面向欧洲葡语市政会议纪要的细粒度主题摘要数据集 CitiLink-Summ，并在其上建立自动摘要基线。

**研究动机**：市政会议纪要篇幅长且语言复杂，现有尤其是低资源语言（如欧洲葡语）在该行政领域缺乏高质量人工摘要数据集，导致自动摘要模型难以开发与评测。

**核心方法**：作者从市政会议纪要中抽取讨论议题，整理成100篇文档与2,322条人工撰写的主题级摘要，并使用BART、PRIMERA等生成模型及大型语言模型进行训练与评测，采用ROUGE、BLEU、METEOR、BERTScore等指标建立基线。

**主要结论**：CitiLink-Summ成为首个面向欧洲葡语市政领域的摘要基准资源，为处理复杂行政文本的自动摘要研究提供了数据基础和性能参考，并显示现有模型在该任务上仍有明显改进空间。

**关键词**：大语言模型, 生成式模型, 自动文本摘要, 神经网络, transformer, 语义评估, 低资源语言处理, 政府会议纪要, 葡萄牙语NLP

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16607v1) | [下载PDF](https://arxiv.org/pdf/2602.16607v1.pdf)

---

## cs.CV

## [9. TeCoNeRV: Leveraging Temporal Coherence for Compressible Neural Representations for Videos](https://arxiv.org/abs/2602.16711v1)

**作者**：Namitha Padmanabhan, Matthew Gwilliam, Abhinav Shrivastava  
**分类**：cs.CV  
**发布时间**：2026-02-18

### 📄 论文摘要

Implicit Neural Representations (INRs) have recently demonstrated impressive performance for video compression. However, since a separate INR must be overfit for each video, scaling to high-resolution videos while maintaining encoding efficiency remains a significant challenge. Hypernetwork-based approaches predict INR weights (hyponetworks) for unseen videos at high speeds, but with low quality, large compressed size, and prohibitive memory needs at higher resolutions. We address these fundamental limitations through three key contributions: (1) an approach that decomposes the weight prediction task spatially and temporally, by breaking short video segments into patch tubelets, to reduce the pretraining memory overhead by 20$\times$; (2) a residual-based storage scheme that captures only differences between consecutive segment representations, significantly reducing bitstream size; and (3) a temporal coherence regularization framework that encourages changes in the weight space to be correlated with video content. Our proposed method, TeCoNeRV, achieves substantial improvements of 2.47dB and 5.35dB PSNR over the baseline at 480p and 720p on UVG, with 36% lower bitrates and 1.5-3$\times$ faster encoding speeds. With our low memory usage, we are the first hypernetwork approach to demonstrate results at 480p, 720p and 1080p on UVG, HEVC and MCL-JCV. Our project page is available at https://namithap10.github.io/teconerv/ .

### 🤖 AI 总结

**一句话总结**：TeCoNeRV 提出一种利用时间一致性的新型可压缩神经视频表示方法，在显著降低比特率和内存的同时提升高分辨率视频压缩质量与编码速度。

**研究动机**：现有基于隐式神经表示的视频压缩方法需要为每个视频单独过拟合，难以兼顾高分辨率、压缩率和编码速度；现有超网络方法虽快但质量低、码流大且高分辨率内存开销过高。

**核心方法**：TeCoNeRV 通过三点改进：将视频划分为空间–时间 patch tubelets 分别预测权重以降低预训练内存；采用只存连续片段权重差分的残差存储以缩小码流；引入时间一致性正则，使权重随时间变化与视频内容变化对齐，从而提升压缩效率与表示稳定性。

**主要结论**：在 UVG、HEVC、MCL-JCV 等数据集上，TeCoNeRV 在 480p/720p/1080p 上首次实现超网络方法的系统性评测，相比基线在 480p 和 720p 上分别提升约 2.47dB 和 5.35dB PSNR，同时比特率降低约 36%、编码速度提升 1.5–3 倍，并显著减少内存占用。

**关键词**：神经网络, 隐式神经表示, 视频压缩, 超网络, 权重预测, 时序一致性正则, 残差编码, 高分辨率视频, rag

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16711v1) | [下载PDF](https://arxiv.org/pdf/2602.16711v1.pdf)

---

## [10. Are Object-Centric Representations Better At Compositional Generalization?](https://arxiv.org/abs/2602.16689v1)

**作者**：Ferdinand Kapl, Amir Mohammad Karimi Mamaghan, Maximilian Seitzer 等 7 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-02-18

### 📄 论文摘要

Compositional generalization, the ability to reason about novel combinations of familiar concepts, is fundamental to human cognition and a critical challenge for machine learning. Object-centric (OC) representations, which encode a scene as a set of objects, are often argued to support such generalization, but systematic evidence in visually rich settings is limited. We introduce a Visual Question Answering benchmark across three controlled visual worlds (CLEVRTex, Super-CLEVR, and MOVi-C) to measure how well vision encoders, with and without object-centric biases, generalize to unseen combinations of object properties. To ensure a fair and comprehensive comparison, we carefully account for training data diversity, sample size, representation size, downstream model capacity, and compute. We use DINOv2 and SigLIP2, two widely used vision encoders, as the foundation models and their OC counterparts. Our key findings reveal that (1) OC approaches are superior in harder compositional generalization settings; (2) original dense representations surpass OC only on easier settings and typically require substantially more downstream compute; and (3) OC models are more sample efficient, achieving stronger generalization with fewer images, whereas dense encoders catch up or surpass them only with sufficient data and diversity. Overall, object-centric representations offer stronger compositional generalization when any one of dataset size, training data diversity, or downstream compute is constrained.

### 🤖 AI 总结

**一句话总结**：论文系统比较了带/不带物体归纳偏置的视觉编码器，发现物体中心表示在受数据量、数据多样性或下游算力限制时能显著提升组合泛化能力。

**研究动机**：组合泛化是人类认知核心能力，但当前视觉模型在遇到“熟悉属性的新组合”时表现不佳；虽然理论上物体中心表示被认为有助于组合泛化，但在复杂视觉场景中的系统性实证证据仍然不足。

**核心方法**：作者基于三个人工可控视觉世界（CLEVRTex、Super-CLEVR、MOVi-C）构建VQA基准，控制训练数据多样性、样本量、表示维度、下游模型容量和算力，并以DINOv2和SigLIP2为基底，对比其原始致密表示与加入物体中心偏置的OC版本在未见属性组合上的表现。

**主要结论**：实验表明：(1) 在更困难的组合泛化设置中，物体中心表示明显优于致密表示；(2) 致密表示只在较简单场景中占优且往往需要更多下游算力；(3) OC模型在样本效率上更好，在数据或多样性不足时泛化更强，而致密模型只有在数据和多样性足够大时才能追平或超越；整体而言，当数据规模、多样性或算力任一受限时，物体中心表示更能支持组合泛化。

**关键词**：机器学习, 深度学习, 神经网络, 视觉问答, 组合泛化, 对象中心表示, 视觉编码器, DINOv2, SigLIP2, 样本效率, machine learning

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16689v1) | [下载PDF](https://arxiv.org/pdf/2602.16689v1.pdf)

---

## [11. Learning Situated Awareness in the Real World](https://arxiv.org/abs/2602.16682v1)

**作者**：Chuhan Li, Ruilin Han, Joy Hsu 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-18

### 📄 论文摘要

A core aspect of human perception is situated awareness, the ability to relate ourselves to the surrounding physical environment and reason over possible actions in context. However, most existing benchmarks for multimodal foundation models (MFMs) emphasize environment-centric spatial relations (relations among objects in a scene), while largely overlooking observer-centric relationships that require reasoning relative to agent's viewpoint, pose, and motion. To bridge this gap, we introduce SAW-Bench (Situated Awareness in the Real World), a novel benchmark for evaluating egocentric situated awareness using real-world videos. SAW-Bench comprises 786 self-recorded videos captured with Ray-Ban Meta (Gen 2) smart glasses spanning diverse indoor and outdoor environments, and over 2,071 human-annotated question-answer pairs. It probes a model's observer-centric understanding with six different awareness tasks. Our comprehensive evaluation reveals a human-model performance gap of 37.66%, even with the best-performing MFM, Gemini 3 Flash. Beyond this gap, our in-depth analysis uncovers several notable findings; for example, while models can exploit partial geometric cues in egocentric videos, they often fail to infer a coherent camera geometry, leading to systematic spatial reasoning errors. We position SAW-Bench as a benchmark for situated spatial intelligence, moving beyond passive observation to understanding physically grounded, observer-centric dynamics.

### 🤖 AI 总结

**一句话总结**：本文提出针对第一人称视角的“情境感知”评估基准SAW-Bench，揭示现有多模态基础模型在观察者中心空间推理上与人类存在巨大差距。

**研究动机**：现有多模态评测多关注场景内物体之间的空间关系，而很少考察相机/观察者自身的视角、姿态与运动相关的推理能力，因此难以全面衡量模型在真实世界中的情境感知与行动相关理解。

**核心方法**：作者构建SAW-Bench基准：使用Ray-Ban Meta智能眼镜在多种室内外环境中录制786段真实第一人称视频，人工标注2071个与观察者相关的问答样本，覆盖六类情境感知任务，并系统评测包括Gemini 3 Flash在内的多种多模态基础模型表现。

**主要结论**：实验显示最强模型与人类之间仍有约37.66%的性能差距，模型虽能利用部分几何线索，但难以形成完整的相机几何与连贯空间表征，导致系统性空间推理错误，表明需要专门面向观察者中心、具身化情境智能的新方法与训练范式。

**关键词**：多模态大模型, 深度学习, 神经网络, agent, 观察者视角理解, 自我定位, 空间推理评测, 第一人称视频, 情境感知基准, 人机性能差距分析

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16682v1) | [下载PDF](https://arxiv.org/pdf/2602.16682v1.pdf)

---

## [12. VETime: Vision Enhanced Zero-Shot Time Series Anomaly Detection](https://arxiv.org/abs/2602.16681v1)

**作者**：Yingyuan Yang, Tian Lan, Yifei Gao 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-18

### 📄 论文摘要

Time-series anomaly detection (TSAD) requires identifying both immediate Point Anomalies and long-range Context Anomalies. However, existing foundation models face a fundamental trade-off: 1D temporal models provide fine-grained pointwise localization but lack a global contextual perspective, while 2D vision-based models capture global patterns but suffer from information bottlenecks due to a lack of temporal alignment and coarse-grained pointwise detection. To resolve this dilemma, we propose VETime, the first TSAD framework that unifies temporal and visual modalities through fine-grained visual-temporal alignment and dynamic fusion. VETime introduces a Reversible Image Conversion and a Patch-Level Temporal Alignment module to establish a shared visual-temporal timeline, preserving discriminative details while maintaining temporal sensitivity. Furthermore, we design an Anomaly Window Contrastive Learning mechanism and a Task-Adaptive Multi-Modal Fusion to adaptively integrate the complementary perceptual strengths of both modalities. Extensive experiments demonstrate that VETime significantly outperforms state-of-the-art models in zero-shot scenarios, achieving superior localization precision with lower computational overhead than current vision-based approaches. Code available at: https://github.com/yyyangcoder/VETime.

### 🤖 AI 总结

**一句话总结**：VETime 提出一个统一时序与视觉模态的零样本时间序列异常检测框架，在保持精细点级定位的同时获得全局上下文感知。

**研究动机**：现有1D时序模型缺乏全局上下文，而2D视觉模型又因时间对齐不足和信息瓶颈难以精细定位异常，二者存在根本性权衡，限制了零样本异常检测效果。

**核心方法**：VETime 通过可逆图像转换和补丁级时间对齐建立共享的视觉-时间轴，并结合异常窗口对比学习与任务自适应多模态融合，以动态整合时序和视觉两种感知优势。

**主要结论**：实验表明 VETime 在零样本时间序列异常检测任务上显著优于现有方法，实现更高的异常定位精度和更低的计算开销，其代码已开源便于复现与扩展。

**关键词**：深度学习, 神经网络, 多模态对齐, 时间序列异常检测, 零样本检测, 对比学习, 视觉时间融合, 可逆图像转换, 时间片对齐, 多模态融合, context

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16681v1) | [下载PDF](https://arxiv.org/pdf/2602.16681v1.pdf)

---

## [13. PredMapNet: Future and Historical Reasoning for Consistent Online HD Vectorized Map Construction](https://arxiv.org/abs/2602.16669v1)

**作者**：Bo Lang, Nirav Savaliya, Zhihao Zheng 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-18

### 📄 论文摘要

High-definition (HD) maps are crucial to autonomous driving, providing structured representations of road elements to support navigation and planning. However, existing query-based methods often employ random query initialization and depend on implicit temporal modeling, which lead to temporal inconsistencies and instabilities during the construction of a global map. To overcome these challenges, we introduce a novel end-to-end framework for consistent online HD vectorized map construction, which jointly performs map instance tracking and short-term prediction. First, we propose a Semantic-Aware Query Generator that initializes queries with spatially aligned semantic masks to capture scene-level context globally. Next, we design a History Rasterized Map Memory to store fine-grained instance-level maps for each tracked instance, enabling explicit historical priors. A History-Map Guidance Module then integrates rasterized map information into track queries, improving temporal continuity. Finally, we propose a Short-Term Future Guidance module to forecast the immediate motion of map instances based on the stored history trajectories. These predicted future locations serve as hints for tracked instances to further avoid implausible predictions and keep temporal consistency. Extensive experiments on the nuScenes and Argoverse2 datasets demonstrate that our proposed method outperforms state-of-the-art (SOTA) methods with good efficiency.

### 🤖 AI 总结

**一句话总结**：PredMapNet 提出一个结合历史跟踪与短期预测的端到端框架，实现在线高清矢量地图的时序一致构建。

**研究动机**：现有基于查询的HD地图构建方法采用随机查询初始化且仅做隐式时间建模，导致全局地图在时间上不稳定、元素不连续，难以满足自动驾驶对可靠时空一致地图的需求。

**核心方法**：方法包括：1）使用语义感知查询生成器，以空间对齐的语义掩码初始化查询获取全局场景语义；2）构建历史栅格化地图记忆，显式存储每个实例的精细地图；3）通过历史地图引导模块将栅格化信息融合进跟踪查询以增强时间连续性；4）利用短期未来引导模块基于历史轨迹预测实例的短期运动，将未来位置作为先验约束避免不合理预测。

**主要结论**：在 nuScenes 和 Argoverse2 上，PredMapNet 在精度和时序一致性方面均优于现有SOTA方法，同时保持较好推理效率，验证了引入显式历史记忆与短期预测对在线HD矢量地图构建的有效性。

**关键词**：深度学习, 神经网络, transformer, 语义感知查询, 矢量化高清地图, 时序一致性建图, 历史轨迹记忆, 短期未来预测, 自动驾驶场景理解, 端到端在线建图

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16669v1) | [下载PDF](https://arxiv.org/pdf/2602.16669v1.pdf)

---

## [14. Unpaired Image-to-Image Translation via a Self-Supervised Semantic Bridge](https://arxiv.org/abs/2602.16664v1)

**作者**：Jiaming Liu, Felix Petersen, Yunhe Gao 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-18

### 📄 论文摘要

Adversarial diffusion and diffusion-inversion methods have advanced unpaired image-to-image translation, but each faces key limitations. Adversarial approaches require target-domain adversarial loss during training, which can limit generalization to unseen data, while diffusion-inversion methods often produce low-fidelity translations due to imperfect inversion into noise-latent representations. In this work, we propose the Self-Supervised Semantic Bridge (SSB), a versatile framework that integrates external semantic priors into diffusion bridge models to enable spatially faithful translation without cross-domain supervision. Our key idea is to leverage self-supervised visual encoders to learn representations that are invariant to appearance changes but capture geometric structure, forming a shared latent space that conditions the diffusion bridges. Extensive experiments show that SSB outperforms strong prior methods for challenging medical image synthesis in both in-domain and out-of-domain settings, and extends easily to high-quality text-guided editing.

### 🤖 AI 总结

**一句话总结**：本文提出自监督语义桥接(SSB)框架，将自监督视觉编码器提供的几何一致语义空间与扩散桥模型结合，实现无需成对数据的高保真跨域图像翻译。

**研究动机**：现有无配对图像翻译方法中，对抗式方法依赖目标域判别器，泛化性差；扩散反演方法又因噪声潜空间反演不准导致细节和结构失真，尤其在医疗图像等高要求场景表现不足。

**核心方法**：利用自监督视觉编码器学习对外观变化不敏感但几何结构一致的共享语义潜空间，以此作为条件输入扩散桥模型，在无跨域监督下实现结构保真的图像到图像转换，并可扩展到文本引导编辑。

**主要结论**：在多种困难医疗图像合成任务中，SSB在域内与域外测试均优于强基线，并展示了良好的泛化性与结构一致性，同时证明该框架可自然扩展到高质量的文本驱动图像编辑。

**关键词**：扩散模型, 自监督表示学习, 语义嵌入, 无配对图像翻译, 跨域图像合成, 医学影像合成, 文本引导图像编辑, diffusion

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16664v1) | [下载PDF](https://arxiv.org/pdf/2602.16664v1.pdf)

---

## [15. Arc2Morph: Identity-Preserving Facial Morphing with Arc2Face](https://arxiv.org/abs/2602.16569v1)

**作者**：Nicolò Di Domenico, Annalisa Franco, Matteo Ferrara 等 4 位作者  
**分类**：cs.CV, cs.CR  
**发布时间**：2026-02-18

### 📄 论文摘要

Face morphing attacks are widely recognized as one of the most challenging threats to face recognition systems used in electronic identity documents. These attacks exploit a critical vulnerability in passport enrollment procedures adopted by many countries, where the facial image is often acquired without a supervised live capture process. In this paper, we propose a novel face morphing technique based on Arc2Face, an identity-conditioned face foundation model capable of synthesizing photorealistic facial images from compact identity representations. We demonstrate the effectiveness of the proposed approach by comparing the morphing attack potential metric on two large-scale sequestered face morphing attack detection datasets against several state-of-the-art morphing methods, as well as on two novel morphed face datasets derived from FEI and ONOT. Experimental results show that the proposed deep learning-based approach achieves a morphing attack potential comparable to that of landmark-based techniques, which have traditionally been regarded as the most challenging. These findings confirm the ability of the proposed method to effectively preserve and manage identity information during the morph generation process.

### 🤖 AI 总结

**一句话总结**：本文提出基于Arc2Face的Arc2Morph方法，在保持多主体身份特征的同时生成高攻击力的面部伪造图像，对现有人脸识别系统构成严重威胁。

**研究动机**：电子身份证和护照采集流程中缺乏实时活体监督，使得攻击者可以用融合多人的人脸图像绕过识别系统，因此需要更逼真且身份信息可控的变脸生成方法来评估与强化防御。

**核心方法**：利用Arc2Face这一身份条件生成模型，将多个人的紧凑身份表征在特征空间中融合，再由模型生成高保真、同时保留多主体身份特征的伪造人脸图像，并在多种数据集上与多种现有变脸技术进行对比。

**主要结论**：实验表明，Arc2Morph在两个大规模保留数据集和两个新构建数据集上取得与传统关键点（landmark）方法相当的高“攻击潜力”，验证了其在生成同时保留和管理多重身份信息的伪造人脸方面的有效性与威胁性。

**关键词**：深度学习, 人脸识别, 生成式模型, 神经网络, 特征嵌入, 人脸伪造检测, 身份表征, 人证合一验证, 电子证件安全, deep learning

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16569v1) | [下载PDF](https://arxiv.org/pdf/2602.16569v1.pdf)

---

## [16. Let's Split Up: Zero-Shot Classifier Edits for Fine-Grained Video Understanding](https://arxiv.org/abs/2602.16545v1)

**作者**：Kaiting Liu, Hazel Doughty  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-02-18

### 📄 论文摘要

Video recognition models are typically trained on fixed taxonomies which are often too coarse, collapsing distinctions in object, manner or outcome under a single label. As tasks and definitions evolve, such models cannot accommodate emerging distinctions and collecting new annotations and retraining to accommodate such changes is costly. To address these challenges, we introduce category splitting, a new task where an existing classifier is edited to refine a coarse category into finer subcategories, while preserving accuracy elsewhere. We propose a zero-shot editing method that leverages the latent compositional structure of video classifiers to expose fine-grained distinctions without additional data. We further show that low-shot fine-tuning, while simple, is highly effective and benefits from our zero-shot initialization. Experiments on our new video benchmarks for category splitting demonstrate that our method substantially outperforms vision-language baselines, improving accuracy on the newly split categories without sacrificing performance on the rest. Project page: https://kaitingliu.github.io/Category-Splitting/.

### 🤖 AI 总结

**一句话总结**：本文提出“类别拆分”任务，并通过零样本编辑现有视频分类器，在无需额外标注的情况下把粗粒度类别细化为子类别，同时保持其他类别性能不降。

**研究动机**：现有视频识别模型依赖固定且粗糙的标签体系，将不同物体、动作方式或结果混为一谈，难以适应不断演化的任务需求，而重新标注与训练成本高昂。

**核心方法**：作者提出类别拆分任务，并利用视频分类器内部潜在的组合结构进行零样本模型编辑，将一个粗类别拆分为多个细粒度子类别；同时设计少样本微调方案，以零样本编辑结果作为初始化进一步提升细粒度识别效果。

**主要结论**：在新构建的视频类别拆分基准上，该方法相较视觉-语言基线显著提升新拆分子类的识别准确率，且基本不损失对原有其他类别的性能，少样本微调在零样本初始化基础上进一步增强了效果。

**关键词**：深度学习, 视频分类, 零样本学习, 类别细粒度划分, 模型编辑, 少样本微调, 视觉语言模型, 分类器可塑性, rag

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16545v1) | [下载PDF](https://arxiv.org/pdf/2602.16545v1.pdf)

---

## cs.LG

## [17. Knowledge-Embedded Latent Projection for Robust Representation Learning](https://arxiv.org/abs/2602.16709v1)

**作者**：Weijing Tang, Ming Yuan, Zongqi Xia 等 4 位作者  
**分类**：cs.LG, math.ST, stat.ME  
**发布时间**：2026-02-18

### 📄 论文摘要

Latent space models are widely used for analyzing high-dimensional discrete data matrices, such as patient-feature matrices in electronic health records (EHRs), by capturing complex dependence structures through low-dimensional embeddings. However, estimation becomes challenging in the imbalanced regime, where one matrix dimension is much larger than the other. In EHR applications, cohort sizes are often limited by disease prevalence or data availability, whereas the feature space remains extremely large due to the breadth of medical coding system. Motivated by the increasing availability of external semantic embeddings, such as pre-trained embeddings of clinical concepts in EHRs, we propose a knowledge-embedded latent projection model that leverages semantic side information to regularize representation learning. Specifically, we model column embeddings as smooth functions of semantic embeddings via a mapping in a reproducing kernel Hilbert space. We develop a computationally efficient two-step estimation procedure that combines semantically guided subspace construction via kernel principal component analysis with scalable projected gradient descent. We establish estimation error bounds that characterize the trade-off between statistical error and approximation error induced by the kernel projection. Furthermore, we provide local convergence guarantees for our non-convex optimization procedure. Extensive simulation studies and a real-world EHR application demonstrate the effectiveness of the proposed method.

### 🤖 AI 总结

**一句话总结**：本文提出一种将外部语义知识嵌入潜在空间的投影模型，在样本数远小于特征数的失衡场景下实现更稳健的表示学习。

**研究动机**：在电子健康记录等场景中，患者数量有限而特征（医疗编码）极多，传统潜在空间模型在这种高度失衡设定下估计不稳定，而又存在大量可利用的临床概念预训练语义嵌入尚未被有效整合。

**核心方法**：作者将列嵌入建模为语义嵌入在再生核Hilbert空间中的平滑函数，通过核PCA构造由语义指导的低维子空间，再结合投影梯度下降进行两步估计，并给出统计误差与核投影近似误差之间权衡的误差界以及非凸优化的局部收敛保证。

**主要结论**：仿真和真实EHR数据实验表明，该知识嵌入的潜在投影方法在小样本、大特征的失衡场景下能显著提升表示学习的准确性和稳健性，理论分析则展示了其在误差控制和收敛性质上的可靠性。

**关键词**：机器学习, 深度学习, 表示学习, 语义嵌入, 核方法, kPCA, 投影梯度下降, 电子健康记录, EHR表示学习, 鲁棒表征, 高维数据建模, embedding

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16709v1) | [下载PDF](https://arxiv.org/pdf/2602.16709v1.pdf)

---

## [18. Protecting the Undeleted in Machine Unlearning](https://arxiv.org/abs/2602.16697v1)

**作者**：Aloni Cohen, Refael Kohen, Kobbi Nissim 等 4 位作者  
**分类**：cs.LG, cs.DS  
**发布时间**：2026-02-18

### 📄 论文摘要

Machine unlearning aims to remove specific data points from a trained model, often striving to emulate "perfect retraining", i.e., producing the model that would have been obtained had the deleted data never been included. We demonstrate that this approach, and security definitions that enable it, carry significant privacy risks for the remaining (undeleted) data points. We present a reconstruction attack showing that for certain tasks, which can be computed securely without deletions, a mechanism adhering to perfect retraining allows an adversary controlling merely $ω(1)$ data points to reconstruct almost the entire dataset merely by issuing deletion requests. We survey existing definitions for machine unlearning, showing they are either susceptible to such attacks or too restrictive to support basic functionalities like exact summation. To address this problem, we propose a new security definition that specifically safeguards undeleted data against leakage caused by the deletion of other points. We show that our definition permits several essential functionalities, such as bulletin boards, summations, and statistical learning.

### 🤖 AI 总结

**一句话总结**：论文指出现有以“完美重训练”为目标的机器反遗忘定义会泄露未被删除样本隐私，并提出一种专门保护未删数据的新安全定义。

**研究动机**：现有机器反遗忘工作多以模拟“从未见过被删样本”的完美重训练为目标，却几乎未考虑此过程对剩余未删样本隐私造成的潜在泄露风险。

**核心方法**：作者构造了一类重构攻击：对满足完美重训练的机制，只需控制ω(1)个样本并多次发起删除请求，就能几乎重建整个训练数据；随后系统性分析既有反遗忘安全定义的不足，并在形式化模型下给出新定义，证明其既能抵抗此类攻击又支持公告板、求和与统计学习等功能。

**主要结论**：完美重训练作为机器反遗忘的安全目标在隐私上并不安全，现有定义要么易受重构攻击要么过于严格难以实用；新提出的“保护未删数据”的安全定义在可行性与隐私间提供了更合理折中，可安全支持若干关键数据分析与学习任务。

**关键词**：机器学习, 深度学习, 机器反学习, 模型删除, 数据隐私保护, 重构攻击, 安全定义, 统计学习, 隐私风险分析, agent

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16697v1) | [下载PDF](https://arxiv.org/pdf/2602.16697v1.pdf)

---

## [19. Retrieval-Augmented Foundation Models for Matched Molecular Pair Transformations to Recapitulate Medicinal Chemistry Intuition](https://arxiv.org/abs/2602.16684v1)

**作者**：Bo Pan, Peter Zhiping Zhang, Hao-Wei Pang 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-18

### 📄 论文摘要

Matched molecular pairs (MMPs) capture the local chemical edits that medicinal chemists routinely use to design analogs, but existing ML approaches either operate at the whole-molecule level with limited edit controllability or learn MMP-style edits from restricted settings and small models. We propose a variable-to-variable formulation of analog generation and train a foundation model on large-scale MMP transformations (MMPTs) to generate diverse variables conditioned on an input variable. To enable practical control, we develop prompting mechanisms that let the users specify preferred transformation patterns during generation. We further introduce MMPT-RAG, a retrieval-augmented framework that uses external reference analogs as contextual guidance to steer generation and generalize from project-specific series. Experiments on general chemical corpora and patent-specific datasets demonstrate improved diversity, novelty, and controllability, and show that our method recovers realistic analog structures in practical discovery scenarios.

### 🤖 AI 总结

**一句话总结**：本文提出基于大规模匹配分子对变换（MMPT）的检索增强基础模型，用可控与检索引导的方式自动生成符合药物化学直觉的分子类似物。

**研究动机**：现有分子生成方法要么在整分子层面缺乏精细“局部改造”控制，要么仅在小数据和受限场景学习有限的MMP式编辑，难以复现药物化学家在项目中的实际修饰策略。

**核心方法**：作者将类似物设计形式化为“变量到变量”的MMPT生成任务，在大规模MMP上训练基础模型，并引入可指定转化模式的提示机制与基于外部参考类似物的检索增强框架MMPT-RAG，以项目特异性的结构为条件引导生成。

**主要结论**：在通用化学语料和专利数据上，该方法在多样性、新颖性和可控性上优于现有方法，且能在真实药物发现场景中较好复现合理的类似物结构，体现出将药物化学直觉规模化建模的潜力。

**关键词**：深度学习, 神经网络, 生成式模型, 检索增强生成RAG, 分子生成, 药物发现, 匹配分子对, 基础模型, 条件生成, 化学空间探索

**评分**：43

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16684v1) | [下载PDF](https://arxiv.org/pdf/2602.16684v1.pdf)

---

## [20. Factorization Machine with Quadratic-Optimization Annealing for RNA Inverse Folding and Evaluation of Binary-Integer Encoding and Nucleotide Assignment](https://arxiv.org/abs/2602.16643v1)

**作者**：Shuta Kikuchi, Shu Tanaka  
**分类**：cs.LG, cond-mat.stat-mech  
**发布时间**：2026-02-18

### 📄 论文摘要

The RNA inverse folding problem aims to identify nucleotide sequences that preferentially adopt a given target secondary structure. While various heuristic and machine learning-based approaches have been proposed, many require a large number of sequence evaluations, which limits their applicability when experimental validation is costly. We propose a method to solve the problem using a factorization machine with quadratic-optimization annealing (FMQA). FMQA is a discrete black-box optimization method reported to obtain high-quality solutions with a limited number of evaluations. Applying FMQA to the problem requires converting nucleotides into binary variables. However, the influence of integer-to-nucleotide assignments and binary-integer encoding on the performance of FMQA has not been thoroughly investigated, even though such choices determine the structure of the surrogate model and the search landscape, and thus can directly affect solution quality. Therefore, this study aims both to establish a novel FMQA framework for RNA inverse folding and to analyze the effects of these assignments and encoding methods. We evaluated all 24 possible assignments of the four nucleotides to the ordered integers (0-3), in combination with four binary-integer encoding methods. Our results demonstrated that one-hot and domain-wall encodings outperform binary and unary encodings in terms of the normalized ensemble defect value. In domain-wall encoding, nucleotides assigned to the boundary integers (0 and 3) appeared with higher frequency. In the RNA inverse folding problem, assigning guanine and cytosine to these boundary integers promoted their enrichment in stem regions, which led to more thermodynamically stable secondary structures than those obtained with one-hot encoding.

### 🤖 AI 总结

**一句话总结**：本文基于因子分解机与退火式二次优化（FMQA）构建RNA反折叠求解框架，并系统比较不同二进制编码与碱基赋值策略对优化效果的影响。

**研究动机**：现有RNA反折叠方法往往需要大量序列评估，成本高且对离散优化与编码方式的系统分析不足，尤其是不同二进制编码与碱基→整数映射如何影响搜索景观与解质量。

**核心方法**：作者将RNA序列设计建模为FMQA的离散黑盒优化问题，穷举四种二进制编码（一位一元、域壁、普通二进制、unary）与24种碱基到0–3整数的赋值组合，在固定结构目标下比较优化得到的序列（以normalized ensemble defect评价）。

**主要结论**：一位一元编码和域壁编码显著优于普通二进制与unary编码；在域壁编码中，被赋值为边界整数0和3的碱基出现频率更高，将G、C映射到0和3可增强茎区GC富集、提升结构热稳定性，优于一位一元编码下的结果。

**关键词**：机器学习, 深度学习, 黑盒优化, 因子分解机, 离散优化, 序列设计, RNA反折叠, 二进制编码, machine learning

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16643v1) | [下载PDF](https://arxiv.org/pdf/2602.16643v1.pdf)

---

## [21. Optimizer choice matters for the emergence of Neural Collapse](https://arxiv.org/abs/2602.16642v1)

**作者**：Jim Zhao, Tin Sum Cheng, Wojciech Masarczyk 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-18

### 📄 论文摘要

Neural Collapse (NC) refers to the emergence of highly symmetric geometric structures in the representations of deep neural networks during the terminal phase of training. Despite its prevalence, the theoretical understanding of NC remains limited. Existing analyses largely ignore the role of the optimizer, thereby suggesting that NC is universal across optimization methods. In this work, we challenge this assumption and demonstrate that the choice of optimizer plays a critical role in the emergence of NC. The phenomenon is typically quantified through NC metrics, which, however, are difficult to track and analyze theoretically. To overcome this limitation, we introduce a novel diagnostic metric, NC0, whose convergence to zero is a necessary condition for NC. Using NC0, we provide theoretical evidence that NC cannot emerge under decoupled weight decay in adaptive optimizers, as implemented in AdamW. Concretely, we prove that SGD, SignGD with coupled weight decay (a special case of Adam), and SignGD with decoupled weight decay (a special case of AdamW) exhibit qualitatively different NC0 dynamics. Also, we show the accelerating effect of momentum on NC (beyond convergence of train loss) when trained with SGD, being the first result concerning momentum in the context of NC. Finally, we conduct extensive empirical experiments consisting of 3,900 training runs across various datasets, architectures, optimizers, and hyperparameters, confirming our theoretical results. This work provides the first theoretical explanation for optimizer-dependent emergence of NC and highlights the overlooked role of weight-decay coupling in shaping the implicit biases of optimizers.

### 🤖 AI 总结

**一句话总结**：论文表明“Neural Collapse”并非与优化器无关，而是强烈依赖于优化器形式，尤其是权重衰减是耦合还是解耦。

**研究动机**：现有对Neural Collapse的理论多数忽略优化器差异，默认其为普适现象，但在实践中不同优化器（如SGD与AdamW）表现出不同的几何结构，亟需统一的理论解释。

**核心方法**：作者提出一个新的诊断指标NC0，用其刻画Neural Collapse出现的必要条件，并在理论上对比分析SGD、带耦合权重衰减的SignGD（类Adam）和带解耦权重衰减的SignGD（类AdamW）的NC0动态行为，并辅以涵盖多数据集/结构/优化器/超参的3900次大规模实验验证。

**主要结论**：结果证明带解耦权重衰减的自适应优化器（如AdamW）在理论上无法自然产生Neural Collapse，而SGD及带动量的变体不仅更易产生Neural Collapse，动量还会加速其形成；权重衰减的耦合方式是优化器隐式偏置和NC涌现的关键因素。

**关键词**：深度学习, 神经网络, 优化器选择, 权重衰减耦合, 自适应优化算法, 动量加速训练, 表示学习几何结构, 训练隐式偏置, neural network

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16642v1) | [下载PDF](https://arxiv.org/pdf/2602.16642v1.pdf)

---

## [22. Almost Sure Convergence of Differential Temporal Difference Learning for Average Reward Markov Decision Processes](https://arxiv.org/abs/2602.16629v1)

**作者**：Ethan Blaser, Jiuqi Wang, Shangtong Zhang  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-18

### 📄 论文摘要

The average reward is a fundamental performance metric in reinforcement learning (RL) focusing on the long-run performance of an agent. Differential temporal difference (TD) learning algorithms are a major advance for average reward RL as they provide an efficient online method to learn the value functions associated with the average reward in both on-policy and off-policy settings. However, existing convergence guarantees require a local clock in learning rates tied to state visit counts, which practitioners do not use and does not extend beyond tabular settings. We address this limitation by proving the almost sure convergence of on-policy $n$-step differential TD for any $n$ using standard diminishing learning rates without a local clock. We then derive three sufficient conditions under which off-policy $n$-step differential TD also converges without a local clock. These results strengthen the theoretical foundations of differential TD and bring its convergence analysis closer to practical implementations.

### 🤖 AI 总结

**一句话总结**：本文证明了平均回报强化学习中差分TD算法在更接近实际使用的学习率设定下几乎必然收敛。

**研究动机**：以平均回报为目标的RL中，差分TD是高效的在线方法，但现有收敛性分析依赖与状态访问次数绑定的“本地时钟”学习率，既不实用也难以推广到非表格设置。

**核心方法**：作者在理论上分析任意n步差分TD，首先对在策略情形下使用全局递减学习率（无本地时钟）建立几乎必然收敛性证明，随后提出三类足够条件，使离策略n步差分TD在同样的无本地时钟设定下也可证明收敛。

**主要结论**：文章表明在标准的递减全局学习率下，n步在策略差分TD必然收敛，且在满足特定条件时离策略情形也能收敛，从而显著强化了差分TD的理论基础，并使收敛分析更贴近实际强化学习实现。

**关键词**：强化学习, 平均回报, 时序差分学习, 价值函数估计, 在线学习, 收敛性分析, 马尔可夫决策过程, n步TD算法, agent

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16629v1) | [下载PDF](https://arxiv.org/pdf/2602.16629v1.pdf)

---

## [23. Sequential Membership Inference Attacks](https://arxiv.org/abs/2602.16596v1)

**作者**：Thomas Michel, Debabrota Basu, Emilie Kaufmann  
**分类**：cs.LG, cs.CR, math.ST, stat.ML  
**发布时间**：2026-02-18

### 📄 论文摘要

Modern AI models are not static. They go through multiple updates in their lifecycles. Thus, exploiting the model dynamics to create stronger Membership Inference (MI) attacks and tighter privacy audits are timely questions. Though the literature empirically shows that using a sequence of model updates can increase the power of MI attacks, rigorous analysis of the `optimal' MI attacks is limited to static models with infinite samples. Hence, we develop an `optimal' MI attack, SeMI*, that uses the sequence of model updates to identify the presence of a target inserted at a certain update step. For the empirical mean computation, we derive the optimal power of SeMI*, while accessing a finite number of samples with or without privacy. Our results retrieve the existing asymptotic analysis. We observe that having access to the model sequence avoids the dilution of MI signals unlike the existing attacks on the final model, where the MI signal vanishes as training data accumulates. Furthermore, an adversary can use SeMI* to tune both the insertion time and the canary to yield tighter privacy audits. Finally, we conduct experiments across data distributions and models trained or fine-tuned with DP-SGD demonstrating that practical variants of SeMI* lead to tighter privacy audits than the baselines.

### 🤖 AI 总结

**一句话总结**：这篇论文提出并分析了一种利用模型多次更新序列的最优顺序成员推断攻击 SeMI*，在理论和实验上都比仅针对最终模型的传统攻击更强。

**研究动机**：现有成员推断研究多针对静态模型且依赖无限样本，现实中模型会多轮更新，且只看最终模型时隐私信号会随训练数据增多而被“稀释”，需要系统研究如何利用整个更新序列进行更有力的隐私攻击与审计。

**核心方法**：作者形式化“目标样本在某一轮被插入”的顺序成员推断问题，在经验均值计算场景下推导出利用模型更新序列的最优攻击策略 SeMI* 的检验统计量与统计功效，包括有限样本、带/不带差分隐私噪声的情况，并构造实际可实现的变体用于实验。

**主要结论**：理论上，SeMI* 能在有限样本下达到最优功效并收敛到既有的渐近结果，同时利用更新序列可避免传统“只看最终模型”时信号随数据量增大而消失；实践上，在多种数据分布和使用 DP-SGD 训练或微调的模型上，SeMI* 的实现版本给出的隐私审计显著比现有基线更紧。

**关键词**：机器学习, 深度学习, 神经网络, 模型更新序列, 成员推断攻击, 差分隐私训练, DP-SGD隐私审计, 目标插入检测, 最优攻击策略, agent

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16596v1) | [下载PDF](https://arxiv.org/pdf/2602.16596v1.pdf)

---

## [24. AIFL: A Global Daily Streamflow Forecasting Model Using Deterministic LSTM Pre-trained on ERA5-Land and Fine-tuned on IFS](https://arxiv.org/abs/2602.16579v1)

**作者**：Maria Luisa Taccari, Kenza Tazi, Oisín M. Morrison 等 10 位作者  
**分类**：cs.LG, cs.AI, physics.app-ph  
**发布时间**：2026-02-18

### 📄 论文摘要

Reliable global streamflow forecasting is essential for flood preparedness and water resource management, yet data-driven models often suffer from a performance gap when transitioning from historical reanalysis to operational forecast products. This paper introduces AIFL (Artificial Intelligence for Floods), a deterministic LSTM-based model designed for global daily streamflow forecasting. Trained on 18,588 basins curated from the CARAVAN dataset, AIFL utilises a novel two-stage training strategy to bridge the reanalysis-to-forecast domain shift. The model is first pre-trained on 40 years of ERA5-Land reanalysis (1980-2019) to capture robust hydrological processes, then fine-tuned on operational Integrated Forecasting System (IFS) control forecasts (2016-2019) to adapt to the specific error structures and biases of operational numerical weather prediction. To our knowledge, this is the first global model trained end-to-end within the CARAVAN ecosystem. On an independent temporal test set (2021-2024), AIFL achieves high predictive skill with a median modified Kling-Gupta Efficiency (KGE') of 0.66 and a median Nash-Sutcliffe Efficiency (NSE) of 0.53. Benchmarking results show that AIFL is highly competitive with current state-of-the-art global systems, achieving comparable accuracy while maintaining a transparent and reproducible forcing pipeline. The model demonstrates exceptional reliability in extreme-event detection, providing a streamlined and operationally robust baseline for the global hydrological community.

### 🤖 AI 总结

**一句话总结**：AIFL 是一个基于确定性 LSTM 的全球日尺度径流预报模型，通过在 ERA5-Land 预训练并在 IFS 预报上微调，有效提升从再分析到业务预报场景的预测性能。

**研究动机**：现有数据驱动径流模型在从再分析数据转到业务数值预报产品时存在明显性能衰减，影响全球洪水预警和水资源管理的可靠性。

**核心方法**：在 CARAVAN 数据集中选取 18,588 个流域，先用 40 年 ERA5-Land 再分析数据对 LSTM 进行预训练以学习稳健水文过程，再用 2016–2019 年 IFS 控制预报进行微调，从而适配业务模式的误差结构和偏差，并在 2021–2024 年独立时段上评估性能。

**主要结论**：AIFL 在独立测试集上取得中位 KGE' 为 0.66、NSE 为 0.53 的高预报技巧，整体效果与当前最先进全球系统相当，且在极端事件识别上表现可靠，为全球水文界提供了透明、可复现的基线方案。

**关键词**：机器学习, 深度学习, 神经网络, LSTM, 时间序列预测, 水文预报, 洪水预警, 全球流量预测, 再分析数据预训练, 领域自适应, artificial intelligence

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16579v1) | [下载PDF](https://arxiv.org/pdf/2602.16579v1.pdf)

---

## [25. MoDE-Boost: Boosting Shared Mobility Demand with Edge-Ready Prediction Models](https://arxiv.org/abs/2602.16573v1)

**作者**：Antonios Tziorvas, George S. Theodoropoulos, Yannis Theodoridis  
**分类**：cs.LG  
**发布时间**：2026-02-18

### 📄 论文摘要

Urban demand forecasting plays a critical role in optimizing routing, dispatching, and congestion management within Intelligent Transportation Systems. By leveraging data fusion and analytics techniques, traffic demand forecasting serves as a key intermediate measure for identifying emerging spatial and temporal demand patterns. In this paper, we tackle this challenge by proposing two gradient boosting model variations, one for classiffication and one for regression, both capable of generating demand forecasts at various temporal horizons, from 5 minutes up to one hour. Our overall approach effectively integrates temporal and contextual features, enabling accurate predictions that are essential for improving the efficiency of shared (micro-) mobility services. To evaluate its effectiveness, we utilize open shared mobility data derived from e-scooter and e-bike networks in five metropolitan areas. These real-world datasets allow us to compare our approach with state-of-the-art methods as well as a Generative AI-based model, demonstrating its effectiveness in capturing the complexities of modern urban mobility. Ultimately, our methodology offers novel insights on urban micro-mobility management, helping to tackle the challenges arising from rapid urbanization and thus, contributing to more sustainable, efficient, and livable cities.

### 🤖 AI 总结

**一句话总结**：本文提出两种梯度提升模型（分类与回归），在边缘设备上高效预测共享微出行在5分钟到1小时多时间尺度上的需求，并在多城市真实数据上优于多种对比方法。

**研究动机**：随着城市共享电动车、共享单车等微出行迅速发展，精准预测不同时间与区域的出行需求对于调度车辆、缓解拥堵和提升系统效率至关重要，尤其需要既准确又能在边缘侧部署的轻量级模型。

**核心方法**：作者设计了名为 MoDE-Boost 的两种梯度提升变体（一个用于分类，一个用于回归），融合历史时序信息和多种上下文特征（如时间、空间与环境因素），在5分钟至1小时多时间粒度上进行需求预测，并利用五个大城市的共享电动滑板车/电动自行车公开数据，与现有方法和一个生成式AI模型进行系统对比。

**主要结论**：实验结果表明，MoDE-Boost 能更好捕捉城市微出行需求的时空复杂性，在多城市数据上取得优于现有方法和生成式AI基线的预测表现，适合部署在边缘环境中，为共享微出行运维与城市交通管理提供更高效和可持续的决策支持。

**关键词**：机器学习, 深度学习, 生成式模型, 梯度提升模型, 共享出行需求预测, 时空特征融合, 边缘计算部署, 智能交通系统, 微出行调度, generative

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16573v1) | [下载PDF](https://arxiv.org/pdf/2602.16573v1.pdf)

---

## [26. Steering diffusion models with quadratic rewards: a fine-grained analysis](https://arxiv.org/abs/2602.16570v1)

**作者**：Ankur Moitra, Andrej Risteski, Dhruv Rohatgi  
**分类**：cs.LG, cs.DS  
**发布时间**：2026-02-18

### 📄 论文摘要

Inference-time algorithms are an emerging paradigm in which pre-trained models are used as subroutines to solve downstream tasks. Such algorithms have been proposed for tasks ranging from inverse problems and guided image generation to reasoning. However, the methods currently deployed in practice are heuristics with a variety of failure modes -- and we have very little understanding of when these heuristics can be efficiently improved.   In this paper, we consider the task of sampling from a reward-tilted diffusion model -- that is, sampling from $p^{\star}(x) \propto p(x) \exp(r(x))$ -- given a reward function $r$ and pre-trained diffusion oracle for $p$. We provide a fine-grained analysis of the computational tractability of this task for quadratic rewards $r(x) = x^\top A x + b^\top x$. We show that linear-reward tilts are always efficiently sampleable -- a simple result that seems to have gone unnoticed in the literature. We use this as a building block, along with a conceptually new ingredient -- the Hubbard-Stratonovich transform -- to provide an efficient algorithm for sampling from low-rank positive-definite quadratic tilts, i.e. $r(x) = x^\top A x$ where $A$ is positive-definite and of rank $O(1)$. For negative-definite tilts, i.e. $r(x) = - x^\top A x$ where $A$ is positive-definite, we prove that the problem is intractable even if $A$ is of rank 1 (albeit with exponentially-large entries).

### 🤖 AI 总结

**一句话总结**：论文从理论上分析了在扩散模型上施加二次奖励（reward tilt）进行采样的可计算性边界，并给出对特定形式奖励的高效算法与不可能结果。

**研究动机**：现有基于预训练扩散模型的推理时算法多是启发式方法，缺乏关于“在给定奖励函数下能否高效重采样分布”的系统理解，尤其是当奖励是常用的二次形式时。

**核心方法**：形式化问题为从 p*(x) ∝ p(x)exp(r(x)) 采样；先证明线性奖励 tilt 总是可高效采样，然后引入 Hubbard-Stratonovich 变换，将低秩正定二次奖励分解为若干线性 tilt 的组合，从而构造高效采样算法，并对负定二次 tilt 进行复杂度下界分析。

**主要结论**：1）线性奖励 tilt 在扩散模型下始终可高效采样；2）对秩为 O(1) 的正定低秩二次奖励，可用 Hubbard-Stratonovich 变换得到高效采样算法；3）对于负定二次 tilt，即便只是秩 1 且系数指数级，也可以证明采样问题在计算上是不可行，从而刻画了扩散模型在二次奖励 steering 下的可行与不可行边界。

**关键词**：扩散模型, diffusion, 生成式, 奖励模型, 推理时算法, 采样算法, 低秩矩阵, 正定二次型, 图像生成

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16570v1) | [下载PDF](https://arxiv.org/pdf/2602.16570v1.pdf)

---

## [27. Illustration of Barren Plateaus in Quantum Computing](https://arxiv.org/abs/2602.16558v1)

**作者**：Gerhard Stenzel, Tobias Rohe, Michael Kölle 等 6 位作者  
**分类**：cs.LG, quant-ph  
**发布时间**：2026-02-18

### 📄 论文摘要

Variational Quantum Circuits (VQCs) have emerged as a promising paradigm for quantum machine learning in the NISQ era. While parameter sharing in VQCs can reduce the parameter space dimensionality and potentially mitigate the barren plateau phenomenon, it introduces a complex trade-off that has been largely overlooked. This paper investigates how parameter sharing, despite creating better global optima with fewer parameters, fundamentally alters the optimization landscape through deceptive gradients -- regions where gradient information exists but systematically misleads optimizers away from global optima. Through systematic experimental analysis, we demonstrate that increasing degrees of parameter sharing generate more complex solution landscapes with heightened gradient magnitudes and measurably higher deceptiveness ratios. Our findings reveal that traditional gradient-based optimizers (Adam, SGD) show progressively degraded convergence as parameter sharing increases, with performance heavily dependent on hyperparameter selection. We introduce a novel gradient deceptiveness detection algorithm and a quantitative framework for measuring optimization difficulty in quantum circuits, establishing that while parameter sharing can improve circuit expressivity by orders of magnitude, this comes at the cost of significantly increased landscape deceptiveness. These insights provide important considerations for quantum circuit design in practical applications, highlighting the fundamental mismatch between classical optimization strategies and quantum parameter landscapes shaped by parameter sharing.

### 🤖 AI 总结

**一句话总结**：论文系统研究了变分量子电路中参数共享对优化景观的影响，发现其虽能提升表达能力、缓解平坦高原，但会显著增加“欺骗性梯度”导致优化困难。

**研究动机**：虽然参数共享被认为可减少参数维度并缓解 barren plateau 问题，但其如何改变量子电路的损失与梯度景观、以及对经典优化器的真实影响仍缺乏系统理解。

**核心方法**：作者构造不同程度参数共享的变分量子电路，通过大规模数值实验分析梯度分布、解空间结构与收敛行为，并提出梯度欺骗性检测算法和量化优化难度的指标体系。

**主要结论**：随着参数共享程度提高，电路解空间更复杂、梯度幅值增大但欺骗性比例上升，传统梯度优化器（Adam、SGD）收敛性能显著恶化并高度依赖超参数；参数共享在提升电路表达能力的同时引入严重的景观欺骗性，凸显经典优化策略与此类量子参数景观之间的根本错配，需要在电路设计与优化方法上统筹权衡。

**关键词**：量子机器学习, 深度学习, 神经网络, variational quantum circuits, 参数共享优化, 梯度欺骗检测, 优化景观复杂度, 量子电路设计, 梯度下降收敛性, machine learning

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16558v1) | [下载PDF](https://arxiv.org/pdf/2602.16558v1.pdf)

---

## [28. RIDER: 3D RNA Inverse Design with Reinforcement Learning-Guided Diffusion](https://arxiv.org/abs/2602.16548v1)

**作者**：Tianmeng Hu, Yongzheng Cui, Biao Luo 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-18

### 📄 论文摘要

The inverse design of RNA three-dimensional (3D) structures is crucial for engineering functional RNAs in synthetic biology and therapeutics. While recent deep learning approaches have advanced this field, they are typically optimized and evaluated using native sequence recovery, which is a limited surrogate for structural fidelity, since different sequences can fold into similar 3D structures and high recovery does not necessarily indicate correct folding. To address this limitation, we propose RIDER, an RNA Inverse DEsign framework with Reinforcement learning that directly optimizes for 3D structural similarity. First, we develop and pre-train a GNN-based generative diffusion model conditioned on the target 3D structure, achieving a 9% improvement in native sequence recovery over state-of-the-art methods. Then, we fine-tune the model with an improved policy gradient algorithm using four task-specific reward functions based on 3D self-consistency metrics. Experimental results show that RIDER improves structural similarity by over 100% across all metrics and discovers designs that are distinct from native sequences.

### 🤖 AI 总结

**一句话总结**：RIDER 提出一种结合扩散模型与强化学习的3D RNA反向设计框架，直接优化生成序列的三维结构相似度而非仅仅追求原生序列还原率。

**研究动机**：现有RNA反向设计方法多以“原生序列恢复率”作为优化和评估目标，但同一3D结构可对应多种不同序列，高恢复率并不等价于正确折叠，因此需要直接针对三维结构保真度进行优化。

**核心方法**：作者首先构建并预训练一个以目标3D结构为条件的GNN扩散生成模型，用于生成RNA序列；随后引入改进的策略梯度算法，以四个基于3D自洽性的任务奖励函数对模型进行强化学习微调，从而使生成序列在三维结构上更加接近目标构型。

**主要结论**：实验表明，RIDER在原生序列恢复率上相比现有方法提升约9%，并在多种三维结构相似性指标上实现超过100%的提升，同时能够产生与原生序列明显不同但能折叠到相似3D结构的RNA设计。

**关键词**：深度学习, 扩散模型, 生成式模型, 强化学习, 奖励模型, 逆向分子设计, RNA三维结构设计, GNN建模, deep learning

**评分**：41

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16548v1) | [下载PDF](https://arxiv.org/pdf/2602.16548v1.pdf)

---

## [29. Vulnerability Analysis of Safe Reinforcement Learning via Inverse Constrained Reinforcement Learning](https://arxiv.org/abs/2602.16543v1)

**作者**：Jialiang Fan, Shixiong Jiang, Mengyu Liu 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-18

### 📄 论文摘要

Safe reinforcement learning (Safe RL) aims to ensure policy performance while satisfying safety constraints. However, most existing Safe RL methods assume benign environments, making them vulnerable to adversarial perturbations commonly encountered in real-world settings. In addition, existing gradient-based adversarial attacks typically require access to the policy's gradient information, which is often impractical in real-world scenarios. To address these challenges, we propose an adversarial attack framework to reveal vulnerabilities of Safe RL policies. Using expert demonstrations and black-box environment interaction, our framework learns a constraint model and a surrogate (learner) policy, enabling gradient-based attack optimization without requiring the victim policy's internal gradients or the ground-truth safety constraints. We further provide theoretical analysis establishing feasibility and deriving perturbation bounds. Experiments on multiple Safe RL benchmarks demonstrate the effectiveness of our approach under limited privileged access.

### 🤖 AI 总结

**一句话总结**：论文提出一种黑盒对抗攻击框架，通过逆约束强化学习暴露安全强化学习策略在现实对抗扰动下的脆弱性。

**研究动机**：现有安全强化学习方法通常假设环境良性，且多数对抗攻击需要访问策略梯度，在真实场景中不现实，因此需要在有限访问、未知约束的条件下系统性评估并攻击Safe RL策略。

**核心方法**：利用专家示例和与环境的黑盒交互，首先通过逆约束强化学习学习环境的约束模型和代理策略，再在该代理上进行梯度驱动的对抗扰动优化，并给出可行性与扰动大小的理论界。

**主要结论**：实验表明，在多种安全强化学习基准上，该黑盒攻击在仅有有限特权信息的情况下仍能有效破坏安全策略的约束满足性，揭示当前Safe RL方法在对抗环境下存在显著安全隐患。

**关键词**：强化学习, 安全强化学习, 深度学习, reward model, 逆向约束强化学习, 对抗攻击, 黑盒环境交互, 策略鲁棒性分析, 安全约束建模, 专家示范学习

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16543v1) | [下载PDF](https://arxiv.org/pdf/2602.16543v1.pdf)

---

## [30. Transfer Learning of Linear Regression with Multiple Pretrained Models: Benefiting from More Pretrained Models via Overparameterization Debiasing](https://arxiv.org/abs/2602.16531v1)

**作者**：Daniel Boharon, Yehuda Dar  
**分类**：cs.LG  
**发布时间**：2026-02-18

### 📄 论文摘要

We study transfer learning for a linear regression task using several least-squares pretrained models that can be overparameterized.   We formulate the target learning task as optimization that minimizes squared errors on the target dataset with penalty on the distance of the learned model from the pretrained models. We analytically formulate the test error of the learned target model and provide the corresponding empirical evaluations.   Our results elucidate when using more pretrained models can improve transfer learning. Specifically, if the pretrained models are overparameterized, using sufficiently many of them is important for beneficial transfer learning. However, the learning may be compromised by overparameterization bias of pretrained models, i.e., the minimum $\ell_2$-norm solution's restriction to a small subspace spanned by the training examples in the high-dimensional parameter space. We propose a simple debiasing via multiplicative correction factor that can reduce the overparameterization bias and leverage more pretrained models to learn a target predictor.

### 🤖 AI 总结

**一句话总结**：本文研究线性回归场景下如何利用多个（可能过参数化的）预训练最小二乘模型进行迁移学习，并通过去偏策略从更多预训练模型中获益。

**研究动机**：在过参数化线性模型广泛存在的背景下，现有迁移学习通常只利用少量或单个预训练模型，尚不清楚在存在过参数化偏差时，如何系统地利用“更多”预训练模型来提高目标任务的泛化性能。

**核心方法**：将目标任务形式化为：在目标数据上最小化平方误差，同时加上与多个预训练模型参数距离的惩罚项；在此框架下推导目标模型的测试误差解析式，并提出通过一个简单的乘性修正因子对预训练权重进行去偏，以缓解过参数化带来的子空间限制。

**主要结论**：理论与实验表明：当预训练模型是过参数化时，只有在数量足够多时多模型迁移才明显受益，但其效果会受到最小ℓ2范数解所带来的过参数化偏差限制；通过提出的乘性去偏修正，可以显著减弱这一偏差，使更多预训练模型在目标任务中被更有效地整合，从而提升迁移学习性能。

**关键词**：机器学习, 迁移学习, 线性回归, 预训练模型, 过参数化去偏, 泛化误差分析, 正则化优化, 高维统计理论, rag

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16531v1) | [下载PDF](https://arxiv.org/pdf/2602.16531v1.pdf)

---

