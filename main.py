"""项目运行入口。"""

from pprint import pprint

from src.router import Router


def _dump_state(state: object) -> dict:
    """兼容 pydantic v1 / v2 的状态导出。"""
    if hasattr(state, "model_dump"):
        return state.model_dump(mode="json", exclude_none=True)
    if hasattr(state, "dict"):
        return state.dict(exclude_none=True)
    raise TypeError("Unsupported state object for dump.")


def _print_story_elements(story_elements: object) -> None:
    """按中文标题打印灵感拆解结果。"""
    data = _dump_state(story_elements)
    labels = [
        ("raw_fragments", "原始灵感碎片"),
        ("character_drives", "外在目标与内在缺陷"),
        ("antagonist_force", "核心反派力量"),
        ("high_stakes", "核心赌注"),
        ("world_rules", "关键设定与道具"),
        ("thematic_premise", "核心困境主题"),
        ("opening_hook", "黄金开局点"),
        ("missing_elements", "缺失要素"),
    ]

    for key, label in labels:
        print(f"{label}:")
        pprint(data.get(key))
        print()


def main() -> None:
    """构造 Router，只演示 Agent1 的最小可运行结果。"""
    mock_user_input = (
        "我想做一个都市情感短剧：女主是失业编剧，男主是假装冷漠的投资人，"
        "两人因为一起改造老剧场而不断碰撞，整体希望有反转和情绪拉扯。"
    )

    router = Router()
    final_state = router.run_agent1_only(mock_user_input)

    print("=== 原始输入 ===")
    print(mock_user_input)
    print()

    print("=== Agent1 灵感拆解结果 ===")
    _print_story_elements(final_state.story_elements)
    print()

    print("=== PipelineState ===")
    pprint(_dump_state(final_state))


if __name__ == "__main__":
    main()
