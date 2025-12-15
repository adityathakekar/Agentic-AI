
import os
import google.generativeai as genai
from src.agents import SwarmManager

def main():
    # Load API Key
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key: return print("❌ No API Key found.")
    
    genai.configure(api_key=api_key)
    
    # Run Swarm
    try:
        swarm = SwarmManager()
        report = swarm.run_mission("Agentic AI Trends 2025")
        
        # Save output
        with open("Investment_Memo.md", "w") as f:
            f.write(report)
        print("\n✅ MISSION SUCCESS! Saved to 'Investment_Memo.md'")
        print("-" * 40)
        print(report[:500] + "... (See file for full report)")
        
    except Exception as e:
        print(f"\n❌ Error during execution: {e}")

if __name__ == "__main__":
    main()
