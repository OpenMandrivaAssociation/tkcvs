%define name tkcvs
%define version 8.2.1
%define ver %(echo %{version} | sed -e 's/\\./_/g')

Summary:	Tk interface for CVS
Name:		%{name}
Version: 	%{version}
Release: 	%mkrel 1
License:	GPLv2
Group:		Development/Other
Source:		http://www.twobarleycorns.net/%{name}_%{ver}.tar.gz
Patch0:		tkcvs-8.2.1-fix-paths.patch
Url: 		http://www.twobarleycorns.net/tkcvs.html
BuildRoot:	%_tmppath/%name-%version-%release-root
Requires:	tk cvs tcl
BuildArch:	noarch
Epoch:		1

%description
TkCVS is a Tcl/Tk-based graphical interface to the CVS and Subversion 
configuration management systems.  It includes facilities for providing 
"user friendly" names to modules and directories within the repository, 
and provides a facility to interactively browse the repository looking 
for modules and directories.

%prep
%setup -q -n %{name}_%ver
%patch0 -p0

%install
rm -fr %buildroot

install -d %buildroot/%_bindir/
install -d %buildroot/%_datadir/tkcvs/bitmaps
install -d %buildroot/%_mandir/man1

install tkcvs/tkcvs.tcl %buildroot/%_bindir/tkcvs
install tkdiff/tkdiff %buildroot/%_bindir/tkdiff
install tkcvs/*.tcl       %buildroot/%_datadir/tkcvs
install tkcvs/tclIndex    %buildroot/%_datadir/tkcvs
install tkcvs/bitmaps/*         %buildroot/%_datadir/tkcvs/bitmaps/
install tkcvs/*.1         %buildroot/%_mandir/man1
rm -f %buildroot/%_mandir/tkcvs/tkcvs_def.tcl
install -d %buildroot/%_sysconfdir/cvs/
install tkcvs/tkcvs_def.tcl %buildroot/%_sysconfdir/cvs/

#README.tkcvs tkdiff/COPYING tkcvs/vendor.readme tkcvs/branchgen.sh
ln tkdiff/COPYING tkdiff.COPYING 

# Menu support

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=TkCVS
Comment=Graphical interface to CVS and SVN
Exec=%{_bindir}/%{name} 
Icon=development_tools_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Development;RevisionControl;X-MandrivaLinux-MoreApplications-Development-Tools;
EOF

cat > %{buildroot}%{_datadir}/applications/mandriva-tkdiff.desktop <<EOF
[Desktop Entry]
Name=TkDiff
Comment=Graphical interface to diff
Exec=%{_bindir}/tkdiff
Icon=development_tools_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Development;RevisionControl;X-MandrivaLinux-MoreApplications-Development-Tools;
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ CHANGELOG tkdiff.COPYING
%attr(755,root,root) %_bindir/*
%{_datadir}/tkcvs/*.tcl
%dir %{_datadir}/tkcvs/
%dir %{_datadir}/tkcvs/bitmaps/
%{_datadir}/tkcvs/tclIndex
%{_datadir}/applications/*.desktop
%_mandir/man*/*
%{_datadir}/tkcvs/bitmaps/*
%config(noreplace) %_sysconfdir/cvs/tkcvs_def.tcl
