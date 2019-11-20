from typing import Any, Optional, Callable, Sequence, Tuple, Union, List, Dict, Sized, overload
from typing_extensions import TypedDict


# _Location: contains information about a location of a symbol. The first string
# is the absolute file path, the second is the file path relative to the
# project, the third element is a two-element tuple of the row and column
_Location = Tuple[str, str, Tuple[int, int]]
# value: any of the Python data types bool, int, float, str, list or dict
_Value = Union[dict, list, str, float, bool, None]
# _Layout: a dict such as {"cols": [0, 0.5, 1], "rows": [0, 0.5, 1],
# "cells": [[0, 0, 1, 2], [1, 0, 2, 1], [1, 1, 2, 2]]}
_Layout = TypedDict("_Layout",
                    {
                        "cols": Sequence[float],
                        "rows": Sequence[float],
                        "cells": Sequence[Sequence[int]]
                    })
# _Vector: represents x and y coordinates
_Vector = Tuple[float, float]


class _LogWriter:
    def flush(self): ...

    def write(self, s): ...


HOVER_TEXT: int
HOVER_GUTTER: int
HOVER_MARGIN: int
ENCODED_POSITION: int
TRANSIENT: int
FORCE_GROUP: int
IGNORECASE: int
LITERAL: int
MONOSPACE_FONT: int
KEEP_OPEN_ON_FOCUS_LOST: int
HTML: int
COOPERATE_WITH_AUTO_COMPLETE: int
HIDE_ON_MOUSE_MOVE: int
HIDE_ON_MOUSE_MOVE_AWAY: int
DRAW_EMPTY: int
HIDE_ON_MINIMAP: int
DRAW_EMPTY_AS_OVERWRITE: int
PERSISTENT: int
DRAW_OUTLINED: int
DRAW_NO_FILL: int
DRAW_NO_OUTLINE: int
DRAW_SOLID_UNDERLINE: int
DRAW_STIPPLED_UNDERLINE: int
DRAW_SQUIGGLY_UNDERLINE: int
HIDDEN: int
OP_EQUAL: int
OP_NOT_EQUAL: int
OP_REGEX_MATCH: int
OP_NOT_REGEX_MATCH: int
OP_REGEX_CONTAINS: int
OP_NOT_REGEX_CONTAINS: int
CLASS_WORD_START: int
CLASS_WORD_END: int
CLASS_PUNCTUATION_START: int
CLASS_PUNCTUATION_END: int
CLASS_SUB_WORD_START: int
CLASS_SUB_WORD_END: int
CLASS_LINE_START: int
CLASS_LINE_END: int
CLASS_EMPTY_LINE: int
INHIBIT_WORD_COMPLETIONS: int
INHIBIT_EXPLICIT_COMPLETIONS: int
DIALOG_CANCEL: int
DIALOG_YES: int
DIALOG_NO: int
UI_ELEMENT_SIDE_BAR: int
UI_ELEMENT_MINIMAP: int
UI_ELEMENT_TABS: int
UI_ELEMENT_STATUS_BAR: int
UI_ELEMENT_MENU: int
UI_ELEMENT_OPEN_FILES: int
LAYOUT_INLINE: int
LAYOUT_BELOW: int
LAYOUT_BLOCK: int


def version() -> str: ...


def platform() -> str: ...


def arch() -> str: ...


def channel() -> str: ...


def executable_path() -> str: ...


def executable_hash() -> Tuple[str, str, str]: ...


def packages_path() -> str: ...


def installed_packages_path() -> str: ...


def cache_path() -> str: ...


def status_message(msg: str) -> None: ...


def error_message(msg: str) -> None: ...


def message_dialog(msg: str) -> None: ...


def ok_cancel_dialog(msg: str, ok_title: str = ...) -> bool: ...


def yes_no_cancel_dialog(msg: str, yes_title: str = ...,
                         no_title: str = ...) -> int: ...


def run_command(cmd: str, args: Optional[Dict[str, Any]] = ...) -> None: ...


def get_clipboard(size_limit: int = ...) -> str: ...


def set_clipboard(text: str) -> None: ...


def log_commands(flag: bool) -> None: ...


def log_input(flag: bool) -> None: ...


def log_result_regex(flag: bool) -> None: ...


def log_indexing(flag: bool) -> None: ...


def log_build_systems(flag: bool) -> None: ...


def score_selector(scope_name: str, selector: str) -> int: ...


def load_resource(name: str) -> str: ...


def load_binary_resource(name: str) -> bytes: ...


def find_resources(pattern: str) -> List[str]: ...


def encode_value(val: _Value, pretty: bool = ...) -> str: ...


def decode_value(data: str) -> _Value: ...


@overload
def expand_variables(val: str, variables: Dict[str, str]) -> str: ...


@overload
def expand_variables(val: List[str], variables: Dict[str, str]) -> List[str]: ...


@overload
def expand_variables(val: Dict[str, str], variables: Dict[str, str]) -> Dict[str, str]: ...


def load_settings(base_name: str) -> 'Settings': ...


def save_settings(base_name: str) -> None: ...


def set_timeout(f: Callable[[], None], timeout_ms: int = ...) -> None: ...


def set_timeout_async(f: Callable[[], None], timeout_ms: int = ...) -> None: ...


def active_window() -> 'Window': ...


def windows() -> 'List[Window]': ...


def get_macro() -> List[dict]: ...


class Window:
    window_id: int
    settings_object: 'Optional[Settings]'
    template_settings_object: 'Optional[Settings]'

    def __init__(self, id: int) -> None: ...

    def __eq__(self, other) -> bool: ...

    def __bool__(self) -> bool: ...

    def id(self) -> int: ...

    def is_valid(self) -> bool: ...

    def hwnd(self) -> int: ...

    def active_sheet(self) -> 'Optional[Sheet]': ...

    def active_view(self) -> 'Optional[View]': ...

    def run_command(self, cmd: str, args: Optional[Dict[str, Any]] = ...) -> None: ...

    def new_file(self, flags: int = ..., syntax: str = ...) -> 'View': ...

    def open_file(self, fname: str, flags: int = ...,
                  group: int = ...) -> 'View': ...

    def find_open_file(self, fname: str) -> 'Optional[View]': ...

    def num_groups(self) -> int: ...

    def active_group(self) -> int: ...

    def focus_group(self, idx: int) -> None: ...

    def focus_sheet(self, sheet: 'Sheet') -> None: ...

    def focus_view(self, view: 'View') -> None: ...

    def get_sheet_index(self, sheet: 'Sheet') -> Tuple[int, int]: ...

    def get_view_index(self, view: 'View') -> Tuple[int, int]: ...

    def set_sheet_index(self, sheet: 'Sheet', group: int, idx: int) -> None: ...

    def set_view_index(self, view: 'View', group: int, idx: int) -> None: ...

    def sheets(self) -> 'List[Sheet]': ...

    def views(self) -> 'List[View]': ...

    def active_sheet_in_group(self, group: int) -> 'Optional[Sheet]': ...

    def active_view_in_group(self, group: int) -> 'Optional[View]': ...

    def sheets_in_group(self, group: int) -> 'List[Sheet]': ...

    def views_in_group(self, group: int) -> 'List[View]': ...

    def transient_sheet_in_group(self, group: int) -> 'Optional[Sheet]': ...

    def transient_view_in_group(self, group: int) -> 'Optional[View]': ...

    def layout(self) -> _Layout: ...

    def getlayout(self): ...

    def setlayout(self, layout: _Layout) -> None: ...

    def create_output_panel(self, name: str, unlisted: bool = ...) -> 'View': ...

    def find_output_panel(self, name: str) -> 'Optional[View]': ...

    def destroy_output_panel(self, name: str) -> None: ...

    def active_panel(self) -> Optional[str]: ...

    def panels(self) -> List[str]: ...

    def get_output_panel(self, name): ...

    def show_input_panel(self,
                         caption: str,
                         initial_text: str,
                         on_done: Optional[Callable[[str], None]],
                         on_change: Optional[Callable[[str], None]],
                         on_cancel: Callable[[], None]) -> 'View': ...

    def show_quick_panel(self,
                         items: Union[Sequence[str], Sequence[Sequence[str]]],
                         on_select: Callable[[int], None],
                         flags: int = ...,
                         selected_index: int = ...,
                         on_highlight: Optional[Callable[[int], None]] = ...) -> None: ...

    def is_sidebar_visible(self) -> bool: ...

    def set_sidebar_visible(self, flag: bool) -> None: ...

    def is_minimap_visible(self) -> bool: ...

    def set_minimap_visible(self, flag: bool) -> None: ...

    def is_status_bar_visible(self) -> bool: ...

    def set_status_bar_visible(self, flag: bool) -> None: ...

    def get_tabs_visible(self) -> bool: ...

    def set_tabs_visible(self, flag: bool) -> None: ...

    def is_menu_visible(self) -> bool: ...

    def set_menu_visible(self, flag: bool) -> None: ...

    def folders(self) -> List[str]: ...

    def project_file_name(self) -> str: ...

    def project_data(self) -> Optional[Dict[str, _Value]]: ...

    def set_project_data(self, v: Dict[str, _Value]) -> None: ...

    def settings(self) -> 'Settings': ...

    def template_settings(self) -> 'Settings': ...

    def lookup_symbol_in_index(self, sym: str) -> List[_Location]: ...

    def lookup_symbol_in_open_files(self, sym: str) -> List[_Location]: ...

    def extract_variables(self) -> Dict[str, str]: ...

    def status_message(self, msg: str) -> None: ...


class Edit:
    edit_token: Any

    def __init__(self, token) -> None: ...


class Region:
    a: int
    b: int
    xpos: int

    def __init__(self, a: int, b: Optional[int] = ..., xpos: int = ...) -> None: ...

    def __len__(self) -> int: ...

    def __eq__(self, rhs) -> bool: ...

    def __lt__(self, rhs: 'Region') -> bool: ...

    def __bool__(self) -> bool: ...

    def __contains__(self, x: 'Union[Region, int]') -> bool: ...

    def is_empty(self) -> bool: ...

    def empty(self) -> bool: ...

    def begin(self) -> int: ...

    def end(self) -> int: ...

    def size(self) -> int: ...

    def contains(self, x: 'Union[Region, int]') -> bool: ...

    def cover(self, rhs: 'Region') -> 'Region': ...

    def intersection(self, rhs: 'Region') -> 'Region': ...

    def intersects(self, rhs: 'Region') -> bool: ...


class Selection(Sized):
    view_id: Any

    def __init__(self, id: int) -> None: ...

    def __len__(self) -> int: ...

    def __getitem__(self, index: int) -> Region: ...

    def __delitem__(self, index: int) -> None: ...

    def __contains__(self, region: Region) -> bool: ...

    def __eq__(self, rhs) -> bool: ...

    def __lt__(self, rhs) -> bool: ...

    def __bool__(self) -> bool: ...

    def is_valid(self) -> bool: ...

    def clear(self) -> None: ...

    def add(self, x: Union[Region, int]) -> None: ...

    def add_all(self, regions: Sequence[Union[Region, int]]) -> None: ...

    def subtract(self, region: Region) -> None: ...

    def contains(self, region: Region) -> None: ...


class Sheet:
    sheet_id: int

    def __init__(self, id: int) -> None: ...

    def __eq__(self, other) -> bool: ...

    def id(self) -> int: ...

    def window(self) -> Optional[Window]: ...

    def view(self) -> 'Optional[View]': ...


class View:
    view_id: int
    selection: Selection
    settings_object: 'Settings'

    def __init__(self, id: int) -> None: ...

    def __len__(self) -> int: ...

    def __eq__(self, other) -> bool: ...

    def __bool__(self) -> bool: ...

    def id(self) -> int: ...

    def buffer_id(self) -> int: ...

    def is_valid(self) -> bool: ...

    def is_primary(self) -> bool: ...

    def window(self) -> Optional[Window]: ...

    def file_name(self) -> Optional[str]: ...

    def close(self) -> bool: ...

    def retarget(self, new_fname: str) -> None: ...

    def name(self) -> str: ...

    def set_name(self, name: str) -> None: ...

    def reset_reference_document(self) -> None: ...

    def set_reference_document(self, reference: str) -> None: ...

    def is_loading(self) -> bool: ...

    def is_dirty(self) -> bool: ...

    def is_read_only(self) -> bool: ...

    def set_read_only(self, read_only: bool) -> None: ...

    def is_scratch(self) -> bool: ...

    def set_scratch(self, scratch: bool) -> None: ...

    def encoding(self) -> str: ...

    def set_encoding(self, encoding_name: str) -> None: ...

    def line_endings(self) -> str: ...

    def set_line_endings(self, line_ending_name: str) -> None: ...

    def size(self) -> int: ...

    def begin_edit(self, edit_token, cmd,
                   args: Optional[Dict[str, Any]] = ...): ...

    def end_edit(self, edit: Edit) -> None: ...

    def is_in_edit(self) -> bool: ...

    def insert(self, edit: Edit, pt: int, text: str) -> int: ...

    def erase(self, edit: Edit, r: Region) -> None: ...

    def replace(self, edit: Edit, r: Region, text: str) -> None: ...

    def change_count(self) -> None: ...

    def run_command(self,
                    cmd: str,
                    args: Optional[Dict[str, Any]] = ...) -> None: ...

    def sel(self) -> Selection: ...

    def substr(self, x: Union[Region, int]) -> str: ...

    def find(self, pattern: str, start_pt: int, flags: int = ...) -> Optional[Region]: ...

    def find_all(self,
                 pattern: str,
                 flags: int = ...,
                 fmt: Optional[str] = ...,
                 extractions: Optional[List[str]] = ...) -> List[_Vector]: ...

    def settings(self) -> 'Settings': ...

    def meta_info(self, key, pt: int): ...

    def extract_tokens_with_scopes(
        self, r: Region) -> List[Tuple[_Vector, str]]: ...

    def extract_scope(self, pt: int) -> Region: ...

    def scope_name(self, pt: int) -> str: ...

    def match_selector(self, pt: int, selector: str) -> bool: ...

    def score_selector(self, pt: int, selector: str) -> int: ...

    def find_by_selector(self, selector: str) -> List[Region]: ...

    def style(self) -> Dict[str, str]: ...

    def style_for_scope(self, scope: str) -> Dict[str, Any]: ...

    def indented_region(self, pt: int) -> Region: ...

    def indentation_level(self, pt: int) -> int: ...

    def has_non_empty_selection_region(self) -> bool: ...

    def lines(self, r: Region) -> List[Region]: ...

    def split_by_newlines(self, r: Region) -> List[Region]: ...

    def line(self, x: Union[Region, int]) -> Region: ...

    def full_line(self, x: Union[Region, int]) -> Region: ...

    def word(self, x: Union[Region, int]) -> Region: ...

    def classify(self, pt: int) -> int: ...

    def find_by_class(self, pt: int, forward: bool,
                      classes: int, separators: str = ...) -> Region: ...

    def expand_by_class(
        self, x: Union[Region, int], classes: int, separators: str = ...) -> Region: ...

    def rowcol(self, tp: int) -> Tuple[int, int]: ...

    def text_point(self, row: int, col: int) -> int: ...

    def visible_region(self) -> Region: ...

    def show(self, x: Union[Selection, Region, int],
             show_surrounds: bool = ...) -> None: ...

    def show_at_center(self, x: Union[Selection, Region, int]) -> None: ...

    def viewport_position(self) -> _Vector: ...

    def set_viewport_position(
        self, xy: _Vector, animate: bool = ...) -> None: ...

    def viewport_extent(self) -> _Vector: ...

    def layout_extent(self) -> _Vector: ...

    def text_tolayout(self, tp: int) -> _Vector: ...

    def layout_to_text(self, xy: _Vector): ...

    def window_tolayout(self, xy: _Vector) -> _Vector: ...

    def window_to_text(self, xy: _Vector) -> int: ...

    def line_height(self) -> float: ...

    def em_width(self) -> float: ...

    def is_folded(self, sr) -> bool: ...

    def folded_regions(self): ...

    def fold(self, x: Union[Region, List[Region]]) -> bool: ...

    def unfold(self, x: Union[Region, List[Region]]) -> List[Region]: ...

    def add_regions(self, key: str, regions: List[Region], scope: str = ...,
                    icon: str = ..., flags: int = ...) -> None: ...

    def get_regions(self, key: str) -> List[Region]: ...

    def erase_regions(self, key: str) -> None: ...

    def add_phantom(self, key: str, region: Region, content: str,
                    layout, on_navigate: Optional[Any] = ...): ...

    def erase_phantoms(self, key: str) -> None: ...

    def erase_phantom_by_id(self, pid: int) -> None: ...

    def query_phantom(self, pid: int): ...

    def query_phantoms(self, pids: List[int]): ...

    def assign_syntax(self, syntax_file: str) -> None: ...

    def set_syntax_file(self, syntax_file: str) -> None: ...

    def symbols(self) -> List[Tuple[Region, str]]: ...

    def get_symbols(self): ...

    def indexed_symbols(self): ...

    def set_status(self, key: str, value: str) -> None: ...

    def get_status(self, key: str) -> str: ...

    def erase_status(self, key: str) -> None: ...

    def extract_completions(self, prefix: str, tp: int = ...): ...

    def find_all_results(self): ...

    def find_all_results_with_text(self): ...

    def command_history(
        self, delta: int, modifying_only: bool = ...) -> Tuple[str, dict, int]: ...

    def overwrite_status(self) -> bool: ...

    def set_overwrite_status(self, value: bool) -> None: ...

    def show_popup_menu(
        self, items: Sequence[str], on_select: Callable[[int], None], flags: int = ...) -> None: ...

    def show_popup(self, content: str, flags: int = ..., location: int = ..., max_width: int = ...,
                   max_height: int = ..., on_navigate: Optional[Callable[[str], None]] = ..., on_hide: Optional[Callable[[], None]] = ...) -> None: ...

    def update_popup(self, content: str) -> None: ...

    def is_popup_visible(self) -> bool: ...

    def hide_popup(self) -> None: ...

    def is_auto_complete_visible(self) -> bool: ...


class Settings:
    settings_id: int

    def __init__(self, id: int) -> None: ...

    def get(self, key: str, default: Optional[_Value] = ...) -> _Value: ...

    def has(self, key: str) -> bool: ...

    def set(self, key: str, value: _Value) -> None: ...

    def erase(self, key: str) -> None: ...

    def add_on_change(self, tag: str, callback: Callable[[], None]) -> None: ...

    def clear_on_change(self, tag: str) -> None: ...


class Phantom:
    region: Region
    content: str
    layout: int
    on_navigate: Optional[Callable[[str], None]]
    id: Any

    def __init__(self, region: Region, content: str, layout: int,
                 on_navigate: Optional[Callable[str], None] = ...) -> None: ...

    def __eq__(self, rhs) -> bool: ...


class PhantomSet:
    view: View
    key: Any
    phantoms: Any

    def __init__(self, view: View, key: str = ...) -> None: ...

    def __del__(self) -> None: ...

    def update(self, new_phantoms: Sequence[Phantom]): ...


class Html:
    data: Any

    def __init__(self, data) -> None: ...

    def __str__(self) -> str: ...