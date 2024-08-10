# Documentation

## Table of Contents
#### 1. Setup Instructions
#### 2. Project Overview
#### 3. Success Criteria
#### 4. Design Decisions
#### 5. Challenges Encountered
#### 6. Room for Improvement/Scalability

## Setup Instructions

#### Backend Setup
1. Sign up on MultiOn's developer console.
2. Create an API key.
3. Install the MultiOn SDK
```python
pip install multion
```
4. Find the MultiOn Browser Extension on the Chrome Web Store and click "Add to Chrome". Make sure the "API Enabled" option is checked.

If you are encountering further issues, refer to the MultiOn API documentation: https://docs.multion.ai/welcome

#### Frontend Setup
1. Install flask
```python
pip install flask
```
2. Run flask application
```python
pip install flask
```
3. Navigate to http://127.0.0.1:5000/

## Project Overview
In this project, we use MultiOn API in order to scrape unstructured data from the H&M webpage and convert it into structured data. This is accomplished by a single agent by simply using the retrieve() method from the MultiOn API. From here, we facilitate communication between this agent and a second agent in order to browse for cheaper products on Amazon. Among finding a relevant product, the second agent adds the product to our cart. 

## Success Criteria
Among completing development, the success criteria was measured with the following:
  1. Can agent #1 consistently and accurately scrape unstructured webpage data and convert it into a structured form?
  2. Can agent #1 package and send data to agent #2 according to the user's will?
  3. Can agent #2 browse for a similar but cheaper product and decide on a relevant product to add to the cart?

## Design Decisions
On their documentation, MultiOn API supports TypeScript and Python usage. I chose Python for its simplicity and scalability. I originally decided to implement the agents into different python files, with the first file prompting the user for input via terminal to see what webpage it should scrape, convert the data into structured form, and then ask the user which product they wished to be cross referenced. From here, it called a function that existed in a separate file, sending the relevant product information as parameters. This function would create the second agent's session and browse Amazon for a product that fits the description it was given. The separation of these tasks into two files created a clear distinction between the two agents. After creating a working prototype that prompts through the terminal's command line, I then chose to implement a simple frontend using Flask. While a framework such as Next.js or Angular would be better for creating a larger scale application, I chose Flask for ease of implementation as I felt that the frontend was of lower priority to the success criteria for this project. In doing this, I modified the first agent's file so that the prompting would be done in the index.html file and the first agent's file simply contained the logic it needed to scrape and communicate with the second agent. 

## Challenges Encountered
Throughout implementation, these are the main challenges I encountered:
  1. MultiOn being a new technology had limited documentation. Specifically, its not clear how powerful the API's language processing abilities are so it was difficult to tell what commands it would respond properly to.
  2. The API's browsing functionality is inconsistent and sometimes unreliable.
  3. After establishing a working prototype in the backend, it was difficult to revamp the first agent to receive its input data from the frontend rather from the command line. 

## Room for Improvement/Scalability
In terms of improvement and scalability, this application has significant potential. For starters, the frontend is very minimal and can clearly be improved for both user experience and interface. A shortcoming of the prompting is that the user needs to give very specific inputs, because the smallest typos or errors can jeopardize the functionality. This could be improved by using an LLM or NLP to parse more flexible inputs into the necessary fields. 

In terms of success criteria, agent #1 does a solid job of fulfilling the first success criteria, as it can consistently scrape unstructured web data and turn it into structured data. However, this consistency drops when the webpage being scraped isn't the H&M website. The agent is capable of having some success on other e-commerce sites such as Urban Outfitters, but not at the same reliability as H&M. Additionally, agent #1 can be further scaled to ask how many products the user wants to see and potentially ask agent #2 to cross-reference multiple products. 

If the agent does scrape the data successfully, it does a very good job of communicating the necessary data with agent #2. This success criteria was fulfilled very sufficiently. 

The last success criteria leaves much more room for improvement as the browse() functionality of MultiOn's API is quite inconsistent. For example, if the program were to be ran with the same inputs twice, it is likely that agent #2 would add a different item to the cart the second time. The agent also will choose a random size and color scheme for the product if the user does not provide one, and it will almost never prompt for these fields. Additionally, the agent should ask the user if they are satisfied with the similar product that it finds before it adds it to the cart, but it rarely does this. Overall, while the agent is quite consistent at finding a cheaper product of similar nature and adding it to the cart, it could do a lot better in confirming with the user that the item meets their preferences, or even better, independently runs algorithms that determine whether a product is similar enough.
