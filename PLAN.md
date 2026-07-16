# TUiDo Development Plan

## Now

- [ ] Define the supported commands
- [x] Add persistent JSON storage
- [x] Implement `create-list`
- [x] Implement `show-lists`

## Next

- [ ] Add items to a list
- [ ] Mark items complete
- [ ] Delete items and lists
- [ ] Add tests

## Later

- [ ] Replace JSON with SQLite
- [ ] Package TUiDo as an installable command
- [ ] Add colors and improved output

## Decisions

- Start with JSON because it is easy to inspect.
- Keep CLI commands separate from storage functions.
