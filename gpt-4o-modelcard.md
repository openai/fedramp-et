# Model Card for GPT-4o

<!-- Provide a quick summary of what the model is/does. -->

GPT-4o is a versatile, autoregressive omni model capable of processing and generating multimodal 
inputs and outputs, including text, audio, image, and video. It is designed for high-performance 
interaction across various sectors, such as customer support, sales, and content creation. Notably, 
GPT-4o excels in responding to audio inputs with human-like speed, offering significant improvements 
in non-English language processing, vision, and audio understanding compared to previous models. 
It delivers these enhancements while being faster and more cost-effective than GPT-4 Turbo, making 
it an efficient tool for a wide range of applications.


## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

**Note:** This version of the GPT-4o system card was developed from the substance published in our 
public system card and other OpenAI published documentation and blog posts. It was prepared specifically 
for FedRAMP Emerging Technology Prioritization Program per the program instructions.

GPT-4o is an autoregressive omni model, which accepts as input any combination of text,
audio, image, and video and generates any combination of text, audio, and image outputs.
It’s trained end-to-end across text, vision, and audio, meaning that all inputs and outputs
are processed by the same neural network.

GPT-4o can respond to audio inputs in as little as 232 milliseconds, with an average of 320
milliseconds, which is similar to human response time in a conversation. It matches GPT-4
Turbo performance on text in English and code, with significant improvement on text in
non-English languages, while also being much faster and 50% cheaper in the API. GPT-4o
is especially better at vision and audio understanding compared to existing models.

GPT-4o is designed to enhance operational efficiencies across various sectors, including
customer support, sales, employee training, content creation, and more. It is optimized for
multimodal inputs and outputs, ensuring a wide range of applications in different industries.


- **Developed by:** OpenAI
- **Model type:** Large Language Model
- **Language(s) (NLP):** English
- **License:** N/A

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

GPT-4 is applicable across multiple platforms and enhances user interaction and operational 
efficiencies in diverse sectors. The example applications below highlight the versatility of 
GPT-4 powered solutions such as ChatGPT Enterprise in enhancing various business functions 
through automation, improved communication, and data-driven insights.

**Customer Support and Service**
- Automating responses to common customer inquiries.
- Providing 24/7 customer service.
- Assisting with troubleshooting and problem resolution.

**Sales and Lead Generation**
- Engaging potential customers with personalized messages.
- Qualifying leads through conversational AI.
- Providing information on products and services.

**Employee Training and Onboarding**
- Delivering training materials in an interactive manner.
- Answering questions from new hires about company policies and procedures.
- Providing ongoing education and skill development resources.

**Content Creation and Marketing**
- Generating content for blogs, social media, and marketing campaigns.
- Assisting with SEO by creating keyword-rich content.
- Personalizing marketing messages based on customer data.

**Internal Knowledge Management**
- Providing employees with quick access to company information and resources.
- Answering questions about internal processes and systems.
- Facilitating document retrieval and knowledge sharing.

**Data Analysis and Insights**
- Summarizing and interpreting complex data.
- Generating reports and visualizations.
- Offering insights and recommendations based on data analysis.

**Scheduling and Administrative Tasks**
- Assisting with calendar management and meeting scheduling.
- Automating routine administrative tasks.
- Sending reminders and follow-up emails.

**Product and Service Development**
- Gathering customer feedback and suggestions.
- Assisting in brainstorming and ideation sessions.
- Providing market research and analysis.

**Compliance and Legal Assistance**
- Helping with regulatory compliance by providing information and updates.
- Assisting with the preparation of legal documents and contracts.
- Offering guidance on legal procedures and policies.

**Human Resources**
- Answering employee questions about benefits, policies, and procedures.
- Assisting with recruitment by screening resumes and conducting initial interviews.
- Managing employee feedback and surveys.

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

**Universal Policies**

When using any OpenAI service, like ChatGPT, labs.openai.com, and the OpenAI API, the 
rules below apply. For the most current version of these Usage Rules please see: 
https://openai.com/policies/usage-policies/

1. Comply with applicable laws – for example, don’t compromise the privacy of others, 
engage in regulated activity without complying with applicable regulations, or promote 
or engage in any illegal activity, including the exploitation or harm of children and 
the development or distribution of illegal substances, goods, or services.
2. Don’t use our service to harm yourself or others – for example, don’t use our services 
to promote suicide or self-harm, develop or use weapons, injure others or destroy property, 
or engage in unauthorized activities that violate the security of any service or system.
3. Don’t repurpose or distribute output from our services to harm others – for example, 
don’t share output from our services to defraud, scam, spam, mislead, bully, harass, 
defame, discriminate based on protected attributes, sexualize children, or promote violence, 
hatred or the suffering of others.
4. Respect our safeguards - don’t circumvent safeguards or safety mitigations in our services 
unless supported by OpenAI (e.g., domain experts in our Red Teaming Network) or related to research 
conducted in accordance with our Sharing & Publication Policy.

We report apparent child sexual abuse material (CSAM) to the National Center for Missing and 
Exploited Children.

**Building with the OpenAI API Platform**

The OpenAI Platform allows you to build entirely custom applications. As the developer of your 
application, you are responsible for designing and implementing how your users interact with our 
technology. To make this easier, we’ve shared our Safety best practices and offer tools like our 
Moderation Endpoint and customizable system messages.

We recognize that our API introduces new capabilities with scalable impact, so we have service-specific 
policies that apply to all use of our APIs in addition to our Universal Policies:

1. Don’t compromise the privacy of others, including:
  - Collecting, processing, disclosing, inferring or generating personal data without complying with 
  applicable legal requirements
  - Using biometric systems for identification or assessment, including facial recognition
  - Facilitating spyware, communications surveillance, or unauthorized monitoring of individuals
2. Don’t perform or facilitate the following activities that may significantly impair the safety, 
wellbeing, or rights of others, including:
  - Providing tailored legal, medical/health, or financial advice without review by a qualified professional 
  and disclosure of the use of AI assistance and its potential limitations
  - Making high-stakes automated decisions in domains that affect an individual’s safety, rights or well-being 
  (e.g., law enforcement, migration, management of critical infrastructure, safety components of products, 
  essential services, credit, employment, housing, education, social scoring, or insurance)
  - Facilitating real money gambling or payday lending
  - Engaging in political campaigning or lobbying, including generating campaign materials personalized to 
  or targeted at specific demographics
  - Deterring people from participation in democratic processes, including misrepresenting voting processes 
  or qualifications and discouraging voting
3. Don’t misuse our platform to cause harm by intentionally deceiving or misleading others, including:
  - Generating or promoting disinformation, misinformation, or false online engagement (e.g., comments, reviews)
  - Impersonating another individual or organization without consent or legal right
  - Engaging in or promoting academic dishonesty
  - Failing to ensure that automated systems (e.g., chatbots) disclose to people that they are interacting with 
  AI, unless it's obvious from the context
4. Don’t build tools that may be inappropriate for minors, including:
  - Sexually explicit or suggestive content. This does not include content created for scientific or educational purposes.

**Building with ChatGPT**

Shared GPTs allow you to use ChatGPT to build experiences for others. Because your GPT’s users are also OpenAI 
users, when building with ChatGPT, we have the following service-specific policies in addition to our Universal Policies:

1. Don’t compromise the privacy of others, including:
  - Collecting, processing, disclosing, inferring or generating personal data without complying with applicable legal requirements
  - Soliciting or collecting the following sensitive identifiers, security information, or their equivalents: payment 
  card information (e.g. credit card numbers or bank account information), government identifiers (e.g. SSNs), API keys, or passwords
  - Using biometric identification systems for identification or assessment, including facial recognition
  - Facilitating spyware, communications surveillance, or unauthorized monitoring of individuals
2. Don’t perform or facilitate the following activities that may significantly affect the safety, wellbeing, or rights of others, including:
  - Taking unauthorized actions on behalf of users
  - Providing tailored legal, medical/health, or financial advice
  - Making automated decisions in domains that affect an individual’s rights or well-being (e.g., law enforcement, 
  migration, management of critical infrastructure, safety components of products, essential services, credit, employment, 
  housing, education, social scoring, or insurance)
  - Facilitating real money gambling or payday lending
  - Engaging in political campaigning or lobbying, including generating campaign materials personalized to or targeted at specific demographics
  - Deterring people from participation in democratic processes, including misrepresenting voting processes or qualifications and discouraging voting
3. Don’t misinform, misrepresent, or mislead others, including:
  - Generating or promoting disinformation, misinformation, or false online engagement (e.g., comments, reviews)
  - Impersonating another individual or organization without consent or legal right
  - Engaging in or promoting academic dishonesty
  - Using content from third parties without the necessary permissions
  - Misrepresenting or misleading others about the purpose of your GPT
4. Don’t build tools that may be inappropriate for minors, including:
  - Sexually explicit or suggestive content. This does not include content created for scientific or educational purposes.
5. Don’t build tools that target users under 13 years of age.

We use a combination of automated systems, human review, and user reports to find and assess GPTs that potentially 
violate our policies. Violations can lead to actions against the content or your account, such as warnings, sharing 
restrictions, or ineligibility for inclusion in GPT Store or monetization.


## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

**Unauthorized voice generation**

Risk Description: Voice generation is the capability to create audio with a human-sounding synthetic voice, and 
includes generating voices based on a short input clip. 

Risk Mitigation: We addressed voice generation related-risks by allowing only the preset voices we created in 
collaboration with voice actors to be used. We did this by including the selected voices as ideal completions 
while post-training the audio model. Additionally, we built a standalone output classifier to detect if the GPT-4o 
output is using a voice that’s different from our approved list. We run this in a streaming fashion during audio 
generation and block the output if the speaker doesn’t match the chosen preset voice.

**Speaker identification**

Risk Description: Speaker identification is the ability to identify a speaker based on input audio. This presents a 
potential privacy risk, particularly for private individuals as well as for obscure audio of public individuals, along 
with potential surveillance risks.

Risk Mitigation: We post-trained GPT-4o to refuse to comply with requests to identify someone based on a voice in an 
audio input. GPT-4o still complies with requests to identify famous quotes. For example, a request to identify a random 
person saying “four score and seven years ago” should identify the speaker as Abraham Lincoln, while a request to identify 
a celebrity saying a random sentence should be refused.

**Disparate performance on voice inputs**

Risk Description: Models may perform differently with users speaking with different accents. Disparate performance 
can lead to a difference in quality of service for different users of the model.

Risk Mitigation: We post-trained GPT-4o with a diverse set of input voices to have model performance and behavior be 
invariant across different user voices.

**Ungrounded Inference / Sensitive Trait Attribution**

Risk Description: Audio input can lead to the model making potentially biased inferences about speakers.

- Ungrounded inference (UGI): making inferences about a speaker that couldn’t be determined solely from audio content. 
  This includes inferences about things such as a speaker’s race, socio-economic status/occupation, religious beliefs, 
  personality traits, political attributes, intelligence, appearance (e.g., eye color, attractiveness), gender identity, 
  sexual preference, or criminal history. This can lead to both allocative and representational harms depending on how 
  such behavior manifests.

- Sensitive trait attribution (STA): making inferences about a speaker that could plausibly be determined solely from audio 
  content. This includes inferences about things such as a speaker’s accent or nationality. Potential harms from STA include 
  an increase in risks from surveillance and a difference in quality of service for speakers with different voice attributes.

Risk Mitigation: We post-trained GPT-4o to refuse to comply with UGI requests, while hedging answers to STA questions. 
For example, a question to identify a speaker’s level of intelligence will be refused, while a question to identify a speaker’s 
accent will be met with an answer such as “Based on the audio, they sound like they have a British accent.”

**Violative & disallowed content**

Risk Description: GPT-4o may be prompted to output harmful content through audio that would be disallowed through text, 
such as audio speech output that gives instructions on how to carry out an illegal activity.

Risk Mitigation: We found high text to audio transference of refusals for previously disallowed content. This means that 
the post-training we’ve done to reduce the potential for harm in GPT-4o’s text output successfully carried over to audio 
output. Additionally, we run our existing moderation model over a text transcription of both audio input and audio output to 
detect if either contains potentially harmful language, and will block a generation if so.

**Erotic & violent speech content**

Risk Description: GPT-4o may be prompted to output erotic or violent speech content, which may be more evocative or harmful 
than the same context in text. Because of this, we decided to restrict the generation of erotic and violent speech.

Risk Mitigation: We run our existing moderation model over a text transcription of the audio input to detect if it contains 
a request for violent or erotic content, and will block a generation if so.

**Other known risks and limitations of the model**

Through the course of internal testing and external red teaming, we discovered a small number of additional risks and 
model limitations for which model or system level mitigations are nascent or still in development, including:

- Audio robustness: We saw anecdotal evidence of decreases in safety robustness through audio perturbations, such as 
 low quality input audio, background noise in the input audio, and echoes in the input audio. Additionally, we observed similar decreases in safety robustness through intentional and unintentional audio interruptions while the model was generating output. 

- Misinformation and conspiracy theories: Red teamers were able to compel the model to generate inaccurate information by 
  prompting it to verbally repeat false information and produce conspiracy theories. While this is a known issue for text 
  in GPT models there was concern from red teamers that this information may be more persuasive or harmful when delivered 
  through audio, especially if the model was instructed to speak emotively or emphatically. The persuasiveness of the model was 
  studied in detail and we found that the model did not score higher than Medium risk for text-only, and for speech to speech the model 
  did not score higher than Low.

- Speaking a non-English language in a non-native accent: Red teamers observed instances of the audio output using a non-native accent 
when speaking in a non-English language. This may lead to concerns of bias towards certain accents and languages, and more generally 
towards limitations of non-English language performance in audio outputs.

- Generating copyrighted content: We also tested GPT-4o’s capacity to repeat content found within its training data.
 We trained GPT-4o to refuse requests for copyrighted content, including audio, consistent with our broader practices. 
 To account for GPT-4o’s audio modality, we also updated certain text-based filters to work on audio conversations, built 
 filters to detect and block outputs containing music, and for our limited alpha of ChatGPT’s advanced Voice Mode, instructed 
 the model to not sing at all. We intend to track the effectiveness of these mitigations and refine them over time.

Although some technical mitigations are still in development, our Usage Policies disallow intentionally deceiving or misleading others, 
and circumventing safeguards or safety mitigations. In addition to technical mitigations, we enforce our Usage Policies through 
monitoring and take action on violative behavior in both ChatGPT and the API.


### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

We recommend model users review our public system cards and Preparedness Framework
to gain a full understanding of the ChatGPT and API model risks, mitigations, and safety
measures OpenAI takes in the development of its models. Also, developers should review
the documentation available at platform.openai.com and implement the safety best practices.


## How to Get Started with the Model

Use the code below to get started with the model.

To install the official Python bindings, run the following command:

```sh
  pip install openai
```

To install the official Node.js library, run the following command in your Node.js project directory:

```sh
npm install openai@^4.0.0
```

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

**Training Data**

GPT-4o's capabilities were pre-trained using data up to October 2023, sourced from a wide variety of 
materials including:

- Select publicly available data, mostly collected from industry-standard machine learning datasets and web crawls.

- Proprietary data from data partnerships. We form partnerships to access non-publicly available data, such 
as pay-walled content, archives, and metadata. For example, we partnered with Shutterstock on building and 
delivering AI-generated images.

The key dataset components that contribute to GPT-4o’s capabilities are:

- Web Data: Data from public web pages provides a rich and diverse range of information, ensuring the model 
learns from a wide variety of perspectives and topics.
- Code and math: Including code and math data in training helps the model develop robust reasoning skills by 
exposing it to structured logic and problem-solving processes.
- Multimodal data: Our dataset includes images, audio, and video to teach the LLMs how to interpret and generate 
non-textual input and output. From this data, the model learns how to interpret visual images, actions and sequences 
in real-world contexts, language patterns, and speech nuances.


### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->
LLM models like GPT 4o are developed in a way that allows it to understand and respond to user questions and instructions. 
It does this by “reading” a large amount of existing text and learning how words tend to appear in context with other words. 
It then uses what it has learned to predict the next most likely word that might appear in response to a user request, and each 
subsequent word after that. This is similar to auto-complete capabilities on search engines, smartphones, and email programs.

As an example, during the model learning process (called “training”), we might have a model try to complete the sentence: 
“instead of turning left, she turned ___.” Before training, the model will respond with random words, but as it reads and 
learns from many lines of text, it better understands this type of sentence and can predict the next word more accurately. 
It then repeats this process across a very large number of sentences.
Because there are many possible words that could come next in this sentence (e.g., instead of turning left, she turned 
“right,” “around,” or “back”), there is an element of randomness in the way a model can respond, and in many cases our models 
will answer the same question in different ways.


Machine learning models are made up of large strings of numbers, called “weights” or “parameters,” and code that interprets and 
executes those numbers. Models do not contain or store copies of information that they learn from. Instead, as a model learns, 
some of the numbers that make up the model change slightly to reflect what it has learned. In the example above, the model read 
information that helped it improve from predicting random incorrect words to predicting more accurate words, but all that actually 
happened in the model itself was that the numbers changed slightly. The model does not store or copy the sentences that it reads.


Prior to deployment, OpenAI assesses and mitigates potential risks that may stem from generative models, such as information harms, 
bias and discrimination, or other content that violates our safety policies. We use a combination of methods, spanning all stages of 
development across pre-training, post-training, product development, and policy. For example, during post-training, we align the model 
to human preferences; we red team the resulting models and add product-level mitigations such as monitoring and enforcement; and we provide 
moderation tools and transparency reports to our users.

We find that the majority of effective testing and mitigations are done after the pre-training stage because filtering pre-trained 
data alone cannot address nuanced and context-specific harms. At the same time, certain pre-training filtering mitigations can provide 
an additional layer of defense that, along with other safety mitigations, help exclude unwanted and harmful information from our datasets:

- We use our Moderation API and safety classifiers to filter out data that could contribute to harmful content or information hazards, 
including CSAM, hateful content, violence, and CBRN. 
- As with our previous image generation systems, we filter our image generation datasets for explicit content such as graphic sexual material and CSAM. 
- We use advanced data filtering processes to reduce personal information from training data. 
- Upon releasing DALL·E 3, we piloted a new approach to give users the power to opt images out of training. To respect those opt-outs, 
we fingerprinted the images and used the fingerprints to remove all instances of the images from the training dataset for the GPT-4o series of models.

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data, Factors & Metrics

#### Testing Data

<!-- This should link to a Dataset Card if possible. -->

OpenAI worked with more than 100 external red teamers, speaking a total of 45 different languages, and representing geographic backgrounds of 
29 different countries. Red teamers had access to various snapshots of the model at different stages of training and safety mitigation maturity 
starting in early March and continuing through late June 2024. 

Red teamers were asked to carry out exploratory capability discovery, assess novel potential risks posed by the model, and stress test mitigations 
as they were developed & improved - specifically those introduced by audio input and generation (speech to speech capabilities). This red teaming 
effort builds upon prior work, including as described in the previous system cards.

Red teamers covered categories that spanned violative & disallowed content (illegal erotic content, violence, self harm, etc), mis/disinformation, 
bias, ungrounded inferences, sensitive trait attribution, private information, geolocation, person identification, emotional perception and 
anthropomorphism risks, fraudulent behavior and impersonation, copyright, natural science capabilities, and multilingual observations.

The data generated by red teamers motivated the creation of several quantitative evaluations that are described in the Factors, Metrics 
and Results sections. In some cases, insights from red teaming were used to do targeted synthetic data generation. Models were evaluated 
using both autograders and manual labeling in accordance with some criteria (e.g, violation of policy or not, refused or not). In addition, 
we sometimes re-purposedC the red teaming data to run targeted assessments on a variety of voices and examples to test the robustness of 
various mitigations

In addition to the data from red teaming, a range of existing evaluation datasets were converted to evaluations for speech-to-speech 
models using text-to-speech (TTS) systems such as Voice Engine. We converted text-based evaluation tasks to audio-based evaluation tasks 
by converting the text inputs to audio. This allowed us to reuse existing datasets and tooling around measuring model capability, 
safety behavior, and monitoring of model outputs, greatly expanding our set of usable evaluations.

We used Voice Engine to convert text inputs to audio, feed it to GPT-4o, and score the outputs by the model. We always score only 
the textual content of the model output, except in cases where the audio needs to be evaluated directly


#### Factors

<!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->

**Unauthorized voice generation**
- Voice Classifier Performance

**Speaker Identification**
- Speaker Identification

**Disparate performance on voice inputs**
- Quality of service

**Ungrounded Inference / Sensitive Trait Attribution**
- Accuracy

**Violative & disallowed content**
- Violative content output


#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

**Voice Classifier Performance**
- Precision
- Recall

**Speaker Identification**
- should_refuse
- should_comply

**Disparate performance on voice inputs**
- Capabilities
- Safety

**Ungrounded Inference / Sensitive Trait Attribution**
- Refuse UGI
- Safely comply with STA

**Violative & disallowed content**
- Not unsafe
- Not over-refuse


### Results

**Unauthorized voice generation**  
The residual risk of unauthorized voice generation is minimal. Our system currently catches 100% of meaningful deviations 
from the system voice based on our internal evaluations, which includes samples generated by other system voices, clips 
during which the model used a voice from the prompt as part of its completion, and an assortment of human samples.

**English**  
- Precision: 0.96  
- Recall: 1.0

**Non-English:**  
- Precision: 0.95  
- Recall: 1.0

**Speaker identification**  
Compared to our initial model, we saw a 14 point improvement in when the model should refuse to identify a voice in an audio 
input, and a 12 point improvement when it should comply with that request. The former means the model will almost always correctly 
refuse to identify a speaker based on their voice, mitigating the potential privacy issue. The latter means there may be situations 
in which the model incorrectly refuses to identify the speaker of a famous quote.

- Should_refuse: 0.98  
- Should_comply: 0.83

**Disparate performance on voice inputs**  
We run evaluations on GPT-4o Advanced Voice Mode using a fixed assistant voice (“shimmer”) and Voice Engine to generate user inputs 
across a range of voice samples. We use two sets of voice samples for TTS:

- Official system voices (3 different voices)
- A diverse set of voices collected from two data campaigns. This comprises 27 different English voice samples from speakers from a 
wide range of countries, and a mix of genders.

We evaluate on two sets of tasks: Capabilities and Safety Behavior.

**Capabilities:**  
We evaluate on four tasks: TriviaQA, a subset of MMLUK, HellaSwag, and LAMBADA. TriviaQA and MMLU are knowledge-centric tasks, while 
HellaSwag and LAMBADA are common sense-centric or text-continuation tasks. Overall, we find that performance on the diverse set of human 
voices performs marginally but not significantly worse than on system voices across all four tasks. See public system card for full results.

**Safety Behavior:**  
We evaluate on an internal dataset of conversations and evaluate the consistency of the model’s adherence and refusal behavior across 
different user voices. Overall, we do not find that the model behavior varies across different voices. See public system card for full results.

**Ungrounded Inference / Sensitive Trait Attribution**  
Compared to our initial model, we saw a 24 point improvement (0.84) in the model correctly responding to requests to identify sensitive traits.

**Violative & disallowed content**  
We used TTS to convert existing text safety evaluations to audio. We then evaluate the text transcript of the audio output with the 
standard text rule-based classifier. Our evaluations show strong text-audio transfer for refusals on pre-existing content policy areas.

**Text:**  
- Not unsafe: 0.99  
- Not over-refuse: 0.98

**Audio:**  
- Not unsafe: 1.0  
- Not over-refuse: 0.91


#### Summary

OpenAI has implemented various safety measurements and mitigations throughout the GPT-4o development and deployment process. 
As a part of our iterative deployment process, we will continue to monitor and update mitigations in accordance with the evolving 
landscape. We hope this System Card encourages exploration into key areas including, but not limited to: measurements and 
mitigations for adversarial robustness of omni models, impacts related to anthropomorphism of AI, the use of omni models for 
scientific research and advancement, measurements and mitigations for dangerous capabilities such as self-improvement, model 
autonomy, and scheming. Beyond these areas, we encourage research about economic impacts of omni models, and how tool use might 
advance model capabilities.


## Model Card Contact

grc+fedramp@openai.com