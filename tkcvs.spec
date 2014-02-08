%define name tkcvs
%define version 8.2.1
%define ver %(echo %{version} | sed -e 's/\\./_/g')

Summary:	Tk interface for CVS
Name:		%{name}
Version: 	%{version}
Release: 	5
License:	GPLv2
Group:		Development/Other
Source:		http://www.twobarleycorns.net/%{name}_%{ver}.tar.gz
Patch0:		tkcvs-8.2.1-paths.patch
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
%patch0 -p1 -b .paths

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


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1:8.2.1-4mdv2011.0
+ Revision: 670710
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1:8.2.1-3mdv2011.0
+ Revision: 608023
- rebuild

* Wed Jun 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1:8.2.1-2mdv2010.1
+ Revision: 546913
- rediff patch0 correctly (based on patch from older svn rev) fixes (mdv#59595)

* Tue Apr 06 2010 Sandro Cazzaniga <kharec@mandriva.org> 1:8.2.1-1mdv2010.1
+ Revision: 531967
- remove post && postun
- fix license
- rediff patch0, partially applied
- update to 8.2.1

* Tue Mar 30 2010 Frederic Crozat <fcrozat@mandriva.com> 1:8.2-5mdv2010.1
+ Revision: 529787
- Add missing dependency on tcl

* Tue Mar 30 2010 Frederic Crozat <fcrozat@mandriva.com> 1:8.2-4mdv2010.1
+ Revision: 529719
- Remove patch1, fixes Mdv bug #40077

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1:8.2-3mdv2010.1
+ Revision: 520287
- rebuilt for 2010.1

* Wed Aug 12 2009 Frederik Himpe <fhimpe@mandriva.org> 1:8.2-2mdv2010.0
+ Revision: 415721
- Really update to new version 8.2
- Make source version number automatically from package version so
  mdvsys update works fine next time
- update to new version 8.2

* Sun May 31 2009 Olivier Thauvin <nanardon@mandriva.org> 1:8.0.4-5mdv2010.0
+ Revision: 381630
- fix #40077

* Sat Mar 21 2009 Funda Wang <fwang@mandriva.org> 1:8.0.4-4mdv2009.1
+ Revision: 359933
- rediff patch

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1:8.0.4-4mdv2009.0
+ Revision: 225773
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1:8.0.4-3mdv2008.1
+ Revision: 179654
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill explicit icon extension
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Fri Jun 15 2007 Adam Williamson <awilliamson@mandriva.org> 1:8.0.4-2mdv2008.0
+ Revision: 40187
- new release 8.0.4; XDG menu; rebuild for new era
- Import tkcvs



* Tue Apr 18 2006 Olivier Thauvin <nanardon@mandriva.org> 1:8.0.3-1mdk
- 8_0_3

* Sun Feb 12 2006 Olivier Thauvin <nanardon@mandriva.org> 1:8.0.2-1mdk
- 8.0.2
- remove patch1, merge upstream

* Wed Jan 04 2006 Oden Eriksson <oeriksson@mandrakesoft.com> 1:7.2.2-2mdk
- P1: security fix for CVE-2005-3343

* Wed Feb 09 2005 Frederic Lepied <flepied@mandrakesoft.com> 1:7.2.2-1mdk
- New release 7.2.2

* Mon Aug 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 7.2-3mdk
- Rebuild with new menu

* Wed Jun 02 2004 Michael Scherer <misc@mandrake.org> 7.2-2mdk 
- [DIRM]
- allows to use %%dir

* Tue Jan 27 2004 Frederic Lepied <flepied@mandrakesoft.com> 7.2-1mdk
- 7.2

* Fri Dec 12 2003 Frederic Lepied <flepied@mandrakesoft.com> 7.1.4-1mdk
- 7.1.4
- tkdiff 4.0b4

* Fri Jul 25 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 7.1.2-3mdk
- rebuild

* Thu Feb 27 2003 David BAUDENS <baudens@mandrakesoft.com> 7.1.2-2mdk
- Fix icons

* Sun Dec 29 2002 Frederic Lepied <flepied@mandrakesoft.com> 7.1.2-1mdk
- 7.1.2

* Thu Dec  5 2002 Frederic Lepied <flepied@mandrakesoft.com> 7.1.1-1mdk
- 7.1.1

* Sun Nov 10 2002 Frederic Lepied <flepied@mandrakesoft.com> 7.1-1mdk
- 7.1

* Fri Feb  8 2002 Frederic Lepied <flepied@mandrakesoft.com> 7.0.3-1mdk
- 7.0.3

* Wed Jan 09 2002 David BAUDENS <baudens@mandrakesoft.com> 7.0.2-2mdk
- Fix menu entries (png icons)

* Thu Nov 22 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 7.0.2-1mdk
- new release

* Tue Sep 11 2001 David BAUDENS <baudens@mandrakesoft.com> 7.0-3mdk
- Really use new icons
- Fix update/clean_menus

* Wed Aug 29 2001 David BAUDENS <baudens@mandrakesoft.com> 7.0-2mdk
- Use new icons

* Thu Jul 19 2001 Frederic Lepied <flepied@mandrakesoft.com> 7.0-1mdk
- 7.0

* Mon Nov 13 2000 Frederic Lepied <flepied@mandrakesoft.com> 6.4-2mdk
- added longtitles.

* Sun Oct 15 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 6.4-1mdk
- 6.4.

* Mon Oct 09 2000 Daouda Lo <daouda@mandrakesoft.com> 6.3-3mdk
- icons forever
- macroz..

* Wed Aug 30 2000 Frederic Lepied <flepied@mandrakesoft.com> 6.3-2mdk
- noreplace

* Wed Aug 23 2000 Frederic Lepied <flepied@mandrakesoft.com> 6.3-1mdk
- 6.3

* Tue Mar 28 2000 Frederic Lepied <flepied@mandrakesoft.com> 6.3b3-1mdk
- 6.3b3

* Mon Mar 27 2000 Frederic Lepied <flepied@mandrakesoft.com> 6.2b3-2mdk
- group fix.
- menu support.

* Tue Dec 28 1999 Jerome Dumonteil <jd@mandrakesoft.com>
- change version
- Mandrake adaptations
- default cvsroot to /var/cvs

* Wed Dec 23 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- initial rpm release
