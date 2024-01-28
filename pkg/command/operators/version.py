from __future__ import annotations

import typing

from .. import operator, cmdmgr, entities, errors
from ...utils import updater


@operator.operator_class(
    name="version",
    help="显示版本信息",
    usage='!version'
)
class VersionCommand(operator.CommandOperator):

    async def execute(
        self,
        context: entities.ExecuteContext
    ) -> typing.AsyncGenerator[entities.CommandReturn, None]:
        reply_str = f"当前版本: \n{updater.get_current_version_info()}"

        try:
            if updater.is_new_version_available():
                reply_str += "\n\n有新版本可用, 使用 !update 更新"
        except:
            pass

        yield entities.CommandReturn(text=reply_str.strip())