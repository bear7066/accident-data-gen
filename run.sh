#!/usr/bin/env bash
set -euo pipefail

NUM_VIDEOS="${NUM_VIDEOS:-1}"

ACTION_LABELS=(
  fall_forward
  fall_face_first
  fall_backward
  fall_sideways_left
  fall_sideways_right
  fall_diagonal_forward_left
  fall_diagonal_forward_right
  fall_rotational
  fall_slip_wet_floor
  fall_trip_obstacle
  fall_trip_own_feet
  fall_lose_balance_standing
  fall_from_chair
  fall_from_bed
  fall_from_wheelchair
  fall_down_stairs
  fall_while_carrying_object
  fall_while_turning
  collapse_sudden_drop
  collapse_slow_slump
  collapse_with_clutching_body
  collapse_with_wall_slide
  collapse_with_stiffening_and_shaking
  collapse_with_unilateral_weakness
  collapse_post_transition
  collapse_stumble_loss_of_motor_control
  accident_door_collision
  accident_falling_object_hit
  accident_one_on_one_collision
  accident_crowd_jostle
  accident_collision_with_stationary_object
  accident_step_off_edge
  post_fall_motionless
  post_fall_struggling_to_get_up
  post_fall_crawling_for_help
  post_fall_calling_for_help
  post_fall_rolling_in_pain
  post_fall_unconscious
  hn_sit_down_floor
  hn_lie_down_floor
  hn_stand_up_from_floor
  hn_stand_up_from_chair
  hn_bend_over_pick_up
  hn_squat_tie_shoes
  hn_yoga_floor_pose
  hn_stretching_floor
  hn_pushup_situp
  hn_play_with_child_floor
)

for action_label in "${ACTION_LABELS[@]}"; do
  uv run src/generate.py \
    --num-videos "$NUM_VIDEOS" \
    --action-label "$action_label" \
    --video-json-output-dir "output/records" \
    --video-output-dir "output/videos"
done
