
import google.generativeai as genai
from .tools import search_web

def get_working_model():
    # Priority list for models
    priority = ["models/gemini-1.5-flash", "models/gemini-1.5-pro", "models/gemini-pro"]
    
    # 1. Get available models from API
    try:
        my_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    except:
        return "gemini-pro" # Safe fallback

    # 2. Match priority
    for p in priority:
        if p in my_models:
            print(f"   [SYSTEM] Using Model: {p}")
            return p.replace("models/", "")
            
    return "gemini-pro"

class SwarmManager:
    def __init__(self):
        self.model_name = get_working_model()
        
    def create_agent(self, role, instruction):
        return genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction=f"ROLE: {role}. {instruction}"
        )

    def run_mission(self, topic):
        # Initialize Agents
        researcher = self.create_agent("Researcher", "Find facts. Output [SEARCH: query] if needed.")
        editor = self.create_agent("Editor", "Synthesize data into a Markdown report.")
        
        print(f"\n🤖 [SWARM] Starting Analysis on: {topic}")
        
        # --- STEP 1: RESEARCH ---
        print(f"🕵️ [Researcher] Gathering intelligence...")
        prompt = f"Find top 3 startups and risks for: {topic}"
        
        # Generate first thought
        resp = researcher.generate_content(prompt)
        text = resp.text
        
        # Check for tool use
        if "[SEARCH:" in text:
            try:
                q = text.split("[SEARCH:")[1].split("]")[0].strip()
                data = search_web(q)
                # Feed data back to agent
                text = researcher.generate_content(f"{prompt}\n\nSEARCH DATA: {data}").text
            except:
                pass # Continue if search fails
            
        # --- STEP 2: EDITING ---
        print(f"📝 [Editor] Writing Investment Memo...")
        final = editor.generate_content(f"Write a comprehensive report based on this research:\n{text}")
        return final.text
