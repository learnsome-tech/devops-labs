    recovery = [(fix["at"] - broken["at"]).total_seconds() / 60
                for broken in deploys if broken["tag"] in remediations
                for fix in [remediations[broken["tag"]]]]
