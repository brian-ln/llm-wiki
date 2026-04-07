 Mixture of experts - Wikipedia                        

[Jump to content](#bodyContent)

 Main menu

Main menu

move to sidebar hide

Navigation

-   [Main page](/wiki/Main_Page "Visit the main page [z]")
-   [Contents](/wiki/Wikipedia:Contents "Guides to browsing Wikipedia")
-   [Current events](/wiki/Portal:Current_events "Articles related to current events")
-   [Random article](/wiki/Special:Random "Visit a randomly selected article [x]")
-   [About Wikipedia](/wiki/Wikipedia:About "Learn about Wikipedia and how it works")
-   [Contact us](//en.wikipedia.org/wiki/Wikipedia:Contact_us "How to contact Wikipedia")

Contribute

-   [Help](/wiki/Help:Contents "Guidance on how to use and edit Wikipedia")
-   [Learn to edit](/wiki/Help:Introduction "Learn how to edit Wikipedia")
-   [Community portal](/wiki/Wikipedia:Community_portal "The hub for editors")
-   [Recent changes](/wiki/Special:RecentChanges "A list of recent changes to Wikipedia [r]")
-   [Upload file](/wiki/Wikipedia:File_upload_wizard "Add images or other media for use on Wikipedia")
-   [Special pages](/wiki/Special:SpecialPages "A list of all special pages [q]")

  [![](/static/images/icons/enwiki-25.svg) ![Wikipedia](/static/images/mobile/copyright/wikipedia-wordmark-en-25.svg) ![The Free Encyclopedia](/static/images/mobile/copyright/wikipedia-tagline-en-25.svg)](/wiki/Main_Page)

[Search](/wiki/Special:Search "Search Wikipedia [f]")

Search

 Appearance

-   [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
-   [Create account](/w/index.php?title=Special:CreateAccount&returnto=Mixture+of+experts "You are encouraged to create an account and log in; however, it is not mandatory")
-   [Log in](/w/index.php?title=Special:UserLogin&returnto=Mixture+of+experts "You're encouraged to log in; however, it's not mandatory. [o]")

 Personal tools

-   [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
-   [Create account](/w/index.php?title=Special:CreateAccount&returnto=Mixture+of+experts "You are encouraged to create an account and log in; however, it is not mandatory")
-   [Log in](/w/index.php?title=Special:UserLogin&returnto=Mixture+of+experts "You're encouraged to log in; however, it's not mandatory. [o]")

## Contents

move to sidebar hide

-   [
    
    (Top)
    
    ](#)
-   [
    
    1 Basic theory
    
    ](#Basic_theory)Toggle Basic theory subsection
    -   [
        
        1.1 Meta-pi network
        
        ](#Meta-pi_network)
        
    -   [
        
        1.2 Adaptive mixtures of local experts
        
        ](#Adaptive_mixtures_of_local_experts)
        
    -   [
        
        1.3 Hierarchical MoE
        
        ](#Hierarchical_MoE)
        
    -   [
        
        1.4 Variants
        
        ](#Variants)
        
-   [
    
    2 Deep learning
    
    ](#Deep_learning)Toggle Deep learning subsection
    -   [
        
        2.1 Sparsely-gated MoE layer
        
        ](#Sparsely-gated_MoE_layer)
        
    -   [
        
        2.2 Load balancing
        
        ](#Load_balancing)
        
    -   [
        
        2.3 Capacity factor
        
        ](#Capacity_factor)
        
    -   [
        
        2.4 Routing
        
        ](#Routing)
        
    -   [
        
        2.5 Applications to transformer models
        
        ](#Applications_to_transformer_models)
        
-   [
    
    3 See also
    
    ](#See_also)
    
-   [
    
    4 References
    
    ](#References)
    
-   [
    
    5 Further reading
    
    ](#Further_reading)
    

 Toggle the table of contents

# Mixture of experts

 9 languages

-   [العربية](https://ar.wikipedia.org/wiki/%D8%AE%D9%84%D9%8A%D8%B7_%D8%A7%D9%84%D8%AE%D8%A8%D8%B1%D8%A7%D8%A1 "خليط الخبراء – Arabic")
-   [Català](https://ca.wikipedia.org/wiki/Barreja_d%27experts "Barreja d'experts – Catalan")
-   [Español](https://es.wikipedia.org/wiki/Mezcla_de_expertos "Mezcla de expertos – Spanish")
-   [فارسی](https://fa.wikipedia.org/wiki/%D8%AA%D8%B1%DA%A9%DB%8C%D8%A8_%D9%85%D8%AA%D8%AE%D8%B5%D8%B5%D8%A7%D9%86 "ترکیب متخصصان – Persian")
-   [Ido](https://io.wikipedia.org/wiki/Mixuro_di_experti "Mixuro di experti – Ido")
-   [Italiano](https://it.wikipedia.org/wiki/Mistura_di_esperti "Mistura di esperti – Italian")
-   [Polski](https://pl.wikipedia.org/wiki/Mieszanka_ekspert%C3%B3w "Mieszanka ekspertów – Polish")
-   [粵語](https://zh-yue.wikipedia.org/wiki/%E6%B7%B7%E5%90%88%E5%B0%88%E5%AE%B6%E6%A8%A1%E5%9E%8B "混合專家模型 – Cantonese")
-   [中文](https://zh.wikipedia.org/wiki/%E6%B7%B7%E5%90%88%E4%B8%93%E5%AE%B6%E6%A8%A1%E5%9E%8B "混合专家模型 – Chinese")

[Edit links](https://www.wikidata.org/wiki/Special:EntityPage/Q30688561#sitelinks-wikipedia "Edit interlanguage links")

-   [Article](/wiki/Mixture_of_experts "View the content page [c]")
-   [Talk](/wiki/Talk:Mixture_of_experts "Discuss improvements to the content page [t]")

 English

-   [Read](/wiki/Mixture_of_experts)
-   [Edit](/w/index.php?title=Mixture_of_experts&action=edit "Edit this page [e]")
-   [View history](/w/index.php?title=Mixture_of_experts&action=history "Past revisions of this page [h]")

 Tools

Tools

move to sidebar hide

Actions

-   [Read](/wiki/Mixture_of_experts)
-   [Edit](/w/index.php?title=Mixture_of_experts&action=edit "Edit this page [e]")
-   [View history](/w/index.php?title=Mixture_of_experts&action=history)

General

-   [What links here](/wiki/Special:WhatLinksHere/Mixture_of_experts "List of all English Wikipedia pages containing links to this page [j]")
-   [Related changes](/wiki/Special:RecentChangesLinked/Mixture_of_experts "Recent changes in pages linked from this page [k]")
-   [Upload file](//en.wikipedia.org/wiki/Wikipedia:File_Upload_Wizard "Upload files [u]")
-   [Permanent link](/w/index.php?title=Mixture_of_experts&oldid=1346279093 "Permanent link to this revision of this page")
-   [Page information](/w/index.php?title=Mixture_of_experts&action=info "More information about this page")
-   [Cite this page](/w/index.php?title=Special:CiteThisPage&page=Mixture_of_experts&id=1346279093&wpFormIdentifier=titleform "Information on how to cite this page")
-   [Get shortened URL](/w/index.php?title=Special:UrlShortener&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMixture_of_experts)

Print/export

-   [Download as PDF](/w/index.php?title=Special:DownloadAsPdf&page=Mixture_of_experts&action=show-download-screen "Download this page as a PDF file")
-   [Printable version](/w/index.php?title=Mixture_of_experts&printable=yes "Printable version of this page [p]")

In other projects

-   [Wikidata item](https://www.wikidata.org/wiki/Special:EntityPage/Q30688561 "Structured data on this page hosted by Wikidata [g]")

Appearance

move to sidebar hide

From Wikipedia, the free encyclopedia

Machine learning technique

"MoE" redirects here. For other uses, see [Moe](/wiki/MOE_\(disambiguation\) "MOE (disambiguation)").

Part of a series on

[Machine learning](/wiki/Machine_learning "Machine learning")  
and [data mining](/wiki/Data_mining "Data mining")

Paradigms

-   [Supervised learning](/wiki/Supervised_learning "Supervised learning")
-   [Unsupervised learning](/wiki/Unsupervised_learning "Unsupervised learning")
-   [Semi-supervised learning](/wiki/Semi-supervised_learning "Semi-supervised learning")
-   [Self-supervised learning](/wiki/Self-supervised_learning "Self-supervised learning")
-   [Reinforcement learning](/wiki/Reinforcement_learning "Reinforcement learning")
-   [Meta-learning](/wiki/Meta-learning_\(computer_science\) "Meta-learning (computer science)")
-   [Online learning](/wiki/Online_machine_learning "Online machine learning")
-   [Batch learning](/wiki/Batch_learning "Batch learning")
-   [Curriculum learning](/wiki/Curriculum_learning "Curriculum learning")
-   [Rule-based learning](/wiki/Rule-based_machine_learning "Rule-based machine learning")
-   [Neuro-symbolic AI](/wiki/Neuro-symbolic_AI "Neuro-symbolic AI")
-   [Neuromorphic engineering](/wiki/Neuromorphic_engineering "Neuromorphic engineering")
-   [Quantum machine learning](/wiki/Quantum_machine_learning "Quantum machine learning")

Problems

-   [Classification](/wiki/Statistical_classification "Statistical classification")
-   [Generative modeling](/wiki/Generative_model "Generative model")
-   [Regression](/wiki/Regression_analysis "Regression analysis")
-   [Clustering](/wiki/Cluster_analysis "Cluster analysis")
-   [Dimensionality reduction](/wiki/Dimensionality_reduction "Dimensionality reduction")
-   [Density estimation](/wiki/Density_estimation "Density estimation")
-   [Anomaly detection](/wiki/Anomaly_detection "Anomaly detection")
-   [Data cleaning](/wiki/Data_cleaning "Data cleaning")
-   [AutoML](/wiki/Automated_machine_learning "Automated machine learning")
-   [Association rules](/wiki/Association_rule_learning "Association rule learning")
-   [Semantic analysis](/wiki/Semantic_analysis_\(machine_learning\) "Semantic analysis (machine learning)")
-   [Structured prediction](/wiki/Structured_prediction "Structured prediction")
-   [Feature engineering](/wiki/Feature_engineering "Feature engineering")
-   [Feature learning](/wiki/Feature_learning "Feature learning")
-   [Learning to rank](/wiki/Learning_to_rank "Learning to rank")
-   [Grammar induction](/wiki/Grammar_induction "Grammar induction")
-   [Ontology learning](/wiki/Ontology_learning "Ontology learning")
-   [Multimodal learning](/wiki/Multimodal_learning "Multimodal learning")

[Supervised learning](/wiki/Supervised_learning "Supervised learning")  
(**[classification](/wiki/Statistical_classification "Statistical classification")** • **[regression](/wiki/Regression_analysis "Regression analysis")**)

-   [Apprenticeship learning](/wiki/Apprenticeship_learning "Apprenticeship learning")
-   [Decision trees](/wiki/Decision_tree_learning "Decision tree learning")
-   [Ensembles](/wiki/Ensemble_learning "Ensemble learning")
    -   [Bagging](/wiki/Bootstrap_aggregating "Bootstrap aggregating")
    -   [Boosting](/wiki/Boosting_\(machine_learning\) "Boosting (machine learning)")
    -   [Random forest](/wiki/Random_forest "Random forest")
-   [*k*\-NN](/wiki/K-nearest_neighbors_algorithm "K-nearest neighbors algorithm")
-   [Linear regression](/wiki/Linear_regression "Linear regression")
-   [Naive Bayes](/wiki/Naive_Bayes_classifier "Naive Bayes classifier")
-   [Artificial neural networks](/wiki/Artificial_neural_network "Artificial neural network")
-   [Logistic regression](/wiki/Logistic_regression "Logistic regression")
-   [Perceptron](/wiki/Perceptron "Perceptron")
-   [Relevance vector machine (RVM)](/wiki/Relevance_vector_machine "Relevance vector machine")
-   [Support vector machine (SVM)](/wiki/Support_vector_machine "Support vector machine")

[Clustering](/wiki/Cluster_analysis "Cluster analysis")

-   [BIRCH](/wiki/BIRCH "BIRCH")
-   [CURE](/wiki/CURE_algorithm "CURE algorithm")
-   [Hierarchical](/wiki/Hierarchical_clustering "Hierarchical clustering")
-   [*k*\-means](/wiki/K-means_clustering "K-means clustering")
-   [Fuzzy](/wiki/Fuzzy_clustering "Fuzzy clustering")
-   [Expectation–maximization (EM)](/wiki/Expectation%E2%80%93maximization_algorithm "Expectation–maximization algorithm")
-     
    [DBSCAN](/wiki/DBSCAN "DBSCAN")
-   [OPTICS](/wiki/OPTICS_algorithm "OPTICS algorithm")
-   [Mean shift](/wiki/Mean_shift "Mean shift")

[Dimensionality reduction](/wiki/Dimensionality_reduction "Dimensionality reduction")

-   [Factor analysis](/wiki/Factor_analysis "Factor analysis")
-   [CCA](/wiki/Canonical_correlation "Canonical correlation")
-   [ICA](/wiki/Independent_component_analysis "Independent component analysis")
-   [LDA](/wiki/Linear_discriminant_analysis "Linear discriminant analysis")
-   [NMF](/wiki/Non-negative_matrix_factorization "Non-negative matrix factorization")
-   [PCA](/wiki/Principal_component_analysis "Principal component analysis")
-   [PGD](/wiki/Proper_generalized_decomposition "Proper generalized decomposition")
-   [t-SNE](/wiki/T-distributed_stochastic_neighbor_embedding "T-distributed stochastic neighbor embedding")
-   [SDL](/wiki/Sparse_dictionary_learning "Sparse dictionary learning")

[Structured prediction](/wiki/Structured_prediction "Structured prediction")

-   [Graphical models](/wiki/Graphical_model "Graphical model")
    -   [Bayes net](/wiki/Bayesian_network "Bayesian network")
    -   [Conditional random field](/wiki/Conditional_random_field "Conditional random field")
    -   [Hidden Markov](/wiki/Hidden_Markov_model "Hidden Markov model")

[Anomaly detection](/wiki/Anomaly_detection "Anomaly detection")

-   [RANSAC](/wiki/Random_sample_consensus "Random sample consensus")
-   [*k*\-NN](/wiki/K-nearest_neighbors_algorithm "K-nearest neighbors algorithm")
-   [Local outlier factor](/wiki/Local_outlier_factor "Local outlier factor")
-   [Isolation forest](/wiki/Isolation_forest "Isolation forest")

[Neural networks](/wiki/Neural_network_\(machine_learning\) "Neural network (machine learning)")

-   [Autoencoder](/wiki/Autoencoder "Autoencoder")
-   [Deep learning](/wiki/Deep_learning "Deep learning")
-   [Feedforward neural network](/wiki/Feedforward_neural_network "Feedforward neural network")
-   [Recurrent neural network](/wiki/Recurrent_neural_network "Recurrent neural network")
    -   [LSTM](/wiki/Long_short-term_memory "Long short-term memory")
    -   [GRU](/wiki/Gated_recurrent_unit "Gated recurrent unit")
    -   [ESN](/wiki/Echo_state_network "Echo state network")
    -   [reservoir computing](/wiki/Reservoir_computing "Reservoir computing")
-   [Boltzmann machine](/wiki/Boltzmann_machine "Boltzmann machine")
    -   [Restricted](/wiki/Restricted_Boltzmann_machine "Restricted Boltzmann machine")
-   [GAN](/wiki/Generative_adversarial_network "Generative adversarial network")
-   [Diffusion model](/wiki/Diffusion_model "Diffusion model")
-   [SOM](/wiki/Self-organizing_map "Self-organizing map")
-   [Convolutional neural network](/wiki/Convolutional_neural_network "Convolutional neural network")
    -   [U-Net](/wiki/U-Net "U-Net")
    -   [LeNet](/wiki/LeNet "LeNet")
    -   [AlexNet](/wiki/AlexNet "AlexNet")
    -   [DeepDream](/wiki/DeepDream "DeepDream")
-   [Neural field](/wiki/Neural_field "Neural field")
    -   [Neural radiance field](/wiki/Neural_radiance_field "Neural radiance field")
    -   [Physics-informed neural networks](/wiki/Physics-informed_neural_networks "Physics-informed neural networks")
-   [Transformer](/wiki/Transformer_\(deep_learning_architecture\) "Transformer (deep learning architecture)")
    -   [Vision](/wiki/Vision_transformer "Vision transformer")
-   [Mamba](/wiki/Mamba_\(deep_learning_architecture\) "Mamba (deep learning architecture)")
-   [Spiking neural network](/wiki/Spiking_neural_network "Spiking neural network")
-   [Memtransistor](/wiki/Memtransistor "Memtransistor")
-   [Electrochemical RAM](/wiki/Electrochemical_RAM "Electrochemical RAM") (ECRAM)

[Reinforcement learning](/wiki/Reinforcement_learning "Reinforcement learning")

-   [Q-learning](/wiki/Q-learning "Q-learning")
-   [Policy gradient](/wiki/Policy_gradient_method "Policy gradient method")
-   [SARSA](/wiki/State%E2%80%93action%E2%80%93reward%E2%80%93state%E2%80%93action "State–action–reward–state–action")
-   [Temporal difference (TD)](/wiki/Temporal_difference_learning "Temporal difference learning")
-   [Multi-agent](/wiki/Multi-agent_reinforcement_learning "Multi-agent reinforcement learning")
    -   [Self-play](/wiki/Self-play_\(reinforcement_learning_technique\) "Self-play (reinforcement learning technique)")

Learning with humans

-   [Active learning](/wiki/Active_learning_\(machine_learning\) "Active learning (machine learning)")
-   [Crowdsourcing](/wiki/Crowdsourcing "Crowdsourcing")
-   [Human-in-the-loop](/wiki/Human-in-the-loop "Human-in-the-loop")
-   [Mechanistic interpretability](/wiki/Mechanistic_interpretability "Mechanistic interpretability")
-   [RLHF](/wiki/Reinforcement_learning_from_human_feedback "Reinforcement learning from human feedback")

Model diagnostics

-   [Coefficient of determination](/wiki/Coefficient_of_determination "Coefficient of determination")
-   [Confusion matrix](/wiki/Confusion_matrix "Confusion matrix")
-   [Learning curve](/wiki/Learning_curve_\(machine_learning\) "Learning curve (machine learning)")
-   [ROC curve](/wiki/Receiver_operating_characteristic "Receiver operating characteristic")

Mathematical foundations

-   [Kernel machines](/wiki/Kernel_machines "Kernel machines")
-   [Bias–variance tradeoff](/wiki/Bias%E2%80%93variance_tradeoff "Bias–variance tradeoff")
-   [Computational learning theory](/wiki/Computational_learning_theory "Computational learning theory")
-   [Empirical risk minimization](/wiki/Empirical_risk_minimization "Empirical risk minimization")
-   [Occam learning](/wiki/Occam_learning "Occam learning")
-   [PAC learning](/wiki/Probably_approximately_correct_learning "Probably approximately correct learning")
-   [Statistical learning](/wiki/Statistical_learning_theory "Statistical learning theory")
-   [VC theory](/wiki/Vapnik%E2%80%93Chervonenkis_theory "Vapnik–Chervonenkis theory")
-   [Topological deep learning](/wiki/Topological_deep_learning "Topological deep learning")

Journals and conferences

-   [AAAI](/wiki/AAAI_Conference_on_Artificial_Intelligence "AAAI Conference on Artificial Intelligence")
-   [ECML PKDD](/wiki/ECML_PKDD "ECML PKDD")
-   [NeurIPS](/wiki/Conference_on_Neural_Information_Processing_Systems "Conference on Neural Information Processing Systems")
-   [ICML](/wiki/International_Conference_on_Machine_Learning "International Conference on Machine Learning")
-   [ICLR](/wiki/International_Conference_on_Learning_Representations "International Conference on Learning Representations")
-   [IJCAI](/wiki/International_Joint_Conference_on_Artificial_Intelligence "International Joint Conference on Artificial Intelligence")
-   [ML](/wiki/Machine_Learning_\(journal\) "Machine Learning (journal)")
-   [JMLR](/wiki/Journal_of_Machine_Learning_Research "Journal of Machine Learning Research")

Related articles

-   [Glossary of artificial intelligence](/wiki/Glossary_of_artificial_intelligence "Glossary of artificial intelligence")
-   [List of datasets for machine-learning research](/wiki/List_of_datasets_for_machine-learning_research "List of datasets for machine-learning research")
    -   [List of datasets in computer vision and image processing](/wiki/List_of_datasets_in_computer_vision_and_image_processing "List of datasets in computer vision and image processing")
-   [Outline of machine learning](/wiki/Outline_of_machine_learning "Outline of machine learning")

-   [v](/wiki/Template:Machine_learning "Template:Machine learning")
-   [t](/wiki/Template_talk:Machine_learning "Template talk:Machine learning")
-   [e](/wiki/Special:EditPage/Template:Machine_learning "Special:EditPage/Template:Machine learning")

**Mixture of experts** (**MoE**) is a [machine learning](/wiki/Machine_learning "Machine learning") technique where multiple expert [networks](/wiki/Neural_network_\(machine_learning\) "Neural network (machine learning)") (learners) are used to divide a problem space into homogeneous regions.[\[1\]](#cite_note-1) MoE represents a form of [ensemble learning](/wiki/Ensemble_learning "Ensemble learning").[\[2\]](#cite_note-2) They were also called **committee machines**.[\[3\]](#cite_note-3)

## Basic theory

\[[edit](/w/index.php?title=Mixture_of_experts&action=edit&section=1 "Edit section: Basic theory")\]

MoE always has the following components, but they are implemented and combined differently according to the problem being solved:

-   **Experts** f 1 , . . . , f n {\\displaystyle f\_{1},...,f\_{n}} ![{\displaystyle f_{1},...,f_{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/56add4996a8ffb2d648fd1b373476afd13c2a117) , each taking the same input x {\\displaystyle x} ![{\displaystyle x}](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4) , and producing outputs f 1 ( x ) , . . . , f n ( x ) {\\displaystyle f\_{1}(x),...,f\_{n}(x)} ![{\displaystyle f_{1}(x),...,f_{n}(x)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b54f3c51e771adfad997a70f5facc417e6fb11d7) .
-   A **weighting function** (also known as a **gating function**) w {\\displaystyle w} ![{\displaystyle w}](https://wikimedia.org/api/rest_v1/media/math/render/svg/88b1e0c8e1be5ebe69d18a8010676fa42d7961e6) , which takes input x {\\displaystyle x} ![{\displaystyle x}](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4) and produces a vector of outputs ( w ( x ) 1 , . . . , w ( x ) n ) {\\displaystyle (w(x)\_{1},...,w(x)\_{n})} ![{\displaystyle (w(x)_{1},...,w(x)_{n})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/27ac6c715cbf196e148b2f3d2c9c497d72658814) . This may or may not be a probability distribution, but in both cases, its entries are non-negative.
-   θ \= ( θ 0 , θ 1 , . . . , θ n ) {\\displaystyle \\theta =(\\theta \_{0},\\theta \_{1},...,\\theta \_{n})} ![{\displaystyle \theta =(\theta _{0},\theta _{1},...,\theta _{n})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c1f47bb0eb8effc062c65b6f51850198bdd4547d) is the set of parameters. The parameter θ 0 {\\displaystyle \\theta \_{0}} ![{\displaystyle \theta _{0}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/18b67de6bf25dba7a24e66967ff6319858798734) is for the weighting function. The parameters θ 1 , … , θ n {\\displaystyle \\theta \_{1},\\dots ,\\theta \_{n}} ![{\displaystyle \theta _{1},\dots ,\theta _{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6ade44c658e0e5f72012979bde72c07d88a1b4f5) are for the experts.
-   Given an input x {\\displaystyle x} ![{\displaystyle x}](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4) , the **mixture of experts** produces a single output by combining f 1 ( x ) , . . . , f n ( x ) {\\displaystyle f\_{1}(x),...,f\_{n}(x)} ![{\displaystyle f_{1}(x),...,f_{n}(x)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b54f3c51e771adfad997a70f5facc417e6fb11d7) according to the weights w ( x ) 1 , . . . , w ( x ) n {\\displaystyle w(x)\_{1},...,w(x)\_{n}} ![{\displaystyle w(x)_{1},...,w(x)_{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8db8c57eafa107c634b435bd05907cf34c29f13b) in some way, usually by f ( x ) \= ∑ i w ( x ) i f i ( x ) {\\displaystyle f(x)=\\sum \_{i}w(x)\_{i}f\_{i}(x)} ![{\displaystyle f(x)=\sum _{i}w(x)_{i}f_{i}(x)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/45ec9e10514355d7c1a9a122009a8338ac4b7509) .

Both the experts and the weighting function are trained by minimizing some [loss function](/wiki/Loss_function "Loss function"), generally via [gradient descent](/wiki/Gradient_descent "Gradient descent"). There is much freedom in choosing the precise form of experts, the weighting function, and the loss function.

### Meta-pi network

\[[edit](/w/index.php?title=Mixture_of_experts&action=edit&section=2 "Edit section: Meta-pi network")\]

The **meta-pi network**, reported by Hampshire and Waibel,[\[4\]](#cite_note-4) uses f ( x ) \= ∑ i w ( x ) i f i ( x ) {\\displaystyle f(x)=\\sum \_{i}w(x)\_{i}f\_{i}(x)} ![{\displaystyle f(x)=\sum _{i}w(x)_{i}f_{i}(x)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/45ec9e10514355d7c1a9a122009a8338ac4b7509) as the output. The model is trained by performing gradient descent on the mean-squared error loss L := 1 N ∑ k ‖ y k − f ( x k ) ‖ 2 {\\displaystyle L:={\\frac {1}{N}}\\sum \_{k}\\|y\_{k}-f(x\_{k})\\|^{2}} ![{\displaystyle L:={\frac {1}{N}}\sum _{k}\|y_{k}-f(x_{k})\|^{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/47297a3c260005b30b02bf08e69ecbbe5243a530) . The experts may be arbitrary functions.

In their original publication, they were solving the problem of classifying [phonemes](/wiki/Phoneme "Phoneme") in speech signal from 6 different Japanese speakers, 2 females and 4 males. They trained 6 experts, each being a "time-delayed neural network"[\[5\]](#cite_note-5) (essentially a multilayered [convolution network](/wiki/Convolutional_neural_network "Convolutional neural network") over the [mel spectrogram](/wiki/Mel-frequency_cepstrum "Mel-frequency cepstrum")). They found that the resulting mixture of experts dedicated 5 experts for 5 of the speakers, but the 6th (male) speaker does not have a dedicated expert, instead his voice was classified by a linear combination of the experts for the other 3 male speakers.

### Adaptive mixtures of local experts

\[[edit](/w/index.php?title=Mixture_of_experts&action=edit&section=3 "Edit section: Adaptive mixtures of local experts")\]

The **adaptive mixtures of local experts** [\[6\]](#cite_note-6)[\[7\]](#cite_note-7) uses a [Gaussian mixture model](/wiki/Gaussian_mixture_model "Gaussian mixture model"). Each expert simply predicts a Gaussian distribution, and totally ignores the input. Specifically, the i {\\displaystyle i} ![{\displaystyle i}](https://wikimedia.org/api/rest_v1/media/math/render/svg/add78d8608ad86e54951b8c8bd6c8d8416533d20) \-th expert predicts that the output is y ∼ N ( μ i , I ) {\\displaystyle y\\sim N(\\mu \_{i},I)} ![{\displaystyle y\sim N(\mu _{i},I)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4ffa0de0461c283a44af62da1735c99027bf28d1) , where μ i {\\displaystyle \\mu \_{i}} ![{\displaystyle \mu _{i}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/dea0a0293841cce9eef98b55e53a92b82ae59ee4) is a learnable parameter. The weighting function is a linear-softmax function: w ( x ) i \= e k i T x + b i ∑ j e k j T x + b j {\\displaystyle w(x)\_{i}={\\frac {e^{k\_{i}^{T}x+b\_{i}}}{\\sum \_{j}e^{k\_{j}^{T}x+b\_{j}}}}} ![{\displaystyle w(x)_{i}={\frac {e^{k_{i}^{T}x+b_{i}}}{\sum _{j}e^{k_{j}^{T}x+b_{j}}}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/890f1042bef5b0e8587935a360cfe65a7bf360ac) The mixture of experts predict that the output is distributed according to the log-probability density function: ln ⁡ f θ ( y | x ) \= ln ⁡ \[ ∑ i e k i T x + b i ∑ j e k j T x + b j N ( y | μ i , I ) \] \= ln ⁡ \[ ( 2 π ) − d / 2 ∑ i e k i T x + b i ∑ j e k j T x + b j e − 1 2 ‖ y − μ i ‖ 2 \] {\\displaystyle \\ln f\_{\\theta }(y|x)=\\ln \\left\[\\sum \_{i}{\\frac {e^{k\_{i}^{T}x+b\_{i}}}{\\sum \_{j}e^{k\_{j}^{T}x+b\_{j}}}}N(y|\\mu \_{i},I)\\right\]=\\ln \\left\[(2\\pi )^{-d/2}\\sum \_{i}{\\frac {e^{k\_{i}^{T}x+b\_{i}}}{\\sum \_{j}e^{k\_{j}^{T}x+b\_{j}}}}e^{-{\\frac {1}{2}}\\|y-\\mu \_{i}\\|^{2}}\\right\]} ![{\displaystyle \ln f_{\theta }(y|x)=\ln \left[\sum _{i}{\frac {e^{k_{i}^{T}x+b_{i}}}{\sum _{j}e^{k_{j}^{T}x+b_{j}}}}N(y|\mu _{i},I)\right]=\ln \left[(2\pi )^{-d/2}\sum _{i}{\frac {e^{k_{i}^{T}x+b_{i}}}{\sum _{j}e^{k_{j}^{T}x+b_{j}}}}e^{-{\frac {1}{2}}\|y-\mu _{i}\|^{2}}\right]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/1ce08069e085bce94601d55679a4b30c567f2f13) It is trained by maximal likelihood estimation, that is, gradient ascent on f ( y | x ) {\\displaystyle f(y|x)} ![{\displaystyle f(y|x)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2aee2f6ab4af1ca8832dd59ba06a5217f8f00014) . The gradient for the i {\\displaystyle i} ![{\displaystyle i}](https://wikimedia.org/api/rest_v1/media/math/render/svg/add78d8608ad86e54951b8c8bd6c8d8416533d20) \-th expert is

∇ μ i ln ⁡ f θ ( y | x ) \= w ( x ) i N ( y | μ i , I ) ∑ j w ( x ) j N ( y | μ j , I ) ( y − μ i ) {\\displaystyle \\nabla \_{\\mu \_{i}}\\ln f\_{\\theta }(y|x)={\\frac {w(x)\_{i}N(y|\\mu \_{i},I)}{\\sum \_{j}w(x)\_{j}N(y|\\mu \_{j},I)}}\\;(y-\\mu \_{i})} ![{\displaystyle \nabla _{\mu _{i}}\ln f_{\theta }(y|x)={\frac {w(x)_{i}N(y|\mu _{i},I)}{\sum _{j}w(x)_{j}N(y|\mu _{j},I)}}\;(y-\mu _{i})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/272a75eff2d606a404776e350f86938a74e595a7) 

and the gradient for the weighting function is ∇ \[ k i , b i \] ln ⁡ f θ ( y | x ) \= \[ x 1 \] w ( x ) i ∑ j w ( x ) j N ( y | μ j , I ) ( f i ( x ) − f θ ( y | x ) ) {\\displaystyle \\nabla \_{\[k\_{i},b\_{i}\]}\\ln f\_{\\theta }(y|x)={\\begin{bmatrix}x\\\\1\\end{bmatrix}}{\\frac {w(x)\_{i}}{\\sum \_{j}w(x)\_{j}N(y|\\mu \_{j},I)}}(f\_{i}(x)-f\_{\\theta }(y|x))} ![{\displaystyle \nabla _{[k_{i},b_{i}]}\ln f_{\theta }(y|x)={\begin{bmatrix}x\\1\end{bmatrix}}{\frac {w(x)_{i}}{\sum _{j}w(x)_{j}N(y|\mu _{j},I)}}(f_{i}(x)-f_{\theta }(y|x))}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0c14be69e3d3e6a84c2ac2cc2fd089540dda090a) 

For each input-output pair ( x , y ) {\\displaystyle (x,y)} ![{\displaystyle (x,y)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/41cf50e4a314ca8e2c30964baa8d26e5be7a9386) , the weighting function is changed to increase the weight on all experts that performed above average, and decrease the weight on all experts that performed below average. This encourages the weighting function to learn to select only the experts that make the right predictions for each input.

The i {\\displaystyle i} ![{\displaystyle i}](https://wikimedia.org/api/rest_v1/media/math/render/svg/add78d8608ad86e54951b8c8bd6c8d8416533d20) \-th expert is changed to make its prediction closer to y {\\displaystyle y} ![{\displaystyle y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b8a6208ec717213d4317e666f1ae872e00620a0d) , but the amount of change is proportional to w ( x ) i N ( y | μ i , I ) {\\displaystyle w(x)\_{i}N(y|\\mu \_{i},I)} ![{\displaystyle w(x)_{i}N(y|\mu _{i},I)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/907b094baece0c5fcaed8760575fa24693d9846d) . This has a Bayesian interpretation. Given input x {\\displaystyle x} ![{\displaystyle x}](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4) , the [prior probability](/wiki/Prior_probability "Prior probability") that expert i {\\displaystyle i} ![{\displaystyle i}](https://wikimedia.org/api/rest_v1/media/math/render/svg/add78d8608ad86e54951b8c8bd6c8d8416533d20) is the right one is w ( x ) i {\\displaystyle w(x)\_{i}} ![{\displaystyle w(x)_{i}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/26a3735495f6d75e6e4a83b8346b2f4befd03af8) , and N ( y | μ i , I ) {\\displaystyle N(y|\\mu \_{i},I)} ![{\displaystyle N(y|\mu _{i},I)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/92abd51cd5123823f11059135dd3dd1b7df1ef00) is the [likelihood](/wiki/Likelihood_function "Likelihood function") of evidence y {\\displaystyle y} ![{\displaystyle y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b8a6208ec717213d4317e666f1ae872e00620a0d) . So, w ( x ) i N ( y | μ i , I ) ∑ j w ( x ) j N ( y | μ j , I ) {\\displaystyle {\\frac {w(x)\_{i}N(y|\\mu \_{i},I)}{\\sum \_{j}w(x)\_{j}N(y|\\mu \_{j},I)}}} ![{\displaystyle {\frac {w(x)_{i}N(y|\mu _{i},I)}{\sum _{j}w(x)_{j}N(y|\mu _{j},I)}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a92376a9810f19e5346201936d0855bf5502ef27) is the [posterior probability](/wiki/Posterior_probability "Posterior probability") for expert i {\\displaystyle i} ![{\displaystyle i}](https://wikimedia.org/api/rest_v1/media/math/render/svg/add78d8608ad86e54951b8c8bd6c8d8416533d20) , and so the rate of change for the i {\\displaystyle i} ![{\displaystyle i}](https://wikimedia.org/api/rest_v1/media/math/render/svg/add78d8608ad86e54951b8c8bd6c8d8416533d20) \-th expert is proportional to its posterior probability.

In words, the experts that, in hindsight, seemed like the good experts to consult, are asked to learn on the example. The experts that, in hindsight, were not, are left alone.

The combined effect is that the experts become specialized: Suppose two experts are both good at predicting a certain kind of input, but one is slightly better, then the weighting function would eventually learn to favor the better one. After that happens, the lesser expert is unable to obtain a high gradient signal, and becomes even worse at predicting such kind of input. Conversely, the lesser expert can become better at predicting other kinds of input, and increasingly pulled away into another region. This has a positive feedback effect, causing each expert to move apart from the rest and take care of a local region alone (thus the name "*local* experts").

### Hierarchical MoE

\[[edit](/w/index.php?title=Mixture_of_experts&action=edit&section=4 "Edit section: Hierarchical MoE")\]

**Hierarchical mixtures of experts**[\[8\]](#cite_note-:0-8)[\[9\]](#cite_note-:2-9) uses multiple levels of gating in a tree. Each gating is a probability distribution over the next level of gatings, and the experts are on the leaf nodes of the tree. They are similar to [decision trees](/wiki/Decision_tree_learning "Decision tree learning").

For example, a 2-level hierarchical MoE would have a first order gating function w i {\\displaystyle w\_{i}} ![{\displaystyle w_{i}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/fe22f0329d3ecb2e1880d44d191aba0e5475db68) , and second order gating functions w j | i {\\displaystyle w\_{j|i}} ![{\displaystyle w_{j|i}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/bce7d5ef4b03308a52504b16a2c1a9241fa6b34b) and experts f j | i {\\displaystyle f\_{j|i}} ![{\displaystyle f_{j|i}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b58427bc66d66eed6180d6555ac076b83e6b1e43) . The total prediction is then ∑ i w i ( x ) ∑ j w j | i ( x ) f j | i ( x ) {\\displaystyle \\sum \_{i}w\_{i}(x)\\sum \_{j}w\_{j|i}(x)f\_{j|i}(x)} ![{\displaystyle \sum _{i}w_{i}(x)\sum _{j}w_{j|i}(x)f_{j|i}(x)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7d11b65b826ba9f638271cae56b8056a1edb08fd) .

### Variants

\[[edit](/w/index.php?title=Mixture_of_experts&action=edit&section=5 "Edit section: Variants")\]

The mixture of experts, being similar to the gaussian mixture model, can also be trained by the [expectation-maximization algorithm, just like gaussian mixture models](/wiki/Expectation%E2%80%93maximization_algorithm#Gaussian_mixture "Expectation–maximization algorithm"). Specifically, during the expectation step, the "burden" for explaining each data point is assigned over the experts, and during the maximization step, the experts are trained to improve the explanations they got a high burden for, while the gate is trained to improve its burden assignment. This can converge faster than gradient ascent on the log-likelihood.[\[9\]](#cite_note-:2-9)[\[10\]](#cite_note-:3-10)

The choice of gating function is often softmax. Other than that, gating may use [gaussian distributions](/wiki/Normal_distribution "Normal distribution")[\[11\]](#cite_note-11) and [exponential families](/wiki/Exponential_family "Exponential family").[\[10\]](#cite_note-:3-10)

Instead of performing a weighted sum of all the experts, in hard MoE,[\[12\]](#cite_note-12) only the highest ranked expert is chosen. That is, f ( x ) \= f arg ⁡ max i w i ( x ) ( x ) {\\displaystyle f(x)=f\_{\\arg \\max \_{i}w\_{i}(x)}(x)} ![{\displaystyle f(x)=f_{\arg \max _{i}w_{i}(x)}(x)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f1cf82fe8ff005f571eca5e46aa01e40006393dd) . This can accelerate training and inference time.[\[13\]](#cite_note-13)

The experts can use more general forms of multivariant gaussian distributions. For example,[\[8\]](#cite_note-:0-8) proposed f i ( y | x ) \= N ( y | A i x + b i , Σ i ) {\\displaystyle f\_{i}(y|x)=N(y|A\_{i}x+b\_{i},\\Sigma \_{i})} ![{\displaystyle f_{i}(y|x)=N(y|A_{i}x+b_{i},\Sigma _{i})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/3c8d64f71d4e3bd365d0ed7b8ce9d0741486eee7) , where A i , b i , Σ i {\\displaystyle A\_{i},b\_{i},\\Sigma \_{i}} ![{\displaystyle A_{i},b_{i},\Sigma _{i}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/dc450dcded751672750b36fb17b0d88251627837) are learnable parameters. In words, each expert learns to do linear regression, with a learnable uncertainty estimate.

One can use different experts than gaussian distributions. For example, one can use [Laplace distribution](/wiki/Laplace_distribution "Laplace distribution"),[\[14\]](#cite_note-14) or [Student's t-distribution](/wiki/Student%27s_t-distribution "Student's t-distribution").[\[15\]](#cite_note-15) For binary classification, it also proposed [logistic regression](/wiki/Logistic_regression "Logistic regression") experts, with f i ( y | x ) \= { 1 1 + e β i T x + β i , 0 , y \= 0 1 − 1 1 + e β i T x + β i , 0 , y \= 1 {\\displaystyle f\_{i}(y|x)={\\begin{cases}{\\frac {1}{1+e^{\\beta \_{i}^{T}x+\\beta \_{i,0}}}},&y=0\\\\1-{\\frac {1}{1+e^{\\beta \_{i}^{T}x+\\beta \_{i,0}}}},&y=1\\end{cases}}} ![{\displaystyle f_{i}(y|x)={\begin{cases}{\frac {1}{1+e^{\beta _{i}^{T}x+\beta _{i,0}}}},&y=0\\1-{\frac {1}{1+e^{\beta _{i}^{T}x+\beta _{i,0}}}},&y=1\end{cases}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a1fb490a4e7746a051f5848c171354290d5bcd41) where β i , β i , 0 {\\displaystyle \\beta \_{i},\\beta \_{i,0}} ![{\displaystyle \beta _{i},\beta _{i,0}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2dc5b1cd4d33317ddfb7c56206e709c0b56b7822) are learnable parameters. This is later generalized for multi-class classification, with [multinomial logistic regression](/wiki/Multinomial_logistic_regression "Multinomial logistic regression") experts.[\[16\]](#cite_note-16)

One paper proposed **mixture of softmaxes** for autoregressive language modelling.[\[17\]](#cite_note-17) Specifically, consider a language model that given a previous text c {\\displaystyle c} ![{\displaystyle c}](https://wikimedia.org/api/rest_v1/media/math/render/svg/86a67b81c2de995bd608d5b2df50cd8cd7d92455) , predicts the next word x {\\displaystyle x} ![{\displaystyle x}](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4) . The network encodes the text into a vector v c {\\displaystyle v\_{c}} ![{\displaystyle v_{c}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/780b816790d75e7641e3e8949591231e76dc5624) , and predicts the probability distribution of the next word as S o f t m a x ( v c W ) {\\displaystyle \\mathrm {Softmax} (v\_{c}W)} ![{\displaystyle \mathrm {Softmax} (v_{c}W)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/46eade118793363ff2703704c8317965cad22cfe) for an embedding matrix W {\\displaystyle W} ![{\displaystyle W}](https://wikimedia.org/api/rest_v1/media/math/render/svg/54a9c4c547f4d6111f81946cad242b18298d70b7) . In mixture of softmaxes, the model outputs multiple vectors v c , 1 , … , v c , n {\\displaystyle v\_{c,1},\\dots ,v\_{c,n}} ![{\displaystyle v_{c,1},\dots ,v_{c,n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/31a35c7734bca98534e88a160be7087b9236fe2b) , and predict the next word as ∑ i \= 1 n p i S o f t m a x ( v c , i W i ) {\\displaystyle \\sum \_{i=1}^{n}p\_{i}\\;\\mathrm {Softmax} (v\_{c,i}W\_{i})} ![{\displaystyle \sum _{i=1}^{n}p_{i}\;\mathrm {Softmax} (v_{c,i}W_{i})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b9d533f93e72999b787eb6bc89a24496ff7f8f94) , where p i {\\displaystyle p\_{i}} ![{\displaystyle p_{i}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5bab39399bf5424f25d957cdc57c84a0622626d2) is a probability distribution by a linear-softmax operation on the activations of the hidden neurons within the model. The original paper demonstrated its effectiveness for [recurrent neural networks](/wiki/Recurrent_neural_network "Recurrent neural network"). This was later found to work for Transformers as well.[\[18\]](#cite_note-18)

## Deep learning

\[[edit](/w/index.php?title=Mixture_of_experts&action=edit&section=6 "Edit section: Deep learning")\]

The previous section described MoE as it was used before the era of [deep learning](/wiki/Deep_learning "Deep learning"). After deep learning, MoE found applications in running the largest models, as a simple way to perform *conditional computation*: only parts of the model are used, the parts chosen according to what the input is.[\[19\]](#cite_note-19)

The earliest paper that applies MoE to deep learning dates back to 2013,[\[20\]](#cite_note-20) which proposed to use a different gating network at each layer in a deep neural network. Specifically, each gating is a linear-ReLU-linear-softmax network, and each expert is a linear-ReLU network. Since the output from the gating is not [sparse](/wiki/Sparse_matrix "Sparse matrix"), all expert outputs are needed, and no conditional computation is performed.

The key goal when using MoE in deep learning is to reduce computing cost. Consequently, for each query, only a small subset of the experts should be queried. This makes MoE in deep learning different from classical MoE. In classical MoE, the output for each query is a weighted sum of *all* experts' outputs. In deep learning MoE, the output for each query can only involve a few experts' outputs. Consequently, the key design choice in MoE becomes routing: given a batch of queries, how to route the queries to the best experts.

### Sparsely-gated MoE layer

\[[edit](/w/index.php?title=Mixture_of_experts&action=edit&section=7 "Edit section: Sparsely-gated MoE layer")\]

The **sparsely-gated MoE layer**,[\[21\]](#cite_note-21) published by researchers from [Google Brain](/wiki/Google_Brain "Google Brain"), uses [feedforward networks](/wiki/Feedforward_neural_network "Feedforward neural network") as experts, and linear-softmax gating. Similar to the previously proposed hard MoE, they achieve sparsity by a weighted sum of only the top-k experts, instead of the weighted sum of all of them. Specifically, in a MoE layer, there are [feedforward networks](/wiki/Feedforward_neural_network "Feedforward neural network") f 1 , . . . , f n {\\displaystyle f\_{1},...,f\_{n}} ![{\displaystyle f_{1},...,f_{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/56add4996a8ffb2d648fd1b373476afd13c2a117) , and a gating network w {\\displaystyle w} ![{\displaystyle w}](https://wikimedia.org/api/rest_v1/media/math/render/svg/88b1e0c8e1be5ebe69d18a8010676fa42d7961e6) . The gating network is defined by w ( x ) \= s o f t m a x ( t o p k ( W x + noise ) ) {\\displaystyle w(x)=\\mathrm {softmax} (\\mathrm {top} \_{k}(Wx+{\\text{noise}}))} ![{\displaystyle w(x)=\mathrm {softmax} (\mathrm {top} _{k}(Wx+{\text{noise}}))}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a798679ed693da58522319f96c3cc9e9bbbd895e) , where t o p k {\\displaystyle \\mathrm {top} \_{k}} ![{\displaystyle \mathrm {top} _{k}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b953143d48919e247b136b74223d2f8f07f0a089) is a function that keeps the top-k entries of a vector the same, but sets all other entries to − ∞ {\\displaystyle -\\infty } ![{\displaystyle -\infty }](https://wikimedia.org/api/rest_v1/media/math/render/svg/ca2608c4b5fd3bffc73585f8c67e379b4e99b6f1) . The addition of noise helps with load balancing.

The choice of k {\\displaystyle k} ![{\displaystyle k}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c3c9a2c7b599b37105512c5d570edc034056dd40) is a hyperparameter that is chosen according to application. Typical values are k \= 1 , 2 {\\displaystyle k=1,2} ![{\displaystyle k=1,2}](https://wikimedia.org/api/rest_v1/media/math/render/svg/32e3eb178c6c625b6ce7ac0a3a72e53d5fff44d6) . The k \= 1 {\\displaystyle k=1} ![{\displaystyle k=1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6c035ffa69b5bca8bf2d16c3da3aaad79a8bcbfa) version is also called the Switch Transformer. The original Switch Transformer was applied to a [T5 language model](/wiki/T5_\(language_model\) "T5 (language model)").[\[22\]](#cite_note-:1-22)

As demonstration, they trained a series of models for machine translation with alternating layers of MoE and [LSTM](/wiki/Long_short-term_memory "Long short-term memory"), and compared with deep LSTM models.[\[23\]](#cite_note-23) Table 3 shows that the MoE models used less inference time compute, despite having 30x more parameters.

This architectural module was published in 2017-01, within a few months of the publication of the [Transformer architecture](/wiki/Transformer_\(deep_learning\) "Transformer (deep learning)") (2017-06-12), and they were combined into a [multimodal](/wiki/Multimodal_learning "Multimodal learning") architecture called MultiModel published 4 days later (2017-06-16).[\[24\]](#cite_note-24)

### Load balancing

\[[edit](/w/index.php?title=Mixture_of_experts&action=edit&section=8 "Edit section: Load balancing")\]

Vanilla MoE tend to have issues of **load balancing**: some experts are consulted often, while other experts rarely or not at all. To encourage the gate to select each expert with equal frequency (proper load balancing) within each batch, each MoE layer has two auxiliary loss functions. This is improved by Switch Transformer[\[22\]](#cite_note-:1-22) into a single **auxiliary loss** function. Specifically, let n {\\displaystyle n} ![{\displaystyle n}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a601995d55609f2d9f5e233e36fbe9ea26011b3b) be the number of experts, then for a given batch of queries { x 1 , x 2 , . . . , x T } {\\displaystyle \\{x\_{1},x\_{2},...,x\_{T}\\}} ![{\displaystyle \{x_{1},x_{2},...,x_{T}\}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/83e91f0aa9841c2ddf2aa21ad35a7c2c4a7c040a) , the auxiliary loss for the batch is n ∑ i \= 1 n f i P i {\\displaystyle n\\sum \_{i=1}^{n}f\_{i}P\_{i}} ![{\displaystyle n\sum _{i=1}^{n}f_{i}P_{i}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e63bf8fbd0916eb3ad3c2b69ed2bad86ecf4b0a) Here, f i \= 1 T # ( queries sent to expert  i ) {\\displaystyle f\_{i}={\\frac {1}{T}}\\#({\\text{queries sent to expert }}i)} ![{\displaystyle f_{i}={\frac {1}{T}}\#({\text{queries sent to expert }}i)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6241be8c3a29ffc5188bd5239fbb0a6cc97432c6) is the fraction of tokens that chose expert i {\\displaystyle i} ![{\displaystyle i}](https://wikimedia.org/api/rest_v1/media/math/render/svg/add78d8608ad86e54951b8c8bd6c8d8416533d20) , and P i \= 1 T ∑ j \= 1 T w i ( x j ) ∑ i ′ ∈ experts w i ′ ( x j ) {\\displaystyle P\_{i}={\\frac {1}{T}}\\sum \_{j=1}^{T}{\\frac {w\_{i}(x\_{j})}{\\sum \_{i'\\in {\\text{experts}}}w\_{i'}(x\_{j})}}} ![{\displaystyle P_{i}={\frac {1}{T}}\sum _{j=1}^{T}{\frac {w_{i}(x_{j})}{\sum _{i'\in {\text{experts}}}w_{i'}(x_{j})}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b08a6c0f7731c272ce567b9d5f2c36d095d03a5) is the fraction of weight on expert i {\\displaystyle i} ![{\displaystyle i}](https://wikimedia.org/api/rest_v1/media/math/render/svg/add78d8608ad86e54951b8c8bd6c8d8416533d20) . This loss is minimized at 1 {\\displaystyle 1} ![{\displaystyle 1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/92d98b82a3778f043108d4e20960a9193df57cbf) , precisely when every expert has equal weight 1 / n {\\displaystyle 1/n} ![{\displaystyle 1/n}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f0e10667bad240500f5044257143510127e03d69) in all situations.

[![](//upload.wikimedia.org/wikipedia/commons/thumb/2/20/DeepSeek_MoE_and_MLA_%28DeepSeek-V2%29.svg/250px-DeepSeek_MoE_and_MLA_%28DeepSeek-V2%29.svg.png)](/wiki/File:DeepSeek_MoE_and_MLA_\(DeepSeek-V2\).svg)

The DeepSeek MoE architecture. Also shown is MLA, a variant of attention mechanism in Transformer.[\[25\]](#cite_note-:7-25): Figure 2 

Researchers at [DeepSeek](/wiki/DeepSeek "DeepSeek") designed a variant of MoE, with "shared experts" that are always queried, and "routed experts" that might not be. They found that standard load balancing encourages the experts to be equally consulted, but this then causes experts to replicate the same core capacity, such as English grammar. They proposed the shared experts to learn core capacities that are often used, and let the routed experts to learn the peripheral capacities that are rarely used.[\[26\]](#cite_note-:12-26)

They also proposed "auxiliary-loss-free load balancing strategy", which does not use auxiliary loss. Instead, each expert i {\\displaystyle i} ![{\displaystyle i}](https://wikimedia.org/api/rest_v1/media/math/render/svg/add78d8608ad86e54951b8c8bd6c8d8416533d20) has an extra "expert bias" b i {\\displaystyle b\_{i}} ![{\displaystyle b_{i}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/40a8c2db2990a53c683e75961826167c5adac7c3) . If an expert is being neglected, then their bias increases, and vice versa. During token assignment, each token picks the top-k experts, but with the bias added in. That is:[\[27\]](#cite_note-27) f ( x ) \= ∑ i  is in the top-k of  { w ( x ) j + b j } j w ( x ) i f i ( x ) {\\displaystyle f(x)=\\sum \_{i{\\text{ is in the top-k of }}\\{w(x)\_{j}+b\_{j}\\}\_{j}}w(x)\_{i}f\_{i}(x)} ![{\displaystyle f(x)=\sum _{i{\text{ is in the top-k of }}\{w(x)_{j}+b_{j}\}_{j}}w(x)_{i}f_{i}(x)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/cf78a4d7158076a4bd2536a853f1ce2096475511) Note that the expert bias matters for picking the experts, but not in adding up the responses from the experts.

### Capacity factor

\[[edit](/w/index.php?title=Mixture_of_experts&action=edit&section=9 "Edit section: Capacity factor")\]

Suppose there are n {\\displaystyle n} ![{\displaystyle n}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a601995d55609f2d9f5e233e36fbe9ea26011b3b) experts in a layer. For a given batch of queries { x 1 , x 2 , . . . , x T } {\\displaystyle \\{x\_{1},x\_{2},...,x\_{T}\\}} ![{\displaystyle \{x_{1},x_{2},...,x_{T}\}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/83e91f0aa9841c2ddf2aa21ad35a7c2c4a7c040a) , each query is routed to one or more experts. For example, if each query is routed to one expert as in Switch Transformers, and if the experts are load-balanced, then each expert should expect on average T / n {\\displaystyle T/n} ![{\displaystyle T/n}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e923812b990a1397e62786430eaf98baceb1e3f0) queries in a batch. In practice, the experts cannot expect perfect load balancing: in some batches, one expert might be underworked, while in other batches, it would be overworked.

Since the inputs cannot move through the layer until every expert in the layer has finished the queries it is assigned, load balancing is important. The **capacity factor** is sometimes used to enforce a hard constraint on load balancing. Each expert is only allowed to process up to c ⋅ T / n {\\displaystyle c\\cdot T/n} ![{\displaystyle c\cdot T/n}](https://wikimedia.org/api/rest_v1/media/math/render/svg/de9b5df73678442848db7580a54a85f6a8cb96c4) queries in a batch. The ST-MoE report found c ∈ \[ 1.25 , 2 \] {\\displaystyle c\\in \[1.25,2\]} ![{\displaystyle c\in [1.25,2]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/084b549d92989556d3d5a9686e2960eb0d3b3444) to work well in practice.[\[28\]](#cite_note-:4-28)

### Routing

\[[edit](/w/index.php?title=Mixture_of_experts&action=edit&section=10 "Edit section: Routing")\]

In the original sparsely-gated MoE, only the top-k experts are queried, and their outputs are weighted-summed. There are other methods.[\[28\]](#cite_note-:4-28) Generally speaking, routing is an [assignment problem](/wiki/Assignment_problem "Assignment problem"): How to assign tokens to experts, such that a variety of constraints are followed (such as throughput, load balancing, etc.)? There are typically three classes of routing algorithm: the experts choose the tokens ("**expert choice**"),[\[29\]](#cite_note-29) the tokens choose the experts (the original sparsely-gated MoE), and a global assigner matching experts and tokens.[\[30\]](#cite_note-:5-30)

During inference, the MoE works over a large batch of tokens at any time. If the tokens were to choose the experts, then some experts might get few tokens, while a few experts get so many tokens that it exceeds their maximum batch size, so they would have to ignore some of the tokens. Similarly, if the experts were to choose the tokens, then some tokens might not be picked by any expert. This is the "**token drop**" problem. Dropping a token is not necessarily a serious problem, since in Transformers, due to [residual connections](/wiki/Residual_connection "Residual connection"), if a token is "dropped", it does not disappear. Instead, its vector representation simply passes through the feedforward layer without change.[\[30\]](#cite_note-:5-30)

Other approaches include solving it as a [constrained linear programming](/wiki/Linear_programming "Linear programming") problem,[\[31\]](#cite_note-31) using [reinforcement learning](/wiki/Reinforcement_learning "Reinforcement learning") to train the routing algorithm (since picking an expert is a discrete action, like in RL).[\[32\]](#cite_note-32) The token-expert match may involve no learning ("**static routing**"): It can be done by a deterministic [hash function](/wiki/Hash_function "Hash function")[\[33\]](#cite_note-33) or a random number generator.[\[34\]](#cite_note-34)

### Applications to transformer models

\[[edit](/w/index.php?title=Mixture_of_experts&action=edit&section=11 "Edit section: Applications to transformer models")\]

MoE layers are used in the largest [transformer models](/wiki/Transformer_\(machine_learning_model\) "Transformer (machine learning model)"), for which learning and inferring over the full model is too costly. They are typically sparsely-gated, with sparsity 1 or 2. In Transformer models, the MoE layers are often used to select the [feedforward layers](/wiki/Feedforward_neural_network "Feedforward neural network") (typically a linear-ReLU-linear network), appearing in each Transformer block after the multiheaded attention. This is because the feedforward layers take up an increasing portion of the computing cost as models grow larger. For example, in the Palm-540B model, 90% of parameters are in its feedforward layers.[\[35\]](#cite_note-35)

A trained Transformer can be converted to a MoE by duplicating its feedforward layers, with randomly initialized gating, then trained further. This is a technique called "sparse upcycling".[\[36\]](#cite_note-36)

There are a large number of design choices involved in Transformer MoE that affect the training stability and final performance. The OLMoE report describes these in some detail.[\[37\]](#cite_note-37)

As of 2023[\[update\]](https://en.wikipedia.org/w/index.php?title=Mixture_of_experts&action=edit), models large enough to use MoE tend to be [large language models](/wiki/Large_language_model "Large language model"), where each expert has on the order of 10 billion parameters. Other than language models, Vision MoE[\[38\]](#cite_note-38) is a Transformer model with MoE layers. They demonstrated it by training a model with 15 billion parameters. MoE Transformer has also been applied for [diffusion models](/wiki/Diffusion_model "Diffusion model").[\[39\]](#cite_note-39)

A series of large language models from [Google](/wiki/Google "Google") used MoE. GShard[\[40\]](#cite_note-40) uses MoE with up to top-2 experts per layer. Specifically, the top-1 expert is always selected, and the top-2th expert is selected with probability proportional to that experts' weight according to the gating function. Later, GLaM[\[41\]](#cite_note-41) demonstrated a language model with 1.2 trillion parameters, each MoE layer using top-2 out of 64 experts. Switch Transformers[\[22\]](#cite_note-:1-22) use top-1 in all MoE layers.

The NLLB-200 by [Meta AI](/wiki/Meta_AI "Meta AI") is a machine translation model for 200 languages.[\[42\]](#cite_note-42) Each MoE layer uses a hierarchical MoE with two levels. On the first level, the gating function chooses to use either a "shared" feedforward layer, or to use the experts. If using the experts, then another gating function computes the weights and chooses the top-2 experts.[\[43\]](#cite_note-43)

MoE large language models can be adapted for downstream tasks by [instruction tuning](/wiki/Instruction_tuning "Instruction tuning").[\[44\]](#cite_note-44)

In December 2023, [Mistral AI](/wiki/Mistral_AI "Mistral AI") released Mixtral 8x7B under Apache 2.0 license. It is a MoE language model with 46.7B parameters, 8 experts, and sparsity 2. They also released a version finetuned for instruction following.[\[45\]](#cite_note-45)[\[46\]](#cite_note-46)

In March 2024, Databricks released [DBRX](/wiki/DBRX "DBRX"). It is a MoE language model with 132B parameters, 16 experts, and sparsity 4. They also released a version finetuned for instruction following.[\[47\]](#cite_note-:02-47)[\[48\]](#cite_note-48)

## See also

\[[edit](/w/index.php?title=Mixture_of_experts&action=edit&section=12 "Edit section: See also")\]

-   [Product of experts](/wiki/Product_of_experts "Product of experts")
-   [Mixture models](/wiki/Mixture_model "Mixture model")
-   [Mixture of gaussians](/wiki/Mixture_of_gaussians "Mixture of gaussians")
-   [Ensemble learning](/wiki/Ensemble_learning "Ensemble learning")

## References

\[[edit](/w/index.php?title=Mixture_of_experts&action=edit&section=13 "Edit section: References")\]

1.  **[^](#cite_ref-1)** Baldacchino, Tara; Cross, Elizabeth J.; Worden, Keith; Rowson, Jennifer (2016). "Variational Bayesian mixture of experts models and sensitivity analysis for nonlinear dynamical systems". *Mechanical Systems and Signal Processing*. 66–67: 178–200\. [Bibcode](/wiki/Bibcode_\(identifier\) "Bibcode (identifier)"):[2016MSSP...66..178B](https://ui.adsabs.harvard.edu/abs/2016MSSP...66..178B). [doi](/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/j.ymssp.2015.05.009](https://doi.org/10.1016%2Fj.ymssp.2015.05.009).
2.  **[^](#cite_ref-2)** Rokach, Lior (November 2009). *Pattern Classification Using Ensemble Methods*. Series in Machine Perception and Artificial Intelligence. Vol. 75. WORLD SCIENTIFIC. p. 142. [doi](/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1142/7238](https://doi.org/10.1142%2F7238). [ISBN](/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-981-4271-06-6](/wiki/Special:BookSources/978-981-4271-06-6 "Special:BookSources/978-981-4271-06-6").
3.  **[^](#cite_ref-3)** TRESP, V. (2001). ["Committee Machines"](https://cir.nii.ac.jp/crid/1573387450424676096). *Handbook of Neural Network Signal Processing*. Electrical Engineering & Applied Signal Processing Series. Vol. 5. [doi](/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1201/9781420038613.ch5](https://doi.org/10.1201%2F9781420038613.ch5) (inactive 1 July 2025). [ISBN](/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-8493-2359-1](/wiki/Special:BookSources/978-0-8493-2359-1 "Special:BookSources/978-0-8493-2359-1").`{{[cite book](/wiki/Template:Cite_book "Template:Cite book")}}`: CS1 maint: DOI inactive as of July 2025 ([link](/wiki/Category:CS1_maint:_DOI_inactive_as_of_July_2025 "Category:CS1 maint: DOI inactive as of July 2025"))
4.  **[^](#cite_ref-4)** Hampshire, J.B.; Waibel, A. (July 1992). ["The Meta-Pi network: building distributed knowledge representations for robust multisource pattern recognition"](https://isl.anthropomatik.kit.edu/downloads/The_Meta-Pi_Network-_Building_Distributed_Knowledge_Representations_for_Robust_Multi-Source_Pattern_Recognition.pdf) (PDF). *IEEE Transactions on Pattern Analysis and Machine Intelligence*. **14** (7): 751–769\. [doi](/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1109/34.142911](https://doi.org/10.1109%2F34.142911).
5.  **[^](#cite_ref-5)** Alexander Waibel; Toshiyuki Hanazawa; Geoffrey Hinton; Kiyohiro Shikano; Kevin J. Lang (1995). ["Phoneme Recognition Using Time-Delay Neural Networks\*"](https://www.taylorfrancis.com/chapters/edit/10.4324/9780203763247-2/phoneme-recognition-using-time-delay-neural-networks-alexander-waibel-toshiyuki-hanazawa-geoffrey-hinton-kiyohiro-shikano-kevin-lang). In Chauvin, Yves; Rumelhart, David E. (eds.). *Backpropagation*. Psychology Press. [doi](/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.4324/9780203763247](https://doi.org/10.4324%2F9780203763247). [ISBN](/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-203-76324-7](/wiki/Special:BookSources/978-0-203-76324-7 "Special:BookSources/978-0-203-76324-7").
6.  **[^](#cite_ref-6)** Nowlan, Steven; Hinton, Geoffrey E (1990). ["Evaluation of Adaptive Mixtures of Competing Experts"](https://proceedings.neurips.cc/paper/1990/hash/432aca3a1e345e339f35a30c8f65edce-Abstract.html). *Advances in Neural Information Processing Systems*. **3**. Morgan-Kaufmann.
7.  **[^](#cite_ref-7)** Jacobs, Robert A.; Jordan, Michael I.; Nowlan, Steven J.; Hinton, Geoffrey E. (February 1991). ["Adaptive Mixtures of Local Experts"](https://direct.mit.edu/neco/article/3/1/79-87/5560). *Neural Computation*. **3** (1): 79–87\. [doi](/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1162/neco.1991.3.1.79](https://doi.org/10.1162%2Fneco.1991.3.1.79). [ISSN](/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0899-7667](https://search.worldcat.org/issn/0899-7667). [PMID](/wiki/PMID_\(identifier\) "PMID (identifier)") [31141872](https://pubmed.ncbi.nlm.nih.gov/31141872). [S2CID](/wiki/S2CID_\(identifier\) "S2CID (identifier)") [572361](https://api.semanticscholar.org/CorpusID:572361).
8.  ^ [***a***](#cite_ref-:0_8-0) [***b***](#cite_ref-:0_8-1) Jordan, Michael; Jacobs, Robert (1991). ["Hierarchies of adaptive experts"](https://proceedings.neurips.cc/paper_files/paper/1991/hash/59b90e1005a220e2ebc542eb9d950b1e-Abstract.html). *Advances in Neural Information Processing Systems*. **4**. Morgan-Kaufmann.
9.  ^ [***a***](#cite_ref-:2_9-0) [***b***](#cite_ref-:2_9-1) Jordan, Michael I.; Jacobs, Robert A. (March 1994). ["Hierarchical Mixtures of Experts and the EM Algorithm"](https://direct.mit.edu/neco/article/6/2/181-214/5779). *Neural Computation*. **6** (2): 181–214\. [doi](/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1162/neco.1994.6.2.181](https://doi.org/10.1162%2Fneco.1994.6.2.181). [hdl](/wiki/Hdl_\(identifier\) "Hdl (identifier)"):[1721.1/7206](https://hdl.handle.net/1721.1%2F7206). [ISSN](/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0899-7667](https://search.worldcat.org/issn/0899-7667).
10.  ^ [***a***](#cite_ref-:3_10-0) [***b***](#cite_ref-:3_10-1) Jordan, Michael I.; Xu, Lei (1995-01-01). "Convergence results for the EM approach to mixtures of experts architectures %2895%2900014-3". *Neural Networks*. **8** (9): 1409–1431\. [doi](/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/0893-6080(95)00014-3](https://doi.org/10.1016%2F0893-6080%2895%2900014-3). [hdl](/wiki/Hdl_\(identifier\) "Hdl (identifier)"):[1721.1/6620](https://hdl.handle.net/1721.1%2F6620). [ISSN](/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0893-6080](https://search.worldcat.org/issn/0893-6080).
11.  **[^](#cite_ref-11)** Xu, Lei; Jordan, Michael; Hinton, Geoffrey E (1994). ["An Alternative Model for Mixtures of Experts"](https://proceedings.neurips.cc/paper/1994/hash/c8fbbc86abe8bd6a5eb6a3b4d0411301-Abstract.html). *Advances in Neural Information Processing Systems*. **7**. MIT Press.
12.  **[^](#cite_ref-12)** Collobert, Ronan; Bengio, Samy; Bengio, Yoshua (2001). ["A Parallel Mixture of SVMs for Very Large Scale Problems"](https://proceedings.neurips.cc/paper_files/paper/2001/hash/36ac8e558ac7690b6f44e2cb5ef93322-Abstract.html). *Advances in Neural Information Processing Systems*. **14**. MIT Press.
13.  **[^](#cite_ref-13)** Goodfellow, Ian; Bengio, Yoshua; Courville, Aaron (2016). "12: Applications". *Deep learning*. Adaptive computation and machine learning. Cambridge, Mass: The MIT press. [ISBN](/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-262-03561-3](/wiki/Special:BookSources/978-0-262-03561-3 "Special:BookSources/978-0-262-03561-3").
14.  **[^](#cite_ref-14)** Nguyen, Hien D.; McLachlan, Geoffrey J. (2016-01-01). ["Laplace mixture of linear experts"](https://www.sciencedirect.com/science/article/pii/S0167947314003089). *Computational Statistics & Data Analysis*. **93**: 177–191\. [doi](/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/j.csda.2014.10.016](https://doi.org/10.1016%2Fj.csda.2014.10.016). [ISSN](/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0167-9473](https://search.worldcat.org/issn/0167-9473).
15.  **[^](#cite_ref-15)** Chamroukhi, F. (2016-07-01). ["Robust mixture of experts modeling using the t distribution"](https://www.sciencedirect.com/science/article/pii/S0893608016000435). *Neural Networks*. **79**: 20–36\. [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[1701.07429](https://arxiv.org/abs/1701.07429). [doi](/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/j.neunet.2016.03.002](https://doi.org/10.1016%2Fj.neunet.2016.03.002). [ISSN](/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0893-6080](https://search.worldcat.org/issn/0893-6080). [PMID](/wiki/PMID_\(identifier\) "PMID (identifier)") [27093693](https://pubmed.ncbi.nlm.nih.gov/27093693). [S2CID](/wiki/S2CID_\(identifier\) "S2CID (identifier)") [3171144](https://api.semanticscholar.org/CorpusID:3171144).
16.  **[^](#cite_ref-16)** Chen, K.; Xu, L.; Chi, H. (1999-11-01). ["Improved learning algorithms for mixture of experts in multiclass classification"](https://www.sciencedirect.com/science/article/pii/S089360809900043X). *Neural Networks*. **12** (9): 1229–1252\. [doi](/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/S0893-6080(99)00043-X](https://doi.org/10.1016%2FS0893-6080%2899%2900043-X). [ISSN](/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0893-6080](https://search.worldcat.org/issn/0893-6080). [PMID](/wiki/PMID_\(identifier\) "PMID (identifier)") [12662629](https://pubmed.ncbi.nlm.nih.gov/12662629).
17.  **[^](#cite_ref-17)** Yang, Zhilin; Dai, Zihang; Salakhutdinov, Ruslan; Cohen, William W. (2017-11-10). "Breaking the Softmax Bottleneck: A High-Rank RNN Language Model". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[1711.03953](https://arxiv.org/abs/1711.03953) \[[cs.CL](https://arxiv.org/archive/cs.CL)\].
18.  **[^](#cite_ref-18)** Narang, Sharan; Chung, Hyung Won; Tay, Yi; Fedus, William; Fevry, Thibault; Matena, Michael; Malkan, Karishma; Fiedel, Noah; Shazeer, Noam (2021-02-23). "Do Transformer Modifications Transfer Across Implementations and Applications?". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2102.11972](https://arxiv.org/abs/2102.11972) \[[cs.LG](https://arxiv.org/archive/cs.LG)\].
19.  **[^](#cite_ref-19)** Bengio, Yoshua; Léonard, Nicholas; Courville, Aaron (2013). "Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[1308.3432](https://arxiv.org/abs/1308.3432) \[[cs.LG](https://arxiv.org/archive/cs.LG)\].
20.  **[^](#cite_ref-20)** Eigen, David; Ranzato, Marc'Aurelio; Sutskever, Ilya (2013). "Learning Factored Representations in a Deep Mixture of Experts". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[1312.4314](https://arxiv.org/abs/1312.4314) \[[cs.LG](https://arxiv.org/archive/cs.LG)\].
21.  **[^](#cite_ref-21)** Shazeer, Noam; Mirhoseini, Azalia; Maziarz, Krzysztof; Davis, Andy; Le, Quoc; Hinton, Geoffrey; Dean, Jeff (2017). "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[1701.06538](https://arxiv.org/abs/1701.06538) \[[cs.LG](https://arxiv.org/archive/cs.LG)\].
22.  ^ [***a***](#cite_ref-:1_22-0) [***b***](#cite_ref-:1_22-1) [***c***](#cite_ref-:1_22-2) Fedus, William; Zoph, Barret; Shazeer, Noam (2022-01-01). ["Switch transformers: scaling to trillion parameter models with simple and efficient sparsity"](https://dl.acm.org/doi/abs/10.5555/3586589.3586709). *The Journal of Machine Learning Research*. **23** (1): 5232–5270\. [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2101.03961](https://arxiv.org/abs/2101.03961). [ISSN](/wiki/ISSN_\(identifier\) "ISSN (identifier)") [1532-4435](https://search.worldcat.org/issn/1532-4435).
23.  **[^](#cite_ref-23)** Wu, Yonghui; Schuster, Mike; Chen, Zhifeng; Le, Quoc V.; Norouzi, Mohammad; Macherey, Wolfgang; Krikun, Maxim; Cao, Yuan; Gao, Qin; Macherey, Klaus; Klingner, Jeff; Shah, Apurva; Johnson, Melvin; Liu, Xiaobing; Kaiser, Łukasz (2016). "Google's Neural Machine Translation System: Bridging the Gap between Human and Machine Translation". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[1609.08144](https://arxiv.org/abs/1609.08144) \[[cs.CL](https://arxiv.org/archive/cs.CL)\].
24.  **[^](#cite_ref-24)** Kaiser, Lukasz; Gomez, Aidan N.; Shazeer, Noam; Vaswani, Ashish; Parmar, Niki; Jones, Llion; Uszkoreit, Jakob (2017-06-16). ["One Model To Learn Them All"](https://arxiv.org/abs/1706.05137v1). *arXiv.org*.
25.  **[^](#cite_ref-:7_25-0)** DeepSeek-AI; Liu, Aixin; Feng, Bei; Wang, Bin; Wang, Bingxuan; Liu, Bo; Zhao, Chenggang; Dengr, Chengqi; Ruan, Chong (19 June 2024). "DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2405.04434](https://arxiv.org/abs/2405.04434) \[[cs.CL](https://arxiv.org/archive/cs.CL)\]..
26.  **[^](#cite_ref-:12_26-0)** Dai, Damai; Deng, Chengqi; Zhao, Chenggang; Xu, R. X.; Gao, Huazuo; Chen, Deli; Li, Jiashi; Zeng, Wangding; Yu, Xingkai (11 January 2024). "DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2401.06066](https://arxiv.org/abs/2401.06066) \[[cs.CL](https://arxiv.org/archive/cs.CL)\].
27.  **[^](#cite_ref-27)** DeepSeek-AI; Liu, Aixin; Feng, Bei; Xue, Bing; Wang, Bingxuan; Wu, Bochao; Lu, Chengda; Zhao, Chenggang; Deng, Chengqi (2024-12-27). "DeepSeek-V3 Technical Report". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2412.19437](https://arxiv.org/abs/2412.19437) \[[cs.CL](https://arxiv.org/archive/cs.CL)\].
28.  ^ [***a***](#cite_ref-:4_28-0) [***b***](#cite_ref-:4_28-1) Zoph, Barret; Bello, Irwan; Kumar, Sameer; Du, Nan; Huang, Yanping; Dean, Jeff; Shazeer, Noam; Fedus, William (2022). "ST-MoE: Designing Stable and Transferable Sparse Expert Models". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2202.08906](https://arxiv.org/abs/2202.08906) \[[cs.CL](https://arxiv.org/archive/cs.CL)\].
29.  **[^](#cite_ref-29)** Zhou, Yanqi; Lei, Tao; Liu, Hanxiao; Du, Nan; Huang, Yanping; Zhao, Vincent; Dai, Andrew M.; Chen, Zhifeng; Le, Quoc V.; Laudon, James (2022-12-06). ["Mixture-of-Experts with Expert Choice Routing"](https://proceedings.neurips.cc/paper_files/paper/2022/hash/2f00ecd787b432c1d36f3de9800728eb-Abstract-Conference.html). *Advances in Neural Information Processing Systems*. **35**: 7103–7114\. [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2202.09368](https://arxiv.org/abs/2202.09368).
30.  ^ [***a***](#cite_ref-:5_30-0) [***b***](#cite_ref-:5_30-1) Fedus, William; Dean, Jeff; Zoph, Barret (2022-09-04). "A Review of Sparse Expert Models in Deep Learning". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2209.01667](https://arxiv.org/abs/2209.01667) \[[cs.LG](https://arxiv.org/archive/cs.LG)\].
31.  **[^](#cite_ref-31)** Lewis, Mike; Bhosale, Shruti; Dettmers, Tim; Goyal, Naman; Zettlemoyer, Luke (2021-07-01). ["BASE Layers: Simplifying Training of Large, Sparse Models"](https://proceedings.mlr.press/v139/lewis21a.html). *Proceedings of the 38th International Conference on Machine Learning*. PMLR: 6265–6274\. [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2103.16716](https://arxiv.org/abs/2103.16716).
32.  **[^](#cite_ref-32)** Bengio, Emmanuel; Bacon, Pierre-Luc; Pineau, Joelle; Precup, Doina (2015). "Conditional Computation in Neural Networks for faster models". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[1511.06297](https://arxiv.org/abs/1511.06297) \[[cs.LG](https://arxiv.org/archive/cs.LG)\].
33.  **[^](#cite_ref-33)** Roller, Stephen; Sukhbaatar, Sainbayar; szlam, arthur; Weston, Jason (2021). ["Hash Layers For Large Sparse Models"](https://proceedings.neurips.cc/paper_files/paper/2021/hash/92bf5e6240737e0326ea59846a83e076-Abstract.html). *Advances in Neural Information Processing Systems*. **34**. Curran Associates, Inc.: 17555–17566.
34.  **[^](#cite_ref-34)** Zuo, Simiao; Liu, Xiaodong; Jiao, Jian; Kim, Young Jin; Hassan, Hany; Zhang, Ruofei; Zhao, Tuo; Gao, Jianfeng (2022-02-03). "Taming Sparsely Activated Transformer with Stochastic Experts". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2110.04260](https://arxiv.org/abs/2110.04260) \[[cs.CL](https://arxiv.org/archive/cs.CL)\].
35.  **[^](#cite_ref-35)** ["Transformer Deep Dive: Parameter Counting"](https://orenleung.com/transformer-parameter-counting). *Transformer Deep Dive: Parameter Counting*. Retrieved 2023-10-10.
36.  **[^](#cite_ref-36)** Komatsuzaki, Aran; Puigcerver, Joan; Lee-Thorp, James; Ruiz, Carlos Riquelme; Mustafa, Basil; Ainslie, Joshua; Tay, Yi; Dehghani, Mostafa; Houlsby, Neil (2023-02-17). "Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2212.05055](https://arxiv.org/abs/2212.05055) \[[cs.LG](https://arxiv.org/archive/cs.LG)\].
37.  **[^](#cite_ref-37)** Muennighoff, Niklas; Soldaini, Luca; Groeneveld, Dirk; Lo, Kyle; Morrison, Jacob; Min, Sewon; Shi, Weijia; Walsh, Pete; Tafjord, Oyvind (2024-09-03). "OLMoE: Open Mixture-of-Experts Language Models". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2409.02060](https://arxiv.org/abs/2409.02060) \[[cs.CL](https://arxiv.org/archive/cs.CL)\].
38.  **[^](#cite_ref-38)** Riquelme, Carlos; Puigcerver, Joan; Mustafa, Basil; Neumann, Maxim; Jenatton, Rodolphe; Susano Pinto, André; Keysers, Daniel; Houlsby, Neil (2021). ["Scaling Vision with Sparse Mixture of Experts"](https://proceedings.neurips.cc/paper/2021/hash/48237d9f2dea8c74c2a72126cf63d933-Abstract.html). *Advances in Neural Information Processing Systems*. **34**: 8583–8595\. [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2106.05974](https://arxiv.org/abs/2106.05974).
39.  **[^](#cite_ref-39)** Fei, Zhengcong; Fan, Mingyuan; Yu, Changqian; Li, Debang; Huang, Junshi (2024-07-16). "Scaling Diffusion Transformers to 16 Billion Parameters". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2407.11633](https://arxiv.org/abs/2407.11633) \[[cs.CV](https://arxiv.org/archive/cs.CV)\].
40.  **[^](#cite_ref-40)** Lepikhin, Dmitry; Lee, HyoukJoong; Xu, Yuanzhong; Chen, Dehao; Firat, Orhan; Huang, Yanping; Krikun, Maxim; Shazeer, Noam; Chen, Zhifeng (2020). "GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2006.16668](https://arxiv.org/abs/2006.16668) \[[cs.CL](https://arxiv.org/archive/cs.CL)\].
41.  **[^](#cite_ref-41)** Du, Nan; Huang, Yanping; Dai, Andrew M.; Tong, Simon; Lepikhin, Dmitry; Xu, Yuanzhong; Krikun, Maxim; Zhou, Yanqi; Yu, Adams Wei; Firat, Orhan; Zoph, Barret; Fedus, Liam; Bosma, Maarten; Zhou, Zongwei; Wang, Tao (2021). "GLaM: Efficient Scaling of Language Models with Mixture-of-Experts". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2112.06905](https://arxiv.org/abs/2112.06905) \[[cs.CL](https://arxiv.org/archive/cs.CL)\].
42.  **[^](#cite_ref-42)** ["200 languages within a single AI model: A breakthrough in high-quality machine translation"](https://web.archive.org/web/20230109051700/https://ai.facebook.com/blog/nllb-200-high-quality-machine-translation/). *ai.facebook.com*. 2022-06-19. Archived from [the original](https://ai.facebook.com/blog/nllb-200-high-quality-machine-translation/) on 2023-01-09.
43.  **[^](#cite_ref-43)** NLLB Team; Costa-jussà, Marta R.; Cross, James; Çelebi, Onur; Elbayad, Maha; Heafield, Kenneth; Heffernan, Kevin; Kalbassi, Elahe; Lam, Janice; Licht, Daniel; Maillard, Jean; Sun, Anna; Wang, Skyler; Wenzek, Guillaume; Youngblood, Al (2022). "No Language Left Behind: Scaling Human-Centered Machine Translation". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2207.04672](https://arxiv.org/abs/2207.04672) \[[cs.CL](https://arxiv.org/archive/cs.CL)\].
44.  **[^](#cite_ref-44)** Shen, Sheng; Hou, Le; Zhou, Yanqi; Du, Nan; Longpre, Shayne; Wei, Jason; Chung, Hyung Won; Zoph, Barret; Fedus, William; Chen, Xinyun; Vu, Tu; Wu, Yuexin; Chen, Wuyang; Webson, Albert; Li, Yunxuan (2023). "Mixture-of-Experts Meets Instruction Tuning:A Winning Combination for Large Language Models". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2305.14705](https://arxiv.org/abs/2305.14705) \[[cs.CL](https://arxiv.org/archive/cs.CL)\].
45.  **[^](#cite_ref-45)** AI, Mistral (2023-12-11). ["Mixtral of experts"](https://mistral.ai/news/mixtral-of-experts/). *mistral.ai*. Retrieved 2024-02-04.
46.  **[^](#cite_ref-46)** Jiang, Albert Q.; Sablayrolles, Alexandre; Roux, Antoine; Mensch, Arthur; Savary, Blanche; Bamford, Chris; Chaplot, Devendra Singh; Casas, Diego de las; Hanna, Emma Bou (2024-01-08). "Mixtral of Experts". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2401.04088](https://arxiv.org/abs/2401.04088) \[[cs.LG](https://arxiv.org/archive/cs.LG)\].
47.  **[^](#cite_ref-:02_47-0)** ["Introducing DBRX: A New State-of-the-Art Open LLM"](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm). *Databricks*. 2024-03-27. Retrieved 2024-03-28.
48.  **[^](#cite_ref-48)** Knight, Will. ["Inside the Creation of the World's Most Powerful Open Source AI Model"](https://www.wired.com/story/dbrx-inside-the-creation-of-the-worlds-most-powerful-open-source-ai-model/). *Wired*. [ISSN](/wiki/ISSN_\(identifier\) "ISSN (identifier)") [1059-1028](https://search.worldcat.org/issn/1059-1028). Retrieved 2024-03-28.

## Further reading

\[[edit](/w/index.php?title=Mixture_of_experts&action=edit&section=14 "Edit section: Further reading")\]

-   Before deep learning era
    -   McLachlan, Geoffrey J.; Peel, David (2000). *Finite mixture models*. Wiley series in probability and statistics applied probability and statistics section. New York Chichester Weinheim Brisbane Singapore Toronto: John Wiley & Sons, Inc. [ISBN](/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-471-00626-8](/wiki/Special:BookSources/978-0-471-00626-8 "Special:BookSources/978-0-471-00626-8").
    -   Yuksel, S. E.; Wilson, J. N.; Gader, P. D. (August 2012). "Twenty Years of Mixture of Experts". *IEEE Transactions on Neural Networks and Learning Systems*. **23** (8): 1177–1193\. [Bibcode](/wiki/Bibcode_\(identifier\) "Bibcode (identifier)"):[2012ITNNL..23.1177Y](https://ui.adsabs.harvard.edu/abs/2012ITNNL..23.1177Y). [doi](/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1109/TNNLS.2012.2200299](https://doi.org/10.1109%2FTNNLS.2012.2200299). [ISSN](/wiki/ISSN_\(identifier\) "ISSN (identifier)") [2162-237X](https://search.worldcat.org/issn/2162-237X). [PMID](/wiki/PMID_\(identifier\) "PMID (identifier)") [24807516](https://pubmed.ncbi.nlm.nih.gov/24807516). [S2CID](/wiki/S2CID_\(identifier\) "S2CID (identifier)") [9922492](https://api.semanticscholar.org/CorpusID:9922492).
    -   Masoudnia, Saeed; Ebrahimpour, Reza (12 May 2012). "Mixture of experts: a literature survey". *Artificial Intelligence Review*. **42** (2): 275–293\. [doi](/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/s10462-012-9338-y](https://doi.org/10.1007%2Fs10462-012-9338-y). [S2CID](/wiki/S2CID_\(identifier\) "S2CID (identifier)") [3185688](https://api.semanticscholar.org/CorpusID:3185688).
    -   Nguyen, Hien D.; Chamroukhi, Faicel (July 2018). ["Practical and theoretical aspects of mixture-of-experts modeling: An overview"](https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.1246). *WIREs Data Mining and Knowledge Discovery*. **8** (4) e1246. [doi](/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1002/widm.1246](https://doi.org/10.1002%2Fwidm.1246). [ISSN](/wiki/ISSN_\(identifier\) "ISSN (identifier)") [1942-4787](https://search.worldcat.org/issn/1942-4787). [S2CID](/wiki/S2CID_\(identifier\) "S2CID (identifier)") [49301452](https://api.semanticscholar.org/CorpusID:49301452).
-   Practical techniques for training MoE Transformer models
    -   Zoph, Barret; Bello, Irwan; Kumar, Sameer; Du, Nan; Huang, Yanping; Dean, Jeff; Shazeer, Noam; Fedus, William (2022). "ST-MoE: Designing Stable and Transferable Sparse Expert Models". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2202.08906](https://arxiv.org/abs/2202.08906) \[[cs.CL](https://arxiv.org/archive/cs.CL)\].
    -   Muennighoff, Niklas; Soldaini, Luca; Groeneveld, Dirk; Lo, Kyle; Morrison, Jacob; Min, Sewon; Shi, Weijia; Walsh, Pete; Tafjord, Oyvind; Lambert, Nathan; Gu, Yuling; Arora, Shane; Bhagia, Akshita; Schwenk, Dustin; Wadden, David; Wettig, Alexander; Hui, Binyuan; Dettmers, Tim; Kiela, Douwe; Farhadi, Ali; Smith, Noah A.; Pang Wei Koh; Singh, Amanpreet; [Hajishirzi, Hannaneh](/wiki/Hanna_Hajishirzi "Hanna Hajishirzi") (2024). "OLMoE: Open Mixture-of-Experts Language Models". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2409.02060](https://arxiv.org/abs/2409.02060) \[[cs.CL](https://arxiv.org/archive/cs.CL)\]., with associated data release at ["allenai/OLMoE"](https://github.com/allenai/OLMoE). Ai2. 2024-10-17. Retrieved 2024-10-18.
    -   Rajbhandari, Samyam; Li, Conglong; Yao, Zhewei; Zhang, Minjia; Reza Yazdani Aminabadi; Ammar Ahmad Awan; Rasley, Jeff; He, Yuxiong (2022). "DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training to Power Next-Generation AI Scale". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2201.05596](https://arxiv.org/abs/2201.05596) \[[cs.LG](https://arxiv.org/archive/cs.LG)\].
    -   DeepSeek-AI; et al. (2024). "DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2405.04434](https://arxiv.org/abs/2405.04434) \[[cs.CL](https://arxiv.org/archive/cs.CL)\].
    -   DeepSeek-AI; et al. (2024). "DeepSeek-V3 Technical Report". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2412.19437](https://arxiv.org/abs/2412.19437) \[[cs.CL](https://arxiv.org/archive/cs.CL)\].
    -   Jin, Chao; Jiang, Ziheng; Bai, Zhihao; Zhong, Zheng; Liu, Juncai; Li, Xiang; Zheng, Ningxin; Wang, Xi; Xie, Cong; Huang, Qi; Heng, Wen; Ma, Yiyuan; Bao, Wenlei; Zheng, Size; Peng, Yanghua; Lin, Haibin; Liu, Xuanzhe; Jin, Xin; Liu, Xin (2025). "MegaScale-MoE: Large-Scale Communication-Efficient Training of Mixture-of-Experts Models in Production". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2505.11432](https://arxiv.org/abs/2505.11432) \[[cs.LG](https://arxiv.org/archive/cs.LG)\].
-   Literature review for deep learning era
    -   Fedus, William; Dean, Jeff; Zoph, Barret (2022). "A Review of Sparse Expert Models in Deep Learning". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2209.01667](https://arxiv.org/abs/2209.01667) \[[cs.LG](https://arxiv.org/archive/cs.LG)\].
    -   Fuzhao, Xue (2024-07-21). ["XueFuzhao/awesome-mixture-of-experts"](https://github.com/XueFuzhao/awesome-mixture-of-experts). *[GitHub](/wiki/GitHub "GitHub")*. Retrieved 2024-07-21.
    -   Vats, Arpita (2024-09-02). ["arpita8/Awesome-Mixture-of-Experts-Papers"](https://github.com/arpita8/Awesome-Mixture-of-Experts-Papers?tab=readme-ov-file). *[GitHub](/wiki/GitHub "GitHub")*. Retrieved 2024-09-06.
    -   Cai, Weilin; Jiang, Juyong; Wang, Fan; Tang, Jing; Kim, Sunghun; Huang, Jiayi (2025). "A Survey on Mixture of Experts in Large Language Models". *IEEE Transactions on Knowledge and Data Engineering*. **37** (7): 3896. [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2407.06204](https://arxiv.org/abs/2407.06204). [Bibcode](/wiki/Bibcode_\(identifier\) "Bibcode (identifier)"):[2025IDSO...37.3896C](https://ui.adsabs.harvard.edu/abs/2025IDSO...37.3896C). [doi](/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1109/TKDE.2025.3554028](https://doi.org/10.1109%2FTKDE.2025.3554028).

![](https://en.wikipedia.org/wiki/Special:CentralAutoLogin/start?useformat=desktop&type=1x1&usesul3=1)

Retrieved from "[https://en.wikipedia.org/w/index.php?title=Mixture\_of\_experts&oldid=1346279093](https://en.wikipedia.org/w/index.php?title=Mixture_of_experts&oldid=1346279093)"

[Category](/wiki/Help:Category "Help:Category"):

-   [Machine learning algorithms](/wiki/Category:Machine_learning_algorithms "Category:Machine learning algorithms")

Hidden categories:

-   [CS1: long volume value](/wiki/Category:CS1:_long_volume_value "Category:CS1: long volume value")
-   [CS1 maint: DOI inactive as of July 2025](/wiki/Category:CS1_maint:_DOI_inactive_as_of_July_2025 "Category:CS1 maint: DOI inactive as of July 2025")
-   [Articles with short description](/wiki/Category:Articles_with_short_description "Category:Articles with short description")
-   [Short description matches Wikidata](/wiki/Category:Short_description_matches_Wikidata "Category:Short description matches Wikidata")
-   [Articles containing potentially dated statements from 2023](/wiki/Category:Articles_containing_potentially_dated_statements_from_2023 "Category:Articles containing potentially dated statements from 2023")
-   [All articles containing potentially dated statements](/wiki/Category:All_articles_containing_potentially_dated_statements "Category:All articles containing potentially dated statements")

-   This page was last edited on 31 March 2026, at 00:23 (UTC).
-   Text is available under the [Creative Commons Attribution-ShareAlike 4.0 License](/wiki/Wikipedia:Text_of_the_Creative_Commons_Attribution-ShareAlike_4.0_International_License "Wikipedia:Text of the Creative Commons Attribution-ShareAlike 4.0 International License"); additional terms may apply. By using this site, you agree to the [Terms of Use](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Terms_of_Use "foundation:Special:MyLanguage/Policy:Terms of Use") and [Privacy Policy](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy "foundation:Special:MyLanguage/Policy:Privacy policy"). Wikipedia® is a registered trademark of the [Wikimedia Foundation, Inc.](https://wikimediafoundation.org/), a non-profit organization.

-   [Privacy policy](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy)
-   [About Wikipedia](/wiki/Wikipedia:About)
-   [Disclaimers](/wiki/Wikipedia:General_disclaimer)
-   [Contact Wikipedia](//en.wikipedia.org/wiki/Wikipedia:Contact_us)
-   [Legal & safety contacts](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Legal:Wikimedia_Foundation_Legal_and_Safety_Contact_Information)
-   [Code of Conduct](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Universal_Code_of_Conduct)
-   [Developers](https://developer.wikimedia.org)
-   [Statistics](https://stats.wikimedia.org/#/en.wikipedia.org)
-   [Cookie statement](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Cookie_statement)
-   [Mobile view](//en.wikipedia.org/w/index.php?title=Mixture_of_experts&mobileaction=toggle_view_mobile)

-   [![Wikimedia Foundation](/static/images/footer/wikimedia.svg)](https://www.wikimedia.org/)
-   [![Powered by MediaWiki](/w/resources/assets/mediawiki_compact.svg)](https://www.mediawiki.org/)

Search

Search

 Toggle the table of contents

Mixture of experts

[](#)[](#)[](#)[](#)[](#)[](#)[](#)

9 languages [Add topic](#)