# 🐧 Building Custom Fedora Image
CentenV's custom Linux build based off of Fedora.


---


## 🎩 Download and Install Fedora
https://fedoraproject.org/

## 🛠️ Installing/Configuring Applications
### Update the OS
```
sudo dnf update
```
### Installing GNOME (reboot when completed)
```
sudo dnf install @base-x gnome-shell gnome-terminal nautilus firefox gnome-browser-connector gnome-tweaks @development-tools
sudo systemctl set-default graphical.target
```
Miscellaneous GNOME Configs
```
gsettings set org.gnome.desktop.wm.preferences button-layout ":minimize,maximize,close"
sudo dnf remove gnome-tour
```
### Installing Extra Dependencies
```
sudo dnf group install "Hardware Support"
sudo dnf install git make vim nano wget
```


## 🔨 OS Configuration
### Expanding the root partition
```
sudo lvextend -r -l +100%FREE /dev/mapper/fedora*
```
### Installing/Setting Up zsh (reboot when completed)
```
sudo dnf install zsh util-linux-user gnu-free*-fonts
chsh -s $(which zsh)
mkdir ~/.zsh
```
#### Oh my Zsh Setup
*Setup zsh before installing Oh my Zsh*
```
cp ~/.zshrc ~/.zshrc.bak
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
#### Zsh Extensions
```
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions
echo "source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh" | tee -a ~/.zshrc
```
#### Zsh Theme (~/.zshrc)
```
ZSH_THEME="jonathan"
```


## 🖥️ Miscellaneous
### Install GNOME Extensions
#### Install the GNOME browser extension
Chrome/Brave: https://chrome.google.com/webstore/detail/gnome-shell-integration/gphhapmejobijbbhgpjhcjognlahblep

Firefox: https://addons.mozilla.org/en-US/firefox/addon/gnome-shell-integration/
#### Extensions:
- https://extensions.gnome.org/extension/3088/extension-list/
- https://extensions.gnome.org/extension/3193/blur-my-shell/
- https://extensions.gnome.org/extension/307/dash-to-dock/
- https://extensions.gnome.org/extension/1460/vitals/
### Gnome Configurations
#### Binding Ctrl + Alt + T to open terminal
`Settings` > `Keyboard` > `View and Customize Shortcuts` > `Custom Shortcuts` > `Add Shortcut`
#### Configuring the time display
`Settings` > `Date & Time` > **Time Format: AM/PM**
#### Enabling battery percentage
`Settings` > `Power` > **Show Battery Percentage=True**
#### Configuring Blur my Shell
`Extension List` > `Blur my Shell Settings` > **Sigma=10, Brightness=0.65,Color and noise effects=True, Panel blur=True, Static blur=True, Disable when a window is near=True, Background blur=True, Overview components style=Transparent, Application folder blur=True, Dash to Dock blur=False, Application blur=False, Lockscreen blur=True**
#### Configuring Dash to Dock
`Extension List` > `Dash to Dock Settings` > **Show on all monitors=True, Intelligent autohide=True, Show trashcan=False, Show overview on startup=False, Customize the dash color=True:black, Customize opacity=Fixed:70%**
#### Configuring Vitals
`Extension List` > `Vitals Settings` > **Position in panel=Center, Use higher precision=True**\
`Vitals Extension` > Add **Processor: Usage, Frequency | Memory: Usage, Free | Storage: Free | Network: Public IP, Device rx**
### Get Wallpapers
```
cd /tmp
git clone https://github.com/CentenV/CustomLinux.git
cd CustomLinux/
cp -r ./Wallpapers/ ~/Pictures/
```
### Configure Plymouth
```
plymouth-set-default-theme -l
sudo plymouth-set-default-theme -R bgrt
```
### Hide GRUB at boot (only when single booting) (/etc/default/grub)
##### Replace
```
GRUB_TIMEOUT=0
```
##### Add
```
GRUB_TIMEOUT_STYLE=hidden
GRUB_DISABLE_OS_PROBER=true
```
UEFI GRUB Rebuild
```
sudo grub2-mkconfig -o /etc/grub2-efi.cfg
```
Legacy GRUB Rebuild
```
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```
### Configuring Fonts
Do this all in `/tmp`
#### Primary Font
```
sudo mkdir /usr/share/fonts/Poppins
wget -o Poppins.zip https://fonts.google.com/download?family=Poppins
sudo unzip Poppins.zip -d /usr/share/fonts/Poppins
sudo fc-cache -fv
```
#### Terminal Font
##### Download font
```
sudo mkdir /usr/share/fonts/ProFont
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.3.3/ProFont.zip
sudo unzip ProFont.zip -d /usr/share/fonts/ProFont
sudo fc-cache -fv
```
##### To check whether fonts are present in the list
```
fc-list
```
#### Apply Fonts
`Tweaks` > `Fonts` > `Interface Text` > **Poppins Semibold, 12**\
`Tweaks` > `Fonts` > `Document Text` > **Poppins Regular, 11**\
`Tweaks` > `Fonts` > `Monospace Text` > **ProFontIIx Nerd Font Mono Regular, 10**\
`Tweaks` > `Fonts` > `Legacy Window Titles` > **Poppins Regular, 11**
### Install Brave
```
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://brave-browser-rpm-release.s3.brave.com/brave-browser.repo
sudo rpm --import https://brave-browser-rpm-release.s3.brave.com/brave-core.asc
sudo dnf install brave-browser
```
### Install Neofetch
```
sudo dnf install neofetch
```
### Install Bashtop/Btop
```
sudo dnf install btop
```
```
cd /tmp
sudo git clone https://github.com/aristocratos/bashtop.git
cd bashtop
sudo make install
```
### Install Visual Studio Code
```
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
```
```
sudo dnf check-update
sudo dnf install code
```
### Install Virtualbox
```
sudo dnf install kernel-headers kernel-devel dkms elfutils-libelf-devel qt5-qtx11extras
```
```
cat <<EOF | sudo tee /etc/yum.repos.d/virtualbox.repo 
[virtualbox]
name=Fedora \$releasever - \$basearch - VirtualBox
baseurl=http://download.virtualbox.org/virtualbox/rpm/fedora/\$releasever/\$basearch
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://www.virtualbox.org/download/oracle_vbox.asc
EOF 
```
```
sudo dnf install VirtualBox-7.0 
```