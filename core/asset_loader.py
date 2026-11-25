import streamlit as st
from huggingface_hub import hf_hub_download
from tqdm.auto import tqdm


def download_asset(file_path: str, progress_bar):

    class StreamlitTqdm(tqdm):
        def __init__(self, *args, **kwargs):
            kwargs["disable"] = False
            super().__init__(*args, **kwargs)
        def update(self, n=1):
            result = super().update(n)
            if self.total:
                progress = min(self.n / self.total, 1.0)
                progress_bar.progress(
                    progress,
                    text=f"Downloading {file_path.split('/')[-1]}: {progress:.0%}"
                )
            return result

    return hf_hub_download(
        repo_id=st.secrets["HF_REPO_ID"],
        filename=file_path,
        repo_type="dataset",
        token=st.secrets["HF_TOKEN"],
        tqdm_class=StreamlitTqdm
    )