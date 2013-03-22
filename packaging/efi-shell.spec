Name:           efi-shell
Version:        2.0
Release:        1
License:        BSD-3-Clause
Summary:        Shell for the firmware
Url:            http://sourceforge.net/projects/edk2/
Group:          Base/Startup
Source0:        packaging/shell.efi

%description
EFI Shell for loading EFI applications including bootloaders.

%prep

%build

%install
rm -fr %{buildroot}
install -D %{SOURCE0} %{buildroot}/boot/EFI/shellx64.efi

%files
%defattr(-,root,root)
/boot/EFI/shellx64.efi
