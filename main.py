"""项目运行入口。"""

from src.router import Router


def _dump_state(state: object) -> dict:
    """兼容 pydantic v1 / v2 的状态导出。"""
    if hasattr(state, "model_dump"):
        return state.model_dump(mode="json", exclude_none=True)
    if hasattr(state, "dict"):
        return state.dict(exclude_none=True)
    raise TypeError("Unsupported state object for dump.")


def main() -> None:
    """构造 Router，只演示 Agent1 的最小可运行结果。"""
    mock_user_input = (
        "我想做一个都市情感短剧：女主是失业编剧，男主是假装冷漠的投资人，"
        "两人因为一起改造老剧场而不断碰撞，整体希望有反转和情绪拉扯。"
    )

    router = Router()
    final_state = router.run_agent1_only(mock_user_input)

    print("=== Raw Input ===")
    print(mock_user_input)
    print()

    print("=== Agent1 StoryElements ===")
    print(_dump_state(final_state.story_elements))
    print()

    print("=== PipelineState ===")
    print(_dump_state(final_state))


if __name__ == "__main__":
    main()
