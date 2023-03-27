Name:           jetbrains-mono-nerd-fonts
Version:        2.3.3
Release:        %{autorelease}
Summary:        Jetbrains Mono font patched with NerdFont symbols

License:        OFL
URL:            https://www.nerdfonts.com/
Source:         https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/JetBrainsMono.zip

BuildArch:      noarch

%description
Nerd Fonts patches developer targeted fonts with a high number of glyphs (icons). Specifically to add a high number of extra glyphs from popular ‘iconic fonts’ such as Font Awesome, Devicons, Octicons, and others.

%global debug_package %{nil}

%prep
%autosetup -c -n JetBrainsMono

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/JetBrainsMono/
install JetBrains* %{buildroot}%{_datadir}/fonts/JetBrainsMono/

%files
%{_datadir}/fonts/JetBrainsMono
