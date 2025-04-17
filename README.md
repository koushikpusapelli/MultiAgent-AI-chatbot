Multi-Agent Real Estate Assistant Chatbot (Image + Text Enabled)
Koushik Pusapelli
pusapellikoushik@gmail.com
www.linkedin.com/in/koushik-pusapelli-8a16002a6
Project Overview
This proof-of-concept demonstrates a multi-agentic chatbot designed to assist users in:
•	Detecting property issues from uploaded images (Agent 1)
•	Answering tenancy-related questions (Agent 2)
The system uses Google Cloud Vision API for image analysis and Gemini-Pro for natural language understanding and response generation.
🧠 Agents Overview
✅ Agent 1: Issue Detection & Troubleshooting Agent (Image + Text)
•	Accepts property images and optional text (e.g., “what’s wrong with this wall?”)
•	Uses Google Cloud Vision API to analyze the image for:
o	Labels (e.g., "mold", "crack", "leak", "damp wall")
o	Detected objects / issues
•	Passes visual context + user prompt to Gemini-Pro
•	Gemini then explains what the issue might be and suggests a solution
•	Example Output:
"There appears to be mold growth and dampness. You should check for leaks and consider using anti-mold paint."
✅ Agent 2: Tenancy FAQ Agent (Text-based)
•	Handles user questions like:
o	“Can my landlord increase rent mid-term?”
o	“What happens if I break my lease early?”
•	Uses Gemini-Pro to generate well-formed answers
•	Can tailor responses based on user’s location (city/country)
•	Example Output:
"In Telangana, landlords typically must give one month’s notice before evicting a tenant."
🔁 Agent Router Logic
Input Condition	Routed to
Image uploaded	                   Agent 1
Text-only input	                   Agent 2
Image + text	                  Agent 1 (uses text as context)
Routing is done within the app by checking whether an image is present in the input. If both image and text are present, Agent 1 uses the text for additional context.

Tools & Technologies Used
Tool / API	Role in System
Google Cloud Vision API	         Extracts image content (labels/objects)
Gemini-1.5-flash	          Natural language understanding and generation
Streamlit	          Simple web interface for testing/chatbot UI
Python	           Backend logic integration
VS code	            Coding 

🖼️ How Image-Based Issue Detection Works (Agent 1)
1.	User uploads an image (e.g., wall with stains).
2.	Vision API analyzes the image and returns a list of labels like:
“mold”, “wall damage”, “water leak”
3.	These labels + user’s question are combined into a prompt:
“The image contains mold and wall damage. The user says: 'Why is this wall stained?'”
4.	Gemini-1.5-flash responds with a diagnostic suggestion:
“This appears to be water damage due to leakage. You should check plumbing and use damp-resistant paint.”
Use Case Examples Covered
Agent 1:
•	“What’s wrong with this corner?” (Image with peeling paint)
•	“Is this a crack in the wall serious?” (Image attached)
Agent 2:
•	“How much notice do I need to vacate in Telangana?”
•	“Can I break a lease early if my job transfers?”
•	“Can a landlord evict me without written notice?”

