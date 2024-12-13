# Changelog

## [Unreleased]
- Update `README.md` to reflect recent changes (modularized frame logic, simplified `TemplatePro`, deleted redundant branches). ([Issue: #4](https://github.com/Kader-the-Coder/TemplatePro/issues/4))

## [1.0.0] - 2024-12-13 ([Issue: #1](https://github.com/Kader-the-Coder/TemplatePro/issues/4))
### Added
- Modularized frame logic by creating a `frame_base` interface for consistency across frame modules.
- Separated each frame's layout and widget setup into individual modules (`frame_top.py`, `frame_left.py`, `frame_body.py`, `frame_bottom.py`).
- Simplified the `TemplatePro` class to focus solely on initializing and managing the application's grid and layout. 
- Moved logic for setting up individual frames out of `TemplatePro` and into the respective frame modules. 
- Introduced a cleaner interface for managing frame events, widgets, styling, and event handlers. 
- Merged and deleted the `refactor/frames_main_modularity` branch from the repository. 

### Changed
- The `TemplatePro` class no longer handles frame setup. It now only manages layout and grid. 
- The overall application structure has been refactored to make each frame modular and self-contained.

## [0.0.1] - 2024-09-20
- Initial upload of application
