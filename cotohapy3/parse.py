from typing import NamedTuple

from .utils import Response

class LinksObj(NamedTuple):
    link: int
    label: str

class DependencyLabelsObj(NamedTuple):
    token_id: int
    label: str

class ChunkInfoObj(NamedTuple):
    id: int
    head: int
    dep: str
    chunk_head: int
    chunk_func: int
    links: list
    predicate: list

class MorphemeInfoObj(NamedTuple):
    id: int
    form: str
    kana: str
    lemma: str
    pos: str
    features: list
    dependency_labels: list
    attributes: object

class ParseResultResponseObj(NamedTuple):
    chunk_info: ChunkInfoObj
    tokens: list

class Parse(Response):
    def __init__(self, r):
        super().__init__(r)
        self.parse_lst = []
        for result_obj in self.result:
            chunk_info_dict = result_obj["chunk_info"]
            links = []
            for l in chunk_info_dict.get("links", []):
                links.append(LinksObj(
                    link = l["link"],
                    label = l["label"]
                ))
            chunk_info_obj = ChunkInfoObj(
                id = chunk_info_dict.get("id"),
                head = chunk_info_dict.get("head"),
                dep = chunk_info_dict.get("dep"),
                chunk_head = chunk_info_dict.get("chunk_head"),
                chunk_func = chunk_info_dict.get("chunk_func"),
                links = links,
                predicate = chunk_info_dict.get("predicate")
            )
            token_lst = []
            for token in result_obj["tokens"]:
                dependency_labels = []
                for d in token.get("dependency_labels", []):
                    dependency_labels.append(DependencyLabelsObj(
                        token_id = d["token_id"],
                        label = d["label"]
                    ))
                token_lst.append(MorphemeInfoObj(
                    id = token.get("id"),
                    form = token.get("form"),
                    kana = token.get("kana"),
                    lemma = token.get("lemma"),
                    pos = token.get("pos"),
                    features = token.get("features"),
                    dependency_labels = dependency_labels,
                    attributes = token.get("attributes")
                ))
            parse_obj = ParseResultResponseObj(
                chunk_info = chunk_info_obj,
                tokens = token_lst
            )
            self.parse_lst.append(parse_obj)
    
    def __iter__(self):
        return iter(self.parse_lst)