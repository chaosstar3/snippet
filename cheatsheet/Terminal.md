## Color
```sh
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
NC='\033[0m'

echo -e "$color: \\033[38;5;${color}m text \\033[0m"
echo -e "$color: \\033[48;5;${color}m bg   \\033[0m"
```

## Notify
### OSC 777

```
printf "\033]777;notify;Title;Body\007"
```

