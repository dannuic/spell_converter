import pandas as pd


def from_enumeration(
        idx_name: str,
        value_name: str,
        enum_def: list[tuple[int, str]]
) -> pd.DataFrame:
    ids, values = tuple([list(t) for t in zip(*enum_def)])

    return pd.DataFrame({
        idx_name: ids,
        value_name: values
    }).set_index([idx_name])


def from_list(
        idx_name: str,
        value_name: str,
        values: list[str]
) -> pd.DataFrame:
    return pd.DataFrame({
        idx_name: list(range(len(values))),
        value_name: values,
    }).set_index([idx_name])
