import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='TestGymv0',
    entry_point='gym_DanL.envs:DanLEnv',
)
