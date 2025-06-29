#!/bin/bash
echo "🔐 Marking /workspace as a safe Git directory..."
git config --global --add safe.directory /workspace
