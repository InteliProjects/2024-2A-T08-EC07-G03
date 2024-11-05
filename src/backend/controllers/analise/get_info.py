from supabase import create_client, Client
import os

url: str = "https://jhmlmzvzxtzbqxifoilb.supabase.co"
key: str = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpobWxtenZ6eHR6YnF4aWZvaWxiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU1NjU0OTQsImV4cCI6MjA0MTE0MTQ5NH0.aVGsLYbW-4a21NTLWmG4NwC72_2V37AQ8NCJ78-LH-M"
)
supabase: Client = create_client(url, key)


async def get_data_entries():
    response = supabase.table("data_entries").select("*").execute()
    data_entries = response.data
    return data_entries


async def get_analysis_results():
    response = supabase.table("analysis_results").select("*").execute()
    analysis_results = response.data
    return analysis_results


async def get_model_training():
    response = supabase.table("model_training").select("*").execute()
    model_training = response.data
    return model_training
