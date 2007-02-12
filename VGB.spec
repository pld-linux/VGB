Summary:	GameBoy emulator
Summary(pl.UTF-8):	Emulator GameBoya
Name:		VGB
Version:	3.0
Release:	1
License:	Copyright (distributable)
Group:		Applications
Source0:	http://fms.komkon.org/VGB/%{name}30-Linux-80x86-bin.tar.Z
# Source0-md5:	e8009549977f1e763b9dd026f219941c
URL:		http://fms.komkon.org/VGB/
ExclusiveArch:  %{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virtual GameBoy (VGB) is an emulator of the GameBoy videogame handheld
produced by Nintendo. It runs GameBoy, Super GameBoy, and GameBoy
Color games on PCs, Macs, PocketPCs, or just about any other
sufficiently fast computer in existence. It can also help to debug
GameBoy software without using a costly development system.

%description -l pl.UTF-8
Virtual GameBoy (VGB) to emulator kieszonkowej gry telewizyjnej
GameBoy produkowanej przez Nintendo. Uruchamia gry z GameBoya, Super
GameBoya i GameBoya Color na komputerach PC, Mac, PocketPC albo innych
wystarczająco szybkich. Może także pomóc przy poprawianiu
oprogramowania dla GameBoya bez kosztownego systemu programistycznego.

%prep
%setup -q -c 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install vgb $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc VGB.html
%attr(755,root,root) %{_bindir}/vgb
