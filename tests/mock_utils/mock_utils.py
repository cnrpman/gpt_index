"""Mock utils."""

from typing import Optional, Set

from gpt_index.indices.keyword_table.utils import simple_extract_keywords


def mock_extract_keywords_response(
    text_chunk: str, max_keywords: Optional[int] = None, filter_stopwords: bool = True
) -> str:
    """Extract keywords mock response.

    Same as simple_extract_keywords but without filtering stopwords.

    """
    return ",".join(
        simple_extract_keywords(
            text_chunk, max_keywords=max_keywords, filter_stopwords=False
        )
    )


def mock_extract_keywords(
    text_chunk: str, max_keywords: Optional[int] = None, filter_stopwords: bool = True
) -> Set[str]:
    """Extract keywords (mock).

    Same as simple_extract_keywords but without filtering stopwords.

    """
    return simple_extract_keywords(
        text_chunk, max_keywords=max_keywords, filter_stopwords=False
    )
