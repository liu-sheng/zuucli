import json
from cliff import columns


class DictListColumn(columns.FormattableColumn):
    """Format column for dict content"""

    def human_readable(self):
        return json.dumps(self._value, indent=4)
