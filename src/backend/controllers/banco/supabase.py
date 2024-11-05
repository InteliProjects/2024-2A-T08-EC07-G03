from supabase import Client, create_client

# from config import api, url

api_url: str = "https://jhmlmzvzxtzbqxifoilb.supabase.co"
key: str = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpobWxtenZ6eHR6YnF4aWZvaWxiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU1NjU0OTQsImV4cCI6MjA0MTE0MTQ5NH0.aVGsLYbW-4a21NTLWmG4NwC72_2V37AQ8NCJ78-LH-M"
)


def create_supabase_client():
    print(api_url)
    supabase: Client = create_client(api_url, key)
    return supabase
