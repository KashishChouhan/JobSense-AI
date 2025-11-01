import re
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

# ✅ Load embedding model only once (fast)
MODEL = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Known skills (expandable)
SKILL_CANONICAL = [
    'python','java','c++','c','javascript','html','css','django','flask',
    'sql','mysql','postgresql','mongodb',
    'excel','power bi','tableau',
    'pandas','numpy','matplotlib','seaborn',
    'machine learning','deep learning','nlp',
    'git','github','aws','azure','gcp',
    'statistics','data analysis','communication'
]

def normalize_token(tok: str) -> str:
    """Normalize and clean a token (lowercase + remove special chars)."""
    t = tok.strip().lower()
    t = re.sub(r'[^a-z0-9+# ]+', ' ', t).strip()
    return t

def extract_skills(text):
    """Convert comma-separated text into a set of cleaned skills."""
    if not text:
        return set()
    return set([s.strip().lower() for s in text.split(",") if s.strip()])

def jaccard(set1: set, set2: set):
    """Calculate Jaccard similarity (for simple overlap %)."""
    if not set1 or not set2:
        return 0.0
    return len(set1 & set2) / len(set1 | set2)

def embed_text(text: str):
    """Convert text into numerical embedding vector using MiniLM."""
    if not text:
        return np.zeros((384,))  # default size for MiniLM embeddings
    return MODEL.encode(text, convert_to_numpy=True)

def cosine_similarity(vec1, vec2):
    """Compute cosine similarity between two vectors safely."""
    if vec1 is None or vec2 is None:
        return 0.0
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return float(np.dot(vec1, vec2) / (norm1 * norm2))

def cluster_jobs(jobs, n_clusters=3):
    """Cluster jobs based on their skills using embeddings + KMeans."""
    if not jobs:
        return []
    job_texts = [job.skills for job in jobs]
    job_embeddings = MODEL.encode(job_texts, convert_to_numpy=True)

    kmeans = KMeans(n_clusters=min(n_clusters, len(jobs)), random_state=42, n_init="auto")
    labels = kmeans.fit_predict(job_embeddings)

    return list(zip(jobs, labels))

# ✅ Learning resources (expandable)
RESOURCE_LINKS = {
    'python': 'https://docs.python.org/3/tutorial/',
    'sql': 'https://www.w3schools.com/sql/',
    'excel': 'https://support.microsoft.com/excel',
    'power bi': 'https://learn.microsoft.com/power-bi/',
    'tableau': 'https://www.tableau.com/learn/training',
    'pandas': 'https://pandas.pydata.org/docs/getting_started/index.html',
    'numpy': 'https://numpy.org/learn/',
    'matplotlib': 'https://matplotlib.org/stable/tutorials/',
    'django': 'https://docs.djangoproject.com/en/stable/intro/tutorial01/',
    'git': 'https://git-scm.com/docs/gittutorial',
    'github': 'https://docs.github.com/',
    'machine learning': 'https://www.coursera.org/learn/machine-learning',
    'statistics': 'https://www.khanacademy.org/math/statistics-probability',
    'aws': 'https://aws.amazon.com/training/',
}

def get_resource(skill):
    """Return a learning resource link if known, else a Google search link."""
    return RESOURCE_LINKS.get(skill.lower(), f"https://www.google.com/search?q=learn+{skill}")
