# Advanced Lifespan Intelligence Virtual Expert (ALIVE)

# Summary

ALIVE is an artificial intelligence-based recommendation system for longevity supplementation. Based on your unique biological profile, ALIVE will recommend a personalized regimen of supplements and drugs to optimize your healthspan. ALIVE places control over your healthspan into your own hands. 

Built for [TreeHacks 2024](https://www.treehacks.com/) at Stanford University.

## Problem Statement 💡
Japan faces a unique and pressing challenge: it is home to one of the world's fastest-aging populations. According to projections, the proportion of the population aged 65 and over is expected to rise significantly, leading to increased healthcare costs, a shrinking workforce, and a greater demand for elderly care services. As this population ages, they may face a decline in healthspan—the period of life free from serious disease and impairment. Far too often, the elderly experience a decline in physical and cognitive function, leading to a lower quality of life and increased reliance on medical interventions.

## Solution 💊

ALIVE offers a proactive approach to addressing the challenges of aging by leveraging artificial intelligence and personalized medicine. By analyzing individuals' biological profiles, including genetic data, biomarkers, and lifestyle factors, ALIVE generates tailored recommendations for longevity supplementation and drug repurposing. These recommendations aim to optimize individuals' healthspan by targeting specific pathways associated with aging, such as inflammation, oxidative stress, and mitochondrial function.

Through its user-friendly interface, ALIVE empowers individuals to take control of their healthspan journey. Users receive personalized recommendations that align with their unique biological needs and preferences, allowing them to make informed decisions about their supplementation and medication regimen. By proactively addressing age-related health concerns, ALIVE helps individuals maintain vitality, independence, and overall well-being as they age.

## Impact 🌍

ALIVE has the potential to significantly impact the aging population in Japan and beyond. By promoting proactive health management and personalized interventions, ALIVE can help delay the onset of age-related diseases, reduce healthcare costs, and improve overall quality of life for older adults. Additionally, ALIVE's approach to supplementation recommendation may lead to the discovery of new uses for existing medications, providing more accessible and cost-effective treatment options for age-related conditions.

Ultimately, ALIVE aims to empower individuals to live longer, healthier lives and contribute to a more sustainable and equitable healthcare system for aging populations worldwide.


# Technical Details

## Large Language Model ✨

The large language model (LLM) that underlies ALIVE was initialized from [meta-llama/Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) and was fine-tuned using [Monster API](https://monsterapi.ai/) on the filtered [DrugAge database](https://genomics.senescence.info/drugs/), a database of aging-related drugs. We used the following prompt for fine-tuning:

```
You are an expert drug development scientist and biomedical researcher studying drugs that can promote longevity and extend healthspan. You must answer an important question. Generate a response that answers this question.

###Question: If you administer the compound {compound_name} in a {species} {strain} {gender} model organism at {dosage} dosage, what will the average lifespan change be in years?

###Response: The average lifespan change will be {avg_lifespan_change} years.
```

### Training Results 📈

Training results are available via Weights & Biases at [this dashboard](https://api.wandb.ai/links/ayushnoori/9xquz6sq).


### HuggingFace Release 🤗

Our fine-tuned large language model was released publicly with a detailed model card at the following HuggingFace link: [ayushnoori/alive](https://huggingface.co/ayushnoori/alive).


## Future Directions 🚀

In the future, we intend to use a deep learning model trained by jointly learning molecular structures and textual descriptions to improve the quality and accuracy of our recommendations. For example, we could use MoleculeSTM, a multi-modal molecule structure–text model trained on over 280,000 chemical structure–text pairs. For more details, please see the associated paper in *Nature Machine Intelligence*:
> Liu, S. et al. Multi-modal molecule structure–text model for text-based retrieval and editing. *Nat Mach Intell* **5**, 1447–1457 (2023). doi: [10.1038/s42256-023-00759-6](https://doi.org/10.1038/s42256-023-00759-6)

## Base Dependencies 📦 

Please see `requirements.txt`, or below.

```
streamlit
pandas
numpy
streamlit-authenticator
transformers
torch
monsterapi==1.0.2b3
load_dotenv
```

## Development Team 🧑‍💻
* [Ayush Noori](mailto:anoori@college.harvard.edu)
* [Sibi Raja](mailto:sraja@college.harvard.edu)
* [Jay Iyer](mailto:sraja@college.harvard.edu)


# References 📚

1. Zhavoronkov, A., Bischof, E. & Lee, K.-F. Artificial intelligence in longevity medicine. *Nat Aging* **1**, 5–7 (2021).

2. Aisopos, F. & Paliouras, G. Comparing methods for drug–gene interaction prediction on the biomedical literature knowledge graph: performance versus explainability. *BMC Bioinformatics* **24**, 272 (2023).

3. Liu, S. et al. Multi-modal molecule structure–text model for text-based retrieval and editing. *Nat Mach Intell* **5**, 1447–1457 (2023).

4. Barardo, D. et al. The DrugAge database of aging-related drugs. *Aging Cell* **16**, 594–597 (2017).

This project was completed during the [TreeHacks 2024](https://www.treehacks.com/) hackathon at Stanford University.
