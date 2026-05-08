import os
import shutil
import argparse
from pathlib import Path

def install_skills(skill_names, target_dir=".claude/skills"):
    """
    Installs selected skills from the repo into the target directory.
    """
    repo_skills_dir = Path("skills")
    repo_hooks_dir = Path("hooks")
    target_path = Path(target_dir)

    # Ensure target directory exists
    target_path.mkdir(parents=True, exist_ok=True)

    skills_to_install = []
    
    if "all" in skill_names:
        skills_to_install = [d.name for d in repo_skills_dir.iterdir() if d.is_dir()]
        hooks_to_install = [d.name for d in repo_hooks_dir.iterdir() if d.is_dir()]
    else:
        skills_to_install = [s for s in skill_names if (repo_skills_dir / s).exists()]
        hooks_to_install = [s for s in skill_names if (repo_hooks_dir / s).exists()]

    for skill in skills_to_install:
        src = repo_skills_dir / skill
        dst = target_path / skill
        if dst.exists():
            print(f"⚠️  Skill '{skill}' already exists in {target_dir}. Overwriting...")
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print(f"✅ Installed Skill: {skill}")

    for hook in hooks_to_install:
        src = repo_hooks_dir / hook
        dst = target_path / hook
        if dst.exists():
            print(f"⚠️  Hook '{hook}' already exists in {target_dir}. Overwriting...")
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print(f"✅ Installed Hook: {hook}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Install Claude Master Skills into your project.")
    parser.add_argument("skills", nargs="*", default=["all"], help="List of skills to install (e.g., repo-roast code-reviewer) or 'all'")
    parser.add_argument("--path", default=".claude/skills", help="Target directory for installation (default: .claude/skills)")
    
    args = parser.parse_args()
    
    print("🚀 Claude Master Skills Installer")
    print("--------------------------------")
    
    try:
        install_skills(args.skills, args.path)
        print("\n✨ Installation Complete! Claude Code will now recognize these as available_skills.")
    except Exception as e:
        print(f"\n❌ Error during installation: {e}")
