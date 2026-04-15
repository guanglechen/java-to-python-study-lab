"""第 2 阶段 Day 5：async/await 示例。 EN: Phase 2 Day 5 async/await demos."""

from __future__ import annotations

import asyncio


async def fetch_user_name(user_id: int, delay: float = 0.01) -> str:
    """模拟异步获取用户名。 EN: Simulate async user-name lookup."""
    await asyncio.sleep(delay)
    return f"user-{user_id}"


async def fetch_user_score(user_id: int, delay: float = 0.01) -> int:
    """模拟异步获取用户积分。 EN: Simulate async user-score lookup."""
    await asyncio.sleep(delay)
    return user_id * 10


async def gather_user_names(user_ids: list[int], delay: float = 0.01) -> list[str]:
    """并发获取一批用户名。 EN: Fetch a batch of user names concurrently."""
    tasks = [fetch_user_name(user_id, delay) for user_id in user_ids]
    return await asyncio.gather(*tasks)


def main() -> None:
    """手动验证 async 示例。 EN: Manual check for async demos."""
    names = asyncio.run(gather_user_names([1, 2, 3], delay=0.01))
    print(f"names={names}")


if __name__ == "__main__":
    main()
