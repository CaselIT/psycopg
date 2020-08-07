"""
Stub representaton of the public objects exposed by the _psycopg3 module.

TODO: this should be generated by mypy's stubgen but it crashes with no
information. Will submit a bug.
"""

# Copyright (C) 2020 The Psycopg Team

import codecs
from typing import Any, Iterable, List, Optional, Sequence, Tuple

from psycopg3.adapt import Dumper, Loader
from psycopg3.proto import AdaptContext, DumpFunc, DumpersMap, DumperType
from psycopg3.proto import LoadFunc, LoadersMap, LoaderType, PQGen
from psycopg3.connection import BaseConnection
from psycopg3 import pq

class Transformer:
    def __init__(self, context: AdaptContext = None): ...
    @property
    def connection(self) -> Optional[BaseConnection]: ...
    @property
    def codec(self) -> codecs.CodecInfo: ...
    @property
    def dumpers(self) -> DumpersMap: ...
    @property
    def loaders(self) -> LoadersMap: ...
    @property
    def pgresult(self) -> Optional[pq.proto.PGresult]: ...
    @pgresult.setter
    def pgresult(self, result: Optional[pq.proto.PGresult]) -> None: ...
    def set_row_types(
        self, types: Sequence[Tuple[int, pq.Format]]
    ) -> None: ...
    def get_dumper(self, obj: Any, format: pq.Format) -> Dumper: ...
    def lookup_dumper(self, src: type, format: pq.Format) -> DumperType: ...
    def load_row(self, row: int) -> Optional[Tuple[Any, ...]]: ...
    def load_sequence(
        self, record: Sequence[Optional[bytes]]
    ) -> Tuple[Any, ...]: ...
    def get_loader(self, oid: int, format: pq.Format) -> Loader: ...
    def lookup_loader(self, oid: int, format: pq.Format) -> LoaderType: ...

def register_builtin_c_loaders() -> None: ...
def connect(conninfo: str) -> PQGen[pq.proto.PGconn]: ...
def execute(pgconn: pq.proto.PGconn) -> PQGen[List[pq.proto.PGresult]]: ...

# vim: set syntax=python:
